# HealthTech Landing Page

Ultra-modern, minimal black-themed pre-launch landing page with glassmorphism effects.

## Features

- 🎨 **Glassmorphism Design** - Modern frosted glass UI elements
- 🌑 **Dark Theme** - Sleek black background with gradient accents
- ✨ **Animated Gradients** - Dynamic floating orb effects
- 📱 **Fully Responsive** - Optimized for all devices
- ⚡ **Pure Static** - No build process required
- 🚀 **Netlify Ready** - Configured for instant deployment

## Tech Stack

- Pure HTML5
- CSS3 (Glassmorphism, Animations, Grid/Flexbox)
- Vanilla JavaScript
- Google Fonts (Inter)

## Local Development

Simply open `index.html` in your browser. No build process needed.

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve

# Using PHP
php -S localhost:8000
```

Then visit `http://localhost:8000`

## Deployment

### GitHub Pages (Recommended)

1. Enable GitHub Pages in repository settings
2. Set source to `main` branch
3. Site will be live at `https://qyntec.github.io/qyntec.ai/`

See [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) for detailed instructions.

### Alternative: Netlify

```bash
netlify deploy --prod
```

## Customization

### Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --bg-primary: #0a0a0a;
    --accent-cyan: #00f5ff;
    --accent-blue: #0066ff;
}
```

### Content
- Update text in `index.html`
- Modify logo and branding
- Adjust feature cards

### Email Collection
Email signups create **GitHub Issues** automatically:
- Each submission creates an issue with `early-access` label
- View all signups: https://github.com/qyntec/qyntec.ai/issues?q=label%3Aearly-access
- Includes email, timestamp, and user agent
- Falls back to localStorage if GitHub API requires auth
- No backend or database required

**Setup:**
See [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) for enabling automatic issue creation

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## License

All rights reserved.
