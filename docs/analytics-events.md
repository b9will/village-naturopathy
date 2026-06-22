# Analytics Events — Village Naturopathy

Provider: [Plausible Analytics](https://plausible.io) (privacy-respecting, cookieless)
Gated behind cookie consent "analytics" toggle for PHIPA transparency.

## Conversion Events

| Event Name | Trigger | Notes |
|---|---|---|
| `CTA_Book` | Click on any `a[href*="book.html"]` link | Fires on all pages — nav CTA, hero buttons, section CTAs, footer |
| `Modal_BookingOpen` | Booking region modal opens (`.open` class added) | Only fires on pages without `.booking-split` (modal pages) |
| `Form_ContactSubmit` | Contact form submitted successfully via Formspree | Fires after 200 response from Formspree |
| `Form_BookingSubmit` | Booking form submitted successfully via Formspree | Fires after 200 response from Formspree |

## A/B Test Events

| Event Name | Trigger | Props |
|---|---|---|
| `AB_Variant` | Page load when an A/B test is active | `test`: test name, `variant`: variant index |

## Core Web Vitals

| Event Name | Trigger | Props |
|---|---|---|
| `CWV_LCP` | Largest Contentful Paint measured | `value`: ms (rounded), `rating`: good/needs-improvement/poor |
| `CWV_CLS` | Cumulative Layout Shift measured | `value`: score × 1000 (rounded), `rating` |
| `CWV_INP` | Interaction to Next Paint measured | `value`: ms (rounded), `rating` |
| `CWV_FCP` | First Contentful Paint measured | `value`: ms (rounded), `rating` |
| `CWV_TTFB` | Time to First Byte measured | `value`: ms (rounded), `rating` |

## Implementation

- Plausible script loaded dynamically by `loadAnalytics()` in `js/main.js`
- Only loads after user accepts analytics in cookie consent
- Custom events use `plausible('EventName', { props: { ... } })`
- web-vitals library loaded from CDN after Plausible initializes
- Domain configured via `<meta name="plausible-domain">` tag in each page
