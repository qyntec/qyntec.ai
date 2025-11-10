# HealthTech Landing Page

Ultra-modern, minimal black-themed pre-launch landing page with glassmorphism effects.

## ✨ Features

- 🎨 **Glassmorphism Design** - Modern frosted glass UI elements
- 🌑 **Dark Theme** - Sleek black background with gradient accents
- ✨ **Animated Gradients** - Dynamic floating orb effects
- 📱 **Fully Responsive** - Optimized for all devices
- ⚡ **Pure Static** - No build process required
- 📧 **Email Notifications** - EmailJS integration for instant alerts

## 🚀 Quick Start

### Local Development
```bash
python -m http.server 8000
# or
npx serve
```
Visit `http://localhost:8000`

### Deploy to GitHub Pages
1. Push to GitHub
2. Enable GitHub Pages in Settings → Pages
3. Live at: `https://qyntec.github.io/qyntec.ai/`

**Full setup guide:** See [SETUP.md](SETUP.md)

## 📧 Email Setup

Configure EmailJS to receive signup notifications:

1. Sign up at [emailjs.com](https://www.emailjs.com/)
2. Get your keys
3. Update `script.js` with your credentials

**Detailed guide:** See [EMAILJS_SETUP.md](EMAILJS_SETUP.md)

## 🎨 Customization

Edit `styles.css` for colors:
```css
:root {
    --bg-primary: #0a0a0a;
    --accent-cyan: #00f5ff;
    --accent-blue: #0066ff;
}
```

Edit `index.html` for content.

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Complete deployment guide
- **[EMAILJS_SETUP.md](EMAILJS_SETUP.md)** - Email notification setup
- **[WEBHOOK_TRIGGER.md](WEBHOOK_TRIGGER.md)** - GitHub webhook integration

## 🛠️ Tech Stack

- Pure HTML5, CSS3, Vanilla JavaScript
- EmailJS for email notifications
- GitHub Pages for hosting
- Google Fonts (Inter)

## 📄 License

All rights reserved.
