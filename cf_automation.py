import os
import re
import requests
import time
import subprocess
from pathlib import Path
from datetime import datetime

class SimpleCodeforcesSync:
    def __init__(self, cf_handle=None, organize_by_rating=True):
        # Automatically detect the script's location and use it
        self.script_dir = Path(__file__).parent
        self.folder_path = self.script_dir  # Same folder as script
        self.api_base = "https://codeforces.com/api/"
        self.problem_cache = {}
        self.submission_cache = {}
        self.cf_handle = cf_handle
        self.organize_by_rating = organize_by_rating
        self.processed_files_log = self.script_dir / ".cf_processed.txt"
        
        print(f"📁 Working in folder: {self.folder_path}")
        if self.cf_handle:
            print(f"👤 Codeforces handle: {self.cf_handle}")
        if self.organize_by_rating:
            print(f"📂 Will organize by rating categories")
        
    def load_processed_files(self):
        """Load list of already processed files"""
        if self.processed_files_log.exists():
            with open(self.processed_files_log, 'r') as f:
                return set(line.strip() for line in f)
        return set()
    
    def mark_as_processed(self, filename):
        """Mark a file as processed"""
        with open(self.processed_files_log, 'a') as f:
            f.write(f"{filename}\n")
    
    def fetch_problem_info(self, contest_id, problem_index):
        """Fetch problem information from Codeforces API"""
        cache_key = f"{contest_id}{problem_index}"
        if cache_key in self.problem_cache:
            return self.problem_cache[cache_key]
        
        try:
            print(f"  🌐 Fetching problem info from Codeforces API...")
            response = requests.get(f"{self.api_base}problemset.problems")
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'OK':
                    problems = data['result']['problems']
                    for problem in problems:
                        if (str(problem.get('contestId')) == str(contest_id) and 
                            problem.get('index') == problem_index):
                            info = {
                                'rating': problem.get('rating', 'Unrated'),
                                'name': problem.get('name', 'Unknown'),
                                'tags': problem.get('tags', []),
                                'contestId': contest_id,
                                'index': problem_index
                            }
                            self.problem_cache[cache_key] = info
                            return info
            time.sleep(0.5)
        except Exception as e:
            print(f"  ❌ Error: {e}")
        return None
    
    def fetch_submission_stats(self, contest_id, problem_index):
        """Fetch actual submission stats (time, memory) from Codeforces"""
        if not self.cf_handle:
            return None, None
        
        cache_key = f"{contest_id}{problem_index}"
        if cache_key in self.submission_cache:
            return self.submission_cache[cache_key]
        
        try:
            print(f"  📊 Fetching your submission stats...")
            # Fetch user's submissions
            response = requests.get(
                f"{self.api_base}user.status",
                params={'handle': self.cf_handle, 'from': 1, 'count': 100}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'OK':
                    submissions = data['result']
                    
                    # Find accepted submission for this problem
                    for sub in submissions:
                        problem = sub.get('problem', {})
                        if (str(problem.get('contestId')) == str(contest_id) and 
                            problem.get('index') == problem_index and
                            sub.get('verdict') == 'OK'):
                            
                            time_ms = sub.get('timeConsumedMillis', 0)
                            memory_bytes = sub.get('memoryConsumedBytes', 0)
                            
                            # Convert memory to KB
                            memory_kb = memory_bytes / 1024
                            
                            stats = (f"{time_ms}ms", f"{int(memory_kb)}KB")
                            self.submission_cache[cache_key] = stats
                            return stats
            
            time.sleep(0.5)
        except Exception as e:
            print(f"  ⚠️  Could not fetch submission stats: {e}")
        
        return None, None
    
    def get_rating_category(self, rating):
        """Determine rating category folder"""
        if rating == 'Unrated':
            return 'Unrated'
        
        rating = int(rating)
        if rating < 800:
            return '0-800'
        elif rating <= 1000:
            return '800-1000'
        elif rating <= 1200:
            return '1000-1200'
        elif rating <= 1400:
            return '1200-1400'
        elif rating <= 1600:
            return '1400-1600'
        elif rating <= 1800:
            return '1600-1800'
        elif rating <= 2000:
            return '1800-2000'
        else:
            return '2000+'
    
    def move_to_category_folder(self, file_path, rating):
        """Move file to appropriate rating category folder"""
        if not self.organize_by_rating:
            return file_path
        
        category = self.get_rating_category(rating)
        category_folder = self.folder_path / category
        
        # Create category folder if it doesn't exist
        category_folder.mkdir(exist_ok=True)
        
        # Move file
        new_path = category_folder / file_path.name
        file_path.rename(new_path)
        
        return new_path
    
    def parse_filename(self, filename):
        """Extract contest ID and problem index from filename"""
        patterns = [
            r'^(\d+)([A-Z]\d?)__',  # 1A__Theatre.py
            r'^(\d+)([A-Z]\d?)_',   # 1A_Theatre.py
            r'^(\d+)([A-Z]\d?)\.',  # 1A.py
        ]
        
        for pattern in patterns:
            match = re.search(pattern, filename)
            if match:
                return match.group(1), match.group(2)
        return None, None
    
    def add_metadata_to_file(self, file_path, problem_info, exec_time=None, memory=None):
        """Add metadata comment to the top of the file"""
        if not problem_info:
            return False
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if metadata already exists
        if 'Problem:' in content[:300] or 'Rating:' in content[:300]:
            return False
        
        tags_str = ', '.join(problem_info['tags'][:6]) if problem_info['tags'] else 'No tags'
        problem_link = f"https://codeforces.com/problemset/problem/{problem_info['contestId']}/{problem_info['index']}"
        
        # Add execution stats if available
        stats_line = ""
        if exec_time and memory:
            stats_line = f"\nExecution: {exec_time} | Memory: {memory}"
        
        ext = file_path.suffix
        if ext == '.py':
            metadata = f'''"""
Problem: {problem_info['name']}
Rating: {problem_info['rating']}
Tags: {tags_str}{stats_line}
Link: {problem_link}
"""

'''
        elif ext in ['.cpp', '.java', '.c', '.js']:
            metadata = f'''/*
 * Problem: {problem_info['name']}
 * Rating: {problem_info['rating']}
 * Tags: {tags_str}{stats_line}
 * Link: {problem_link}
 */

'''
        else:
            metadata = f'''# Problem: {problem_info['name']}
# Rating: {problem_info['rating']}
# Tags: {tags_str}{stats_line}
# Link: {problem_link}

'''
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(metadata + content)
        
        return True
    
    def sync_new_files(self):
        """Find and process only NEW files"""
        processed_files = self.load_processed_files()
        new_files = []
        
        print("\n🔍 Scanning for new files...\n")
        
        for file_path in sorted(self.folder_path.glob('*')):
            # Skip directories and special files
            if file_path.is_dir() or file_path.name.startswith('.'):
                continue
            
            # Only process code files
            if file_path.suffix not in ['.py', '.cpp', '.java', '.c', '.js']:
                continue
            
            filename = file_path.name
            
            # Skip if already processed
            if filename in processed_files:
                continue
            
            contest_id, problem_index = self.parse_filename(filename)
            
            if contest_id and problem_index:
                print(f"📝 NEW FILE: {filename}")
                problem_info = self.fetch_problem_info(contest_id, problem_index)
                
                if problem_info:
                    # Fetch real submission stats from Codeforces
                    exec_time, memory = self.fetch_submission_stats(contest_id, problem_index)
                    
                    # Add metadata
                    if self.add_metadata_to_file(file_path, problem_info, exec_time, memory):
                        print(f"  ✅ {problem_info['name']}")
                        print(f"  📊 Rating: {problem_info['rating']}")
                        if exec_time and memory:
                            print(f"  ⏱️  Stats: {exec_time} | {memory}")
                        else:
                            print(f"  ⚠️  No submission stats found (might be new or not AC)")
                    
                    # Move to category folder
                    new_file_path = self.move_to_category_folder(file_path, problem_info['rating'])
                    if new_file_path != file_path:
                        category = self.get_rating_category(problem_info['rating'])
                        print(f"  📂 Moved to: {category}/")
                    
                    new_files.append((new_file_path, problem_info, exec_time, memory))
                    self.mark_as_processed(filename)
                    print()
                else:
                    print(f"  ⚠️  Could not fetch info, will try again next time\n")
            else:
                print(f"⏭️  Skipping {filename} - not a valid Codeforces problem format\n")
        
        return new_files
    
    def commit_and_push(self, files):
        """Commit each file individually and push all at once"""
        if not files:
            print("✨ No new files to commit!")
            return
        
        try:
            os.chdir(self.folder_path)
            
            print("\n" + "="*60)
            print("🚀 Committing to Git...")
            print("="*60 + "\n")
            
            for file_path, problem_info, exec_time, memory in files:
                # Create commit message with CF stats
                problem_link = f"https://codeforces.com/problemset/problem/{problem_info['contestId']}/{problem_info['index']}"
                
                # Detailed commit message with stats
                commit_title = f"✅ {problem_info['contestId']}{problem_info['index']} - {problem_info['name']}"
                
                stats_line = f"Rating: {problem_info['rating']} ⭐"
                if exec_time and memory:
                    stats_line += f" | Time: {exec_time} ⏱️ | Memory: {memory} 💾"
                
                commit_msg = f"""{commit_title}

{stats_line}
Link: {problem_link}"""
                
                # Add and commit
                subprocess.run(['git', 'add', file_path.name], check=True)
                subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
                
                print(f"✅ Committed: {file_path.name}")
            
            # Push all commits at once
            print("\n📤 Pushing to GitHub...")
            result = subprocess.run(['git', 'push'], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("\n" + "="*60)
                print(f"🎉 SUCCESS! {len(files)} files synced to GitHub!")
                print("="*60 + "\n")
            else:
                print(f"\n⚠️  Push failed: {result.stderr}")
                print("Run 'git push' manually to push changes\n")
            
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Git error: {e}")
            print("Make sure you're in a git repository!\n")
        except Exception as e:
            print(f"\n❌ Error: {e}\n")

def main():
    print("="*60)
    print("🎯 Codeforces GitHub Sync")
    print("="*60)
    print()
    
    # IMPORTANT: Add your Codeforces handle here!
    CF_HANDLE = "PhewwcCoder"  # ← Change this to your handle!
    
    sync = SimpleCodeforcesSync(cf_handle=CF_HANDLE)
    new_files = sync.sync_new_files()
    
    if new_files:
        print(f"📊 Found {len(new_files)} new file(s)")
        
        # Ask for confirmation
        response = input("\n❓ Commit and push to GitHub? (y/n): ").strip().lower()
        
        if response == 'y' or response == 'yes':
            sync.commit_and_push(new_files)
        else:
            print("\n⏸️  Skipped. Files have metadata but not committed.")
            print("   Run this script again when ready to commit.\n")
    else:
        print("✨ All files are already synced!\n")

if __name__ == "__main__":
    main()