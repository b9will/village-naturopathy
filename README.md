# Village Naturopathy — Website

A static, dependency-free website (vanilla HTML/CSS/JS) for Village Naturopathy. No build step, no framework — open `index.html` and it runs. Designed to score 100/100/100/100 on [PageSpeed Insights](https://pagespeed.web.dev/) and to grow into a multi-page site.

## Structure
```
site/
├── index.html          # Homepage
├── css/styles.css      # Self-contained styles + design tokens (AA-clean)
├── js/main.js          # Tiny progressive enhancement (mobile menu only)
├── assets/images/      # Brand photography  ⚠️ replace with optimized AVIF/WebP
├── favicon.svg         # Monogram favicon
├── site.webmanifest    # PWA manifest
├── robots.txt          # Crawl rules
├── sitemap.xml         # Sitemap (update when you add pages)
├── _headers            # Cloudflare: security headers + caching
├── _redirects          # Cloudflare: redirects (empty starter)
└── .gitignore
```

The design tokens (colors, type, spacing) mirror the Village Naturopathy **design system** — keep them in sync if the system changes.

## Run locally
No tooling needed. Any static server works, e.g.:
```bash
cd site
python3 -m http.server 8080      # → http://localhost:8080
# or:  npx serve .
```

## Ship: Git → Cloudflare Pages
1. **Create the repo** (run inside `site/`, or move these files to your repo root):
   ```bash
   git init && git add . && git commit -m "Initial Village Naturopathy site"
   git branch -M main
   git remote add origin git@github.com:YOUR_ORG/village-naturopathy.git
   git push -u origin main
   ```
2. **Cloudflare Pages** → *Create application* → *Pages* → *Connect to Git* → pick the repo.
3. Build settings:
   - **Framework preset:** None
   - **Build command:** *(leave empty)*
   - **Build output directory:** `/` (or `site` if these files live in a subfolder of the repo)
4. Deploy. Add your custom domain under *Custom domains* (Cloudflare auto-provisions HTTPS).
5. `_headers` and `_redirects` are picked up automatically by Pages.

## PageSpeed Insights — 100/100/100/100 checklist
Most of this is already done; the ⚠️ items are the finishing steps that need real assets.

**Performance**
- [x] Static HTML, near-zero JS (deferred, ~0.8 KB)
- [x] LCP hero image preloaded + `fetchpriority="high"`; all other images `loading="lazy"`
- [x] Every `<img>` has `width`/`height` → CLS ≈ 0
- [x] Fonts loaded non-render-blocking; `display=swap`
- [ ] ⚠️ **Replace `assets/images/` with optimized AVIF + WebP**, sized to display. The current images are low-res crops from the brand direction. Add `<picture>` with AVIF/WebP/JPG sources and a real `srcset`.
- [ ] ⚠️ **Self-host the fonts** (Playfair Display + licensed Neue Haas Grotesk) as subset `.woff2`, `<link rel="preload">` the two above-the-fold weights, and add `size-adjust`/`ascent-override` fallback `@font-face` to remove the last sliver of font-swap CLS. This also removes the Google Fonts third-party connection.
- [ ] Enable Brotli (on by default at Cloudflare).

**Accessibility**
- [x] Semantic landmarks (`header`/`nav`/`main`/`footer`), skip link, one `h1`, ordered headings
- [x] Descriptive `alt` on every image; `aria-label`/`aria-current`/`aria-expanded` on nav
- [x] AA contrast for all body-size text (tokens were audited and corrected)
- [x] Visible `:focus-visible` rings; `prefers-reduced-motion` honored

**Best Practices**
- [x] Strict CSP + security headers (`_headers`); HTTPS via Cloudflare; no console errors

**SEO**
- [x] Unique `<title>` + meta description, canonical, Open Graph/Twitter
- [x] `MedicalBusiness` JSON-LD structured data
- [x] `robots.txt` + `sitemap.xml`, mobile-friendly viewport

## Growing the site
- Add pages as sibling `.html` files (e.g. `about.html`, `journal.html`); reuse `css/styles.css`.
- Add each new URL to `sitemap.xml`.
- For a real booking flow, replace the `mailto:` CTA with a form posting to your provider (or a Cloudflare Pages Function under `/functions`).
- Consider extracting the header/footer into a small include step (or migrating to Astro) once you have several pages — the markup is framework-agnostic and ports directly.

## Notes & caveats
- **Imagery** is placeholder-grade (low-res). Swap in licensed, optimized photography before launch.
- **Neue Haas Grotesk** is a licensed font; body text currently uses its Helvetica Neue fallback until the `.woff2` files are added.
