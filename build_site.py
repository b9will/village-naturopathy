#!/usr/bin/env python3
"""One command to regenerate everything that is generated.

    python3 build_site.py

  1. Services + conditions pages            (generate_landing_pages.py)
  2. UK location pages                      (generate_geo_pages.py)
  3. Share images for social/OG             (og/*.jpg, needs Pillow + fontTools)
  4. sitemap.xml, robots.txt, llms.txt, llms-full.txt

Hand-written pages (index, about, fees, ...) are edited directly in HTML.
"""
import glob
import os
import re
import sys
import textwrap

import generate_geo_pages as geo
import generate_landing_pages as landing
import site_common as sc
from site_common import BASE, LASTMOD, plain

ROOT = os.path.dirname(os.path.abspath(__file__))

# Hand-written pages that belong in the sitemap: (path, priority, changefreq)
HAND_PAGES = [
    ("", 1.0, "weekly"), ("about.html", 0.9, "monthly"), ("services.html", 0.9, "monthly"),
    ("fees.html", 0.8, "monthly"), ("resources.html", 0.8, "monthly"), ("journal.html", 0.7, "weekly"),
    ("programs/regulate-method/", 0.8, "monthly"), ("programs/pmos-playbook/", 0.8, "monthly"),
    ("book.html", 0.7, "monthly"), ("contact.html", 0.6, "yearly"), ("careers.html", 0.3, "yearly"),
    ("privacy.html", 0.2, "yearly"),
]


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)


# ------------------------------------------------------------------ OG images
def og_font(name, size, weight=None):
    from PIL import ImageFont
    ttf = f"/tmp/vn-fonts/{name}.ttf"
    if not os.path.exists(ttf):
        from fontTools.ttLib import TTFont
        os.makedirs("/tmp/vn-fonts", exist_ok=True)
        f = TTFont(os.path.join(ROOT, f"assets/fonts/{name}-Variable.woff2"))
        f.flavor = None
        f.save(ttf)
    font = ImageFont.truetype(ttf, size)
    if weight:
        try:
            font.set_variation_by_axes([weight])
        except Exception:
            pass
    return font


def make_og(slug, title, bg_name):
    """1200x630 share card: photo, sage wash, logo, headline."""
    from PIL import Image, ImageDraw
    out = os.path.join(ROOT, "og", f"{slug}.jpg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    W, H = 1200, 630
    src = os.path.join(ROOT, "assets/images", f"{bg_name}.jpg")
    im = Image.open(src).convert("RGB")
    scale = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * scale) + 1, int(im.height * scale) + 1), Image.LANCZOS)
    left, top = (im.width - W) // 2, (im.height - H) // 2
    im = im.crop((left, top, left + W, top + H))
    wash = Image.new("RGBA", (W, H), (44, 51, 39, 0))
    px = wash.load()
    for y in range(H):
        a = int(120 + 110 * (y / H))
        for x in range(W):
            px[x, y] = (44, 51, 39, a)
    im = Image.alpha_composite(im.convert("RGBA"), wash)
    d = ImageDraw.Draw(im)
    logo = Image.open(os.path.join(ROOT, "assets/images/village-logo-white.png")).convert("RGBA")
    lh = 54
    logo = logo.resize((int(logo.width * lh / logo.height), lh), Image.LANCZOS)
    im.alpha_composite(logo, (64, 56))
    f_title = og_font("Zodiak", 70, 360)
    f_sub = og_font("ClashGrotesk", 28, 500)
    lines = textwrap.wrap(plain(title), width=26)[:3]
    y = H - 64 - 28 - 20 - len(lines) * 82
    for ln in lines:
        d.text((64, y), ln, font=f_title, fill=(246, 243, 238, 255))
        y += 82
    d.text((64, H - 84), "Dr. Heather Robinson, ND  ·  Online naturopath, UK & Ontario", font=f_sub, fill=(196, 168, 130, 255))
    im.convert("RGB").save(out, quality=84, optimize=True, progressive=True)


