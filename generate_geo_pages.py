#!/usr/bin/env python3
"""Generate the UK location pages (/uk/...) for Village Naturopathy.

Page types:
  /uk/                              hub
  /uk/scotland/, /uk/northern-ireland/   nation hubs
  /uk/<city>/                       city pages (london, edinburgh, glasgow, belfast)
  /uk/<city>/<area>/                neighbourhood pages
  /uk/scotland/st-andrews/          town page
  /uk/london/<topic>/               London topic pages (hormones, PMOS/PCOS, stress, gut, fatigue)
  /uk/dutch-test/, /uk/<city>/dutch-test/   DUTCH hormone test pages

Content lives in geo_data.py. Shared chrome/schema in site_common.py.
"""
import os

import geo_data as g
import site_common as sc
from site_common import BASE, JANE_BOOK, JANE_DISC, plain

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))

HERO_IMAGES = {
    "uk": "hero-golden", "scotland": "portrait-3", "northern-ireland": "geo-coast",
    "london": "geo-interior", "edinburgh": "geo-courtyard", "glasgow": "stilllife-vase", "belfast": "geo-coast",
    "dutch": "geo-flowers",
}
# Placeholder photography (reused brand images). See docs/image-todo.md for the replacement list.
AREA_ROTATION = ["geo-smile", "geo-flowers", "geo-courtyard", "geo-interior", "hero-golden", "geo-coast", "stilllife-vase"]
IMG_DIMS = {}  # every hero used here is 1456x816 except portrait-3 (2912x1632), handled below

SERVICE_PAGES = {
    "stress-anxiety": "Stress, Mood &amp; Anxiety",
    "hormone-balancing": "Hormone Balancing",
    "gut-health": "Gut Health",
    "fatigue": "Fatigue",
}

CITY_ORDER = ["london", "edinburgh", "glasgow", "belfast"]


# ------------------------------------------------------------------ helpers
def rel_for(path):
    depth = len([p for p in path.strip("/").split("/") if p])
    return "../" * depth


def area_url_path(a):
    if a.get("city"):
        return f"uk/{a['city']}/{a['slug']}/"
    return f"uk/{a['nation']}/{a['slug']}/"


def area_label(a):
    return a["name"]


def hero_img_for(key, idx=0):
    if key in HERO_IMAGES:
        return HERO_IMAGES[key]
    return AREA_ROTATION[idx % len(AREA_ROTATION)]


def og_for(path):
    slug = path.strip("/").replace("/", "-") or "home"
    return f"/og/{slug}.jpg"


def hero(rel, eyebrow, h1, lead, img, alt):
    w, h = (2912, 1632) if img in ("portrait-3", "hero-portrait") else (1456, 816)
    return f'''    <section class="page-hero" aria-labelledby="page-title">
      <div class="hero-bg">
        <picture>
          <source srcset="{rel}assets/images/{img}.webp" type="image/webp">
          <img src="{rel}assets/images/{img}.jpg" alt="{sc.attr(alt)}" width="{w}" height="{h}" fetchpriority="high">
        </picture>
      </div>
      <div class="hero-copy">
        <p class="eyebrow">{eyebrow}</p>
        <h1 id="page-title">{h1}</h1>
        <p class="lead">{lead}</p>
        <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:var(--space-xs)">
          <a class="btn btn--warm" href="{JANE_DISC}" target="_blank" rel="noopener noreferrer">Free discovery call</a>
          <a class="btn btn--on-dark" href="{JANE_BOOK}" target="_blank" rel="noopener noreferrer">Book a consultation</a>
        </div>
      </div>
    </section>'''


def quick(text):
    return f'''    <section class="section reveal" aria-label="Summary">
      <div class="container" style="max-width:760px">
        <p class="lead" style="text-align:center;margin-inline:auto;max-width:62ch">{text}</p>
      </div>
    </section>'''


def prose(h, paras, eyebrow=None, bg=False, hid=None):
    body = "\n".join(f"          <p>{p}</p>" for p in paras)
    style = ' style="background:var(--cream-50)"' if bg else ""
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    hid_attr = f' id="{hid}"' if hid else ""
    labelled = f' aria-labelledby="{hid}"' if hid else ""
    return f'''    <section class="section"{style}{labelled}>
      <div class="container" style="max-width:720px">
        <div class="section-head reveal">
          {eb}
          <h2{hid_attr}>{h}</h2>
        </div>
        <div class="about-content reveal">
{body}
        </div>
      </div>
    </section>'''


