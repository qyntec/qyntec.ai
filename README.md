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

This site is configured for Netlify deployment:

1. Push to GitHub
2. Connect repository to Netlify
3. Deploy automatically

Or use Netlify CLI:

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
Email signups are handled via **Netlify Forms**:
- Automatically captures submissions when deployed to Netlify
- Access submissions in Netlify Dashboard → Forms
- No backend required - works out of the box
- Includes spam protection with honeypot field
- Can integrate with Zapier, Mailchimp, or other services via Netlify

**To view submissions:**
1. Deploy to Netlify
2. Go to your site dashboard
3. Click "Forms" in the sidebar
4. View all early access signups

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## License

All rights reserved.
