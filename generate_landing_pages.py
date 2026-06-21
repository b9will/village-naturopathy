#!/usr/bin/env python3
"""Generate service + condition landing pages for Village Naturopathy."""
import os, json, html

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
REL = "../../"

# ── SVG Icons ──
ICONS = {
    "clipboard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25z"/></svg>',
    "flask": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l.051.054c.649.685.507 1.794-.296 2.273A12.56 12.56 0 0112 19.5a12.56 12.56 0 01-7.555-2.373c-.803-.479-.945-1.588-.296-2.273L4.2 13.854"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155"/></svg>',
}

# ── Reusable HTML fragments ──
def nav_html():
    return f'''  <header class="site-header">
      <nav class="nav" id="nav" aria-label="Primary">
        <a class="brand" href="{REL}" aria-label="Village Naturopathy home"><img src="{REL}assets/images/logo-full-white.png" alt="Village Naturopathy" height="36"></a>
        <ul class="nav-links">
          <li><a href="{REL}about.html">About</a></li>
          <li><a href="{REL}services.html">Services</a></li>
          <li><a href="{REL}journal.html">Journal</a></li>
          <li><a href="{REL}contact.html">Contact</a></li>
        </ul>
        <a class="btn btn--warm btn--sm nav-cta" href="{REL}book.html">Book now</a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Toggle menu">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
        </button>
      </nav>
  </header>'''

def trust_bar():
    return f'''    <div class="container" style="padding-block:0">
      <div class="trust-bar reveal" style="border-bottom:1px solid var(--border-hairline)">
        <div class="trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/></svg>
          Licensed &amp; insured
        </div>
        <div class="trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15.75 10.5l4.72-4.72a.75.75 0 011.28.53v11.38a.75.75 0 01-1.28.53l-4.72-4.72M4.5 18.75h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25h-9A2.25 2.25 0 002.25 7.5v9a2.25 2.25 0 002.25 2.25z"/></svg>
          Virtual appointments
        </div>
        <div class="trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5a17.92 17.92 0 01-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418"/></svg>
          Ontario &amp; UK
        </div>
        <div class="trust-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"/></svg>
          Free discovery call
        </div>
      </div>
    </div>'''

def cta_banner():
    return f'''    <section class="section">
      <div class="container">
        <div class="cta-banner reveal">
          <div class="hero-bg">
            <picture>
              <source srcset="{REL}assets/images/stilllife-vase.webp" type="image/webp">
              <img src="{REL}assets/images/stilllife-vase.jpg" alt="" loading="lazy">
            </picture>
          </div>
          <div class="cta-banner-content">
            <p class="eyebrow" style="color:var(--warm-soft)">Take the first step</p>
            <h2>Book a complimentary discovery call.</h2>
            <p>No obligation, no pressure &mdash; just a conversation about your health goals.</p>
            <a class="btn btn--warm" href="{REL}book.html" style="margin-top:var(--space-xs)">Book a free consult</a>
          </div>
        </div>
      </div>
    </section>'''