def link_list(items, title, eyebrow, bg=False, hid="list-title"):
    """items: [(label, href)]"""
    lis = "\n".join(f'            <li><a href="{href}">{label}</a></li>' for label, href in items)
    style = ' style="background:var(--cream-50)"' if bg else ""
    return f'''    <section class="section"{style} aria-labelledby="{hid}">
      <div class="container">
        <div class="conditions-block reveal">
          <div class="section-head">
            <p class="eyebrow">{eyebrow}</p>
            <h2 id="{hid}">{title}</h2>
          </div>
          <ul class="conditions-list">
{lis}
          </ul>
        </div>
      </div>
    </section>'''


def feature_rows(rows, title, eyebrow, bg=False, hid="rows-title"):
    """rows: [(icon, heading_html, text_html)]"""
    out = ""
    for icon, h, t in rows:
        out += f'''          <div class="feature-row">
            <span class="icon-circle">
              {sc.ICONS[icon]}
            </span>
            <div class="feature-row-content">
              <h3>{h}</h3>
              <p>{t}</p>
            </div>
          </div>
'''
    style = ' style="background:var(--cream-50)"' if bg else ""
    return f'''    <section class="section"{style} aria-labelledby="{hid}">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{eyebrow}</p>
          <h2 id="{hid}">{title}</h2>
        </div>
        <div class="reveal-stagger" style="max-width:720px;margin-inline:auto">
{out}        </div>
      </div>
    </section>'''


def how_it_works():
    return feature_rows([
        ("heart", "1. A free 15-minute discovery call", f'A short, no-pressure conversation to hear what is going on and check we are a good fit. <a href="{JANE_DISC}" target="_blank" rel="noopener noreferrer">Book your call</a>.'),
        ("video", "2. A 75-minute consultation by secure video", "A thorough look at your history, symptoms, cycle, sleep, stress and nutrition. You can attend from home or work, anywhere in the UK."),
        ("leaf", "3. A personalised plan and follow-ups", "Nutrition, targeted supplementation, botanical medicine and lifestyle support, with comprehensive testing recommended only where it will change the plan."),
    ], "How online naturopathic care works", "How it works", hid="how-title")


def about_block(rel):
    return f'''    <section class="section" style="background:var(--surface-warm)" aria-labelledby="about-title">
      <div class="container">
        <div class="split reveal">
          <div class="split-media about-media">
            <picture>
              <source srcset="{rel}assets/images/heather-portrait.webp" type="image/webp">
              <img src="{rel}assets/images/heather-portrait.jpg" width="178" height="210" alt="Dr. Heather Robinson, naturopathic doctor" loading="lazy">
            </picture>
          </div>
          <div class="split-copy">
            <p class="eyebrow">Your practitioner</p>
            <h2 id="about-title">Dr. Heather Robinson, ND</h2>
            <p>Naturopathic doctor, with a B.A. in Psychology from the University of Ottawa and a Certified HeartMath Practitioner. Registered with the College of Naturopaths of Ontario and a full member of the Association of Naturopathic Practitioners (UK). Fully insured, in practice since 2017.</p>
            <p style="color:var(--text-muted)">Naturopathy is not statutorily regulated in the UK. Dr. Heather&rsquo;s UK membership is with the Association of Naturopathic Practitioners.</p>
            <a class="btn btn--ghost" href="{rel}about.html">Read Dr. Heather&rsquo;s story &rarr;</a>
          </div>
        </div>
      </div>
    </section>'''


def fees_block(rel):
    return f'''    <section class="section" aria-labelledby="fees-title">
      <div class="container" style="max-width:720px">
        <div class="section-head reveal">
          <p class="eyebrow">Fees</p>
          <h2 id="fees-title">Simple, transparent fees in pounds sterling</h2>
        </div>
        <div class="faq-list reveal" style="margin-inline:auto">
          <div class="faq-item"><h3 class="faq-question">Discovery call</h3><div class="faq-answer"><p>15 minutes &middot; Complimentary</p></div></div>
          <div class="faq-item"><h3 class="faq-question">Initial consultation</h3><div class="faq-answer"><p>75 minutes &middot; {sc.FEE_INITIAL}</p></div></div>
          <div class="faq-item"><h3 class="faq-question">Follow-up consultations</h3><div class="faq-answer"><p>15&ndash;60 minutes &middot; {sc.FEE_FOLLOWUP}</p></div></div>
        </div>
        <p class="reveal" style="text-align:center;margin-top:var(--space-md);font-size:15px;color:var(--text-muted)">Receipts are provided for every appointment. Whether a private health insurer reimburses naturopathy depends on your policy, so please check with them. <a href="{rel}fees.html">See all fees and UK treatment packages &rarr;</a></p>
      </div>
    </section>'''


