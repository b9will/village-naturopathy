#!/usr/bin/env python3
"""Shared building blocks for Village Naturopathy generated pages.

Used by generate_landing_pages.py (services + conditions), generate_geo_pages.py
(UK location pages) and build_site.py (sitemap, llms.txt, markdown mirrors).
Everything that must stay identical site-wide (nav, footer, entity schema,
booking links, prices) lives here so there is one place to change it.
"""
import html
import json
import re

BASE = "https://villagenaturopathy.com"
EMAIL = "drheather@villagenaturopathy.com"
LASTMOD = "2026-10-25"
ASSET_V = "20261026"  # bump when css/js change (they are cached as immutable)

# Booking (single Jane account, Oct 2026)
JANE_BOOK = "https://villagenaturopathy.janeapp.com/#/staff_member/1"
JANE_DISC = "https://villagenaturopathy.janeapp.com/#/staff_member/1/treatment/36"
JANE_PKG = "https://villagenaturopathy.janeapp.com/#packages"

# Fees shown to UK visitors (GBP). CAD figures live on fees.html only.
FEE_INITIAL = "&pound;200"
FEE_FOLLOWUP = "&pound;50&ndash;170"

SOCIALS = [
    "https://www.facebook.com/villagenaturopathy",
    "https://www.instagram.com/villagenaturopathy",
]

DISCLAIMER = (
    "Naturopathic care is complementary and does not replace advice from your GP or other "
    "healthcare professional. If your symptoms are severe, sudden or worrying, contact your GP or "
    "local urgent care service, or call 999 in an emergency."
)


# ---------------------------------------------------------------- text helpers
def plain(s):
    """HTML-entity string -> plain text (for JSON-LD, markdown, meta)."""
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def attr(s):
    """Escape for use inside a double-quoted HTML attribute."""
    return html.escape(plain(s), quote=True)


