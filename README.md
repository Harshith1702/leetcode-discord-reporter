<div align="center">

# 🧠 LeetCode Discord Reporter

**Automatically tracks your daily LeetCode grind and posts it to Discord — every night, no PC needed.**

![GitHub Actions](https://img.shields.io/badge/Automated-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)
![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 🚀 What It Does

Every day at **10:15 PM IST**, this bot wakes up on GitHub's servers and:

- ✅ Fetches all LeetCode problems you solved that day
- 📬 Posts them directly to your Discord channel
- 💤 Requires **zero input from you** — PC can be completely off

### Example Discord Message

```
Today (3 problems):
1) https://leetcode.com/problems/find-unique-binary-string
2) https://leetcode.com/problems/find-the-smallest-balanced-index
3) https://leetcode.com/problems/minimum-operations-to-sort-a-string
```

> If you didn't solve anything, it posts: `No problems solved today`

---

## ⏰ Tracking Window

The bot captures problems solved between **6:15 AM → 10:15 PM IST** daily.

Late night solves (after 10:15 PM) won't be included — keeping your daily log clean and honest.

---

## 🛠️ Setup Guide

### Step 1 — Get Your LeetCode Cookies

> Your cookies authenticate the request so GitHub's servers aren't blocked by LeetCode.

1. Go to [leetcode.com](https://leetcode.com) and log in
2. Press `F12` → **Application** tab → **Cookies** → `https://leetcode.com`
3. Find and copy these two values:
   - `LEETCODE_SESSION`
   - `csrftoken`

### Step 2 — Create a Discord Webhook

1. Open your Discord server → right-click your channel → **Edit Channel**
2. Go to **Integrations** → **Webhooks** → **New Webhook**
3. Give it a name (e.g. `LeetCode Bot`) and copy the webhook URL

### Step 3 — Add GitHub Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| Secret | Value |
|--------|-------|
| `LEETCODE_USERNAME` | Your LeetCode username |
| `LEETCODE_SESSION` | Cookie from Step 1 |
| `LEETCODE_CSRF` | `csrftoken` from Step 1 |
| `DISCORD_WEBHOOK` | Webhook URL from Step 2 |

### Step 4 — You're Done 🎉

Push the code. GitHub Actions handles everything from here.

---

## 📁 Project Structure

```
leetcode-discord-reporter/
├── send.py                    # Core script — fetches & posts submissions
└── .github/
    └── workflows/
        └── daily.yml          # Scheduler — runs every night at 10:15 PM IST
```

---

## ⚙️ Customization

### Change the posting time

Edit `.github/workflows/daily.yml`:

```yaml
- cron: '45 16 * * *'   # 10:15 PM IST (UTC+5:30)
```

Use [crontab.guru](https://crontab.guru) to convert your time to UTC.

### Change the tracking window

Edit `send.py`:

```python
if now - sub_time < timedelta(hours=16):  # tracks from 6:15 AM IST
```

Increase or decrease the hours as needed.

---

## 🔄 Cookie Refresh (Every ~2 Weeks)

LeetCode session cookies expire. When the bot stops working:

1. Log in to leetcode.com → `F12` → Application → Cookies
2. Copy fresh `LEETCODE_SESSION` and `csrftoken` values
3. Update them in **GitHub → Settings → Secrets**

---

## 🔒 Security Notes

- ✅ All sensitive values are stored as **GitHub Secrets** — never in code
- ⚠️ If your Discord webhook URL leaks, regenerate it immediately:
  `Discord → Channel Settings → Integrations → Webhooks → Regenerate URL`
- ⚠️ Never commit cookies directly into your repo

---

## 💡 Inspiration

In class one day, our sir mentioned a student from another campus who had built something really cool — a script on his local PC that sent his daily LeetCode solved problem links to the college Discord server (where we're supposed to post daily) with just a single button click. Sir was genuinely impressed, said he only found out about it a few days later.

That story stayed with me. I took that same idea and pushed it a step further — no button, no local PC. Mine just runs automatically every night at 10:15 PM and posts on its own, whether my PC is on or not.

Respect to that guy for the inspiration. 🙏

---

<div align="center">

Built with 💪 to keep the grind accountable.

</div>