def footer_html():
    return f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <span class="brand"><img src="{REL}assets/images/logo-full-black.png" alt="Village Naturopathy" height="32"></span>
          <p>Root-cause naturopathic care for women navigating stress, hormones, and everything in between.</p>
          <div class="footer-social">
            <a href="https://www.facebook.com/villagenaturopathy" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </a>
            <a href="https://www.instagram.com/villagenaturopathy" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
            </a>
          </div>
        </div>
        <div class="footer-col">
          <span class="footer-col-title">Clinic</span>
          <a href="{REL}about.html">About Dr. Heather</a>
          <a href="{REL}services.html">Services</a>
          <a href="{REL}conditions.html">Conditions Treated</a>
          <a href="{REL}fees.html">Fees</a>
          <a href="https://villagenaturopathy.fullscript.com" target="_blank" rel="noopener noreferrer">Fullscript</a>
          <a href="{REL}book.html">Book Now</a>
        </div>
        <div class="footer-col">
          <span class="footer-col-title">Learn</span>
          <a href="{REL}journal.html">The Journal</a>
          <a href="{REL}resources.html">Resources</a>
          <a href="{REL}about.html#approach">Our Approach</a>
          <a href="{REL}about.html#faq-title">FAQs</a>
        </div>
        <div class="footer-col">
          <span class="footer-col-title">Connect</span>
          <div class="footer-contact-item">
            <a href="mailto:drheather@villagenaturopathy.com">drheather@villagenaturopathy.com</a>
          </div>
          <div class="footer-contact-item">
            <p>Virtual clinic serving<br>Ontario &amp; the United Kingdom</p>
          </div>
          <div class="footer-contact-item">
            <div class="footer-clocks" id="footer-clocks">
              <div class="footer-clock">
                <span class="footer-clock-label"><img src="{REL}assets/images/flag-canada.svg" alt="" width="16" height="12"> Ontario</span>
                <span class="clock-time" data-tz="America/Toronto"></span>
              </div>
              <div class="footer-clock">
                <span class="footer-clock-label"><img src="{REL}assets/images/flag-uk.svg" alt="" width="16" height="12"> London</span>
                <span class="clock-time" data-tz="Europe/London"></span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Dr. Heather Robinson, ND &middot; Village Naturopathy</p>
        <div class="footer-bottom-links">
          <a href="{REL}contact.html">Contact</a>
          <a href="{REL}privacy.html">Privacy</a>
          <a class="btn btn--warm btn--sm" href="{REL}book.html">Book Now</a>
        </div>
      </div>
    </div>
  </footer>'''

# ── Page data ──
SERVICES = [
    {
        "slug": "stress-anxiety",
        "meta_title": "Stress & Anxiety Treatment",
        "meta_desc": "Root-cause naturopathic treatment for chronic stress, overwhelm, and anxiety. Virtual consultations for Ontario & UK. Book a free discovery call.",
        "eyebrow": "Stress & anxiety",
        "h1": "Naturopathic Care for Stress, Overwhelm & Anxiety",
        "lead": "Stress goes deeper than feeling frazzled &mdash; it disrupts sleep, hormones, digestion, and your ability to feel like yourself. We find the root cause and build a plan that works with your life, not against it.",
        "image": "system-stress",
        "image_alt": "Stacked stones balanced on a hillside at golden hour",
        "parent": "Services",
        "parent_url": "services.html",
        "empathy_h": "When stress becomes your baseline",
        "empathy_p": "You&rsquo;ve been running on adrenaline for so long it feels normal. The sleep issues, the afternoon crashes, the tight shoulders, the brain fog &mdash; they&rsquo;ve become part of your identity. But your body is telling you something. Naturopathic medicine looks at the full picture: your nervous system, your hormones, your gut, your lifestyle &mdash; and builds a path back to feeling grounded.",
        "conditions": ["Chronic stress &amp; overwhelm", "Generalised anxiety disorder", "Panic attacks", "Burnout &amp; adrenal fatigue", "Insomnia &amp; sleep disturbances", "Nervous system dysregulation", "Stress-related weight changes", "Tension headaches &amp; migraines"],
        "conditions_title": "Conditions we treat",
        "approach": [
            ("clipboard", "Comprehensive Assessment", "A 75-minute initial consultation to understand your stress history, triggers, lifestyle, and health goals."),
            ("flask", "Advanced Testing", "DUTCH hormone panels, cortisol mapping, thyroid panels, and nutrient status to see what&rsquo;s happening beneath the surface."),
            ("leaf", "Personalised Protocol", "Evidence-based botanical medicine, targeted nutrition, nervous system regulation techniques, and lifestyle modifications tailored to you."),
            ("chat", "Ongoing Support", "Regular follow-ups, coaching, and adjustments to your plan as you progress. You&rsquo;re never doing this alone."),
        ],
        "faqs": [
            ("What causes chronic stress and anxiety?", "Chronic stress is rarely caused by one thing. It&rsquo;s usually a combination of lifestyle factors, unresolved trauma, hormonal imbalances, nutrient deficiencies, and nervous system dysregulation. Naturopathic medicine looks at all of these together."),
            ("How does naturopathy treat anxiety differently?", "Rather than masking symptoms, we identify root causes &mdash; whether that&rsquo;s a cortisol imbalance, gut-brain axis disruption, or mineral deficiency &mdash; and address them with targeted nutrition, botanicals, and nervous system tools."),
            ("How long does treatment typically take?", "Most patients notice improvements within 4&ndash;6 weeks. A comprehensive treatment plan typically spans 3&ndash;6 months, with follow-ups adjusted to your pace."),
            ("Do you work alongside my GP or therapist?", "Absolutely. Naturopathic care is integrative &mdash; we collaborate with your existing healthcare team to ensure a cohesive approach."),
        ],
        "schema_type": "MedicalTherapy",
    },
    {
        "slug": "hormone-balancing",
        "meta_title": "Hormone Balancing Treatment",
        "meta_desc": "Naturopathic hormone balancing for PCOS, endometriosis, PMS, menopause, and more. Virtual care for Ontario & UK. Book a free discovery call.",
        "eyebrow": "Hormone balancing",
        "h1": "Naturopathic Hormone Balancing for Women",
        "lead": "Hormone issues are common but not normal. We address the root cause of menstrual irregularities, PMS, PCOS, endometriosis, and menopausal transitions with treatment plans tailored to your body.",
        "image": "system-hormones",
        "image_alt": "Three women standing together in warm light",
        "parent": "Services",
        "parent_url": "services.html",
        "empathy_h": "When your hormones feel out of your control",
        "empathy_p": "Irregular periods, weight changes that don&rsquo;t make sense, skin that won&rsquo;t clear, mood swings that leave you feeling like a different person &mdash; you&rsquo;ve tried everything and nothing sticks. Hormone imbalances don&rsquo;t resolve on their own. We use advanced testing to understand your unique hormonal picture and build a protocol that restores balance from the inside out.",
        "conditions": ["PCOS (Polycystic Ovarian Syndrome)", "Endometriosis", "PMS &amp; PMDD", "Irregular or absent periods", "Heavy or painful periods", "Perimenopause &amp; menopause", "Hot flashes &amp; night sweats", "Hormonal acne", "Low libido", "Fertility support", "Post-pill syndrome"],
        "conditions_title": "Conditions we treat",
        "approach": [
            ("clipboard", "Comprehensive Assessment", "A detailed look at your menstrual history, symptoms, lifestyle, stress load, and health goals."),
            ("flask", "Hormone Testing", "DUTCH complete hormone panels, thyroid panels, blood work, and metabolic markers to map your unique hormonal landscape."),
            ("leaf", "Targeted Treatment", "Botanical medicine, clinical nutrition, seed cycling, and lifestyle protocols designed to restore hormonal rhythm naturally."),
            ("chat", "Cycle-Aligned Support", "Follow-ups timed to your cycle so we can track progress and adjust your plan in real time."),
        ],
        "faqs": [
            ("What is DUTCH testing?", "DUTCH (Dried Urine Test for Comprehensive Hormones) measures your sex hormones, cortisol pattern, and hormone metabolites. It gives us a far more detailed picture than standard blood work alone."),
            ("Can naturopathy help with PCOS?", "Yes. Naturopathic treatment for PCOS focuses on insulin regulation, inflammation reduction, and hormonal support through nutrition, botanicals, and lifestyle changes &mdash; addressing the root drivers rather than just symptoms."),
            ("How long does hormone balancing take?", "Hormonal shifts typically take 3&ndash;6 menstrual cycles to fully manifest. Most patients notice improvements in energy and mood within the first month."),
            ("Do I need to stop birth control?", "Not necessarily. We work with wherever you are. If you&rsquo;re considering coming off hormonal contraception, we can support that transition."),
        ],
        "schema_type": "MedicalTherapy",
    },
    {
        "slug": "gut-health",
        "meta_title": "Gut Health Treatment",
        "meta_desc": "Naturopathic gut health treatment for IBS, SIBO, bloating, food sensitivities, and digestive issues. Virtual clinic for Ontario & UK.",
        "eyebrow": "Gut health",
        "h1": "Naturopathic Gut Health Treatment",
        "lead": "A healthy gut means a healthy nervous system and healthy hormones. Whether you&rsquo;re dealing with IBS, SIBO, bloating, or food sensitivities, the gut is the foundation of whole-body health.",
        "image": "system-gut",
        "image_alt": "A kitchen counter with herbal teas, ginger, and glass jars of dried herbs",
        "parent": "Services",
        "parent_url": "services.html",
        "empathy_h": "When your gut is running the show",
        "empathy_p": "Bloating after every meal, nausea that comes and goes, foods you used to love now causing problems. You&rsquo;ve cut out dairy, gluten, sugar &mdash; and still feel terrible. Digestive issues aren&rsquo;t just uncomfortable; they affect your energy, your mood, your hormones, and your immune system. We look beyond the symptoms to find what&rsquo;s actually driving the dysfunction.",
        "conditions": ["IBS (Irritable Bowel Syndrome)", "SIBO (Small Intestinal Bacterial Overgrowth)", "Bloating &amp; gas", "Constipation &amp; diarrhoea", "Food sensitivities &amp; intolerances", "Acid reflux &amp; GERD", "Leaky gut (intestinal permeability)", "Candida overgrowth", "Inflammatory bowel conditions"],
        "conditions_title": "Conditions we treat",
        "approach": [
            ("clipboard", "Comprehensive Assessment", "A thorough review of your digestive history, diet, stress patterns, medication use, and symptom timeline."),
            ("flask", "Functional Testing", "GI-MAP stool analysis, SIBO breath testing, food sensitivity panels, and organic acids testing to identify the root cause."),
            ("leaf", "Gut Restoration Protocol", "A phased approach: remove triggers, replace deficiencies, reinoculate beneficial bacteria, and repair the gut lining with targeted nutrition and botanicals."),
            ("chat", "Ongoing Monitoring", "Regular check-ins to track symptom resolution, adjust the protocol, and retest when needed."),
        ],
        "faqs": [
            ("What is a GI-MAP test?", "GI-MAP is a comprehensive stool test that uses DNA analysis to identify pathogens, parasites, bacterial imbalances, inflammation markers, and digestive function. It&rsquo;s one of the most detailed gut tests available."),
            ("How long does gut healing take?", "It depends on the condition. Simple dysbiosis may resolve in 6&ndash;8 weeks. More complex issues like SIBO or inflammatory conditions typically take 3&ndash;6 months of structured treatment."),
            ("Do I need to follow a restrictive diet?", "Short-term dietary modifications are sometimes helpful, but the goal is always to expand your diet, not restrict it permanently. We focus on healing the gut so you can enjoy food again."),
            ("Can gut health affect my mood?", "Absolutely. The gut-brain axis is a well-established connection. Over 90% of serotonin is produced in the gut, and gut inflammation directly impacts mood, anxiety, and cognitive function."),
        ],
        "schema_type": "MedicalTherapy",
    },
    {
        "slug": "mental-health-counselling",
        "meta_title": "Mental Health & Counselling",
        "meta_desc": "Naturopathic mental health support and CBT counselling for anxiety, depression, and stress. Holistic virtual care for Ontario & UK.",
        "eyebrow": "Mental health",
        "h1": "Naturopathic Mental Health & Counselling",
        "lead": "CBT and holistic counselling for anxiety, depression, and stress management. Training in cognitive and emotional skills to build lasting resilience and treat the whole person.",
        "image": "system-energy",
        "image_alt": "A warm, sunlit bedroom with terracotta bedding",
        "parent": "Services",
        "parent_url": "services.html",
        "empathy_h": "When the weight feels heavier than it should",
        "empathy_p": "You&rsquo;re doing all the right things but still feel flat, foggy, or overwhelmed. The motivation that used to come naturally now takes everything you have. Mental health is not separate from physical health &mdash; it&rsquo;s deeply connected to your gut, your hormones, your sleep, and your nervous system. We combine evidence-based counselling with naturopathic medicine to address the whole picture.",
        "conditions": ["Depression &amp; low mood", "Anxiety disorders", "Emotional overwhelm", "Trauma &amp; PTSD", "Postpartum mood changes", "Seasonal affective disorder (SAD)", "Stress-related cognitive difficulties"],
        "conditions_title": "Conditions we support",
        "approach": [
            ("clipboard", "Intake & Assessment", "A comprehensive look at your mental health history, physical health, lifestyle factors, and what you&rsquo;ve tried before."),
            ("flask", "Root-Cause Investigation", "Nutrient testing, hormone panels, thyroid function, and inflammatory markers &mdash; because mood disorders often have biochemical drivers."),
            ("leaf", "Integrated Treatment", "CBT and holistic counselling combined with targeted supplementation, botanical medicine, and lifestyle interventions."),
            ("chat", "Therapeutic Support", "Regular sessions that adapt to your needs &mdash; whether that&rsquo;s weekly counselling, biweekly naturopathic check-ins, or a combination."),
        ],
        "faqs": [
            ("What is CBT?", "Cognitive Behavioural Therapy (CBT) is an evidence-based form of psychotherapy that helps you identify and change unhelpful thought patterns. It&rsquo;s one of the most effective treatments for anxiety and depression."),
            ("How is this different from seeing a psychologist?", "Dr. Robinson is trained in both naturopathic medicine and psychotherapy. This means she can address the psychological and biochemical sides of mental health simultaneously &mdash; something most practitioners can&rsquo;t do."),
            ("Can supplements really help with depression?", "In many cases, yes. Nutrient deficiencies (B12, iron, vitamin D, magnesium, omega-3s) are well-documented contributors to mood disorders. Targeted supplementation, alongside other interventions, can make a meaningful difference."),
            ("Is this covered by insurance?", "Naturopathic consultations are covered by many extended health plans in Ontario. Check with your provider for your specific coverage."),
        ],
        "schema_type": "MedicalTherapy",
    },
]

CONDITIONS = [
    {
        "slug": "stress-anxiety-nervous-system",
        "meta_title": "Stress, Anxiety & Nervous System",
        "meta_desc": "Naturopathic treatment for chronic stress, anxiety, panic attacks, burnout, insomnia, and nervous system dysregulation. Virtual clinic for Ontario & UK.",
        "eyebrow": "Conditions treated",
        "h1": "Stress, Anxiety & Nervous System Dysregulation",
        "lead": "Root-cause naturopathic care for chronic stress, anxiety, and nervous system imbalances. We address what&rsquo;s driving your symptoms &mdash; not just managing them.",
        "image": "system-stress",
        "image_alt": "Stacked stones balanced on a hillside at golden hour",
        "parent": "Conditions",
        "parent_url": "conditions.html",
        "empathy_h": "Your nervous system is stuck in overdrive",
        "empathy_p": "The constant hum of anxiety, the inability to switch off, the feeling of being wired but tired. Your body has been in fight-or-flight for so long it doesn&rsquo;t know how to rest. This isn&rsquo;t a character flaw &mdash; it&rsquo;s a physiological pattern that can be changed with the right support.",
        "conditions": ["Chronic stress &amp; overwhelm", "Generalised anxiety disorder", "Panic attacks", "Burnout &amp; adrenal fatigue", "Insomnia &amp; sleep disturbances", "Nervous system dysregulation", "Stress-related weight changes", "Tension headaches &amp; migraines"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Comprehensive Assessment", "Understanding your stress timeline, triggers, sleep patterns, and how your body responds to pressure."),
            ("flask", "Functional Testing", "Cortisol mapping, DUTCH panels, thyroid function, and nutrient status to identify the biochemical drivers of your symptoms."),
            ("leaf", "Restorative Protocol", "Adaptogenic botanicals, targeted nutrients, nervous system regulation techniques, and sleep support."),
            ("chat", "Ongoing Guidance", "Regular follow-ups to adjust your protocol and build lasting resilience over time."),
        ],
        "faqs": [
            ("What is nervous system dysregulation?", "It&rsquo;s when your autonomic nervous system gets stuck in a stress response (fight-or-flight) and can&rsquo;t easily return to a calm state. This can manifest as anxiety, insomnia, digestive issues, and chronic fatigue."),
            ("Is burnout the same as adrenal fatigue?", "They&rsquo;re related but not identical. Burnout is a state of chronic stress-induced exhaustion. Adrenal dysfunction (often called adrenal fatigue) refers to measurable changes in cortisol production that can be tested and treated."),
            ("Can naturopathy help with panic attacks?", "Yes. We address the physiological triggers &mdash; blood sugar dysregulation, magnesium deficiency, nervous system patterns &mdash; while also providing tools for in-the-moment regulation."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "hormonal-imbalances-womens-health",
        "meta_title": "Hormonal Imbalances & Women's Health",
        "meta_desc": "Naturopathic treatment for PCOS, endometriosis, PMS, menopause, fertility, and hormonal acne. Virtual care for Ontario & UK.",
        "eyebrow": "Conditions treated",
        "h1": "Hormonal Imbalances & Women&rsquo;s Health",
        "lead": "From PCOS to perimenopause, we treat the full spectrum of hormonal conditions with root-cause naturopathic medicine.",
        "image": "system-hormones",
        "image_alt": "Three women standing together in warm light",
        "parent": "Conditions",
        "parent_url": "conditions.html",
        "empathy_h": "Your hormones are trying to tell you something",
        "empathy_p": "Painful periods, unexplained weight gain, acne that won&rsquo;t quit, mood swings that disrupt your relationships &mdash; these aren&rsquo;t things you should just live with. Hormonal imbalances have identifiable causes and treatable solutions. We dig into the data and create a plan that actually works.",
        "conditions": ["PCOS (Polycystic Ovarian Syndrome)", "Endometriosis", "PMS &amp; PMDD", "Irregular or absent periods", "Heavy or painful periods", "Perimenopause &amp; menopause", "Hot flashes &amp; night sweats", "Hormonal acne", "Low libido", "Fertility support", "Post-pill syndrome"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Detailed Intake", "Your menstrual history, symptom patterns, contraceptive history, and health goals."),
            ("flask", "Hormone Mapping", "DUTCH complete panels, thyroid function, metabolic markers, and blood work for a full hormonal picture."),
            ("leaf", "Personalised Protocol", "Botanical medicine, clinical nutrition, seed cycling, and targeted supplementation to restore balance."),
            ("chat", "Cycle-Tracked Follow-ups", "Progress monitoring aligned with your menstrual cycle for precise adjustments."),
        ],
        "faqs": [
            ("What hormonal conditions do you treat?", "We treat PCOS, endometriosis, PMS/PMDD, irregular periods, perimenopause, menopause, hormonal acne, fertility challenges, post-pill syndrome, and more."),
            ("How is PCOS treated naturopathically?", "We focus on the root drivers: insulin resistance, inflammation, and androgen excess. Treatment includes dietary changes, targeted supplementation, botanical medicine, and stress management."),
            ("Can you help with fertility?", "Yes. We optimise hormonal health, address underlying conditions, and support conception through evidence-based naturopathic protocols. We work alongside fertility specialists when needed."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "digestive-gut-health",
        "meta_title": "Digestive & Gut Health Conditions",
        "meta_desc": "Naturopathic treatment for IBS, SIBO, bloating, food sensitivities, acid reflux, and gut health issues. Virtual clinic for Ontario & UK.",
        "eyebrow": "Conditions treated",
        "h1": "Digestive & Gut Health Conditions",
        "lead": "From IBS to SIBO to food sensitivities, we get to the root of your digestive issues with advanced testing and targeted protocols.",
        "image": "system-gut",
        "image_alt": "A kitchen counter with herbal teas, ginger, and glass jars",
        "parent": "Conditions",
        "parent_url": "conditions.html",
        "empathy_h": "You deserve to eat without fear",
        "empathy_p": "The bloating, the unpredictability, the growing list of foods you can&rsquo;t tolerate. Digestive issues affect everything &mdash; your energy, your mood, your confidence, your social life. We use functional testing to identify exactly what&rsquo;s going on and create a structured plan to restore your gut health.",
        "conditions": ["IBS (Irritable Bowel Syndrome)", "SIBO (Small Intestinal Bacterial Overgrowth)", "Bloating &amp; gas", "Constipation &amp; diarrhoea", "Food sensitivities &amp; intolerances", "Acid reflux &amp; GERD", "Leaky gut (intestinal permeability)", "Candida overgrowth", "Inflammatory bowel conditions"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Digestive History", "A thorough review of your symptoms, diet, stress, medications, and past treatments."),
            ("flask", "Functional Testing", "GI-MAP stool analysis, SIBO breath testing, food sensitivity panels, and organic acids testing."),
            ("leaf", "Gut Restoration", "A phased 5R protocol: Remove, Replace, Reinoculate, Repair, and Rebalance with targeted nutrition and botanicals."),
            ("chat", "Progress Tracking", "Regular follow-ups with symptom tracking and retesting to ensure lasting resolution."),
        ],
        "faqs": [
            ("What is SIBO?", "Small Intestinal Bacterial Overgrowth (SIBO) occurs when bacteria that normally live in the large intestine migrate to the small intestine, causing bloating, pain, and malabsorption. It&rsquo;s a common underlying cause of IBS."),
            ("How do you test for food sensitivities?", "We use IgG food sensitivity panels alongside elimination diets. However, the goal is always to identify and treat the root cause (often gut inflammation) so you can reintroduce foods over time."),
            ("Can gut issues cause anxiety?", "Yes. The gut-brain axis means gut inflammation and microbial imbalances directly affect neurotransmitter production and nervous system function. Treating the gut often improves mental health."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "fatigue-sleep-energy",
        "meta_title": "Fatigue, Sleep & Energy",
        "meta_desc": "Naturopathic treatment for chronic fatigue, adrenal dysfunction, insomnia, brain fog, and low energy. Virtual clinic for Ontario & UK.",
        "eyebrow": "Conditions treated",
        "h1": "Fatigue, Sleep & Energy Conditions",
        "lead": "Tired of being tired? We identify the root cause of your fatigue &mdash; whether it&rsquo;s adrenal dysfunction, thyroid issues, nutrient deficiency, or something else entirely.",
        "image": "system-energy",
        "image_alt": "A warm, sunlit bedroom with terracotta bedding",
        "parent": "Conditions",
        "parent_url": "conditions.html",
        "empathy_h": "Exhaustion is not a lifestyle",
        "empathy_p": "You wake up tired, push through the day on caffeine, crash in the afternoon, and can&rsquo;t sleep at night. You&rsquo;ve been told your labs are &ldquo;normal&rdquo; but you know something isn&rsquo;t right. Fatigue always has a cause &mdash; and it&rsquo;s almost always treatable once we find it.",
        "conditions": ["Chronic fatigue", "Adrenal dysfunction", "Poor sleep quality", "Difficulty waking or staying asleep", "Low energy &amp; brain fog", "Iron deficiency &amp; anaemia", "Thyroid-related fatigue"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Energy Audit", "A comprehensive review of your sleep, energy patterns, diet, stress, and symptom history."),
            ("flask", "Root-Cause Testing", "Thyroid panels (full, not just TSH), iron studies, B12, vitamin D, cortisol mapping, and metabolic markers."),
            ("leaf", "Restorative Protocol", "Targeted supplementation, adaptogenic herbs, sleep hygiene optimisation, and dietary strategies to rebuild your energy reserves."),
            ("chat", "Progress Monitoring", "Regular check-ins to track improvement and refine your plan until you feel consistently well."),
        ],
        "faqs": [
            ("Why am I always tired even though my blood work is normal?", "Standard blood work often uses wide reference ranges that miss subclinical issues. We use functional ranges and comprehensive panels (thyroid, iron, B12, cortisol) to catch what conventional testing misses."),
            ("What is adrenal dysfunction?", "Often called adrenal fatigue, it&rsquo;s a pattern of abnormal cortisol production caused by chronic stress. It can cause morning fatigue, afternoon crashes, disrupted sleep, and poor stress tolerance."),
            ("How long does it take to recover from chronic fatigue?", "It depends on the cause. Nutrient deficiencies may resolve in weeks; adrenal or thyroid issues typically take 3&ndash;6 months of consistent treatment."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "mental-health-emotional-wellbeing",
        "meta_title": "Mental Health & Emotional Wellbeing",
        "meta_desc": "Naturopathic support for depression, anxiety, trauma, PTSD, postpartum mood changes, and emotional wellbeing. Virtual care for Ontario & UK.",
        "eyebrow": "Conditions treated",
        "h1": "Mental Health & Emotional Wellbeing",
        "lead": "Holistic support for depression, anxiety, trauma, and emotional health &mdash; combining naturopathic medicine with evidence-based counselling.",
        "image": "system-energy",
        "image_alt": "A warm, sunlit bedroom with terracotta bedding",
        "parent": "Conditions",
        "parent_url": "conditions.html",
        "empathy_h": "Your mental health deserves more than a prescription",
        "empathy_p": "Depression, anxiety, trauma &mdash; these aren&rsquo;t character flaws or things you should just push through. They&rsquo;re complex conditions with psychological, biochemical, and lifestyle components. We address all three, combining talk therapy with targeted naturopathic interventions.",
        "conditions": ["Depression &amp; low mood", "Anxiety disorders", "Emotional overwhelm", "Trauma &amp; PTSD", "Postpartum mood changes", "Seasonal affective disorder (SAD)", "Stress-related cognitive difficulties"],
        "conditions_title": "What we support in this area",
        "approach": [
            ("clipboard", "Comprehensive Intake", "Your mental health history, physical symptoms, lifestyle, relationships, and what you&rsquo;ve tried before."),
            ("flask", "Biochemical Assessment", "Testing for nutrient deficiencies, hormonal imbalances, thyroid function, and inflammatory markers that affect mood."),
            ("leaf", "Integrated Care", "CBT, naturopathic supplementation, botanical medicine, and lifestyle interventions working together."),
            ("chat", "Therapeutic Relationship", "Consistent, compassionate support with sessions adapted to your evolving needs."),
        ],
        "faqs": [
            ("Can naturopathy treat depression?", "Naturopathic medicine can be a powerful part of depression treatment. We address biochemical contributors (nutrient deficiencies, hormonal imbalances, inflammation) alongside counselling to support the whole person."),
            ("What is postpartum mood support?", "The postpartum period involves massive hormonal shifts that can trigger depression, anxiety, and mood instability. We provide nutritional, hormonal, and emotional support during this transition."),
            ("Do you work with patients on medication?", "Yes. We work collaboratively with your prescribing physician. Naturopathic care can complement medication and, in some cases, support a supervised transition off medication when appropriate."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "thyroid-autoimmune",
        "meta_title": "Thyroid & Autoimmune Conditions",
        "meta_desc": "Naturopathic treatment for hypothyroidism, Hashimoto's, autoimmune conditions, chronic inflammation, and mould illness. Virtual care for Ontario & UK.",
        "eyebrow": "Conditions treated",
        "h1": "Thyroid & Autoimmune Conditions",
        "lead": "Comprehensive naturopathic care for thyroid dysfunction, autoimmune conditions, chronic inflammation, and environmental illness.",
        "image": "system-stress",
        "image_alt": "Stacked stones balanced on a hillside at golden hour",
        "parent": "Conditions",
        "parent_url": "conditions.html",
        "empathy_h": "When your body turns on itself",
        "empathy_p": "Autoimmune conditions are confusing and frustrating. You might have symptoms that come and go, labs that look &ldquo;borderline,&rdquo; or a diagnosis with limited treatment options. Naturopathic medicine focuses on calming the immune response, reducing inflammation, and supporting the organs affected &mdash; giving your body the tools to find balance again.",
        "conditions": ["Hypothyroidism", "Hashimoto&rsquo;s thyroiditis", "Hyperthyroidism &amp; Graves&rsquo; disease", "Autoimmune conditions", "Chronic inflammation", "Mould illness &amp; mycotoxin exposure"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Detailed Assessment", "Your symptom history, family history, environmental exposures, and autoimmune markers."),
            ("flask", "Comprehensive Testing", "Full thyroid panels (TSH, T3, T4, antibodies), inflammatory markers, mould/mycotoxin testing, and nutrient status."),
            ("leaf", "Immune Modulation", "Anti-inflammatory nutrition, gut healing (the gut-immune connection), botanical immune modulators, and environmental interventions."),
            ("chat", "Long-Term Management", "Autoimmune conditions require ongoing support. We provide consistent monitoring and protocol adjustments."),
        ],
        "faqs": [
            ("What is Hashimoto's thyroiditis?", "Hashimoto&rsquo;s is an autoimmune condition where the immune system attacks the thyroid gland, gradually reducing its function. It&rsquo;s the most common cause of hypothyroidism and is often underdiagnosed."),
            ("Can naturopathy help autoimmune conditions?", "Yes. While we can&rsquo;t cure autoimmune disease, naturopathic medicine can reduce flares, calm inflammation, heal the gut (a major driver of autoimmunity), and improve quality of life significantly."),
            ("What is mould illness?", "Chronic Inflammatory Response Syndrome (CIRS) from mould exposure can cause fatigue, brain fog, joint pain, and respiratory issues. We test for mycotoxins and provide targeted detoxification protocols."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "skin-conditions-general-wellness",
        "meta_title": "Skin Conditions & General Wellness",
        "meta_desc": "Naturopathic treatment for eczema, psoriasis, acne, rosacea, hair loss, histamine intolerance, and general wellness. Virtual care for Ontario & UK.",
        "eyebrow": "Conditions treated",
        "h1": "Skin Conditions & General Wellness",
        "lead": "Your skin is a window into your internal health. We treat eczema, acne, rosacea, and more by addressing the gut, hormones, and immune factors that drive them.",
        "image": "system-gut",
        "image_alt": "A kitchen counter with herbal teas, ginger, and glass jars",
        "parent": "Conditions",
        "parent_url": "conditions.html",
        "empathy_h": "Your skin is telling a deeper story",
        "empathy_p": "Creams and topicals only treat the surface. Persistent skin conditions &mdash; eczema, psoriasis, acne, rosacea &mdash; are almost always driven by internal factors: gut health, hormonal imbalances, food sensitivities, or histamine overload. We find and treat the internal cause so your skin can heal from the inside out.",
        "conditions": ["Eczema &amp; psoriasis", "Acne &amp; rosacea", "Hair loss", "Histamine intolerance", "Weight management", "Recurrent infections", "General wellness optimisation"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Comprehensive Intake", "Your skin history, diet, digestive health, stress, environmental exposures, and treatment history."),
            ("flask", "Internal Investigation", "Food sensitivity testing, gut analysis, hormone panels, and histamine/inflammation markers."),
            ("leaf", "Inside-Out Protocol", "Gut healing, anti-inflammatory nutrition, botanical medicine, and targeted supplementation to address root causes."),
            ("chat", "Ongoing Support", "Skin healing takes time. Regular follow-ups to track progress and adjust your protocol."),
        ],
        "faqs": [
            ("How is acne related to gut health?", "The gut-skin axis is well-established. Gut inflammation, bacterial imbalances, and intestinal permeability can trigger systemic inflammation that manifests as acne, eczema, or rosacea."),
            ("What is histamine intolerance?", "It&rsquo;s a condition where your body can&rsquo;t break down histamine efficiently, leading to hives, flushing, headaches, digestive issues, and skin reactions. It&rsquo;s often related to gut health and can be treated."),
            ("Can naturopathy help with weight management?", "Yes. We address the root causes of weight resistance &mdash; hormonal imbalances, thyroid dysfunction, cortisol dysregulation, insulin resistance &mdash; rather than prescribing restrictive diets."),
        ],
        "schema_type": "MedicalCondition",
    },
]

def build_schema(page, page_type):
    base_url = "https://villagenaturopathy.com"
    if page_type == "service":
        folder = "services"
        schema_item = {
            "@type": "MedicalTherapy",
            "name": page["h1"].replace("&rsquo;", "'").replace("&mdash;", "—"),
            "description": page["meta_desc"],
            "url": f"{base_url}/{folder}/{page['slug']}/"
        }
    else:
        folder = "conditions"
        schema_item = {
            "@type": "MedicalCondition",
            "name": page["h1"].replace("&rsquo;", "'").replace("&mdash;", "—"),
            "description": page["meta_desc"],
            "possibleTreatment": {
                "@type": "MedicalTherapy",
                "name": "Naturopathic Treatment",
                "description": "Root-cause naturopathic strategies tailored to your unique health picture."
            }
        }

    faq_entities = []
    for q, a in page["faqs"]:
        faq_entities.append({
            "@type": "Question",
            "name": q.replace("&rsquo;", "'"),
            "acceptedAnswer": {"@type": "Answer", "text": a.replace("&rsquo;", "'").replace("&mdash;", "—").replace("&ndash;", "–").replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&amp;", "&")}
        })

    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "MedicalBusiness",
                "name": "Village Naturopathy",
                "url": f"{base_url}/",
                "email": "drheather@villagenaturopathy.com",
                "medicalSpecialty": "Naturopathic",
                "areaServed": ["Ontario", "United Kingdom"],
                "availableService" if page_type == "service" else "makesOffer": schema_item
            },
            {"@type": "FAQPage", "mainEntity": faq_entities},
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{base_url}/"},
                    {"@type": "ListItem", "position": 2, "name": page["parent"], "item": f"{base_url}/{page['parent_url']}"},
                    {"@type": "ListItem", "position": 3, "name": page["meta_title"]}
                ]
            }
        ]
    }
    return json.dumps(graph, indent=2, ensure_ascii=False)

def render_page(page, page_type):
    folder = "services" if page_type == "service" else "conditions"
    canonical = f"https://villagenaturopathy.com/{folder}/{page['slug']}/"

    conditions_html = "\n".join(f'            <li>{c}</li>' for c in page["conditions"])
    approach_html = ""
    for icon_key, title, text in page["approach"]:
        approach_html += f'''          <div class="feature-row">
            <span class="icon-circle">
              {ICONS[icon_key]}
            </span>
            <div class="feature-row-content">
              <h3>{title}</h3>
              <p>{text}</p>
            </div>
          </div>
