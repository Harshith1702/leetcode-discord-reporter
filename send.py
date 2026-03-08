import requests
from datetime import datetime, timezone
import os

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
seen = set()

for sub in res["data"]["recentSubmissionList"]:
    if sub["statusDisplay"] == "Accepted":
        d = datetime.fromtimestamp(int(sub["timestamp"]), tz=timezone.utc).date()
        if d == today:
            link = f"https://leetcode.com/problems/{sub['titleSlug']}"
            if link not in seen:
                seen.add(link)
                links.append(link)

print("Solved today:", links)

if len(links) == 0:
    print("No problems solved today")
    exit()

msg = f"Today ({len(links)} problems):\n"

for i, l in enumerate(links, 1):
    msg += f"{i}) {l}\n"

print("Sending message:", msg)

requests.post(webhook, json={"content": msg})
