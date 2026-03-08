import requests
import os
from datetime import datetime, timedelta

username = os.environ["LEETCODE_USERNAME"]
webhook = os.environ["DISCORD_WEBHOOK"]
session = os.environ["LEETCODE_SESSION"]

url = "https://leetcode.com/graphql"
query = {
    "query": """
    query recentSubmissions($username: String!) {
        recentSubmissionList(username: $username) {
            titleSlug
            timestamp
            statusDisplay
        }
    }
    """,
    "variables": {"username": username}
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}
cookies = {
    "LEETCODE_SESSION": session
}

res = requests.post(url, json=query, headers=headers, cookies=cookies).json()
subs = res["data"]["recentSubmissionList"]
requests.post(webhook, json={"content": str(subs[:3])})

now = datetime.utcnow()
links, seen = [], set()

for sub in subs:
    sub_time = datetime.utcfromtimestamp(int(sub["timestamp"]))
    if now - sub_time < timedelta(hours=24):
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