'''

    faq_html = ""
    for q, a in page["faqs"]:
        faq_html += f'''          <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
            <button class="faq-question" itemprop="name">{q}</button>
            <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
              <div itemprop="text"><p>{a}</p></div>
            </div>
          </div>
'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page["meta_title"]} &mdash; Village Naturopathy</title>
  <meta name="description" content="{page["meta_desc"]}">
  <link rel="canonical" href="{canonical}">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Village Naturopathy">
  <meta property="og:title" content="{page["meta_title"]} &mdash; Village Naturopathy">
  <meta property="og:description" content="{page["meta_desc"]}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://villagenaturopathy.com/assets/images/{page["image"]}.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#F6F3EE">

  <link rel="icon" href="{REL}favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{REL}apple-touch-icon.png">
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link rel="manifest" href="{REL}site.webmanifest">
  <link rel="preload" href="{REL}assets/fonts/Zodiak-Variable.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="{REL}assets/fonts/ClashGrotesk-Variable.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{REL}css/styles.css">
  <noscript><style>.reveal, .reveal-stagger > * {{ opacity: 1 !important; transform: none !important; }}</style></noscript>

  <script type="application/ld+json">
  {build_schema(page, page_type)}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

{nav_html()}

  <main id="main">
    <section class="page-hero" aria-labelledby="page-title">
      <div class="hero-bg">
        <picture>
          <source srcset="{REL}assets/images/{page["image"]}.webp" type="image/webp">
          <img src="{REL}assets/images/{page["image"]}.jpg" alt="{page["image_alt"]}" fetchpriority="high">
        </picture>
      </div>
      <div class="hero-copy">
        <p class="eyebrow">{page["eyebrow"]}</p>
        <h1 id="page-title">{page["h1"]}</h1>
        <p class="lead">{page["lead"]}</p>
      </div>
    </section>

