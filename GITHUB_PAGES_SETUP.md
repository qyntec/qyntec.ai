## GitHub Pages Deployment

### Enable GitHub Pages

1. Go to your repository: https://github.com/qyntec/qyntec.ai
2. Click **Settings** → **Pages**
3. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main` / `(root)`
4. Click **Save**

Your site will be available at: `https://qyntec.github.io/qyntec.ai/`

### Form Submissions → GitHub Issues

The landing page form automatically creates GitHub Issues for each signup:

**How it works:**
1. User submits email on landing page
2. JavaScript attempts to create a GitHub Issue via API
3. If API requires auth (which it does for public repos), it falls back to localStorage
4. You can manually review submissions in browser console or localStorage

**To enable automatic issue creation:**

#### Option 1: GitHub Personal Access Token (Recommended)
1. Create a fine-grained personal access token:
   - Go to https://github.com/settings/tokens?type=beta
   - Click "Generate new token"
   - Repository access: Only select repositories → `qyntec.ai`
   - Permissions: Issues → Read and write
   - Generate token

2. Add token to your site (for testing locally):
   ```javascript
   // In script.js, add before the fetch call:
   headers: {
       'Authorization': 'Bearer YOUR_TOKEN_HERE',
       'Content-Type': 'application/json',
       'Accept': 'application/vnd.github.v3+json'
   }
   ```

#### Option 2: GitHub Actions Workflow (Better for production)
Create `.github/workflows/process-signups.yml`:

```yaml
name: Process Email Signups

on:
  workflow_dispatch:
    inputs:
      email:
        description: 'Email address'
        required: true

jobs:
  create-issue:
    runs-on: ubuntu-latest
    steps:
      - name: Create Issue
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: `Early Access Signup: ${{ github.event.inputs.email }}`,
              body: `## New Early Access Signup\n\n**Email:** ${{ github.event.inputs.email }}\n**Timestamp:** ${new Date().toISOString()}`,
              labels: ['early-access', 'signup']
            });
```

#### Option 3: Use GitHub Issue Forms
Users can click a link to create an issue directly:
- Link: https://github.com/qyntec/qyntec.ai/issues/new?template=early-access-signup.yml

### View Submissions

All signups will appear as GitHub Issues with the `early-access` label:
https://github.com/qyntec/qyntec.ai/issues?q=is%3Aissue+label%3Aearly-access

### Custom Domain (Optional)

1. Add a `CNAME` file with your domain:
   ```
   qyntec.ai
   ```

2. Configure DNS:
   - Add CNAME record pointing to `qyntec.github.io`
   - Or A records pointing to GitHub Pages IPs

3. In GitHub Settings → Pages, add your custom domain

### Analytics (Optional)

Add Google Analytics or Plausible to track visitors:

```html
<!-- Add to index.html <head> -->
<script defer data-domain="qyntec.ai" src="https://plausible.io/js/script.js"></script>
```
