import os
import random
from datetime import datetime, timedelta

repo_path = r"C:\Users\ASUS\Desktop\github-activity"
os.chdir(repo_path)

# Get yesterday and today
dates = [
    datetime.now() - timedelta(days=1),  # yesterday
    datetime.now()                       # today
]

for commit_date in dates:
    for _ in range(random.randint(1, 3)):  # 1-3 commits per day
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        date_str = commit_date.replace(hour=hour, minute=minute, second=second).strftime("%Y-%m-%d %H:%M:%S")
        os.system(f'git commit --allow-empty --date="{date_str}" -m "update"')

# Push commits to GitHub
os.system("git push origin main")