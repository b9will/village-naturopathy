# Website revisions: status (Oct 25, 2026)

Source: "Village Naturopathy: Website Revisions" (Heather, Oct 2026). Staging: https://village-naturopathy.will-69d.workers.dev/

## Done
- All site-wide rules (focus, no menopause/CBT/psychotherapy/"psychologist", Regulate Method rename, acne, PMOS/PCOS, PMS, "Virtual consultations", "Notes on being well", em dashes, focus order, 75-minute consult, italic testing note, Jane links, FAQPage schema).
- Page changes for Home, About, Services (+ UK Treatment Packages card), Fees (GBP + CAD, packages section), Programs, Journal heading, and the Stress, Hormone, Gut and Fatigue pages.
- Fatigue page replaces Mental Health: `/services/mental-health-counselling/` 301s to `/services/fatigue/`.
- Mental health condition page folded into Stress (301). Skin condition page rebuilt as "Acne & Hormonal Skin Health" (301 from old URL).
- Single Jane account: the Ontario/UK region modal is gone; every booking button goes to Jane. `book.html` is kept as a simple two-button page (discovery call / consultation).
- "Request a consultation" / "Book a consult" buttons point to the Jane booking link (this was an open question; easy to revert).
- Homepage testimonials section removed until Heather confirms testimonials are allowed.
- Programs show "Coming soon"; placeholder Stripe links and the "30-day money-back guarantee" line were removed from the program pages.

## Waiting on Heather (not built; see the Open questions in the Google Doc)
Testimonials allowed? / follow-up length (30-60 vs 15-60) / keep "Holistic Health Coaching"? / add fertility to condition lists / Fatigue above Gut / hero eyebrow / "Physical & spiritual" subheading / soften "clinical psychology" / "skin conditions" vs "acne" on About / "third brain" / "Hormonal hair loss" / "adrenal fatigue" vs "stress-related fatigue" / "Mental health" journal category / draft FAQ answers and UK package descriptions (package text on Fees is a DRAFT: replace with the exact text from Jane).

## Needs a decision or setup (not just copy)
- Program checkout (Stripe Payment Links is the lightest option; Shopify also works).
- Free guide + email list platform (Kit, Flodesk or Mailchimp), then the sitewide pop-up.
- Journal CMS so Heather can publish herself (posts link out to Substack).
- Contact form: `action` is still `https://formspree.io/f/PLACEHOLDER_FORM_ID`.
- GA4: `<meta name="ga-id">` is still `G-XXXXXXXXXX` (analytics never loads).
- In Jane (not the website): CAD fee note, bio mentioning the Holistic Stress Solution, "Mental health" new-patient item.