def og_bg_for(path):
    parts = [p for p in path.strip("/").split("/") if p]
    if len(parts) >= 2 and parts[0] == "uk":
        k = parts[1]
        if k in geo.HERO_IMAGES:
            return geo.HERO_IMAGES[k]
        if k == "dutch-test":
            return geo.HERO_IMAGES["dutch"]
    if parts and parts[0] == "uk":
        return geo.HERO_IMAGES["uk"]
    return "hero-golden"


def build_og(items):
    ok = True
    try:
        import PIL  # noqa: F401
        import fontTools  # noqa: F401
    except ImportError:
        print("Pillow/fontTools not installed; skipping OG images")
        return
    for slug, title, bg in items:
        try:
            make_og(slug, title, bg)
        except Exception as e:  # keep building even if one card fails
            ok = False
            print("OG failed", slug, e)
    print("OG images:", len(items), "ok" if ok else "with errors")


# ------------------------------------------------------------------ sitemap & robots
def url_entry(path, lastmod, freq, prio):
    return (f"  <url>\n    <loc>{BASE}/{path}</loc>\n    <lastmod>{lastmod}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n    <priority>{prio:.1f}</priority>\n  </url>\n")


def build_sitemap(landing_pages, geo_pages):
    out = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n']
    for p, prio, freq in HAND_PAGES:
        out.append(url_entry(p, LASTMOD, freq, prio))
    for p, prio in landing_pages:
        out.append(url_entry(p, LASTMOD, "monthly", prio))
    for g in geo_pages:
        out.append(url_entry(g["path"], LASTMOD, "monthly", g["priority"]))
    for f in sorted(glob.glob(os.path.join(ROOT, "all-articles/**/index.html"), recursive=True) +
                    glob.glob(os.path.join(ROOT, "all-recipes/**/index.html"), recursive=True)):
        rel = os.path.relpath(f, ROOT)[: -len("index.html")]
        out.append(url_entry(rel, "2026-06-20", "yearly", 0.4))
    out.append("</urlset>\n")
    write("sitemap.xml", "".join(out))


ROBOTS = f"""# Village Naturopathy
User-agent: *
Allow: /
Disallow: /review.html

# AI search and answer engines are welcome to read and cite this site.
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /

Sitemap: {BASE}/sitemap.xml
"""


