# Deployment Instructions

## Option 1: Netlify CLI (Recommended)

1. **Initialize the project:**
   ```bash
   cd /home/shree/src/qyntec
   netlify init
   ```
   
   Follow the prompts:
   - Choose "Yes, create and deploy project manually"
   - Enter a site name (e.g., "healthtech-prelaunch")
   - Set publish directory to "." (current directory)
   
2. **Deploy to production:**
   ```bash
   netlify deploy --prod
   ```

## Option 2: Netlify Web UI

1. Go to [app.netlify.com](https://app.netlify.com)
2. Click "Add new site" → "Deploy manually"
3. Drag and drop the `/home/shree/src/qyntec` folder
4. Your site will be live instantly!

## Option 3: Git + Netlify (Best for continuous deployment)

1. **Initialize git repository:**
   ```bash
   cd /home/shree/src/qyntec
   git init
   git add .
   git commit -m "Initial commit: Health tech landing page"
   ```

2. **Push to GitHub:**
   ```bash
   gh repo create healthtech-landing --public --source=. --push
   ```
   
   Or manually:
   - Create a new repository on GitHub
   - Add remote: `git remote add origin <your-repo-url>`
   - Push: `git push -u origin main`

3. **Connect to Netlify:**
   - Go to [app.netlify.com](https://app.netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Choose GitHub and select your repository
   - Netlify will auto-detect settings from `netlify.toml`
   - Click "Deploy site"

## Custom Domain

After deployment, you can add a custom domain:

1. Go to Site settings → Domain management
2. Click "Add custom domain"
3. Follow DNS configuration instructions

## Netlify Forms Setup

Email submissions are automatically handled by Netlify Forms:

1. **After deployment**, Netlify will detect the form in `index.html`
2. **View submissions**: Site dashboard → Forms tab
3. **Notifications**: Site settings → Forms → Form notifications
   - Set up email notifications for new submissions
   - Integrate with Slack, Zapier, or webhooks

**Form Features:**
- ✅ Spam protection (honeypot field included)
- ✅ Email validation
- ✅ Export submissions as CSV
- ✅ Free tier: 100 submissions/month
- ✅ Paid tier: Unlimited submissions

## Environment Variables

No environment variables needed for basic deployment.
For advanced integrations, add in Netlify UI:
- Site settings → Environment variables

## Site URL

After deployment, your site will be available at:
- `https://[site-name].netlify.app`
- Or your custom domain if configured