def disclaimer():
    return f'''    <section class="section" aria-label="Important information">
      <div class="container" style="max-width:720px"><p style="font-size:13px;color:var(--text-subtle);text-align:center">{sc.DISCLAIMER}</p></div>
    </section>'''


def finish(path, title, desc, hero_html, body_sections, faqs, nodes, hero_img, breadcrumb_items, og_alt):
    """Assemble full page; returns (html, md)."""
    rel = rel_for(path)
    url = f"{BASE}/{path}"
    bc_id = url + "#breadcrumb"
    full_nodes = [
        sc.medical_webpage(url, title.split("|")[0].strip(), desc, image=f"{BASE}/assets/images/{hero_img}.jpg",
                           breadcrumb_id=bc_id),
        {**sc.breadcrumb(breadcrumb_items), "@id": bc_id},
    ] + nodes
    if faqs:
        full_nodes.append(sc.faq_node(faqs, url))
    head = sc.head(rel, title, desc, path, og_for(path), og_alt=og_alt, ld_graph=sc.graph(full_nodes),
                   markdown_alt=path + "index.md")
    sections = [hero_html, sc.trust_bar()] + body_sections
    if faqs:
        sections.append(sc.faq_block(faqs))
    sections += [sc.cta_banner(rel), disclaimer()]
    return sc.page_shell(rel, head, "\n\n".join(sections))


def service_node(url, name, desc, area_name=None, area_node=None):
    node = {
        "@type": "Service", "@id": url + "#service", "name": plain(name),
        "serviceType": "Virtual naturopathic consultation", "description": plain(desc),
        "provider": {"@id": sc.ORG_ID},
        "availableChannel": {"@type": "ServiceChannel", "serviceUrl": JANE_BOOK, "availableLanguage": "English"},
        "offers": {"@type": "Offer", "name": "Initial naturopathic consultation (75 minutes)", "price": "200",
                   "priceCurrency": "GBP", "url": f"{BASE}/fees.html"},
    }
    node["areaServed"] = area_node or {"@type": "Country", "name": "United Kingdom"}
    return node


def city_place(city_key):
    c = g.CITIES[city_key]
    nation = c["nation"]
    return {"@type": "City", "name": c["name"],
            "containedInPlace": {"@type": "AdministrativeArea", "name": nation}}


# ------------------------------------------------------------------ builders
def area_pages_for_city(city_key):
    return [a for a in g.AREAS if a.get("city") == city_key]


def focus_cards(a, rel, city_key):
    """Three focus areas with the area-specific angle sentences."""
    rows = []
    icons = ["leaf", "heart", "clipboard"]
    for i, f in enumerate(a["focus"]):
        meta = g.FOCUS[f]
        href = f"{rel}services/{meta['service']}/"
        if city_key == "london":
            topic = {"stress": "stress-burnout", "hormones": "hormone-balancing", "gut": "gut-health", "fatigue": "fatigue"}[f]
            href = f"{rel}uk/london/{topic}/"
        rows.append((icons[i % 3], f'<a href="{href}">{meta["name"]}</a>', a["angle"][i]))
    return rows