# ------------------------------------------------------------------ llms.txt
def build_llms(geo_pages):
    uk = {p["path"]: p for p in geo_pages}

    def link(path, title, desc):
        return f"- [{plain(title)}]({BASE}/{path}): {plain(desc)}"

    lines = [
        "# Village Naturopathy",
        "",
        "> Village Naturopathy is a virtual naturopathic clinic for women, led by Dr. Heather Robinson, ND. "
        "Appointments are by secure video across the United Kingdom (London, Edinburgh, Glasgow, Belfast and "
        "everywhere in between) and Ontario, Canada. Areas of focus: hormones (PMS, PMOS/PCOS, endometriosis, "
        "irregular periods, hormonal acne), stress, mood and anxiety, fatigue, and gut health (IBS, SIBO).",
        "",
        "## Key facts",
        "- Practitioner: Dr. Heather Robinson, ND. B.A. Psychology (University of Ottawa), Certified HeartMath Practitioner.",
        "- Credentials: registered with the College of Naturopaths of Ontario; full member of the Association of Naturopathic Practitioners (UK); fully insured. Naturopathy is not statutorily regulated in the UK.",
        "- Format: virtual clinic only. No physical clinic or in-person appointments.",
        "- Fees (UK): free 15-minute discovery call; 75-minute initial consultation GBP 200; follow-ups GBP 50-170.",
        f"- Booking: {sc.JANE_BOOK} (discovery call: {sc.JANE_DISC})",
        f"- Email: {sc.EMAIL}",
        "- Care is complementary and does not replace advice from a GP or other healthcare professional.",
        "",
        "## Services",
        link("services/hormone-balancing/", "Hormone balancing", "PMOS/PCOS, PMS and PMDD, endometriosis, irregular periods, hormonal acne"),
        link("services/stress-anxiety/", "Stress, mood and anxiety", "Burnout, anxiety, low mood, nervous system regulation"),
        link("services/fatigue/", "Fatigue", "Persistent low energy, iron and B12, thyroid markers, cortisol"),
        link("services/gut-health/", "Gut health", "IBS, SIBO, bloating, reflux, food sensitivities"),
        link("fees.html", "Fees", "Consultation fees in GBP and CAD, UK treatment packages"),
        "",
        "## UK locations",
        link("uk/", "Online naturopath UK", uk["uk/"]["desc"]),
    ]
    for k in geo.CITY_ORDER:
        p = uk[f"uk/{k}/"]
        lines.append(link(p["path"], p["title"], p["desc"]))
    for k in ("scotland", "northern-ireland"):
        p = uk[f"uk/{k}/"]
        lines.append(link(p["path"], p["title"], p["desc"]))
    lines.append(link("uk/dutch-test/", "DUTCH hormone test UK", uk["uk/dutch-test/"]["desc"]))
    lines += ["", "## Neighbourhood pages (virtual care for each area)"]
    for p in geo_pages:
        parts = p["path"].strip("/").split("/")
        if len(parts) == 3 and parts[2] not in ("dutch-test",) + tuple(geo.g.TOPICS):
            lines.append(f"- [{plain(p['title'])}]({BASE}/{p['path']})")
    lines += ["", "## More",
              f"- [About Dr. Heather Robinson]({BASE}/about.html)",
              f"- [Programs: The Regulate Method, PMOS Playbook]({BASE}/resources.html)",
              f"- [Journal]({BASE}/journal.html)",
              f"- [Full site text for LLMs]({BASE}/llms-full.txt)", ""]
    write("llms.txt", "\n".join(lines))

    # llms-full.txt: concatenated markdown mirrors of generated pages
    chunks = ["# Village Naturopathy: full text of key pages", ""]
    mds = (sorted(glob.glob(os.path.join(ROOT, "services/*/index.md"))) +
           sorted(glob.glob(os.path.join(ROOT, "uk/index.md"))) +
           sorted(glob.glob(os.path.join(ROOT, "uk/*/index.md"))) +
           sorted(glob.glob(os.path.join(ROOT, "uk/*/*/index.md"))))
    for m in mds:
        chunks.append(open(m).read())
        chunks.append("\n\n")
    write("llms-full.txt", "\n".join(chunks))


# ------------------------------------------------------------------ main
def add_img_dimensions():
    """Set intrinsic width/height on local <img> tags (prevents layout shift)."""
    import glob, re
    from PIL import Image
    cache = {}
    def dims(page, src):
        if src.startswith(("http", "data:", "//")):
            return None
        path = os.path.normpath(os.path.join(os.path.dirname(page), src.split("?")[0]))
        if path not in cache:
            try:
                with Image.open(path) as im:
                    cache[path] = im.size
            except Exception:
                cache[path] = None
        return cache[path]
    for page in glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True):
        rel = os.path.relpath(page, ROOT)
        if rel.startswith(("docs", "og")):
            continue
        html = open(page, encoding="utf-8").read()
        def fix(m):
            tag = m.group(0)
            if "width=" in tag and "height=" in tag:
                return tag
            src = re.search(r'src="([^"]+)"', tag)
            d = dims(page, src.group(1)) if src else None
            if not d:
                return tag
            w, h = d
            if "height=" in tag and "width=" not in tag:
                hh = int(re.search(r'height="(\d+)"', tag).group(1))
                return tag.replace("<img ", '<img width="%d" ' % round(w * hh / h), 1)
            tag = re.sub(r'\s(width|height)="[^"]*"', "", tag)
            return tag.replace("<img ", '<img width="%d" height="%d" ' % (w, h), 1)
        new = re.sub(r"<img\b[^>]*>", fix, html)
        if new != html:
            open(page, "w", encoding="utf-8").write(new)


