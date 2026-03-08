import requests
import os
from datetime import datetime, timedelta

username = os.environ["LEETCODE_USERNAME"]
webhook = os.environ["DISCORD_WEBHOOK"]
session = os.environ["LEETCODE_SESSION"]
csrf = os.environ["LEETCODE_CSRF"]

url = "https://leetcode.com/graphql"
query = {
    "query": """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            title
            titleSlug
            timestamp
        }
    }
    """,
    "variables": {"username": username, "limit": 10}
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "x-csrftoken": csrf,
    "Referer": "https://leetcode.com"
}
cookies = {
    "LEETCODE_SESSION": session,
    "csrftoken": csrf
}

res = requests.post(url, json=query, headers=headers, cookies=cookies).json()
subs = res["data"]["recentAcSubmissionList"]

now = datetime.utcnow()
links, seen = [], set()

for sub in subs:
    sub_time = datetime.utcfromtimestamp(int(sub["timestamp"]))
    if now - sub_time < timedelta(hours=16):
        link = f"https://leetcode.com/problems/{sub['titleSlug']}"
        if link not in seen:
            seen.add(link)
            links.append(link)

if not links:
    requests.post(webhook, json={"content": "No problems solved today"})
else:
    msg = f"Today ({len(links)} problems):\n"
    msg += "\n".join(f"{i}) {l}" for i, l in enumerate(links, 1))
    requests.post(webhook, json={"content": msg})
