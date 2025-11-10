# Setup Guide

Complete guide for deploying and configuring the landing page.

---

## 🚀 Quick Deploy (GitHub Pages)

### 1. Enable GitHub Pages

1. Go to repository settings: https://github.com/qyntec/qyntec.ai/settings/pages
2. Under "Build and deployment":
   - **Source:** GitHub Actions
3. The workflow will run automatically on push

**Your site:** `https://qyntec.github.io/qyntec.ai/`

### 2. Custom Domain (Optional)

Add a `CNAME` file with your domain:
```
qyntec.ai
```

Configure DNS:
- Add CNAME record: `qyntec.github.io`
- Or A records to GitHub Pages IPs

---

## 📧 Email Notifications (EmailJS)

### Setup (5 minutes)

1. **Sign up:** [emailjs.com](https://www.emailjs.com/) (free: 200/month)

2. **Add Email Service:**
   - Dashboard → Email Services → Add New Service
   - Choose Gmail (or any provider)
   - Connect your account
   - Note your **Service ID**

3. **Create Template:**
   - Dashboard → Email Templates → Create New Template
   - **Subject:** `New Early Access: {{user_email}}`
   - **To Email:** Your email or `your-group@googlegroups.com`
   - **Content:**
     ```
     New signup from landing page!
     
     Email: {{user_email}}
     Time: {{timestamp}}
     Referrer: {{referrer}}
     ```
   - Note your **Template ID**

4. **Get Public Key:**
   - Dashboard → Account → General
   - Copy your **Public Key**

5. **Update `script.js`:**
   ```javascript
   const EMAILJS_PUBLIC_KEY = 'your_public_key';
   const EMAILJS_SERVICE_ID = 'service_abc123';
   const EMAILJS_TEMPLATE_ID = 'template_xyz789';
   ```

6. **Test:** Submit form and check your email!

### Sending to Google Groups

Set template's "To Email" to: `your-team@googlegroups.com`

Make sure group allows external posts:
- Google Groups → Settings → Permissions → Post → "Public"

---

## 🔧 Alternative: GitHub Issues

If you prefer GitHub Issues over email:

### Manual Workflow

1. Go to: https://github.com/qyntec/qyntec.ai/actions
2. Select "Process Email Signups"
3. Click "Run workflow"
4. Enter email address
5. Creates issue automatically

### Automated (via webhook)

Use Zapier/Make.com to trigger:
- Form submission → Webhook → GitHub Issues

See `WEBHOOK_TRIGGER.md` for details.

---

## 📊 View Submissions

### With EmailJS
- Check your email inbox
- Or EmailJS Dashboard → History

### With GitHub Issues
- https://github.com/qyntec/qyntec.ai/issues?q=label%3Aearly-access

### Fallback (localStorage)
If EmailJS isn't configured, emails are stored in browser localStorage.

Open browser console:
```javascript
JSON.parse(localStorage.getItem('earlyAccessEmails'))
```

---

## 🎨 Customization

### Colors
Edit `styles.css`:
```css
:root {
    --bg-primary: #0a0a0a;
    --accent-cyan: #00f5ff;
    --accent-blue: #0066ff;
}
```

### Content
Edit `index.html`:
- Update hero text
- Modify feature pills
- Change teaser question

### Branding
Replace logo SVG in header section.

---

## 🔒 Security

### EmailJS
- Public key is safe to expose
- Add domain whitelist: Dashboard → Security → Add `qyntec.github.io`
- Rate limiting prevents spam

### GitHub
- Never commit tokens to git
- Use GitHub Secrets for workflows
- Use fine-grained tokens with minimal permissions

---

## 📈 Analytics (Optional)

Add to `index.html` `<head>`:

**Google Analytics:**
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
```

**Plausible (privacy-friendly):**
```html
<script defer data-domain="qyntec.ai" src="https://plausible.io/js/script.js"></script>
```

---

## 🐛 Troubleshooting

### Form not submitting?
- Check browser console for errors
- Verify EmailJS keys are correct
- Check EmailJS quota (200/month free)

### Emails not arriving?
- Check spam folder
- Verify template "To Email" is correct
- Test template in EmailJS dashboard
- For Google Groups: check group permissions

### GitHub Pages not updating?
- Check Actions tab for build status
- Wait 1-2 minutes for deployment
- Clear browser cache

---

## 📝 Files Overview

- `index.html` - Main landing page
- `thank-you.html` - Success page (optional)
- `styles.css` - All styling
- `script.js` - Form handling & EmailJS
- `.github/workflows/` - GitHub Actions
- `README.md` - Project overview

---

## 🚀 Next Steps

1. ✅ Enable GitHub Pages
2. ✅ Set up EmailJS
3. ✅ Test form submission
4. ✅ Add custom domain (optional)
5. ✅ Add analytics (optional)

**Need help?** Check individual guides:
- `EMAILJS_SETUP.md` - Detailed EmailJS guide
- `WEBHOOK_TRIGGER.md` - GitHub webhook integration
- `FORM_SUBMISSION_OPTIONS.md` - Alternative solutions
