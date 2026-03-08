import requests
import os
from datetime import datetime

username = os.environ["LEETCODE_USERNAME"]
webhook = os.environ["DISCORD_WEBHOOK"]
session = os.environ["LEETCODE_SESSION"]

url = "https://leetcode.com/graphql"

query = {
    "query": """{ matchedUser(username: "%s") { submitStats { acSubmissionNum { difficulty count } } } }""" % username
}

cookies = {"LEETCODE_SESSION": session}
headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}

res = requests.post(url, json=query, headers=headers, cookies=cookies).json()
stats = res["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

total = next(s["count"] for s in stats if s["difficulty"] == "All")
easy = next(s["count"] for s in stats if s["difficulty"] == "Easy")
medium = next(s["count"] for s in stats if s["difficulty"] == "Medium")
hard = next(s["count"] for s in stats if s["difficulty"] == "Hard")

msg = f"LeetCode update for {username}:\nTotal: {total} | Easy: {easy} | Medium: {medium} | Hard: {hard}"
requests.post(webhook, json={"content": msg})