def add_mobile_heroes():
    """Give each hero a 800px WebP for phones (LCP) and preload the right one."""
    import glob, re
    from PIL import Image
    made = {}
    def small(src_abs):
        out = src_abs.replace(".webp", "-800.webp")
        if out not in made:
            if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src_abs):
                with Image.open(src_abs) as im:
                    im = im.convert("RGB")
                    im = im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS)
                    im.save(out, "WEBP", quality=72, method=6)
            made[out] = True
        return out
    for page in glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True):
        rel = os.path.relpath(page, ROOT)
        if rel.startswith(("docs", "og")):
            continue
        html = open(page, encoding="utf-8").read()
        if 'class="hero-bg"' not in html or "-800.webp" in html:
            continue
        m = re.search(r'(<div class="hero-bg">\s*<picture>\s*)(<source srcset="([^"]+\.webp)" type="image/webp">)', html)
        if not m:
            continue
        src = m.group(3)
        src_abs = os.path.normpath(os.path.join(os.path.dirname(page), src))
        if not os.path.exists(src_abs):
            continue
        small(src_abs)
        small_src = src.replace(".webp", "-800.webp")
        html = html.replace(m.group(2), '<source media="(max-width:700px)" srcset="%s" type="image/webp">\n          %s' % (small_src, m.group(2)), 1)
        pre = '<link rel="preload" as="image" href="%s" type="image/webp" fetchpriority="high">' % src
        if pre in html:
            html = html.replace(pre,
                '<link rel="preload" as="image" href="%s" type="image/webp" media="(max-width:700px)" fetchpriority="high">\n  '
                '<link rel="preload" as="image" href="%s" type="image/webp" media="(min-width:701px)" fetchpriority="high">' % (small_src, src), 1)
        open(page, "w", encoding="utf-8").write(html)


def main():
    landing_pages = landing.build()
    geo_pages = geo.build()

    og_items = []
    for g in geo_pages:
        slug = g["path"].strip("/").replace("/", "-")
        og_items.append((slug, g["title"], og_bg_for(g["path"])))
    for p in landing.SERVICES + landing.CONDITIONS:
        kind = "services" if p in landing.SERVICES else "conditions"
        og_items.append((f"{kind}-{p['slug']}", p["h1"], p["image"]))
    og_items.append(("conditions", "Conditions treated", "hero-golden"))
    for name, title, bg in [
        ("home", "Online naturopath for women in the UK & Ontario", "hero-portrait"),
        ("about", "About Dr. Heather Robinson, ND", "heather-portrait"),
        ("services", "Naturopathic services", "stilllife-vase"),
        ("fees", "Fees", "hero-golden"),
        ("journal", "The Journal: notes on being well", "portrait-3"),
        ("resources", "Programs", "stilllife-vase"),
        ("regulate-method", "The Regulate Method", "geo-smile"),
        ("pmos-playbook", "The PMOS Playbook", "geo-flowers"),
        ("contact", "Contact", "geo-courtyard"),
        ("book", "Book a consultation", "hero-golden"),
        ("careers", "Careers", "geo-interior"),
    ]:
        og_items.append((name, title, bg))
    build_og(og_items)

    build_sitemap(landing_pages, geo_pages)
    write("robots.txt", ROBOTS)
    build_llms(geo_pages)
    add_img_dimensions()
    add_mobile_heroes()
    print(f"Built {len(landing_pages)} service/condition pages, {len(geo_pages)} UK pages")


if __name__ == "__main__":
    sys.exit(main())
