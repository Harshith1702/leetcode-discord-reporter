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

headers = {
 "Content-Type": "application/json",
 "User-Agent": "Mozilla/5.0"
}

res = requests.post(url, json=query, headers=headers)
data = res.json()

subs = data["data"]["recentSubmissionList"]

now = datetime.utcnow()
links = []
seen = set()

for sub in subs:
 if sub["statusDisplay"] == "Accepted":

  ts = int(sub["timestamp"])
  sub_time = datetime.utcfromtimestamp(ts)

  # check if submission happened in last 24 hours
  if now - sub_time < timedelta(hours=24):

   link = f"https://leetcode.com/problems/{sub['titleSlug']}"

   if link not in seen:
    seen.add(link)
    links.append(link)

if len(links) == 0:
 requests.post(webhook, json={"content": "No problems solved today"})
else:

 msg = f"Today ({len(links)} problems):\n"

 for i,l in enumerate(links,1):
  msg += f"{i}) {l}\n"

 requests.post(webhook, json={"content": msg})