def build_area(a, idx):
    path = area_url_path(a)
    rel = rel_for(path)
    url = f"{BASE}/{path}"
    name = a["name"]
    plain_name = plain(name)
    city_key = a.get("city")
    city = g.CITIES.get(city_key) if city_key else None
    parent_name = city["name"] if city else "Scotland"
    parent_path = f"uk/{city_key}/" if city else "uk/scotland/"
    full_title = f"Online Naturopath in {plain_name} ({plain(a['postcodes'])}) | Village Naturopathy"
    title = full_title if len(full_title) <= 64 else f"Online Naturopath in {plain_name} | Village Naturopathy"
    desc = (f"Virtual naturopathic doctor for women in {plain_name}. Hormones, stress, gut health and fatigue "
            f"with Dr. Heather Robinson, ND. Free discovery call.")
    quick_text = (f"Village Naturopathy offers online naturopathic consultations to women in {name} ({a['postcodes']}) "
                  f"and the surrounding area. Dr. Heather Robinson, ND, a full member of the Association of Naturopathic "
                  f"Practitioners (UK), sees patients by secure video, so there is nothing to travel to. The first step is a "
                  f"free 15-minute discovery call, and the initial 75-minute consultation is {sc.FEE_INITIAL}.")
    img = hero_img_for(city_key or "scotland", idx)
    hero_html = hero(rel, f"Online naturopath &middot; {parent_name}", f"Online Naturopath in {name}",
                     f"Virtual naturopathic care for women in {a['postcodes']}. Hormones, stress, gut health and fatigue with Dr. Heather Robinson, ND.",
                     img, f"Village Naturopathy, online naturopath for {plain_name}")
    nearby = []
    for s in a.get("nearby", []):
        other = next((x for x in g.AREAS if x["slug"] == s), None)
        if other:
            nearby.append((f"Online naturopath in {other['name']}", f"{rel}{area_url_path(other)}"))
    nearby.append((f"All of {parent_name}" if city else "All of Scotland", f"{rel}{parent_path}"))
    nearby.append(("DUTCH hormone testing in the UK", f"{rel}uk/dutch-test/"))

    local_section = prose(
        f"Your health in {name}", [a["local"],
        f"Whatever your week looks like, Dr. Heather&rsquo;s approach is the same: a thorough history, comprehensive testing only where it will change the plan, and a programme you can actually follow. All appointments take place by secure video, so you can attend from home or work in {name}."],
        eyebrow=f"{parent_name} &middot; {a['postcodes']}", hid="local-title")
    focus_html = feature_rows(focus_cards(a, rel, city_key), f"Where we can help if you live in {name}", "Areas of focus",
                              bg=True, hid="focus-title")
    faqs = [
        (f"Can I see a naturopath online in {name}?", f"Yes. Dr. Heather Robinson, ND, sees patients in {name} and across the UK by secure video. Start with a free 15-minute discovery call, then book a 75-minute initial consultation if you would like to go ahead."),
        (f"Do you have a clinic in {name}?", f"No. Village Naturopathy is a virtual clinic and all consultations take place online. {name} patients receive exactly the same care as patients anywhere else in the UK."),
        (f"How much does a naturopath cost in {name}?", f"The initial 75-minute consultation is {sc.FEE_INITIAL} and follow-ups are {sc.FEE_FOLLOWUP} depending on length. The 15-minute discovery call is free. Any testing is optional and discussed with you before you decide."),
        (f"Which postcodes do you cover near {name}?", f"Because care is online, there are no postcode limits. This page is written for {a['postcodes']}, but patients from across {parent_name} and the rest of the UK are welcome."),
    ]
    service_area = {"@type": "Place", "name": plain_name,
                    "address": {"@type": "PostalAddress", "addressLocality": plain_name, "addressRegion": parent_name, "addressCountry": "GB"},
                    "containedInPlace": ({"@type": "City", "name": parent_name} if city else {"@type": "AdministrativeArea", "name": "Scotland"})}
    nodes = [service_node(url, f"Online naturopath in {plain_name}", quick_text, area_node=service_area)]
    crumbs = [("Home", f"{BASE}/"), ("UK", f"{BASE}/uk/")]
    if city and g.CITIES[city_key]["nation_slug"]:
        crumbs.append((g.CITIES[city_key]["nation"], f"{BASE}/uk/{g.CITIES[city_key]['nation_slug']}/"))
    if city:
        crumbs.append((parent_name, f"{BASE}/{parent_path}"))
    else:
        crumbs.append(("Scotland", f"{BASE}/uk/scotland/"))
    crumbs.append((plain_name, None))
    html = finish(path, title, desc, hero_html,
                  [quick(quick_text), local_section, focus_html, how_it_works(), about_block(rel), fees_block(rel),
                   link_list(nearby, f"Nearby areas and related pages", "Explore", bg=True, hid="nearby-title")],
                  faqs, nodes, img, crumbs, f"Online naturopath in {plain_name}")
    md = sc.md_page(f"Online Naturopath in {name}", desc, url,
                    [("Summary", quick_text), (f"Your health in {name}", a["local"]),
                     ("Where we can help", [x[2] for x in focus_cards(a, "", city_key)]),
                     ("Fees", f"Discovery call: free (15 minutes). Initial consultation: {plain(sc.FEE_INITIAL)} (75 minutes). Follow-ups: {plain(sc.FEE_FOLLOWUP)}.")],
                    faqs)
    return path, html, md, f"Online naturopath in {plain_name}", desc, 0.6


