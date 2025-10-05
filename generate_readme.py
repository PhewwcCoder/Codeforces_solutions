import os
import re
import requests
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class ReadmeGenerator:
    def __init__(self):
        self.folder_path = Path(__file__).parent
        self.problem_map = {}
        
    def fetch_all_problems(self):
        """Fetch all problem data from Codeforces API"""
        print("Fetching problem data from Codeforces API...")
        try:
            response = requests.get("https://codeforces.com/api/problemset.problems", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'OK':
                    for problem in data['result']['problems']:
                        key = str(problem.get('contestId')) + str(problem.get('index'))
                        self.problem_map[key] = {
                            'name': problem.get('name', 'Unknown'),
                            'rating': problem.get('rating', 'Unrated'),
                            'tags': problem.get('tags', [])
                        }
                    print(f"Loaded {len(self.problem_map)} problems\n")
                    return True
        except Exception as e:
            print(f"Error fetching data: {e}")
        return False
    
    def parse_filename(self, filename):
        """Extract contest ID and problem index from filename"""
        patterns = [r'^(\d+)([A-Z]\d?)__', r'^(\d+)([A-Z]\d?)_']
        for pattern in patterns:
            match = re.search(pattern, filename)
            if match:
                return match.group(1), match.group(2)
        return None, None
    
    def get_solutions_by_rating(self):
        """Organize solutions by rating category"""
        solutions = defaultdict(list)
        rating_folders = ['800-1000', '1000-1200', '1200-1400', '1400-1600', 'Unrated']
        
        for folder_name in rating_folders:
            folder_path = self.folder_path / folder_name
            if folder_path.exists():
                for file in sorted(folder_path.glob('*.py')):
                    contest_id, problem_index = self.parse_filename(file.name)
                    if contest_id and problem_index:
                        key = contest_id + problem_index
                        problem_info = self.problem_map.get(key, {
                            'name': 'Unknown Problem',
                            'rating': 'Unrated',
                            'tags': []
                        })
                        
                        solutions[folder_name].append({
                            'file': file.name,
                            'contest_id': contest_id,
                            'index': problem_index,
                            'name': problem_info['name'],
                            'rating': problem_info['rating'],
                            'tags': problem_info['tags'],
                            'relative_path': f"{folder_name}/{file.name}"
                        })
        
        return solutions
    
    def get_rating_title(self, rating_range):
        """Get proper title for each rating range"""
        titles = {
            '800-1000': '🟢 Newbie (800-1000)',
            '1000-1200': '🟢 Pupil (1000-1200)',
            '1200-1400': '🟦 Specialist (1200-1400)',
            '1400-1600': '🟦 Expert (1400-1600)',
            'Unrated': '⚪ Unrated'
        }
        return titles.get(rating_range, rating_range)
    
    def generate_readme(self):
        """Generate README.md file"""
        if not self.fetch_all_problems():
            print("Warning: Could not fetch problem data. Generating basic README...")
        
        solutions = self.get_solutions_by_rating()
        total_problems = sum(len(sols) for sols in solutions.values())
        
        readme_content = f"""# 🎯 Codeforces Solutions in Python

> **Why Python?** While most competitive programmers use C++ for its speed, I've chosen Python to prove that elegant, readable code can be just as competitive. Every solution here demonstrates that algorithmic thinking matters more than language choice.

## 📊 Statistics

- **Total Problems Solved:** {total_problems}
- **Languages:** Python 🐍
- **Profile:** [PhewwcCoder](https://codeforces.com/profile/PhewwcCoder)
- **Last Updated:** {datetime.now().strftime('%B %d, %Y')}

## 💡 Why Python for Competitive Programming?

Most competitive programmers choose C++ for its blazing speed, but I've taken a different path:

- **🧠 Readability First:** Clean, maintainable code that's easy to understand and debug
- **⚡ Smart Optimization:** Proving that algorithmic efficiency beats language speed
- **🎯 Focus on Logic:** Less time wrestling with syntax, more time solving problems
- **🐍 Python Power:** Built-in data structures, elegant syntax, rapid prototyping

**The Challenge:** Making Python competitive where others say it's too slow. Spoiler: It works!

## 📁 Repository Structure

Solutions are organized by Codeforces rating ranges:
- `800-1000/` - 🟢 Newbie level
- `1000-1200/` - 🟢 Pupil level  
- `1200-1400/` - 🟦 Specialist level
- `1400-1600/` - 🟦 Expert level
- `Unrated/` - Problems without official rating

## 🗂️ Solutions by Rating

"""
        
        rating_order = ['800-1000', '1000-1200', '1200-1400', '1400-1600', 'Unrated']
        
        for rating_folder in rating_order:
            if rating_folder in solutions and solutions[rating_folder]:
                sols = solutions[rating_folder]
                title = self.get_rating_title(rating_folder)
                readme_content += f"### {title}\n"
                readme_content += f"**{len(sols)} problems**\n\n"
                readme_content += "| Problem | Rating | Tags | Solution |\n"
                readme_content += "|---------|--------|------|----------|\n"
                
                for sol in sols:
                    problem_link = f"https://codeforces.com/problemset/problem/{sol['contest_id']}/{sol['index']}"
                    problem_name = f"[{sol['contest_id']}{sol['index']} - {sol['name']}]({problem_link})"
                    solution_link = f"[Code]({sol['relative_path']})"
                    
                    tags = ', '.join(sol['tags'][:3]) if sol['tags'] else 'implementation'
                    rating_badge = f"`{sol['rating']}`" if sol['rating'] != 'Unrated' else '`Unrated`'
                    
                    readme_content += f"| {problem_name} | {rating_badge} | {tags} | {solution_link} |\n"
                
                readme_content += "\n"
        
        readme_content += """---

## 🚀 How to Use

1. **Browse by difficulty:** Solutions are organized by rating ranges
2. **Click problem names:** Opens the problem on Codeforces
3. **View solutions:** Click "Code" to see my Python implementation
4. **Learn & adapt:** Each solution includes clean, commented code

Each solution demonstrates:
- Optimal algorithmic approach
- Python-specific optimizations
- Clean, readable code structure

## 📝 Notes

- ✅ All solutions are **tested and accepted** on Codeforces
- 🐍 Python solutions competing with C++ implementations
- 🧹 Code focuses on **clarity and efficiency**
- 🤖 README auto-generated with `generate_readme.py`

## 🔗 Links

- [My Codeforces Profile](https://codeforces.com/profile/PhewwcCoder)
- [Codeforces](https://codeforces.com/)

---

*Generated automatically with Python*
"""
        
        readme_path = self.folder_path / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"✅ README.md generated successfully!")
        print(f"   Total problems: {total_problems}")
        print(f"   Path: {readme_path}")

if __name__ == "__main__":
    generator = ReadmeGenerator()
    generator.generate_readme()
