import os
import subprocess
import requests
import base64

# GitHub repo details
REPO_NAME = "contribution-graph"
README_CONTENT = "Made with https://github.com/0vm/commit-graph-spoof" # Keep this if you want to give me credit :D

# Get user GitHub credentials
GITHUB_USER = input("Enter your GitHub username: ").strip()
GITHUB_TOKEN = input("Enter your GitHub personal access token: ").strip()

# Step 1: Create the repo on GitHub
print("Creating GitHub repository...")

repo_data = {
    "name": REPO_NAME,
    "private": False,  # Change to True if you want a private repo
    "description": "Commit Graph https://github.com/0vm/commit-graph-spoof",
}

response = requests.post(
    "https://api.github.com/user/repos",
    json=repo_data,
    headers={"Authorization": f"token {GITHUB_TOKEN}"}
)

if response.status_code == 201:
    print(f"✅ Repository '{REPO_NAME}' created!")
else:
    print(f"❌ Failed to create repository: {response.json().get('message')}")
    exit(1)

# Step 2: Clone the new repo
GIT_REPO_URL = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{REPO_NAME}.git"
subprocess.run(["git", "clone", GIT_REPO_URL])
os.chdir(REPO_NAME)

# Step 3: Create README.md
with open("README.md", "w") as f:
    f.write(README_CONTENT)

# Step 4: Commit the README with a fake timestamp
subprocess.run(["git", "add", "README.md"])
subprocess.run(["git", "commit", "-m", "GitHub.com/0vm", "--date=1970-01-01T00:00:00"])

# Step 5: Push the commit
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "push", "-u", "origin", "main"])

print(f"Repo '{REPO_NAME}' pushed!")
print(f"View it here: https://github.com/{GITHUB_USER}/{REPO_NAME}")
