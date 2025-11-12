# Qyntec.ai Assets

## Essential Files (Foundation)

### Logo Files (SVG - Scalable, Editable)
- **logo-icon-only.svg** - Heart icon only (752 B)
- **logo-with-name.svg** - Logo with "Qyntec.ai" text (911 B)
- **logo-full.svg** - Full logo with tagline (1.1 KB)
- **linkedin-banner-v4.svg** - LinkedIn banner (9.2 KB)

### Raster Preview
- **logo-icon-only.png** - PNG preview of icon (6.5 KB)

### Animated Logo
- **qyntec-logo-animated.gif** - Animated heart with pulse (100x100, 101 KB)
  - Transparent background
  - 72 BPM heartbeat (medically accurate)
  - 5 complete heartbeat cycles

### Build Tools
- **create-favicon.js** - Script to regenerate favicons
- **logo-animation-icon-only.html** - HTML template for animations

## Favicon Files (In Root Directory)

- **favicon.ico** - Multi-size ICO (16x16, 32x32, 64x64) - 19 KB
- **favicon-32x32.png** - High-quality PNG favicon - 722 B
- **favicon.gif** - Animated favicon (64x64) - 80 KB

## File Format Guide

### When to Use Each Format:

**SVG (Foundation Format)**
- ✅ Best for: Logos, icons, graphics
- ✅ Scalable to any size without quality loss
- ✅ Editable in design tools
- ✅ Smallest file size
- ❌ Not for photos or complex images

**PNG**
- ✅ Best for: Raster images with transparency
- ✅ Lossless compression
- ✅ Good for favicons, screenshots
- ❌ Larger file size than SVG for graphics

**GIF**
- ✅ Best for: Simple animations
- ✅ Transparent background support
- ❌ Limited to 256 colors
- ❌ Larger file size

**ICO**
- ✅ Best for: Browser favicons (maximum compatibility)
- ✅ Can contain multiple sizes in one file
- ❌ Only for favicons

## Regenerating Favicons

```bash
cd assets
node create-favicon.js
cp favicon-animated.gif ../favicon.gif
cp favicon.ico ../
cp favicon-32x32.png ../
```

## Animation Details

- **Heart Rate**: 72 BPM (0.833s per beat)
- **Duration**: 4.165s (5 complete beats)
- **FPS**: 20
- **Quality**: 4x supersampling for smooth edges
- **Background**: Transparent
