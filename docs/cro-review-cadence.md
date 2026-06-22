# CRO Review Cadence — Village Naturopathy

## Monthly Review (15 minutes)

Check GA4 dashboard for:
- **Total pageviews** — trending up, flat, or down?
- **Top pages** — which pages get the most traffic?
- **Referral sources** — where are visitors coming from?
- **Conversion events** — how many CTA_Book, Form_ContactSubmit, Modal_BookingOpen?
- **Bounce rate by page** — any pages losing visitors immediately?

## Quarterly CRO Check (1 hour)

### Metrics to review
- **Hero engagement:** Are visitors scrolling past the hero? (Check if pages beyond the fold get views)
- **CTA click rate:** CTA_Book events / total pageviews — is it improving?
- **Form completion rate:** Form_ContactSubmit / contact page views
- **Booking modal usage:** Modal_BookingOpen events — are people clicking through?

### Action items
- If hero engagement is low → consider testing new headline (use A/B test)
- If CTA clicks are low → test button copy, colour, or placement
- If form completion is low → check for UX issues, simplify the form
- If a landing page has high traffic but low conversion → review copy and CTA positioning

## A/B Testing

### How to run a test
1. Open `data/ab-tests.json`
2. Set `"active": true` on the test you want to run
3. Commit and push — the test starts immediately
4. Let it run for at least 2 weeks or 200 visits (whichever is longer)
5. Check GA4 for `AB_Variant` events — compare conversion rates between variants
6. Set the winning variant as the default text and set `"active": false`

### How to interpret results
- **Clear winner (>10% difference with 200+ visits per variant):** Implement the winner
- **No clear winner:** The difference isn't meaningful — keep the original or test something bigger
- **Surprising loser:** Check if the losing variant had a technical issue before discarding

### What to test (priority order)
1. Hero headline — biggest impact on first impression
2. Primary CTA copy — "Request a consultation" vs "Book your discovery call"
3. Social proof placement — testimonials above or below services
4. Pricing presentation — monthly vs one-time framing on program pages
5. Hero image — different portraits or lifestyle imagery

## Core Web Vitals

Check quarterly via GA4 CWV events:
- **LCP** (Largest Contentful Paint) — target < 2.5s
- **INP** (Interaction to Next Paint) — target < 200ms
- **CLS** (Cumulative Layout Shift) — target < 0.1

If any metric trends into "needs improvement" or "poor," investigate:
- LCP: image optimisation, font loading, server response time
- INP: heavy JavaScript, long event handlers
- CLS: images without dimensions, dynamically injected content