def ld(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------- icons
ICONS = {
    "clipboard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25z"/></svg>',
    "flask": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l.051.054c.649.685.507 1.794-.296 2.273A12.56 12.56 0 0112 19.5a12.56 12.56 0 01-7.555-2.373c-.803-.479-.945-1.588-.296-2.273L4.2 13.854"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/></svg>',
    "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15.75 10.5l4.72-4.72a.75.75 0 011.28.53v11.38a.75.75 0 01-1.28.53l-4.72-4.72M4.5 18.75h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25h-9A2.25 2.25 0 002.25 7.5v9a2.25 2.25 0 002.25 2.25z"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5a17.92 17.92 0 01-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"/></svg>',
}

FB_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>'
IG_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>'
MENU_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'
ANGLE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4.26 10.147a60.438 60.438 0 00-.491 6.347A48.62 48.62 0 0112 20.904a48.62 48.62 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.636 50.636 0 00-2.658-.813A59.906 59.906 0 0112 3.493a59.903 59.903 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.717 50.717 0 0112 13.489a50.702 50.702 0 017.74-3.342"/></svg>'


# ---------------------------------------------------------------- chrome
def nav_html(rel):
    return f'''  <header class="site-header">
      <nav class="nav" id="nav" aria-label="Primary">
        <ul class="nav-links">
          <li><a href="{rel}about.html">About</a></li>
          <li><a href="{rel}services.html">Services</a></li>
          <li class="nav-brand"><a class="brand" href="{rel}index.html" aria-label="Village Naturopathy home"><img src="{rel}assets/images/village-logo-white.png" alt="Village Naturopathy" height="36"></a></li>
          <li><a href="{rel}journal.html">Journal</a></li>
          <li><a href="{rel}resources.html">Programs</a></li>
        </ul>
        <a class="btn btn--warm btn--sm nav-cta" href="{JANE_BOOK}" target="_blank" rel="noopener noreferrer">Book now</a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Toggle menu">
          {MENU_SVG}
        </button>
      </nav>
  </header>'''


def footer_html(rel):
    return f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <span class="brand"><img src="{rel}assets/images/village-logo-black.png" alt="Village Naturopathy" height="128"></span>
          <p>Root-cause naturopathic care for women navigating stress, hormones, and everything in between.</p>
          <div class="footer-social">
            <a href="{SOCIALS[0]}" target="_blank" rel="noopener noreferrer" aria-label="Facebook">{FB_SVG}</a>
            <a href="{SOCIALS[1]}" target="_blank" rel="noopener noreferrer" aria-label="Instagram">{IG_SVG}</a>
          </div>
        </div>
        <div class="footer-col">
          <span class="footer-col-title">Clinic</span>
          <a href="{rel}about.html">About Dr. Heather</a>
          <a href="{rel}services.html">Services</a>
          <a href="{rel}conditions.html">Conditions Treated</a>
          <a href="{rel}fees.html">Fees</a>
          <a href="{JANE_BOOK}" target="_blank" rel="noopener noreferrer">Book Now</a>
          <a href="{rel}careers.html">Careers</a>
        </div>
        <div class="footer-col">
          <span class="footer-col-title">Online naturopath UK</span>
          <a href="{rel}uk/">UK overview</a>
          <a href="{rel}uk/london/">London</a>
          <a href="{rel}uk/edinburgh/">Edinburgh</a>
          <a href="{rel}uk/glasgow/">Glasgow</a>
          <a href="{rel}uk/belfast/">Belfast</a>
          <a href="{rel}uk/dutch-test/">DUTCH hormone test</a>
        </div>
        <div class="footer-col">
          <span class="footer-col-title">Programs</span>
          <a href="{rel}programs/regulate-method/">The Regulate Method</a>
          <a href="{rel}programs/pmos-playbook/">PMOS Playbook</a>
          <a href="https://wholewomanreset.co.uk/" target="_blank" rel="noopener noreferrer">Whole Woman Reset</a>
          <a href="https://ca.fullscript.com/welcome/villagenaturopathy/store-start" target="_blank" rel="noopener noreferrer">Fullscript</a>
        </div>
        <div class="footer-col">
          <span class="footer-col-title">Learn</span>
          <a href="{rel}journal.html">The Journal</a>
          <a href="{rel}resources.html">Resources</a>
          <a href="{rel}about.html#approach">Our Approach</a>
          <a href="{rel}about.html#faq-title">FAQs</a>
        </div>
        <div class="footer-col">
          <span class="footer-col-title">Connect</span>
          <div class="footer-contact-item">
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </div>
          <div class="footer-contact-item">
            <p>Virtual clinic serving<br>the United Kingdom &amp; Ontario</p>
          </div>
          <div class="footer-contact-item">
          <div class="footer-clocks" id="footer-clocks">
              <div class="footer-clock">
                <span class="footer-clock-label"><img src="{rel}assets/images/flag-uk.svg" alt="" width="16" height="12"> London</span>
                <span class="clock-time" data-tz="Europe/London"></span>
              </div>
              <div class="footer-clock">
                <span class="footer-clock-label"><img src="{rel}assets/images/flag-canada.svg" alt="" width="16" height="12"> Ontario</span>
                <span class="clock-time" data-tz="America/Toronto"></span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-cta">
        <a class="btn btn--sage" href="{JANE_DISC}" target="_blank" rel="noopener noreferrer">Schedule a discovery call</a>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Dr. Heather Robinson, ND &middot; Village Naturopathy</p>
        <div class="footer-bottom-links">
          <a href="{rel}contact.html">Contact</a>
          <a href="{rel}privacy.html">Privacy</a>

          <a href="#" data-cookie-settings>Cookie settings</a>
        </div>
      </div>
    </div>
  </footer>'''


def trust_bar():
    items = [
        ("shield", "Registered naturopathic doctor"),
        ("video", "Virtual consultations"),
        ("globe", "UK &amp; Ontario"),
        ("heart", "Complimentary discovery call"),
    ]
    out = ""
    for icon, text in items:
        out += f'''        <div class="trust-item">
          {ICONS[icon]}
          {text}
        </div>
'''
    return f'''    <div class="container" style="padding-block:0">
      <div class="trust-bar reveal" style="border-bottom:1px solid var(--border-hairline)">
{out}      </div>
    </div>'''


def cta_banner(rel, eyebrow="Take the first step", heading="Book a complimentary discovery call.",
               body="A short, no-pressure conversation about your health goals and whether we are the right fit.",
               button="Schedule a discovery call", href=None, image="stilllife-vase", alt=""):
    href = href or JANE_DISC
    return f'''    <section class="section">
      <div class="container">
        <div class="cta-banner reveal">
          <div class="hero-bg">
            <picture>
              <source srcset="{rel}assets/images/{image}.webp" type="image/webp">
              <img src="{rel}assets/images/{image}.jpg" alt="{attr(alt)}" width="1456" height="816" loading="lazy">
            </picture>
          </div>
          <div class="cta-banner-content">
            <p class="eyebrow" style="color:var(--warm-soft)">{eyebrow}</p>
            <h2>{heading}</h2>
            <p>{body}</p>
            <a class="btn btn--warm" href="{href}" target="_blank" rel="noopener noreferrer" style="margin-top:var(--space-xs)">{button}</a>
          </div>
        </div>
      </div>
    </section>'''


def faq_block(faqs, title="Frequently asked questions", eyebrow="Common questions", bg=True):
    """FAQ markup. Structured data is emitted once as JSON-LD (no microdata duplicate)."""
    items = ""
    for q, a in faqs:
        items += f'''          <div class="faq-item">
            <h3 class="faq-question">{q}</h3>
            <div class="faq-answer"><p>{a}</p></div>
          </div>
'''
    style = ' style="background:var(--cream-50)"' if bg else ""
    return f'''    <section class="section"{style} aria-labelledby="faq-title">
      <div class="container" style="max-width:720px">
        <div class="section-head reveal">
          <p class="eyebrow">{eyebrow}</p>
          <h2 id="faq-title">{title}</h2>
        </div>
        <div class="faq-list reveal">
{items}        </div>
      </div>
    </section>'''


def conditions_list(items):
    return "\n".join(f"            <li>{c}</li>" for c in items)


# ---------------------------------------------------------------- schema
ORG_ID = f"{BASE}/#clinic"
PERSON_ID = f"{BASE}/#heather"
SITE_ID = f"{BASE}/#website"

UK_CITIES = [
    ("London", "https://en.wikipedia.org/wiki/London"),
    ("Edinburgh", "https://en.wikipedia.org/wiki/Edinburgh"),
    ("Glasgow", "https://en.wikipedia.org/wiki/Glasgow"),
    ("Belfast", "https://en.wikipedia.org/wiki/Belfast"),
]


def org_nodes(full=True):
    """Entity nodes shared by every page. `full=True` adds the heavyweight properties."""
    clinic = {
        "@type": ["MedicalBusiness", "ProfessionalService"],
        "@id": ORG_ID,
        "name": "Village Naturopathy",
        "alternateName": "Village Naturopathy - Online Naturopath UK & Ontario",
        "url": f"{BASE}/",
        "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/images/village-logo-black.png"},
        "image": f"{BASE}/assets/images/hero-portrait.jpg",
        "email": EMAIL,
        "slogan": "Root-cause naturopathic care for women navigating stress, hormones, and everything in between.",
        "description": ("Virtual naturopathic clinic for hormones, stress, fatigue and gut health in women. "
                        "Led by Dr. Heather Robinson, ND. Appointments by secure video across the UK and Ontario."),
        "foundingDate": "2017",
        "founder": {"@id": PERSON_ID},
        "employee": {"@id": PERSON_ID},
        "knowsAbout": ["Naturopathic medicine", "Hormone health", "PMOS/PCOS", "PMS and PMDD", "Endometriosis",
                       "Stress and burnout", "Anxiety and low mood", "Fatigue", "Gut health", "IBS and SIBO",
                       "DUTCH hormone testing", "Functional testing", "Botanical medicine", "Clinical nutrition"],
        "sameAs": SOCIALS,
        "contactPoint": {
            "@type": "ContactPoint", "contactType": "appointments", "email": EMAIL,
            "availableLanguage": "English", "areaServed": ["GB", "CA-ON"],
        },
        "areaServed": [
            {"@type": "Country", "name": "United Kingdom"},
            {"@type": "AdministrativeArea", "name": "Ontario"},
        ] + [{"@type": "City", "name": c} for c, _ in UK_CITIES],
        "availableChannel": {
            "@type": "ServiceChannel",
            "name": "Online booking and secure video consultation",
            "serviceUrl": JANE_BOOK,
            "availableLanguage": "English",
        },
        "priceRange": "GBP 50-200",
        "currenciesAccepted": "GBP, CAD",
        "paymentAccepted": "Card",
        "isAcceptingNewPatients": True,
        "hasOfferCatalog": {"@id": f"{BASE}/fees.html#catalog"},
        "member": {"@id": PERSON_ID},
    }
    person = {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": "Dr. Heather Robinson, ND",
        "givenName": "Heather", "familyName": "Robinson",
        "honorificPrefix": "Dr.", "honorificSuffix": "ND",
        "jobTitle": "Naturopathic Doctor",
        "description": ("Naturopathic doctor with a B.A. in Psychology and Certified HeartMath Practitioner. "
                        "Founder of Village Naturopathy, seeing patients by video across the UK and Ontario."),
        "url": f"{BASE}/about.html",
        "image": f"{BASE}/assets/images/heather-portrait.jpg",
        "email": EMAIL,
        "worksFor": {"@id": ORG_ID},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "University of Ottawa"},
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree", "name": "B.A. Psychology"},
            {"@type": "EducationalOccupationalCredential", "credentialCategory": "professional certification", "name": "Naturopathic Doctor (ND)"},
            {"@type": "EducationalOccupationalCredential", "credentialCategory": "certification", "name": "Certified HeartMath Practitioner"},
        ],
        "memberOf": [
            {"@type": "Organization", "name": "College of Naturopaths of Ontario"},
            {"@type": "Organization", "name": "Association of Naturopathic Practitioners (UK)"},
            {"@type": "Organization", "name": "Ontario Association of Naturopathic Doctors"},
            {"@type": "Organization", "name": "Canadian Association of Naturopathic Doctors"},
        ],
        "knowsAbout": clinic["knowsAbout"],
        "sameAs": SOCIALS,
    }
    site = {
        "@type": "WebSite",
        "@id": SITE_ID,
        "url": f"{BASE}/",
        "name": "Village Naturopathy",
        "description": "Online naturopath for women in the UK and Ontario.",
        "inLanguage": "en-GB",
        "publisher": {"@id": ORG_ID},
    }
    if not full:
        for k in ("knowsAbout", "contactPoint", "availableChannel", "hasOfferCatalog", "member", "employee",
                  "alternateName", "slogan", "currenciesAccepted", "paymentAccepted", "priceRange",
                  "isAcceptingNewPatients", "foundingDate", "areaServed", "founder", "description", "image", "email", "logo", "sameAs"):
            clinic.pop(k, None)
        for k in ("knowsAbout", "hasCredential", "memberOf", "alumniOf", "description", "image", "email", "sameAs",
                  "givenName", "familyName", "honorificPrefix", "honorificSuffix", "url", "worksFor", "jobTitle"):
            person.pop(k, None)
        site.pop("description", None)
    return [clinic, person, site]


def breadcrumb(crumbs):
    """crumbs: list of (name, url-or-None). Last item has no url."""
    items = []
    for i, (name, url) in enumerate(crumbs, 1):
        item = {"@type": "ListItem", "position": i, "name": plain(name)}
        if url:
            item["item"] = url
        items.append(item)
    return {"@type": "BreadcrumbList", "itemListElement": items}


def faq_node(faqs, page_url):
    return {
        "@type": "FAQPage",
        "@id": page_url + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": plain(q),
             "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
            for q, a in faqs
        ],
    }


def medical_webpage(url, name, description, about=None, image=None, lastmod=LASTMOD, breadcrumb_id=None, kind="MedicalWebPage"):
    node = {
        "@type": [kind, "WebPage"] if kind != "WebPage" else "WebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": plain(name),
        "description": plain(description),
        "inLanguage": "en-GB",
        "isPartOf": {"@id": SITE_ID},
        "about": about or {"@id": ORG_ID},
        "publisher": {"@id": ORG_ID},
        "dateModified": lastmod,
        "lastReviewed": lastmod,
        "reviewedBy": {"@id": PERSON_ID},
        "author": {"@id": PERSON_ID},
        "primaryImageOfPage": {"@type": "ImageObject", "url": image} if image else None,
        "breadcrumb": {"@id": breadcrumb_id} if breadcrumb_id else None,
        "audience": {"@type": "PeopleAudience", "audienceType": "Women"},
    }
    return {k: v for k, v in node.items() if v is not None}


def graph(nodes, full_org=True):
    return ld({"@context": "https://schema.org", "@graph": org_nodes(full_org) + nodes})


# ---------------------------------------------------------------- head
def head(rel, title, description, path, og_image, og_alt="", ld_graph="", robots=None,
         og_type="website", preload=None, extra="", og_dims=(1200, 630), markdown_alt=None):
    """Complete <head>. `path` is the site-absolute path ('' for home, 'uk/london/' etc.)."""
    canonical = f"{BASE}/{path}"
    og_url = f"{BASE}{og_image}" if og_image.startswith("/") else og_image
    robots = robots or "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    desc = attr(description)
    ttl = attr(title)
    pre = ""
    if preload:
        _pw = re.sub(r"\.jpg$", ".webp", preload)
        pre = f'  <link rel="preload" as="image" href="{_pw}" type="image/webp" fetchpriority="high">\n'
    md = ""
    if markdown_alt:
        md = f'  <link rel="alternate" type="text/markdown" href="{BASE}/{markdown_alt}">\n'
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{ttl}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en-GB" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">
{md}
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Village Naturopathy">
  <meta property="og:locale" content="en_GB">
  <meta property="og:title" content="{ttl}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_url}">
  <meta property="og:image:width" content="{og_dims[0]}">
  <meta property="og:image:height" content="{og_dims[1]}">
  <meta property="og:image:alt" content="{attr(og_alt or title)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{ttl}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_url}">
  <meta name="twitter:image:alt" content="{attr(og_alt or title)}">
  <meta name="theme-color" content="#F6F3EE">
  <meta name="author" content="Dr. Heather Robinson, ND">
  <meta name="geo.region" content="GB">
  <meta name="format-detection" content="telephone=no">

  <link rel="icon" href="{rel}favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{rel}apple-touch-icon.png">
  <link rel="manifest" href="{rel}site.webmanifest">
  <link rel="preload" href="{rel}assets/fonts/Zodiak-Variable.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="{rel}assets/fonts/ClashGrotesk-Variable.woff2" as="font" type="font/woff2" crossorigin>
{pre}  <link rel="stylesheet" href="{rel}css/styles.css?v={ASSET_V}">
  <noscript><style>.reveal, .reveal-stagger > * {{ opacity: 1 !important; transform: none !important; }}</style></noscript>

  <meta name="ga-id" content="G-XXXXXXXXXX">
{extra}
  <script type="application/ld+json">
{ld_graph}
  </script>
</head>'''


def page_shell(rel, head_html, main_html):
    return f'''{head_html}
<body>
  <a class="skip-link" href="#main">Skip to content</a>

{nav_html(rel)}

  <main id="main">
{main_html}
  </main>

{footer_html(rel)}

  <script src="{rel}js/main.js?v={ASSET_V}" defer></script>
</body>
</html>
'''


# ---------------------------------------------------------------- markdown mirror
def md_page(title, description, url, sections, faqs=None):
    """Minimal, quotable markdown twin of a page for LLM / agent consumption."""
    out = [f"# {plain(title)}", "", f"> {plain(description)}", "", f"Canonical: {url}",
           "Practitioner: Dr. Heather Robinson, ND (Village Naturopathy)",
           f"Booking: {JANE_BOOK}", ""]
    for h, body in sections:
        out += [f"## {plain(h)}", ""]
        if isinstance(body, (list, tuple)):
            out += [f"- {plain(b)}" for b in body]
        else:
            out.append(plain(body))
        out.append("")
    if faqs:
        out += ["## Frequently asked questions", ""]
        for q, a in faqs:
            out += [f"### {plain(q)}", "", plain(a), ""]
    out += ["---", plain(DISCLAIMER), ""]
    return "\n".join(out)
