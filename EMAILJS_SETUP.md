# EmailJS Setup Guide

Send emails directly from your landing page without backend or redirects!

## Why EmailJS?

✅ **No backend needed** - Pure client-side  
✅ **No redirects** - Users stay on your page  
✅ **Free tier:** 200 emails/month  
✅ **Can send to Gmail, Google Groups, any email**  
✅ **5 minute setup**

---

## Setup Steps

### 1. Create EmailJS Account

1. Go to [https://www.emailjs.com/](https://www.emailjs.com/)
2. Sign up (free account)
3. Verify your email

### 2. Add Email Service

1. Go to **Email Services** tab
2. Click **Add New Service**
3. Choose your email provider:
   - **Gmail** (recommended for personal)
   - **Outlook**
   - **Custom SMTP** (for Google Groups)
4. Connect your account
5. Note your **Service ID** (e.g., `service_abc123`)

### 3. Create Email Template

1. Go to **Email Templates** tab
2. Click **Create New Template**
3. Set up template:

**Template Name:** `early_access_signup`

**Subject:** `New Early Access Signup: {{user_email}}`

**Content:**
```
New early access signup from landing page!

Email: {{user_email}}
Timestamp: {{timestamp}}
User Agent: {{user_agent}}
Referrer: {{referrer}}
Page URL: {{page_url}}

---
Sent via EmailJS from qyntec.ai
```

4. **To Email:** Your email or Google Group email (e.g., `your-group@googlegroups.com`)
5. Click **Save**
6. Note your **Template ID** (e.g., `template_xyz789`)

### 4. Get Public Key

1. Go to **Account** → **General**
2. Find your **Public Key** (e.g., `AbCdEfGhIjKlMnOp`)
3. Copy it

### 5. Update Your Code

Edit `script.js` and replace these values:

```javascript
const EMAILJS_PUBLIC_KEY = 'YOUR_PUBLIC_KEY_HERE';
const EMAILJS_SERVICE_ID = 'service_abc123';
const EMAILJS_TEMPLATE_ID = 'template_xyz789';
```

### 6. Test It!

1. Open your landing page
2. Submit an email
3. Check your inbox!

---

## Sending to Google Groups

### Option A: Direct Email (Recommended)

1. In EmailJS template, set **To Email** to your Google Group email:
   ```
   your-group@googlegroups.com
   ```

2. Make sure your Google Group allows external emails:
   - Go to Google Groups settings
   - **Permissions** → **Post**
   - Allow "Public" or "Anyone on the web"

### Option B: Forward from Gmail

1. Set EmailJS to send to your Gmail
2. Set up Gmail filter to forward to Google Group:
   - Gmail Settings → Filters
   - Create filter for subject: "New Early Access Signup"
   - Forward to: `your-group@googlegroups.com`

---

## Advanced: Multiple Recipients

In your EmailJS template, you can add multiple recipients:

**To Email:**
```
you@gmail.com, team@googlegroups.com, backup@example.com
```

Or use **CC** and **BCC** fields in the template.

---

## Troubleshooting

### Emails not sending?

1. **Check console** - Look for errors in browser console
2. **Verify keys** - Make sure all IDs are correct
3. **Check quota** - Free tier: 200 emails/month
4. **Test template** - Use "Test" button in EmailJS dashboard

### Google Groups not receiving?

1. **Check group settings** - Allow external posts
2. **Check spam** - Emails might be in spam folder
3. **Verify email** - Make sure group email is correct
4. **Use Gmail forward** - More reliable than direct

---

## Cost

- **Free tier:** 200 emails/month
- **Personal:** $7/month - 1,000 emails
- **Professional:** $15/month - 10,000 emails

For a landing page, free tier is usually enough!

---

## Security

✅ **Public key is safe** - Designed to be exposed in client-side code  
✅ **Rate limiting** - EmailJS prevents spam  
✅ **Domain whitelist** - Can restrict to your domain only  

To add domain whitelist:
1. EmailJS Dashboard → Account → Security
2. Add: `qyntec.github.io`

---

## Alternative: Using Gmail API

If you want more control, you can use Gmail API directly, but it requires OAuth setup. EmailJS is much simpler for this use case.

---

## Testing Locally

The code works locally too! Just open `index.html` in your browser after configuring EmailJS.

---

## Next Steps

1. ✅ Set up EmailJS account
2. ✅ Configure email service
3. ✅ Create template
4. ✅ Update `script.js` with your keys
5. ✅ Test submission
6. ✅ Deploy to GitHub Pages

Done! You'll receive emails for every signup, no backend needed! 🎉