def build_city(key):
    c = g.CITIES[key]
    path = f"uk/{key}/"
    rel = rel_for(path)
    url = f"{BASE}/{path}"
    name = c["name"]
    img = hero_img_for(key)
    hero_html = hero(rel, f"Online naturopath &middot; {c['nation']}", c["h1"],
                     f"Virtual naturopathic care for women in {name}. Hormones, stress, gut health and fatigue with Dr. Heather Robinson, ND.",
                     img, f"Village Naturopathy, online naturopath for {name}")
    areas = area_pages_for_city(key)
    sections = [quick(c["quick"]), prose(f"Naturopathic care for life in {name}", c["intro"], eyebrow=c["nation"], hid="intro-title")]
    if areas:
        sections.append(link_list([(f"Online naturopath in {a['name']}", f"{area_url_path(a)[len('uk/'+key+'/'):]}") for a in areas],
                                  f"Areas of {name} we see patients from", "Neighbourhoods", bg=True, hid="areas-title"))
    if key == "london":
        topic_items = []
        for t in c["topics"]:
            if t == "dutch-test":
                topic_items.append(("DUTCH hormone testing in London", "dutch-test/"))
            else:
                topic_items.append((g.TOPICS[t]["h1"], f"{t}/"))
        sections.append(link_list(topic_items, "What we help with in London", "Topics", hid="topics-title"))
    else:
        items = [(f"{SERVICE_PAGES[s]}", f"{rel}services/{s}/") for s in SERVICE_PAGES]
        items.append((f"DUTCH hormone testing in {name}", "dutch-test/"))
        sections.append(link_list(items, f"What we help {name} patients with", "Services", hid="topics-title"))
    sections += [how_it_works(), about_block(rel), fees_block(rel)]
    nodes = [service_node(url, f"Online naturopath in {name}", c["quick"], area_node=city_place(key))]
    crumbs = [("Home", f"{BASE}/"), ("UK", f"{BASE}/uk/")]
    if c["nation_slug"]:
        crumbs.append((c["nation"], f"{BASE}/uk/{c['nation_slug']}/"))
    crumbs.append((name, None))
    c_title = f"Online Naturopath in {name} | Village Naturopathy"
    c_desc = (f"Virtual naturopathic doctor for women in {name}. Hormones, burnout, gut health and fatigue with "
              f"Dr. Heather Robinson, ND. Free discovery call.")
    c["meta_title"], c["meta_desc"] = c_title, c_desc
    html = finish(path, c_title, c_desc, hero_html, sections, c["faqs"], nodes, img, crumbs,
                  f"Online naturopath in {name}")
    md = sc.md_page(c["h1"], c["meta_desc"], url,
                    [("Summary", c["quick"]), (f"Naturopathic care for life in {name}", " ".join(c["intro"])),
                     ("Neighbourhoods", [a["name"] for a in areas]) if areas else ("Services", list(SERVICE_PAGES.values())),
                     ("Fees", f"Discovery call: free (15 minutes). Initial consultation: {plain(sc.FEE_INITIAL)} (75 minutes). Follow-ups: {plain(sc.FEE_FOLLOWUP)}.")],
                    c["faqs"])
    return path, html, md, c["h1"], c["meta_desc"], 0.9


def build_nation(key):
    n = g.NATIONS[key]
    path = f"uk/{key}/"
    rel = rel_for(path)
    url = f"{BASE}/{path}"
    img = hero_img_for(key)
    hero_html = hero(rel, "Online naturopath &middot; UK", n["h1"],
                     f"Virtual naturopathic care for women across {n['name']}. Hormones, stress, gut health and fatigue with Dr. Heather Robinson, ND.",
                     img, f"Village Naturopathy, online naturopath in {n['name']}")
    items = []
    for ck in n["cities"]:
        items.append((g.CITIES[ck]["h1"], f"{rel}uk/{ck}/"))
        for a in area_pages_for_city(ck):
            items.append((f"Online naturopath in {a['name']}", f"{rel}{area_url_path(a)}"))
    for s in n["towns"]:
        a = next(x for x in g.AREAS if x["slug"] == s)
        items.append((f"Online naturopath in {a['name']}", f"{rel}{area_url_path(a)}"))
    sections = [quick(n["quick"]), prose(f"Online care across {n['name']}", [n["intro"]], eyebrow="Where we see patients", hid="intro-title"),
                link_list(items, f"Cities, towns and neighbourhoods in {n['name']}", "Locations", bg=True, hid="locations-title"),
                how_it_works(), about_block(rel), fees_block(rel)]
    nodes = [service_node(url, n["h1"], n["quick"], area_node={"@type": "AdministrativeArea", "name": n["name"]})]
    crumbs = [("Home", f"{BASE}/"), ("UK", f"{BASE}/uk/"), (n["name"], None)]
    n["meta_title"] = f"Online Naturopath in {n['name']} | Village Naturopathy"
    n["meta_desc"] = (f"Virtual naturopathic care for women across {n['name']}. Hormones, stress, gut health and fatigue "
                      f"with Dr. Heather Robinson, ND. Free discovery call.")
    html = finish(path, n["meta_title"], n["meta_desc"], hero_html, sections, n["faqs"], nodes, img, crumbs, n["h1"])
    md = sc.md_page(n["h1"], n["meta_desc"], url, [("Summary", n["quick"]), ("Overview", n["intro"])], n["faqs"])
    return path, html, md, n["h1"], n["meta_desc"], 0.8


