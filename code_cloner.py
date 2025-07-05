import os
import uuid
from git import Repo

def clone_repo(url):
    repo_id = str(uuid.uuid4())[:8]
    path = f"./temp_repos/{repo_id}"
    os.makedirs("temp_repos", exist_ok=True)
    Repo.clone_from(url, path)
    return path
