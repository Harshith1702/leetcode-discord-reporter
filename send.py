import requests
import os
from datetime import datetime, timedelta

username = os.environ["LEETCODE_USERNAME"]
webhook = os.environ["DISCORD_WEBHOOK"]

# Uses public proxy API — no LeetCode blocking
url = f"https://alfa-leetcode-api.onrender.com/{username}/acSubmission?limit=10"

res = requests.get(url)
data = res.json()

subs = data.get("submission", [])

now = datetime.utcnow()
links = []
seen = set()

for sub in subs:
    ts = int(sub["timestamp"])
    sub_time = datetime.utcfromtimestamp(ts)

    if now - sub_time < timedelta(hours=24):
        link = f"https://leetcode.com/problems/{sub['titleSlug']}"
        if link not in seen:
            seen.add(link)
            links.append(link)

if len(links) == 0:
    requests.post(webhook, json={"content": "No problems solved today"})
else:
    msg = f"Today ({len(links)} problems):\n"
    for i, l in enumerate(links, 1):
        msg += f"{i}) {l}\n"
    requests.post(webhook, json={"content": msg})
