# 📊 LeetCode Discord Reporter

Automatically posts your daily LeetCode solved problems to a Discord channel every night — no PC required.

---

## ✨ What it does

Every day at **10:15 PM IST**, GitHub Actions runs a script that:
- Fetches your accepted LeetCode submissions from the past 24 hours
- Posts them to your Discord channel in this format:

```
Today (3 problems):
1) https://leetcode.com/problems/find-unique-binary-string
2) https://leetcode.com/problems/find-the-smallest-balanced-index
3) https://leetcode.com/problems/minimum-operations-to-sort-a-string
```

If nothing was solved:
```
No problems solved today
```

---

## 🛠️ Setup

### 1. Fork / clone this repo

### 2. Get your LeetCode cookies

1. Go to [leetcode.com](https://leetcode.com) and log in
2. Press `F12` → **Application** → **Cookies** → `https://leetcode.com`
3. Copy the values of:
   - `LEETCODE_SESSION`
   - `csrftoken`

> ⚠️ Cookies expire in ~2 weeks. You'll need to refresh them when the bot stops working.

### 3. Create a Discord Webhook

1. Go to your Discord channel → **Edit Channel** → **Integrations** → **Webhooks**
2. Click **New Webhook** → copy the URL

### 4. Add GitHub Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add these 4 secrets:

| Secret Name | Value |
|---|---|
| `LEETCODE_USERNAME` | Your LeetCode username |
| `LEETCODE_SESSION` | Cookie value from step 2 |
| `LEETCODE_CSRF` | `csrftoken` value from step 2 |
| `DISCORD_WEBHOOK` | Webhook URL from step 3 |

### 5. Done 🎉

The workflow runs automatically every day at 10:15 PM IST. No PC needed.

---

## 📁 Files

```
├── send.py                        # Main script
└── .github/
    └── workflows/
        └── daily.yml              # GitHub Actions workflow
```

---

## ⚙️ Workflow Schedule

The cron is set to `45 16 * * *` (UTC) which is **10:15 PM IST**.

To change the time, edit `.github/workflows/daily.yml`:
```yaml
- cron: '45 16 * * *'   # 10:15 PM IST
```

Use [crontab.guru](https://crontab.guru) to convert your preferred time to UTC.

---

## 🔄 Refreshing Cookies

When the bot stops posting (usually after ~2 weeks):

1. Go to leetcode.com → F12 → Application → Cookies
2. Copy new values of `LEETCODE_SESSION` and `csrftoken`
3. Update the secrets in GitHub → Settings → Secrets

---

## 🔒 Security

- Never commit your cookies or webhook URL directly in code
- Always use GitHub Secrets
- If your Discord webhook URL leaks, regenerate it immediately:
  **Discord → Channel Settings → Integrations → Webhooks → Regenerate URL**
