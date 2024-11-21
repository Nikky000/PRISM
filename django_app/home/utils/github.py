import requests
import base64
from urllib.parse import urlparse
import uuid
from .ai_agent import analyze_code_with_llm

def get_owner_and_repo(url):
    passed_url = urlparse(url)
    path_parts = passed_url.path.strip("/").split("/")
    if len(path_parts)>=2:
        owner,repo =  path_parts[0],path_parts[1]
        return owner,repo

    return None,None


def fetch_pr_files(repo_url ,pr_number,github_token=None):
    owner,repo = get_owner_and_repo(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    headers = {"Authorization" : f"token {github_token}"} if github_token else {}
    responese = requests.get(url,headers=headers)
    responese.raise_for_status()
    return responese.json()

def fetch_file_content(repo_url ,file_path,github_token=None):
    owner,repo = get_owner_and_repo(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Authorization" : f"token {github_token}"} if github_token else {}
    responese = requests.get(url,headers=headers)
    responese.raise_for_status()
    content = responese.json()
    return base64.b64decode(content['content']).decode()

def analyze_pr(repo_url,pr_number,github_token = None):
    task_id = str(uuid.uuid4())
    try:
        pr_files = fetch_pr_files(repo_url,pr_number,github_token)
        analysis_results = []
        for file in pr_files:
            file_name = file['filename']
            raw_content = fetch_file_content(repo_url,file_name,github_token)
            analysis_result = analyze_code_with_llm(raw_content,file_name)

            analysis_results.append({"results" : analysis_result ,"file_name":file_name})

        return {"task_id" : task_id,"result" : analysis_results}
    except Exception as e:
        print(e)
        return {"task_id" : task_id, "results" : []}