# Content Update Guide — Village Naturopathy

All content updates are handled by your web team. This document outlines what's editable and how to request changes.

## Requesting Changes

Email your web team with the change you'd like. Include:
- Which page (e.g., "Fees page", "About page")
- Exact copy changes (old text → new text)
- Any new images (see image requirements below)

**Turnaround:** Routine text changes within 1-2 business days. New pages or structural changes may take longer and will be scoped separately.

## What's Editable

### Text & Copy
Any text on any page can be updated: headlines, body copy, fees, FAQs, service descriptions, program details, and contact information.

### Journal Articles
New articles can be added and existing ones updated. Provide:
- Title
- Category (Stress, Hormones, Gut Health, Mental Health, etc.)
- Body copy (can be a Google Doc or plain text)
- Featured image (optional)

### Testimonials
Testimonials are stored in `data/testimonials.json`. Each entry has:
```json
{
  "name": "First name + last initial",
  "location": "City, Province/Country",
  "condition": "Primary area of care",
  "quote": "The testimonial text",
  "rating": 5
}
```
Send new testimonials in this format or as plain text and we'll format them.

### Programs & Fees
All pricing, program descriptions, and fee schedules can be updated. Stripe payment links can be swapped when ready.

### Images
See requirements below.

## Image Requirements

| Use | Recommended size | Format | Notes |
|---|---|---|---|
| Hero / full-width | 1920 × 1080px min | JPG or WebP | Landscape, warm tones |
| Card / thumbnail | 800 × 600px min | JPG or WebP | 4:3 aspect ratio |
| Portrait | 800 × 1000px min | JPG or WebP | Heather portrait, lifestyle |
| Logo | Vector preferred | PNG or SVG | Transparent background |

- File names: lowercase, hyphens, no spaces (e.g., `heather-portrait-2.jpg`)
- Optimise before sending — aim for under 500KB per image
- We'll create WebP versions as needed

## What's NOT Editable Without Development

- Navigation structure
- Page layouts and section ordering
- Design system tokens (colours, fonts, spacing)
- Form logic and integrations
- Analytics and tracking setup

These changes require a development request.

## Stripe Payment Links

The site has placeholder Stripe links for program purchases. When you create your Stripe Payment Links, send us the URLs and we'll swap them in:

- **PMOS Playbook:** `PLACEHOLDER_PMOS_PLAYBOOK`
- **The Regulate Method:** `PLACEHOLDER_REGULATE_METHOD`
- **Essential Health (e-book):** `PLACEHOLDER_ESSENTIAL_HEALTH`
- **7-Day Habit Tracker:** `PLACEHOLDER_HABIT_TRACKER`

## Formspree

The contact form uses Formspree. To activate it:
1. Create a free account at [formspree.io](https://formspree.io)
2. Create a new form and copy the form ID
3. Send us the form ID to replace `PLACEHOLDER_FORM_ID` in the contact page