UK_FAQS = [
    ("Can I see a naturopath online in the UK?", "Yes. Dr. Heather Robinson, ND, sees patients across England, Scotland, Wales and Northern Ireland by secure video. Start with a free 15-minute discovery call, then book a 75-minute initial consultation."),
    ("Is naturopathy regulated in the UK?", "Naturopathy is not statutorily regulated in the UK. Dr. Heather is a full member of the Association of Naturopathic Practitioners (UK), is registered with the College of Naturopaths of Ontario, where naturopathic doctors are regulated, and is fully insured."),
    ("How much does a naturopath cost in the UK?", "At Village Naturopathy the initial 75-minute consultation is &pound;200 and follow-ups are &pound;50&ndash;170 depending on length. The 15-minute discovery call is free. Testing, if recommended, is discussed with you first."),
    ("What can a naturopath help with?", "Dr. Heather focuses on hormones (PMS, PMOS/PCOS, endometriosis, irregular periods, hormonal acne), stress, mood and anxiety, fatigue and gut health (IBS, SIBO, food sensitivities). Care is complementary and works alongside your GP."),
    ("Do you accept private medical insurance?", "Receipts are provided for every appointment, but whether a private health insurer reimburses naturopathy depends on your policy, so please check with your insurer first."),
    ("Do I need to travel anywhere?", "No. Village Naturopathy is a virtual clinic. Consultations and follow-ups take place by secure video, and any recommended testing is explained to you first."),
]


