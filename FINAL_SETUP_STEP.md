# Final Setup Step - Create Email Template

Your EmailJS credentials are already configured! Just one more step:

## Create Email Template (2 minutes)

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
