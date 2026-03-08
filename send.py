import requests
import os
from datetime import datetime, timedelta

username = os.environ["LEETCODE_USERNAME"]
webhook = os.environ["DISCORD_WEBHOOK"]

url = f"https://leetcode.com/api/submissions/{username}"

res = requests.get(url).json()

subs = res["submissions_dump"]

now = datetime.utcnow() + timedelta(hours=5, minutes=30)
today = now.date()

links = []
seen = set()

for sub in subs:
    if sub["status_display"] == "Accepted":
        ts = int(sub["timestamp"])
        sub_time = datetime.utcfromtimestamp(ts) + timedelta(hours=5, minutes=30)

        if sub_time.date() == today:
            link = f"https://leetcode.com/problems/{sub['title_slug']}"
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