def build_hub():
    path = "uk/"
    rel = rel_for(path)
    url = f"{BASE}/{path}"
    title = "Online Naturopath UK | Village Naturopathy"
    desc = ("Online naturopath for women across the UK: hormones, PMOS/PCOS, stress and burnout, gut health and "
            "fatigue. Dr. Heather Robinson, ND. Free discovery call.")
    quick_text = ("Village Naturopathy is a virtual naturopathic clinic for women across the United Kingdom. Dr. Heather "
                  "Robinson, ND, sees patients by secure video in London, Edinburgh, Glasgow, Belfast and everywhere "
                  "in between, with a 75-minute initial consultation (&pound;200) and a free 15-minute discovery call.")
    img = hero_img_for("uk")
    hero_html = hero(rel, "Online naturopath &middot; United Kingdom", "Online Naturopath in the UK",
                     "Root-cause naturopathic care for women navigating stress, hormones and everything in between, from anywhere in the UK.",
                     img, "Village Naturopathy, online naturopath for the UK")
    ci = [(f"Online naturopath in {g.CITIES[k]['name']}", f"{rel}uk/{k}/") for k in CITY_ORDER]
    ci += [("Online naturopath in Scotland", f"{rel}uk/scotland/"), ("Online naturopath in Northern Ireland", f"{rel}uk/northern-ireland/"),
           ("DUTCH hormone testing in the UK", f"{rel}uk/dutch-test/")]
    services = feature_rows([
        ("heart", f'<a href="{rel}services/hormone-balancing/">Hormones, PMOS/PCOS &amp; cycles</a>', "PMS and PMDD, irregular or painful periods, PMOS/PCOS, endometriosis and hormonal acne, with DUTCH testing where it helps."),
        ("leaf", f'<a href="{rel}services/stress-anxiety/">Stress, mood &amp; anxiety</a>', "Burnout, anxiety and low mood: nervous system, sleep, hormones and nutrient status."),
        ("flask", f'<a href="{rel}services/fatigue/">Fatigue &amp; low energy</a>', "Iron, B12, thyroid markers and cortisol, plus the sleep and stress patterns behind persistent tiredness."),
        ("clipboard", f'<a href="{rel}services/gut-health/">Gut health, IBS &amp; SIBO</a>', "Bloating, reflux, IBS and SIBO and food sensitivities, with GI-MAP and breath testing where useful."),
    ], "What Dr. Heather focuses on", "Areas of focus", bg=True, hid="focus-title")
    sections = [quick(quick_text),
                prose("A naturopath you can see from anywhere in the UK",
                      ["Finding a naturopath with the time to listen is hard. Many clinics offer short appointments, and the best-known practitioners are concentrated in a handful of cities. Village Naturopathy is built differently: every consultation takes place online, runs for 75 minutes at the start, and sets out a plan that fits your life.",
                       "Dr. Heather has worked in naturopathic medicine since 2017 and combines a psychology degree with naturopathic training. She sees patients across the UK and Ontario, and is a full member of the Association of Naturopathic Practitioners (UK)."],
                      eyebrow="UK virtual clinic", hid="intro-title"),
                link_list(ci, "Find care near you", "Locations", hid="locations-title"),
                services, how_it_works(), about_block(rel), fees_block(rel)]
    nodes = [service_node(url, "Online naturopath in the UK", quick_text),
             {"@type": "ItemList", "name": "UK locations", "itemListElement": [
                 {"@type": "ListItem", "position": i, "name": plain(n), "url": f"{BASE}/{h.replace(rel, '')}"} for i, (n, h) in enumerate(ci, 1)]}]
    crumbs = [("Home", f"{BASE}/"), ("UK", None)]
    html = finish(path, title, desc, hero_html, sections, UK_FAQS, nodes, img, crumbs, "Online naturopath UK")
    md = sc.md_page("Online Naturopath in the UK", desc, url,
                    [("Summary", quick_text), ("Locations", [n for n, _ in ci]),
                     ("Fees", f"Discovery call: free (15 minutes). Initial consultation: {plain(sc.FEE_INITIAL)} (75 minutes). Follow-ups: {plain(sc.FEE_FOLLOWUP)}.")],
                    UK_FAQS)
    return path, html, md, "Online naturopath UK", desc, 1.0


def build_topic(key):
    t = g.TOPICS[key]
    path = f"uk/london/{key}/"
    rel = rel_for(path)
    url = f"{BASE}/{path}"
    img = hero_img_for("london")
    hero_html = hero(rel, "Online naturopath &middot; London", t["h1"],
                     "Virtual naturopathic care with Dr. Heather Robinson, ND. Free 15-minute discovery call.", img,
                     f"{plain(t['h1'])}")
    sections = [quick(t["quick"])]
    for i, (h, paras) in enumerate(t["sections"]):
        sections.append(prose(h, paras, bg=(i % 2 == 1), hid=f"sec{i}"))
    areas = area_pages_for_city("london")
    sections += [how_it_works(), about_block(rel), fees_block(rel),
                 link_list([(f"Online naturopath in {a['name']}", f"{rel}{area_url_path(a)}") for a in areas] +
                           [(f"More about {SERVICE_PAGES[t['service']]}", f"{rel}services/{t['service']}/"),
                            ("DUTCH hormone testing in London", f"{rel}uk/london/dutch-test/")],
                           "London neighbourhoods and related pages", "Explore", bg=True, hid="explore-title")]
    nodes = [service_node(url, t["h1"], t["quick"], area_node=city_place("london"))]
    crumbs = [("Home", f"{BASE}/"), ("UK", f"{BASE}/uk/"), ("London", f"{BASE}/uk/london/"), (plain(t["h1"]), None)]
    html = finish(path, t["meta_title"], t["meta_desc"], hero_html, sections, t["faqs"], nodes, img, crumbs, plain(t["h1"]))
    md = sc.md_page(t["h1"], t["meta_desc"], url, [("Summary", t["quick"])] + [(h, " ".join(p)) for h, p in t["sections"]], t["faqs"])
    return path, html, md, plain(t["h1"]), t["meta_desc"], 0.8


