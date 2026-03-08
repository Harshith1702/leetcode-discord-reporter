import requests
import os

username = os.environ["LEETCODE_USERNAME"]
webhook = os.environ["DISCORD_WEBHOOK"]
session = os.environ["LEETCODE_SESSION"]

url = "https://leetcode.com/graphql"
query = {
    "query": """{ matchedUser(username: "%s") { submitStats { acSubmissionNum { difficulty count } } } }""" % username
}

cookies = {"LEETCODE_SESSION": session}
headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}

res = requests.post(url, json=query, headers=headers, cookies=cookies)
requests.post(webhook, json={"content": res.text[:1000]})
