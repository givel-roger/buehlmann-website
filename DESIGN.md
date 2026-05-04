---
name: Swiss Artisan System
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#454651'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#757683'
  outline-variant: '#c5c5d3'
  surface-tint: '#4658ac'
  primary: '#000a3f'
  on-primary: '#ffffff'
  primary-container: '#001a72'
  on-primary-container: '#7688e0'
  inverse-primary: '#b9c3ff'
  secondary: '#6d5e00'
  on-secondary: '#ffffff'
  secondary-container: '#fddc00'
  on-secondary-container: '#706000'
  tertiary: '#0e1215'
  on-tertiary: '#ffffff'
  tertiary-container: '#232729'
  on-tertiary-container: '#8a8e91'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dee1ff'
  primary-fixed-dim: '#b9c3ff'
  on-primary-fixed: '#001258'
  on-primary-fixed-variant: '#2d3f93'
  secondary-fixed: '#ffe24a'
  secondary-fixed-dim: '#e3c600'
  on-secondary-fixed: '#211b00'
  on-secondary-fixed-variant: '#524600'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c3c7ca'
  on-tertiary-fixed: '#181c1e'
  on-tertiary-fixed-variant: '#43474a'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  section-padding: 80px
---

## Brand & Style

This design system is built upon the principles of Swiss Design: precision, legibility, and objectivity. It reflects the meticulous craftsmanship of a premium painting company based in Lucerne, balancing the traditional values of a family business with a modern, expert-led service model. 

The visual direction follows a **Corporate / Modern** style. It utilizes structured layouts, intentional white space, and a disciplined color application to evoke a sense of reliability and architectural quality. The UI should feel as organized and clean as a freshly painted high-end interior. The target audience includes both residential homeowners looking for quality and commercial developers seeking professional reliability.

## Colors

The palette is derived directly from the heritage of the company logo. 

*   **Primary (Deep Blue):** Used for navigation, headings, and primary buttons. It represents authority, depth, and Swiss excellence.
*   **Secondary (Sun Yellow):** An energetic accent color used sparingly for calls to action, highlights, and status indicators. It mimics the vibrancy of light reflecting off a perfect finish.
*   **Neutrals:** A range of cool grays and off-whites are used to provide the "canvas." Backgrounds should primarily stay in the light spectrum to maintain a clean, airy feel.
*   **Semantic Colors:** Success (Green), Warning (Amber), and Error (Red) should be desaturated to align with the professional blue.

## Typography

This design system utilizes **Inter** for all typographic needs. Its neutral, utilitarian character provides the high legibility required for a professional service brand.

Headlines should be set with tighter letter-spacing and bold weights to command attention. Body text favors a generous line height (1.5 - 1.6) to ensure readability for detailed service descriptions. Labels and small metadata should be set in uppercase with slight tracking to provide a technical, "blueprint" feel to the interface.

## Layout & Spacing

The layout is based on a **12-column fixed grid** for desktop, ensuring content remains centered and readable on ultra-wide displays. A strict 8px base unit (the "rhythm") governs all padding and margins.

Vertical rhythm is prioritized; large sections should be separated by significant whitespace (80px or more) to emphasize the "clean" brand promise. Components like service cards and blog entries should use the 24px gutter for consistent separation.

## Elevation & Depth

To maintain the Swiss modernist aesthetic, elevation is achieved through **low-contrast outlines** and **tonal layers** rather than heavy shadows.

*   **Surfaces:** Cards use a thin 1px border (#E2E8F0) against a white background.
*   **Interactive State:** On hover, a card may lift using a very soft, diffused shadow (0px 10px 20px rgba(0, 26, 114, 0.05)).
*   **Depth:** Use the Tertiary color (#F4F7FA) as a background for sections to differentiate from the primary white surface, creating a subtle "stacked" feel without visual clutter.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding removes the harshness of sharp corners while maintaining a structured, architectural feel. 

Large-scale components like hero sections or full-width images should remain sharp (0px) to anchor the page, while interactive elements like buttons and input fields utilize the soft rounding.

## Components

### Buttons
*   **Primary:** Deep Blue background, white text, 0.25rem corner radius. High-emphasis.
*   **Secondary:** Sun Yellow background, Deep Blue text. Used exclusively for "Get a Quote" or urgent CTAs.
*   **Ghost:** Transparent background with Deep Blue border.

### Service Showcases
Service components should feature a large, high-resolution image followed by a "headline-md" and a brief description. Use a 1px border container. Include a "Label-md" tag above the title to categorize the service (e.g., EXTERIOR, INTERIOR, RENOVATION).

### Blog & Project Cards
Cards should utilize a 3:2 image aspect ratio. The typography should emphasize the date and category in a small uppercase label font. The title should use "headline-md" with a maximum of two lines.

### Contact Form
Inputs should have a 1px gray border that transitions to Deep Blue on focus. Labels must be clearly visible above the field in "label-md" style. The submit button should be full-width on mobile to ensure ease of use for clients on-site.

### Lists
Use custom Deep Blue checkmarks for "Our Guarantees" or "Service Inclusions" lists to reinforce the brand identity and the concept of "work completed."