def build_dutch(city_key=None):
    d = g.DUTCH
    if city_key:
        name = g.CITIES[city_key]["name"]
        path = f"uk/{city_key}/dutch-test/"
        h1 = f"DUTCH Hormone Test in {name}"
        title = f"DUTCH Hormone Test {name} | Village Naturopathy"
        desc = (f"DUTCH hormone testing for patients in {name}, explained by Dr. Heather Robinson, ND. Home collection, "
                f"cortisol and hormone metabolites.")
        quick_text = (f"DUTCH is a home hormone test, so patients in {name} do not need to travel to a lab or clinic. "
                      f"Dr. Heather Robinson, ND, recommends it case by case and explains what it measures, how it "
                      f"works and what it costs before you decide. It is interpreted alongside your history and is "
                      f"never required to start care.")
        crumbs = [("Home", f"{BASE}/"), ("UK", f"{BASE}/uk/"), (name, f"{BASE}/uk/{city_key}/"), (h1, None)]
        img = hero_img_for(city_key)
        extra = [prose(f"DUTCH testing for {name} patients", [f"DUTCH is a home collection test, so there is nothing to attend in {name}. You collect small dried urine samples at home, return them as instructed and review the results in a follow-up appointment with Dr. Heather. She explains the kit, the timing relative to your cycle and the cost before you order."], eyebrow=name, hid="local-title")]
    else:
        name = "the UK"
        path = "uk/dutch-test/"
        h1 = "DUTCH Hormone Test in the UK"
        title = "DUTCH Hormone Test UK | Village Naturopathy"
        desc = ("DUTCH hormone testing for UK patients, explained by Dr. Heather Robinson, ND. Home collection, cortisol "
                "patterns and hormone metabolites.")
        quick_text = ("DUTCH (Dried Urine Test for Comprehensive Hormones) is a home hormone test that measures sex "
                      "hormones, their metabolites and the daily pattern of cortisol. Dr. Heather Robinson, ND, "
                      "recommends it case by case for UK patients and explains what it measures, how it works and what "
                      "it costs before you decide.")
        crumbs = [("Home", f"{BASE}/"), ("UK", f"{BASE}/uk/"), (h1, None)]
        img = hero_img_for("dutch")
        extra = []
    rel = rel_for(path)
    url = f"{BASE}/{path}"
    hero_html = hero(rel, "Hormone testing", h1, "Understand your hormone and cortisol patterns, explained clearly by Dr. Heather Robinson, ND.", img, h1)
    sections = [quick(quick_text)] + extra
    for i, (h, paras) in enumerate(d["sections"]):
        sections.append(prose(h, paras, bg=(i % 2 == 1), hid=f"sec{i}"))
    related = [("Hormone balancing", f"{rel}services/hormone-balancing/"), ("Stress, mood & anxiety", f"{rel}services/stress-anxiety/"),
               ("Online naturopath in the UK", f"{rel}uk/")] + [(f"DUTCH hormone test in {g.CITIES[k]['name']}", f"{rel}uk/{k}/dutch-test/") for k in CITY_ORDER if k != city_key]
    sections += [how_it_works(), about_block(rel), fees_block(rel), link_list(related, "Related pages", "Explore", bg=True, hid="explore-title")]
    nodes = [service_node(url, h1, quick_text, area_node=city_place(city_key) if city_key else None),
             {"@type": "MedicalTest", "@id": url + "#test", "name": "DUTCH Complete (Dried Urine Test for Comprehensive Hormones)",
              "description": "Home collection test measuring sex hormones, hormone metabolites and cortisol patterns from dried urine samples."}]
    html = finish(path, title, desc, hero_html, sections, d["faqs"], nodes, img, crumbs, h1)
    md = sc.md_page(h1, desc, url, [("Summary", quick_text)] + [(h, " ".join(p)) for h, p in d["sections"]], d["faqs"])
    return path, html, md, h1, desc, 0.8


# ------------------------------------------------------------------ driver
def write(path, content):
    full = os.path.join(SITE_ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)


def all_pages():
    pages = [build_hub(), build_nation("scotland"), build_nation("northern-ireland")]
    pages += [build_city(k) for k in CITY_ORDER]
    for i, a in enumerate(g.AREAS):
        pages.append(build_area(a, i))
    pages += [build_topic(k) for k in g.TOPICS]
    pages.append(build_dutch())
    pages += [build_dutch(k) for k in CITY_ORDER]
    return pages


def build():
    out = []
    for path, html, md, title, desc, prio in all_pages():
        write(path + "index.html", html)
        write(path + "index.md", md)
        out.append({"path": path, "title": title, "desc": desc, "priority": prio})
    return out


if __name__ == "__main__":
    pages = build()
    print(f"Generated {len(pages)} UK pages")
