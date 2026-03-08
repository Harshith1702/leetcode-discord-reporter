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
requests.post(webhook, json={"content": str(res)[:1000]})
