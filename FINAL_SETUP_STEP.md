# Final Setup Steps - Service ID & Template

Your EmailJS **Public Key** is configured: `cMYkn122AR65PvXmE` ✅

Now you need to get your **Service ID** and create a **Template**:

---

## Step 1: Get Your Service ID

1. **Go to Email Services:**
   https://dashboard.emailjs.com/admin

2. **Look for your email service** (Gmail, Outlook, etc.)

3. **Copy the Service ID** (looks like: `service_abc123xyz`)
   - It's shown in the service card

4. **Update `script.js` line 4:**
   ```javascript
   const EMAILJS_SERVICE_ID = 'service_abc123xyz'; // Your service ID here
   ```

---

## Step 2: Create Email Template (2 minutes)

1. **Go to EmailJS Dashboard:**
   https://dashboard.emailjs.com/admin/templates

2. **Click "Create New Template"**

3. **Fill in the template:**

   **Template Name:** `early_access_signup`

   **Subject:**
   ```
   New Early Access Signup: {{user_email}}
   ```

   **Content:**
   ```
   New early access signup from qyntec.ai landing page!

   📧 Email: {{user_email}}
   🕐 Time: {{timestamp}}
   🌐 Referrer: {{referrer}}
   🔗 Page: {{page_url}}
   💻 Browser: {{user_agent}}

   ---
   Sent via EmailJS from qyntec.ai
   ```

   **To Email:** 
   - Your email: `your-email@gmail.com`
   - Or Google Group: `your-group@googlegroups.com`

4. **Click "Save"**

5. **Copy the Template ID** (looks like: `template_abc123xyz`)

6. **Update `script.js`:**
   - Open `script.js`
   - Find line 5: `const EMAILJS_TEMPLATE_ID = 'YOUR_TEMPLATE_ID';`
   - Replace with your template ID: `const EMAILJS_TEMPLATE_ID = 'template_abc123xyz';`

7. **Commit and push:**
   ```bash
   git add script.js
   git commit -m "Add EmailJS template ID"
   git push
   ```

## Test It!

1. Open your GitHub Pages site: https://qyntec.github.io/qyntec.ai/
2. Submit an email
3. Check your inbox!

## Troubleshooting

### Not receiving emails?

1. **Check EmailJS Dashboard:**
   - Go to: https://dashboard.emailjs.com/admin/history
   - See if emails are being sent

2. **Check spam folder**

3. **Verify template "To Email"** is correct

4. **Test template:**
   - In EmailJS dashboard
   - Click "Test" button on your template

### For Google Groups:

Make sure your group allows external posts:
- Google Groups → Settings → Permissions → Post
- Set to "Public" or "Anyone on the web"

## Security (Optional)

Add domain whitelist to prevent abuse:

1. Go to: https://dashboard.emailjs.com/admin/account
2. Click "Security" tab
3. Add allowed domain: `qyntec.github.io`
4. Save

This prevents others from using your EmailJS credentials on different domains.

## That's It!

Your landing page is now fully functional:
- ✅ Beautiful glassmorphism design
- ✅ Email notifications via EmailJS
- ✅ Deployed on GitHub Pages
- ✅ No backend needed

Every form submission will send you an email instantly! 🎉
