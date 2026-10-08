import requests

GITHUB_TOKEN = "~[GITHUB_PERSONAL_TOKEN_0]~"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def list_repos(org: str):
    r = requests.get(f"https://api.github.com/orgs/{org}/repos", headers=HEADERS)
    return r.json()

def create_pr(owner: str, repo: str, title: str, body: str, head: str, base: str = "main"):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/pulls",
        headers=HEADERS,
        json={"title": title, "body": body, "head": head, "base": base}
    )
    return r.json()
