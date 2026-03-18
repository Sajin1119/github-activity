import os
import random
from datetime import datetime, timezone

# Path to your Git repo
repo_path = r"C:\Users\ASUS\Desktop\github-activity"
os.chdir(repo_path)

# Today in UTC
utc_now = datetime.now(timezone.utc)

# Make exactly 3 commits for today
for _ in range(3):
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    dt = utc_now.replace(hour=hour, minute=minute, second=second)
    date_str = dt.strftime("%Y-%m-%d %H:%M:%S +0000")  # UTC
    os.system(f'git commit --allow-empty --date="{date_str}" -m "update"')

# Push commits to GitHub
os.system("git push origin main")