{trust_bar()}

    <!-- Empathy / Problem -->
    <section class="section reveal">
      <div class="container">
        <div class="split">
          <div class="split-media">
            <picture>
              <source srcset="{REL}assets/images/{page["image"]}.webp" type="image/webp">
              <img src="{REL}assets/images/{page["image"]}.jpg" alt="" loading="lazy">
            </picture>
          </div>
          <div class="split-copy">
            <p class="eyebrow">Understanding your experience</p>
            <h2>{page["empathy_h"]}</h2>
            <p>{page["empathy_p"]}</p>
            <a class="btn btn--warm" href="{REL}book.html" style="margin-top:var(--space-sm);align-self:flex-start">Book a free consult</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Conditions list -->
    <section class="section reveal" style="background:var(--cream-50)">
      <div class="container">
        <div class="conditions-block">
          <div class="section-head">
            <p class="eyebrow">{page["conditions_title"]}</p>
          </div>
          <ul class="conditions-list">
{conditions_html}
          </ul>
        </div>
      </div>
    </section>

    <!-- Our approach -->
    <section class="section" aria-labelledby="approach-title">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">Our approach</p>
          <h2 id="approach-title">How we work with you</h2>
        </div>
        <div class="reveal-stagger" style="max-width:720px;margin-inline:auto">
{approach_html}        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section" style="background:var(--cream-50)" aria-labelledby="faq-title">
      <div class="container" style="max-width:720px">
        <div class="section-head reveal">
          <p class="eyebrow">Common questions</p>
          <h2 id="faq-title">Frequently asked questions</h2>
        </div>
        <div class="faq-list reveal" itemscope itemtype="https://schema.org/FAQPage">
{faq_html}        </div>
      </div>
    </section>

{cta_banner()}
  </main>

{footer_html()}

  <script src="{REL}js/main.js" defer></script>
</body>
</html>
'''

def main():
    for page in SERVICES:
        out_dir = os.path.join(SITE_ROOT, "services", page["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(render_page(page, "service"))
        print(f"  services/{page['slug']}/index.html")

    for page in CONDITIONS:
        out_dir = os.path.join(SITE_ROOT, "conditions", page["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(render_page(page, "condition"))
        print(f"  conditions/{page['slug']}/index.html")

    print(f"\nGenerated {len(SERVICES)} service + {len(CONDITIONS)} condition pages")

if __name__ == "__main__":
    main()
