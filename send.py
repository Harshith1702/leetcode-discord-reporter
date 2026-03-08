import requests
import os
from datetime import datetime, timezone

username = os.environ["LEETCODE_USERNAME"]
webhook = os.environ["DISCORD_WEBHOOK"]

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

res = requests.post(url, json=query).json()

today = datetime.now(timezone.utc).date()

links = []

for sub in res["data"]["recentSubmissionList"]:
    if sub["statusDisplay"] == "Accepted":
        d = datetime.fromtimestamp(int(sub["timestamp"]), tz=timezone.utc).date()
        if d == today:
            links.append(f"https://leetcode.com/problems/{sub['titleSlug']}")

links = list(dict.fromkeys(links))

if len(links) == 0:
    requests.post(webhook, json={"content": "No problems solved today"})
else:
    msg = f"Today ({len(links)} problems):\n"
    for i, l in enumerate(links, 1):
        msg += f"{i}) {l}\n"

    requests.post(webhook, json={"content": msg})
