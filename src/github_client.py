import os
from urllib.parse import quote

import requests

API_BASE = "https://api.github.com"
TIMEOUT = (5, 30)  # (connect, read) seconds


def _headers() -> dict:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN environment variable is not set")
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def list_repos(org: str) -> list:
    """Return all repos for an org, following pagination."""
    url = f"{API_BASE}/orgs/{quote(org, safe='')}/repos"
    params = {"per_page": 100}
    repos = []
    while url:
        r = requests.get(url, headers=_headers(), params=params, timeout=TIMEOUT)
        r.raise_for_status()
        repos.extend(r.json())
        url = r.links.get("next", {}).get("url")
        params = None  # the "next" URL already carries the query string
    return repos


def create_pr(owner: str, repo: str, title: str, body: str, head: str, base: str = "main") -> dict:
    r = requests.post(
        f"{API_BASE}/repos/{quote(owner, safe='')}/{quote(repo, safe='')}/pulls",
        headers=_headers(),
        json={"title": title, "body": body, "head": head, "base": base},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()
