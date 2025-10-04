import os
import re
import requests
from pathlib import Path
from collections import defaultdict

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
    
    def generate_readme(self):
        """Generate README.md file"""
        if not self.fetch_all_problems():
            print("Warning: Could not fetch problem data. Generating basic README...")
        
        solutions = self.get_solutions_by_rating()
        total_problems = sum(len(sols) for sols in solutions.values())
        
        readme_content = f"""# 🎯 Codeforces Solutions

A collection of my Codeforces problem solutions, organized by difficulty rating.

## 📊 Statistics

- **Total Problems Solved:** {total_problems}
- **Languages:** Python
- **Last Updated:** Auto-generated

## 📁 Repository Structure

Solutions are organized by rating ranges:
- `800-1000/` - Beginner-friendly problems
- `1000-1200/` - Easy problems
- `1200-1400/` - Medium difficulty
- `1400-1600/` - Intermediate problems
- `Unrated/` - Problems without official rating

## 🗂️ Solutions by Rating

"""
        
        rating_order = ['800-1000', '1000-1200', '1200-1400', '1400-1600', 'Unrated']
        
        for rating_folder in rating_order:
            if rating_folder in solutions and solutions[rating_folder]:
                sols = solutions[rating_folder]
                readme_content += f"### {rating_folder} ({len(sols)} problems)\n\n"
                readme_content += "| Problem | Rating | Tags |\n"
                readme_content += "|---------|--------|------|\n"
                
                for sol in sols:
                    problem_link = f"https://codeforces.com/problemset/problem/{sol['contest_id']}/{sol['index']}"
                    problem_name = f"[{sol['contest_id']}{sol['index']} - {sol['name']}]({problem_link})"
                    solution_link = f"[Solution]({sol['relative_path']})"
                    
                    tags = ', '.join(sol['tags'][:3]) if sol['tags'] else 'implementation'
                    rating_badge = f"`{sol['rating']}`" if sol['rating'] != 'Unrated' else '`Unrated`'
                    
                    readme_content += f"| {problem_name} {solution_link} | {rating_badge} | {tags} |\n"
                
                readme_content += "\n"
        
        readme_content += """---

## 🚀 How to Use

1. Browse solutions by rating category
2. Each solution file contains:
   - Problem metadata (rating, tags, link)
   - Clean, commented code
   - Optimal solution approach

## 📝 Notes

- All solutions are tested and accepted on Codeforces
- Solutions focus on clarity and efficiency
- README is auto-generated using `generate_readme.py`

## 🔗 Links

- [My Codeforces Profile](https://codeforces.com/profile/PhewwcCoder)
- [Codeforces](https://codeforces.com/)

---

*Last generated: Auto-updated*
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
