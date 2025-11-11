# Qyntec.ai Logo Components

This directory contains standalone logo components that can be used across different platforms.

## Files

### 1. `logo.html` + `logo.css`
**Use for:** Web applications, landing pages, web apps

- Clean HTML structure
- External CSS file
- No animations (static)
- Easy to integrate into React, Vue, or vanilla HTML

**Usage:**
```html
<link rel="stylesheet" href="components/logo.css">
<div>
  <!-- Include logo.html content here -->
</div>
```

### 2. `logo-email.html`
**Use for:** Email templates, newsletters, transactional emails

- Inline styles (email-safe)
- Table-based layout (maximum compatibility)
- No external dependencies
- Works in all major email clients (Gmail, Outlook, Apple Mail, etc.)

**Usage:**
Simply copy the entire content and paste it into your email template.

## Logo Specifications

### Colors
- **Primary (Emerald):** `#10b981`
- **Secondary (Teal):** `#06b6d4`
- **Text Secondary:** `#a0a0a0`

### Sizes
- **SVG:** 60x60px
- **Logo Text:** 2rem (32px)
- **Tagline:** 0.875rem (14px)

### Typography
- **Font Family:** Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
- **Logo Weight:** 700 (Bold)
- **Tagline Weight:** 400 (Regular)

## Notes

- All logo components are **static** (no animations) for maximum compatibility
- The animated version is only used on the main website
- SVG gradients are preserved for visual consistency
- Email version uses solid color fallback for text (gradient not supported in all email clients)

## Brand Guidelines

**Tagline:** "Re-architecting Healthcare, One Record at a Time."

**Do:**
- Use on dark backgrounds (#0a0a0a or darker)
- Maintain aspect ratio
- Keep adequate spacing around logo

**Don't:**
- Change colors
- Modify tagline text
- Add effects or filters
- Use on light backgrounds without adjustment
