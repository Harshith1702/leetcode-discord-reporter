import requests
import os
from datetime import datetime, timedelta

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

# current time in IST
now = datetime.utcnow() + timedelta(hours=5, minutes=30)
today = now.date()

links = []

for sub in res["data"]["recentSubmissionList"]:
    if sub["statusDisplay"] == "Accepted":
        ts = int(sub["timestamp"])
        sub_time = datetime.utcfromtimestamp(ts) + timedelta(hours=5, minutes=30)

        if sub_time.date() == today:
            links.append(f"https://leetcode.com/problems/{sub['titleSlug']}")

links = list(dict.fromkeys(links))

if len(links) == 0:
    requests.post(webhook, json={"content": "No problems solved today"})
else:
    msg = f"Today ({len(links)} problems):\n"
    for i, l in enumerate(links, 1):
        msg += f"{i}) {l}\n"

    requests.post(webhook, json={"content": msg})
