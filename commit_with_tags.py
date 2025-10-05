import os
import re
import requests
import subprocess
from pathlib import Path

class CommitWithTags:
    def __init__(self):
        self.folder_path = Path(__file__).parent
        self.problem_map = {}
        
    def fetch_all_problems(self):
        """Fetch all problems once at the start"""
        print("Fetching problem data from Codeforces...")
        try:
            response = requests.get("https://codeforces.com/api/problemset.problems", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'OK':
                    for problem in data['result']['problems']:
                        key = str(problem.get('contestId')) + str(problem.get('index'))
                        self.problem_map[key] = problem.get('tags', ['implementation'])
                    print(f"Loaded {len(self.problem_map)} problems\n")
                    return True
        except Exception as e:
            print(f"Error fetching data: {e}")
        return False
    
    def parse_filename(self, filename):
        patterns = [r'^(\d+)([A-Z]\d?)__', r'^(\d+)([A-Z]\d?)_']
        for pattern in patterns:
            match = re.search(pattern, filename)
            if match:
                return match.group(1), match.group(2)
        return None, None
    
    def get_all_solution_files(self):
        all_files = []
        rating_folders = ['800-1000', '1000-1200', '1200-1400', '1400-1600', 'Unrated']
        
        for folder_name in rating_folders:
            folder_path = self.folder_path / folder_name
            if folder_path.exists():
                for file in sorted(folder_path.glob('*.py')):
                    contest_id, problem_index = self.parse_filename(file.name)
                    if contest_id and problem_index:
                        all_files.append((file, contest_id, problem_index))
        return all_files
    
    def commit_files(self):
        os.chdir(self.folder_path)
        
        if not self.fetch_all_problems():
            print("Failed to fetch problem data. Aborting.")
            return
        
        all_files = self.get_all_solution_files()
        if not all_files:
            print("No files found!")
            return
        
        print(f"Committing {len(all_files)} files...\n")
        
        committed = 0
        for file_path, contest_id, problem_index in all_files:
            key = contest_id + problem_index
            tags = self.problem_map.get(key, ['implementation'])
            commit_msg = ', '.join(tags[:3])
            
            try:
                relative_path = file_path.relative_to(self.folder_path)
                subprocess.run(['git', 'add', str(relative_path)], check=True, capture_output=True)
                subprocess.run(['git', 'commit', '-m', commit_msg], check=True, capture_output=True)
                print(f"✓ {file_path.name}: {commit_msg}")
                committed += 1
            except:
                pass
        
        print(f"\n{committed} files committed!")
        print("Push with: git push origin main")

if __name__ == "__main__":
    print("Commit Codeforces Solutions with Tags\n")
    response = input("Proceed? (y/n): ").strip().lower()
    if response in ['y', 'yes']:
        committer = CommitWithTags()
        committer.commit_files()