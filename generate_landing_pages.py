#!/usr/bin/env python3
"""Generate service + condition pages (and the conditions hub) for Village Naturopathy.

Copy source: "Village Naturopathy: Website Revisions" (Heather, Oct 2026).
Shared chrome, schema and head tags come from site_common.py.
Run via build_site.py (also writes sitemap, llms.txt and markdown mirrors).
"""
import os

import site_common as sc
from site_common import BASE, JANE_BOOK, JANE_DISC, plain

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
REL = "../../"

TESTING_NOTE = ('<em>Testing isn&rsquo;t required to start care. Any testing is recommended case by case, '
                'based on your individual needs.</em>')

# ------------------------------------------------------------------ SERVICES
SERVICES = [
    {
        "slug": "stress-anxiety",
        "meta_title": "Naturopathic Care for Stress, Mood & Anxiety | Village Naturopathy",
        "meta_desc": ("Root-cause naturopathic care for chronic stress, anxiety, low mood and burnout. Virtual "
                      "consultations for Ontario & the UK. Book a free discovery call."),
        "eyebrow": "Stress, mood &amp; anxiety",
        "h1": "Naturopathic Care for Stress, Mood &amp; Anxiety",
        "lead": ("Stress goes deeper than feeling frazzled. It disrupts sleep, hormones, digestion and your ability "
                 "to feel like yourself. We find the root cause of your stress, mood and anxiety concerns and build "
                 "a plan that works with your life, not against it."),
        "quick": ("Village Naturopathy offers virtual naturopathic care for stress, anxiety, low mood and burnout "
                  "across the UK and Ontario. Dr. Heather Robinson, ND, starts with a 75-minute consultation, looks "
                  "at your sleep, nervous system, hormones, gut and nutrient status, then builds a personalised plan."),
        "image": "system-stress",
        "image_alt": "Stacked stones balanced on a hillside at golden hour",
        "parent": "Services", "parent_url": "services.html",
        "empathy_h": "When stress becomes your baseline",
        "empathy_p": ("You&rsquo;ve been running on adrenaline for so long it feels normal. The sleep issues, the "
                      "afternoon crashes, the tight shoulders, the brain fog: they&rsquo;ve become part of your "
                      "identity. But your body is telling you something. Naturopathic medicine looks at the full "
                      "picture of your nervous system, your hormones, your gut and your lifestyle, and builds a path "
                      "back to feeling grounded."),
        "empathy2_h": "When your mood feels out of your control",
        "empathy2_p": ("It can feel scary and overwhelming when your mood and thoughts don&rsquo;t feel like your own. "
                       "We look at whether there are physiological factors behind your mood changes and anxiety, like "
                       "hormone shifts or nutrient deficiencies, or whether psychosocial factors are the main driver "
                       "and need support. Whatever the cause, we have a well-rounded toolbox to support you."),
        "conditions": ["Chronic stress &amp; overwhelm", "Generalised anxiety disorder", "Panic attacks",
                       "Burnout &amp; adrenal fatigue", "Insomnia &amp; sleep disturbances",
                       "Nervous system dysregulation", "Depression &amp; low mood", "PMDD"],
        "conditions_title": "Conditions we treat",
        "approach": [
            ("clipboard", "Comprehensive Assessment", "A 75-minute initial consultation to understand your stress history, triggers, lifestyle, and health goals."),
            ("flask", "Comprehensive Testing", "Comprehensive blood work, DUTCH hormone testing, cortisol mapping and nutrient status to see what&rsquo;s happening beneath the surface. " + TESTING_NOTE),
            ("leaf", "Personalised Plan", "Evidence-based botanical medicine, targeted nutrition, nervous system regulation techniques, and lifestyle modifications tailored to you."),
            ("chat", "Ongoing Support", "Regular follow-ups and adjustments to your plan as you progress. You&rsquo;re never doing this alone."),
        ],
        "faqs": [
            ("What causes chronic stress and anxiety?", "Chronic stress is rarely caused by one thing. It&rsquo;s usually a combination of lifestyle factors, unresolved trauma, hormonal imbalances, nutrient deficiencies, and nervous system dysregulation. Naturopathic medicine looks at all of these together."),
            ("How does naturopathy treat anxiety differently?", "Rather than masking symptoms, we identify root causes, whether that&rsquo;s a cortisol imbalance, gut-brain axis disruption or a mineral deficiency, and address them with targeted nutrition, botanicals and nervous system tools."),
            ("Can a naturopath help with anxiety?", "A naturopathic doctor can look at the physical contributors to anxiety, such as blood sugar swings, nutrient status, hormones, sleep and gut health, and support them alongside the lifestyle and nervous system factors. Appointments are virtual, for patients across the UK and Ontario. Naturopathic care is complementary, so we work alongside your GP or mental health team."),
            ("What is the best natural treatment for stress and anxiety?", "There is no single best option, because stress looks different in every person. A plan usually combines nutrition, targeted supplementation, botanical medicine, sleep support and nervous system regulation practices, chosen after a full history and, where useful, testing. Dr. Heather approves the plan with you, step by step."),
            ("Can naturopathy help with PMDD or low mood?", "Naturopathic care can support the hormonal, nutritional and nervous system factors that often sit behind PMDD and low mood, and it works alongside medical care. Virtual consultations are available in the UK and Ontario. If you are struggling with thoughts of harming yourself, please contact your GP or emergency services straight away, or call Samaritans on 116 123 (UK) or 988 (Canada)."),
            ("How long does treatment typically take?", "Most patients notice improvements within 4&ndash;6 weeks. A comprehensive treatment plan typically spans 3&ndash;6 months, with follow-ups adjusted to your pace."),
            ("Do you work alongside my GP or therapist?", "Absolutely. Naturopathic care is integrative, and we collaborate with your existing healthcare team to ensure a cohesive approach."),
        ],
        "uk_topic": "stress-burnout",
        "uk_label": "burnout and stress",
    },
    {
        "slug": "hormone-balancing",
        "meta_title": "Naturopathic Hormone Balancing | Village Naturopathy",
        "meta_desc": ("Root-cause naturopathic care for PMOS/PCOS, PMS, PMDD, endometriosis, irregular periods and "
                      "hormonal acne. Virtual care for the UK & Ontario. Free discovery call."),
        "eyebrow": "Hormone balancing",
        "h1": "Naturopathic Hormone Balancing",
        "lead": ("Hormone issues are common but not normal. We address the root cause of menstrual irregularities, "
                 "PMS, PMOS/PCOS, endometriosis, acne and hair loss with treatment plans tailored to your body."),
        "quick": ("Village Naturopathy offers virtual naturopathic hormone care across the UK and Ontario. After a "
                  "75-minute consultation, Dr. Heather Robinson, ND, uses your cycle history, symptoms and, where "
                  "appropriate, DUTCH hormone testing and blood work to build a personalised plan for PMOS/PCOS, "
                  "PMS and PMDD, endometriosis, irregular periods and hormonal acne."),
        "image": "system-hormones",
        "image_alt": "Three women standing together in warm light",
        "parent": "Services", "parent_url": "services.html",
        "empathy_h": "When your hormones feel out of your control",
        "empathy_p": ("Irregular periods, weight changes that don&rsquo;t make sense, skin that won&rsquo;t clear, mood "
                      "swings that leave you feeling like a different person. You&rsquo;ve tried everything and nothing "
                      "sticks. Hormone imbalances don&rsquo;t resolve on their own. We use comprehensive testing to "
                      "understand your unique hormonal picture and build a plan that restores balance from the inside out."),
        "conditions": ["PMOS/PCOS (Polyendocrine Metabolic Ovarian Syndrome)", "PMS &amp; PMDD", "Heavy or painful periods",
                       "Endometriosis", "Irregular or absent periods", "Hormonal acne", "Fertility support",
                       "Post-pill syndrome"],
        "conditions_title": "Conditions we treat",
        "approach": [
            ("clipboard", "Comprehensive Assessment", "A 75-minute initial consultation with a detailed look at your menstrual history, symptoms, lifestyle, stress load and health goals."),
            ("flask", "Testing", "Comprehensive blood work, DUTCH hormone testing, thyroid panels and nutrient status to map your unique hormonal landscape. " + TESTING_NOTE),
            ("leaf", "Targeted Treatment", "Clinical nutrition, targeted supplementation, evidence-based botanical medicine, lifestyle and adjunctive support designed to restore hormonal rhythm naturally."),
            ("chat", "Cycle-Aligned Support", "Follow-ups timed to your cycle so we can track progress and adjust your plan in real time."),
        ],
        "faqs": [
            ("What is DUTCH testing?", "DUTCH (Dried Urine Test for Comprehensive Hormones) measures your sex hormones, cortisol pattern, and hormone metabolites. It gives us a far more detailed picture than standard blood work alone."),
            ("Can naturopathy help with PMOS/PCOS?", "Yes. PMOS (Polyendocrine Metabolic Ovarian Syndrome) is the updated name for PCOS. Naturopathic treatment focuses on insulin regulation, reducing inflammation and supporting hormone balance through nutrition, botanicals and lifestyle changes, addressing the root drivers rather than just the symptoms."),
            ("Can a naturopath help with irregular or painful periods?", "Yes. We look at what&rsquo;s driving your cycle changes, from nutrient status and blood sugar to stress and inflammation, and build a plan to support a healthier, more comfortable cycle."),
            ("Can naturopathy help with PMS or PMDD?", "Yes. We assess how your hormones, nervous system and nutrition interact across your cycle, then use targeted nutrition, supplementation and botanicals to reduce symptoms month to month."),
            ("Do you offer online hormone consultations in the UK?", "Yes. All appointments are virtual, and Dr. Heather sees patients across the UK and Ontario."),
            ("How long does hormone balancing take?", "Hormonal shifts typically take 3&ndash;6 menstrual cycles to fully manifest. Most patients notice improvements in energy and mood within the first month."),
            ("Do I need to stop birth control?", "Not necessarily. We work with wherever you are. If you&rsquo;re considering coming off hormonal contraception, we can support that transition."),
        ],
        "uk_topic": "hormone-balancing",
        "uk_label": "hormone health",
    },
    {
        "slug": "gut-health",
        "meta_title": "Naturopathic Gut Health Treatment | Village Naturopathy",
        "meta_desc": ("Root-cause naturopathic care for IBS, SIBO, bloating, food sensitivities and reflux. Virtual "
                      "consultations for the UK & Ontario. Free discovery call."),
        "eyebrow": "Gut health",
        "h1": "Naturopathic Gut Health Treatment",
        "lead": ("A healthy gut means a healthy nervous system and healthy hormones. Whether you&rsquo;re dealing with "
                 "IBS, SIBO, bloating, or food sensitivities, the gut is the foundation of whole-body health."),
        "quick": ("Village Naturopathy offers virtual naturopathic care for IBS, SIBO, bloating, reflux and food "
                  "sensitivities across the UK and Ontario. Dr. Heather Robinson, ND, reviews your digestive history "
                  "in a 75-minute consultation and, where testing is useful, uses GI-MAP stool analysis or SIBO "
                  "breath testing to guide a tailored plan."),
        "image": "system-gut",
        "image_alt": "A kitchen counter with herbal teas, ginger, and glass jars of dried herbs",
        "parent": "Services", "parent_url": "services.html",
        "empathy_h": "When your gut is running the show",
        "empathy_p": ("Bloating after every meal, nausea that comes and goes, foods you used to love now causing "
                      "problems. You&rsquo;ve cut out dairy, gluten and sugar, and still feel terrible. Digestive issues "
                      "aren&rsquo;t just uncomfortable; they affect your energy, your mood, your hormones, and your immune "
                      "system. We look beyond the symptoms to find what&rsquo;s actually driving the dysfunction."),
        "conditions": ["IBS (Irritable Bowel Syndrome)", "SIBO (Small Intestinal Bacterial Overgrowth)", "Bloating &amp; gas",
                       "Constipation &amp; diarrhoea", "Food sensitivities &amp; intolerances", "Acid reflux &amp; GERD",
                       "Leaky gut (intestinal permeability)", "Candida overgrowth", "Inflammatory bowel conditions"],
        "conditions_title": "Conditions we treat",
        "approach": [
            ("clipboard", "Comprehensive Assessment", "A 75-minute initial consultation with a thorough review of your digestive history, diet, stress patterns, medication use and symptom timeline."),
            ("flask", "Functional Testing", "GI-MAP stool analysis, SIBO breath testing, food sensitivity panels, and organic acids testing to identify the root cause. " + TESTING_NOTE),
            ("leaf", "Tailored Gut Protocol", "Through careful history-taking and relevant testing, we create a plan to correct the terrain of your gut, optimise your microbiome and address the other factors that influence gut health, such as nutrient deficiencies and stress. Treatment uses nutraceuticals, botanicals and dietary changes as part of a holistic, whole-person approach."),
            ("chat", "Ongoing Monitoring", "Regular check-ins to track symptom resolution, adjust the protocol, and retest when needed."),
        ],
        "faqs": [
            ("What is a GI-MAP test and do I need one?", "GI-MAP is a comprehensive stool test that uses DNA analysis to identify pathogens, parasites, bacterial imbalances, inflammation markers, and digestive function. It&rsquo;s one of the most detailed gut tests available. Not everyone needs testing. We recommend it based on your symptoms and history."),
            ("How long does it take to heal your gut naturally?", "It depends on the condition. Simple dysbiosis may resolve in 6&ndash;8 weeks. More complex issues like SIBO or inflammatory conditions typically take 3&ndash;6 months of structured treatment."),
            ("Do I need to follow a restrictive diet?", "Short-term dietary modifications are sometimes helpful, but the goal is always to expand your diet, not restrict it permanently. We focus on healing the gut so you can enjoy food again."),
            ("Can gut health affect my mood?", "Absolutely. The gut-brain axis is a well-established connection. Around 90% of the body&rsquo;s serotonin is produced in the gut, and gut inflammation directly impacts mood, anxiety, and cognitive function."),
            ("Can a naturopath help with IBS or SIBO?", "Yes. We look for what&rsquo;s driving your symptoms, whether that&rsquo;s bacterial overgrowth, low stomach acid, stress or food triggers, and build a targeted plan using nutrition, botanicals and nutraceuticals. SIBO breath testing is available when it&rsquo;s useful."),
            ("Why am I bloated after every meal?", "Persistent bloating can come from several causes, including SIBO, food intolerances, low digestive enzymes or stress affecting digestion. An assessment helps identify which ones apply to you."),
            ("Do you offer online gut health consultations in the UK?", "Yes. All appointments are virtual, and Dr. Heather sees patients across the UK and Ontario."),
        ],
        "uk_topic": "gut-health",
        "uk_label": "gut health",
    },
    {
        "slug": "fatigue",
        "meta_title": "Naturopathic Treatment for Fatigue & Low Energy | Village Naturopathy",
        "meta_desc": ("Always tired but your labs are 'normal'? Naturopathic care for fatigue, burnout, low iron and "
                      "B12, and post-viral fatigue. Virtual care for the UK & Ontario."),
        "eyebrow": "Energy",
        "h1": "Naturopathic Approach to Fatigue",
        "lead": ("Fatigue is one of the most common symptoms people experience, which can make the cause hard to pin "
                 "down. We take a deep dive into every potential cause of your fatigue, so no stone is left unturned."),
        "quick": ("Village Naturopathy offers virtual naturopathic care for persistent fatigue across the UK and "
                  "Ontario. Dr. Heather Robinson, ND, combines thorough history-taking with key lab markers such as "
                  "iron, B12, thyroid markers and cortisol to find what is draining your energy, then builds a "
                  "personalised plan."),
        "image": "system-energy",
        "image_alt": "A warm, sunlit bedroom with terracotta bedding",
        "parent": "Services", "parent_url": "services.html",
        "empathy_h": "Helping you come back to feeling like yourself",
        "empathy_p": ("You&rsquo;re doing all the right things, but you still can&rsquo;t shake the 2 p.m. slump. You have "
                      "trouble falling asleep, deal with brain fog, and wake up tired. You&rsquo;re relying on coffee or "
                      "matcha more than you&rsquo;d like to. Your doctor says your labs are fine, but you don&rsquo;t feel "
                      "fine. We combine thorough history-taking with key lab markers to identify the sources of your fatigue."),
        "conditions": ["Burnout &amp; adrenal fatigue", "Postpartum fatigue", "Nutrient deficiencies (e.g. iron and B12)",
                       "Post-viral fatigue"],
        "conditions_title": "Conditions we support",
        "approach": [
            ("clipboard", "Initial Consultation", "A 75-minute initial consultation with a comprehensive look at your health history, relevant labs and what you&rsquo;ve tried before."),
            ("flask", "Root-Cause Investigation", "Comprehensive blood work looking at nutrient status, hormones and cortisol, with more in-depth testing if needed. " + TESTING_NOTE),
            ("leaf", "Targeted Treatment", "We start with the most foundational causes of fatigue identified through your history and labs, then layer on support as needed using nutrition, supplementation, botanical medicine and lifestyle interventions."),
            ("chat", "Ongoing Care", "Regular appointments that adapt to your needs, so we can follow up on your progress and make adjustments as needed."),
        ],
        "faqs": [
            ("Why am I always tired even though my blood work is normal?", "Standard blood work often checks only a few markers, and &lsquo;normal&rsquo; ranges are broad. We look more closely at nutrient status, thyroid function, hormones and cortisol, alongside your sleep, stress and lifestyle, to find what&rsquo;s draining your energy."),
            ("What tests do you use to investigate fatigue?", "Usually comprehensive blood work, including iron, B12, vitamin D, thyroid markers and hormones. More in-depth testing is only recommended if it&rsquo;s needed for you."),
            ("Can low iron or B12 cause fatigue?", "Yes. Iron and B12 deficiencies are among the most common and most overlooked causes of fatigue, especially for women with heavy periods, plant-based diets or digestive issues."),
            ("Can a naturopath help with burnout?", "Yes. We look at how long-term stress has affected your sleep, hormones, nervous system and nutrient levels, then build a plan to help you rebuild your energy step by step."),
            ("How long does it take to get my energy back?", "It depends on what&rsquo;s driving your fatigue. Many patients notice changes within 4&ndash;8 weeks, with a full plan typically running 3&ndash;6 months."),
            ("Is this covered by insurance?", "Naturopathic consultations are covered by many extended health plans in Ontario. Check with your provider for your specific coverage. Appointments are virtual, and available to patients in Ontario and the UK."),
        ],
        "uk_topic": "fatigue",
        "uk_label": "fatigue and low energy",
    },
]

# ---------------------------------------------------------------- CONDITIONS
CONDITIONS = [
    {
        "slug": "stress-anxiety-nervous-system",
        "meta_title": "Stress, Anxiety & Nervous System Support",
        "meta_desc": ("Naturopathic care for chronic stress, anxiety, panic, burnout, low mood and nervous system "
                      "dysregulation. Virtual clinic for the UK & Ontario."),
        "eyebrow": "Conditions treated",
        "h1": "Stress, Anxiety &amp; Nervous System Dysregulation",
        "lead": ("Root-cause naturopathic care for chronic stress, anxiety, and nervous system imbalances. We address "
                 "what&rsquo;s driving your symptoms, not just managing them."),
        "image": "system-stress", "image_alt": "Stacked stones balanced on a hillside at golden hour",
        "parent": "Conditions", "parent_url": "conditions.html",
        "empathy_h": "Your nervous system is stuck in overdrive",
        "empathy_p": ("The constant hum of anxiety, the inability to switch off, the feeling of being wired but tired. "
                      "Your body has been in fight-or-flight for so long it doesn&rsquo;t know how to rest. This isn&rsquo;t "
                      "a character flaw. It&rsquo;s a physiological pattern that can be changed with the right support."),
        "conditions": ["Chronic stress &amp; overwhelm", "Generalised anxiety disorder", "Panic attacks", "Burnout &amp; adrenal fatigue",
                       "Insomnia &amp; sleep disturbances", "Nervous system dysregulation", "Depression &amp; low mood", "PMDD"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Comprehensive Assessment", "Understanding your stress timeline, triggers, sleep patterns, and how your body responds to pressure."),
            ("flask", "Functional Testing", "Cortisol mapping, DUTCH panels, thyroid function, and nutrient status to identify the biochemical drivers of your symptoms. " + TESTING_NOTE),
            ("leaf", "Restorative Plan", "Adaptogenic botanicals, targeted nutrients, nervous system regulation techniques, and sleep support."),
            ("chat", "Ongoing Guidance", "Regular follow-ups to adjust your plan and build lasting resilience over time."),
        ],
        "faqs": [
            ("What is nervous system dysregulation?", "It&rsquo;s when your autonomic nervous system gets stuck in a stress response (fight-or-flight) and can&rsquo;t easily return to a calm state. This can manifest as anxiety, insomnia, digestive issues, and chronic fatigue."),
            ("Is burnout the same as adrenal fatigue?", "They&rsquo;re related but not identical. Burnout is a state of chronic stress-induced exhaustion. Adrenal dysfunction (often called adrenal fatigue) refers to measurable changes in cortisol production that can be tested and treated."),
            ("Can naturopathy help with panic attacks?", "Yes. We address the physiological triggers, such as blood sugar dysregulation, magnesium deficiency and nervous system patterns, while also providing tools for in-the-moment regulation."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "hormonal-imbalances-womens-health",
        "meta_title": "Hormonal Imbalances & Women's Health",
        "meta_desc": ("Naturopathic care for PMOS/PCOS, PMS, PMDD, endometriosis, irregular periods, fertility support and "
                      "hormonal acne. Virtual care for the UK & Ontario."),
        "eyebrow": "Conditions treated",
        "h1": "Hormonal Imbalances &amp; Women&rsquo;s Health",
        "lead": ("From PMOS/PCOS to PMS, we treat the full spectrum of cycle and hormone concerns with root-cause "
                 "naturopathic medicine."),
        "image": "system-hormones", "image_alt": "Three women standing together in warm light",
        "parent": "Conditions", "parent_url": "conditions.html",
        "empathy_h": "Your hormones are trying to tell you something",
        "empathy_p": ("Painful periods, unexplained weight gain, acne that won&rsquo;t quit, mood swings that disrupt your "
                      "relationships: these aren&rsquo;t things you should just live with. Hormonal imbalances have "
                      "identifiable causes and treatable solutions. We dig into the data and create a plan that actually works."),
        "conditions": ["PMOS/PCOS (Polyendocrine Metabolic Ovarian Syndrome)", "PMS &amp; PMDD", "Heavy or painful periods", "Endometriosis",
                       "Irregular or absent periods", "Hormonal acne", "Fertility support", "Post-pill syndrome"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Detailed Intake", "Your menstrual history, symptom patterns, contraceptive history, and health goals."),
            ("flask", "Hormone Mapping", "DUTCH complete panels, thyroid function, metabolic markers, and blood work for a full hormonal picture. " + TESTING_NOTE),
            ("leaf", "Personalised Plan", "Clinical nutrition, evidence-based botanical medicine and targeted supplementation to restore balance."),
            ("chat", "Cycle-Tracked Follow-ups", "Progress monitoring aligned with your menstrual cycle for precise adjustments."),
        ],
        "faqs": [
            ("What hormonal conditions do you treat?", "We treat PMOS/PCOS, endometriosis, PMS/PMDD, irregular periods, hormonal acne, fertility challenges, post-pill syndrome, and more."),
            ("How is PMOS/PCOS treated naturopathically?", "We focus on the root drivers: insulin resistance, inflammation, and androgen excess. Treatment includes dietary changes, targeted supplementation, botanical medicine, and stress management."),
            ("Can you help with fertility?", "Yes. We optimise hormonal health, address underlying conditions, and support conception through evidence-based naturopathic protocols. We work alongside fertility specialists when needed."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "digestive-gut-health",
        "meta_title": "Digestive & Gut Health Conditions",
        "meta_desc": ("Naturopathic care for IBS, SIBO, bloating, food sensitivities, acid reflux and gut health issues. "
                      "Virtual clinic for the UK & Ontario."),
        "eyebrow": "Conditions treated",
        "h1": "Digestive &amp; Gut Health Conditions",
        "lead": ("From IBS to SIBO to food sensitivities, we get to the root of your digestive issues with functional "
                 "testing and targeted protocols."),
        "image": "system-gut", "image_alt": "A kitchen counter with herbal teas, ginger, and glass jars",
        "parent": "Conditions", "parent_url": "conditions.html",
        "empathy_h": "You deserve to eat without fear",
        "empathy_p": ("The bloating, the unpredictability, the growing list of foods you can&rsquo;t tolerate. Digestive "
                      "issues affect everything: your energy, your mood, your confidence, your social life. We use "
                      "functional testing to identify exactly what&rsquo;s going on and create a structured plan to restore "
                      "your gut health."),
        "conditions": ["IBS (Irritable Bowel Syndrome)", "SIBO (Small Intestinal Bacterial Overgrowth)", "Bloating &amp; gas",
                       "Constipation &amp; diarrhoea", "Food sensitivities &amp; intolerances", "Acid reflux &amp; GERD",
                       "Leaky gut (intestinal permeability)", "Candida overgrowth", "Inflammatory bowel conditions"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Digestive History", "A thorough review of your symptoms, diet, stress, medications, and past treatments."),
            ("flask", "Functional Testing", "GI-MAP stool analysis, SIBO breath testing, food sensitivity panels, and organic acids testing. " + TESTING_NOTE),
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
        "meta_desc": ("Naturopathic care for persistent fatigue, adrenal dysfunction, poor sleep, brain fog and low energy. "
                      "Virtual clinic for the UK & Ontario."),
        "eyebrow": "Conditions treated",
        "h1": "Fatigue, Sleep &amp; Energy Conditions",
        "lead": ("Tired of being tired? We identify the root cause of your fatigue, whether it&rsquo;s adrenal "
                 "dysfunction, thyroid issues, nutrient deficiency, or something else entirely."),
        "image": "system-energy", "image_alt": "A warm, sunlit bedroom with terracotta bedding",
        "parent": "Conditions", "parent_url": "conditions.html",
        "empathy_h": "Exhaustion is not a lifestyle",
        "empathy_p": ("You wake up tired, push through the day on caffeine, crash in the afternoon, and can&rsquo;t sleep "
                      "at night. You&rsquo;ve been told your labs are &ldquo;normal&rdquo; but you know something isn&rsquo;t "
                      "right. Fatigue always has a cause, and it&rsquo;s almost always treatable once we find it."),
        "conditions": ["Chronic fatigue", "Adrenal dysfunction", "Poor sleep quality", "Difficulty waking or staying asleep",
                       "Low energy &amp; brain fog", "Iron deficiency &amp; anaemia", "Thyroid-related fatigue"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Energy Audit", "A comprehensive review of your sleep, energy patterns, diet, stress, and symptom history."),
            ("flask", "Root-Cause Testing", "Thyroid panels (full, not just TSH), iron studies, B12, vitamin D, cortisol mapping, and metabolic markers. " + TESTING_NOTE),
            ("leaf", "Restorative Plan", "Targeted supplementation, adaptogenic herbs, sleep hygiene optimisation, and dietary strategies to rebuild your energy reserves."),
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
        "slug": "thyroid-autoimmune",
        "meta_title": "Thyroid & Autoimmune Conditions",
        "meta_desc": ("Naturopathic support for hypothyroidism, Hashimoto's, autoimmune conditions, chronic inflammation and "
                      "mould illness. Virtual care for the UK & Ontario."),
        "eyebrow": "Conditions treated",
        "h1": "Thyroid &amp; Autoimmune Conditions",
        "lead": ("Comprehensive naturopathic care for thyroid dysfunction, autoimmune conditions, chronic inflammation, and "
                 "environmental illness."),
        "image": "system-stress", "image_alt": "Stacked stones balanced on a hillside at golden hour",
        "parent": "Conditions", "parent_url": "conditions.html",
        "empathy_h": "When your body turns on itself",
        "empathy_p": ("Autoimmune conditions are confusing and frustrating. You might have symptoms that come and go, labs "
                      "that look &ldquo;borderline,&rdquo; or a diagnosis with limited treatment options. Naturopathic "
                      "medicine focuses on calming the immune response, reducing inflammation, and supporting the organs "
                      "affected, giving your body the tools to find balance again."),
        "conditions": ["Hypothyroidism", "Hashimoto&rsquo;s thyroiditis", "Hyperthyroidism &amp; Graves&rsquo; disease",
                       "Autoimmune conditions", "Chronic inflammation", "Mould illness &amp; mycotoxin exposure"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Detailed Assessment", "Your symptom history, family history, environmental exposures, and autoimmune markers."),
            ("flask", "Comprehensive Testing", "Full thyroid panels (TSH, T3, T4, antibodies), inflammatory markers, mould/mycotoxin testing, and nutrient status. " + TESTING_NOTE),
            ("leaf", "Immune Support", "Anti-inflammatory nutrition, gut healing (the gut-immune connection), botanical immune modulators, and environmental interventions."),
            ("chat", "Long-Term Management", "Autoimmune conditions require ongoing support. We provide consistent monitoring and plan adjustments."),
        ],
        "faqs": [
            ("What is Hashimoto's thyroiditis?", "Hashimoto&rsquo;s is an autoimmune condition where the immune system attacks the thyroid gland, gradually reducing its function. It&rsquo;s the most common cause of hypothyroidism and is often underdiagnosed."),
            ("Can naturopathy help autoimmune conditions?", "While we can&rsquo;t cure autoimmune disease, naturopathic medicine can support the body by calming inflammation, healing the gut (a major driver of autoimmunity), and improving quality of life. It works alongside your medical care."),
            ("What is mould illness?", "Chronic Inflammatory Response Syndrome (CIRS) from mould exposure can cause fatigue, brain fog, joint pain, and respiratory issues. We test for mycotoxins and provide targeted support."),
        ],
        "schema_type": "MedicalCondition",
    },
    {
        "slug": "acne-hormonal-skin",
        "meta_title": "Acne & Hormonal Skin Health",
        "meta_desc": ("Naturopathic care for hormonal and adult acne, looking at hormones, gut health, stress and nutrition. "
                      "Virtual clinic for the UK & Ontario."),
        "eyebrow": "Conditions treated",
        "h1": "Acne &amp; Hormonal Skin Health",
        "lead": ("Your skin is a window into your internal health. We look at the hormones, gut and stress patterns "
                 "behind persistent acne, and build a plan that works from the inside out."),
        "image": "system-gut", "image_alt": "A kitchen counter with herbal teas, ginger, and glass jars",
        "parent": "Conditions", "parent_url": "conditions.html",
        "empathy_h": "Your skin is telling a deeper story",
        "empathy_p": ("Creams and topicals only treat the surface. Persistent acne is often driven by internal factors: "
                      "hormonal shifts, blood sugar, gut health, food sensitivities or stress. We look for the internal "
                      "drivers so your skin has the support it needs to settle."),
        "conditions": ["Hormonal acne", "Adult acne", "Acne linked to PMOS/PCOS", "Acne linked to gut health or stress", "Hair loss"],
        "conditions_title": "What we treat in this area",
        "approach": [
            ("clipboard", "Comprehensive Intake", "Your skin history, cycle, diet, digestive health, stress, and treatment history."),
            ("flask", "Internal Investigation", "Hormone testing, gut analysis and nutrient markers where they are likely to help. " + TESTING_NOTE),
            ("leaf", "Inside-Out Plan", "Anti-inflammatory nutrition, gut support, botanical medicine and targeted supplementation to address root causes."),
            ("chat", "Ongoing Support", "Skin takes time to settle. Regular follow-ups to track progress and adjust your plan."),
        ],
        "faqs": [
            ("How is acne related to gut health?", "The gut-skin axis is well-established. Gut inflammation, bacterial imbalances, and intestinal permeability can trigger systemic inflammation that may show up on the skin."),
            ("Can hormones cause adult acne?", "Yes. Shifts in androgens, insulin and cortisol are common drivers of adult and hormonal acne, particularly along the jawline and around your cycle. Testing can help clarify what is happening for you."),
            ("Is acne connected to PMOS/PCOS?", "It can be. PMOS (Polyendocrine Metabolic Ovarian Syndrome, also known as PCOS) often involves raised androgens, which may contribute to acne. A full cycle and symptom history is the starting point."),
        ],
        "schema_type": "MedicalCondition",
    },
]

# ------------------------------------------------------------------ rendering
def related_uk(page):
    topic = page.get("uk_topic")
    if not topic:
        return ""
    return f'''    <section class="section" aria-labelledby="uk-title">
      <div class="container" style="max-width:720px">
        <div class="section-head reveal">
          <p class="eyebrow">In the UK</p>
          <h2 id="uk-title">Online care across the United Kingdom</h2>
        </div>
        <div class="about-content reveal">
          <p>Dr. Heather Robinson, ND, is a full member of the Association of Naturopathic Practitioners (UK) and sees patients by secure video across England, Scotland, Wales and Northern Ireland. Find {page["uk_label"]} support near you:</p>
          <ul class="conditions-list">
            <li><a href="{REL}uk/london/{topic}/">London</a></li>
            <li><a href="{REL}uk/edinburgh/">Edinburgh</a></li>
            <li><a href="{REL}uk/glasgow/">Glasgow</a></li>
            <li><a href="{REL}uk/belfast/">Belfast</a></li>
            <li><a href="{REL}uk/">All UK locations</a></li>
            <li><a href="{REL}uk/dutch-test/">DUTCH hormone testing in the UK</a></li>
          </ul>
        </div>
      </div>
    </section>

'''


def quick_of(page):
    return page.get("quick") or (page["lead"] + " Virtual appointments with Dr. Heather Robinson, ND, for patients across the UK and Ontario.")


def page_url(page, kind):
    folder = "services" if kind == "service" else "conditions"
    return f"{BASE}/{folder}/{page['slug']}/", f"{folder}/{page['slug']}/"


def render_page(page, kind):
    url, path = page_url(page, kind)
    img = f"{BASE}/assets/images/{page['image']}.jpg"
    title = page["meta_title"] if "|" in page["meta_title"] else f'{page["meta_title"]} | Village Naturopathy'
    faqs = page["faqs"]

    about = {"@type": "MedicalTherapy" if kind == "service" else "MedicalCondition",
             "name": plain(page["h1"]), "description": plain(page["meta_desc"])}
    if kind == "service":
        about = {"@type": "MedicalTherapy", "name": plain(page["h1"]), "alternateName": "Naturopathic medicine",
                 "description": plain(page["meta_desc"])}
    nodes = [
        sc.medical_webpage(url, page["h1"], page["meta_desc"], about=about, image=img,
                           breadcrumb_id=url + "#breadcrumb"),
        {**sc.breadcrumb([("Home", f"{BASE}/"), (page["parent"], f"{BASE}/{page['parent_url']}"),
                          (page["h1"], None)]), "@id": url + "#breadcrumb"},
        sc.faq_node(faqs, url),
    ]
    if kind == "service":
        nodes.append({
            "@type": "Service", "@id": url + "#service",
            "name": plain(page["h1"]), "serviceType": "Virtual naturopathic consultation",
            "description": plain(quick_of(page)),
            "provider": {"@id": sc.ORG_ID},
            "areaServed": [{"@type": "Country", "name": "United Kingdom"}, {"@type": "AdministrativeArea", "name": "Ontario"}],
            "availableChannel": {"@type": "ServiceChannel", "serviceUrl": JANE_BOOK, "availableLanguage": "English"},
            "offers": {"@type": "Offer", "name": "Initial naturopathic consultation (75 minutes)",
                       "price": "200", "priceCurrency": "GBP", "url": f"{BASE}/fees.html"},
        })

    head = sc.head(REL, title, page["meta_desc"], path, f"/og/{'services' if kind == 'service' else 'conditions'}-{page['slug']}.jpg",
                   og_alt=page["image_alt"], ld_graph=sc.graph(nodes), markdown_alt=path + "index.md")

    approach_html = ""
    for icon_key, h, text in page["approach"]:
        approach_html += f'''          <div class="feature-row">
            <span class="icon-circle">
              {sc.ICONS[icon_key]}
            </span>
            <div class="feature-row-content">
              <h3>{h}</h3>
              <p>{text}</p>
            </div>
          </div>
'''

    empathy2 = ""
    if page.get("empathy2_h"):
        empathy2 = f'''
    <section class="section reveal">
      <div class="container" style="max-width:720px">
        <div class="section-head">
          <p class="eyebrow">Understanding your experience</p>
          <h2>{page["empathy2_h"]}</h2>
        </div>
        <div class="about-content"><p>{page["empathy2_p"]}</p></div>
      </div>
    </section>
'''

    main = f'''    <section class="page-hero" aria-labelledby="page-title">
      <div class="hero-bg">
        <picture>
          <source srcset="{REL}assets/images/{page["image"]}.webp" type="image/webp">
          <img src="{REL}assets/images/{page["image"]}.jpg" alt="{sc.attr(page["image_alt"])}" width="1024" height="1024" fetchpriority="high">
        </picture>
      </div>
      <div class="hero-copy">
        <p class="eyebrow">{page["eyebrow"]}</p>
        <h1 id="page-title">{page["h1"]}</h1>
        <p class="lead">{page["lead"]}</p>
      </div>
    </section>

{sc.trust_bar()}

    <section class="section reveal" aria-label="Summary">
      <div class="container" style="max-width:720px">
        <p class="lead" style="text-align:center;margin-inline:auto;max-width:60ch">{quick_of(page)}</p>
      </div>
    </section>

    <!-- Empathy / Problem -->
    <section class="section reveal">
      <div class="container">
        <div class="split">
          <div class="split-media">
            <picture>
              <source srcset="{REL}assets/images/{page["image"]}.webp" type="image/webp">
              <img src="{REL}assets/images/{page["image"]}.jpg" alt="" width="1024" height="1024" loading="lazy">
            </picture>
          </div>
          <div class="split-copy">
            <p class="eyebrow">Understanding your experience</p>
            <h2>{page["empathy_h"]}</h2>
            <p>{page["empathy_p"]}</p>
            <a class="btn btn--warm" href="{JANE_BOOK}" target="_blank" rel="noopener noreferrer" style="margin-top:var(--space-sm);align-self:flex-start">Book a consultation</a>
          </div>
        </div>
      </div>
    </section>
{empathy2}
    <!-- Conditions list -->
    <section class="section reveal" style="background:var(--cream-50)">
      <div class="container">
        <div class="conditions-block">
          <div class="section-head">
            <p class="eyebrow">{page["conditions_title"]}</p>
          </div>
          <ul class="conditions-list">
{sc.conditions_list(page["conditions"])}
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

{sc.faq_block(faqs)}

{related_uk(page)}{sc.cta_banner(REL)}

    <section class="section" aria-label="Important information">
      <div class="container" style="max-width:720px"><p style="font-size:13px;color:var(--text-subtle);text-align:center">{sc.DISCLAIMER}</p></div>
    </section>'''

    return sc.page_shell(REL, head, main)


def md_for(page, kind):
    url, _ = page_url(page, kind)
    return sc.md_page(
        page["h1"], page["meta_desc"], url,
        [("Summary", quick_of(page)),
         (page["empathy_h"], page["empathy_p"]),
         (page["conditions_title"], page["conditions"]),
         ("How we work with you", [f"{h}: {t}" for _, h, t in page["approach"]]),
         ("Fees", f"Initial consultation (75 minutes): {plain(sc.FEE_INITIAL)}. Follow-ups: {plain(sc.FEE_FOLLOWUP)}. Free 15-minute discovery call.")],
        page["faqs"],
    )


# ----------------------------------------------------------- conditions hub
def render_conditions_hub():
    rel = ""
    url = f"{BASE}/conditions.html"
    desc = ("Naturopathic care for stress, anxiety, hormones, PMOS/PCOS, gut health, fatigue, thyroid and acne. "
            "Virtual appointments for the UK & Ontario.")
    items = [(c["h1"], f"{BASE}/conditions/{c['slug']}/") for c in CONDITIONS]
    nodes = [
        sc.medical_webpage(url, "Conditions treated at Village Naturopathy", desc, kind="MedicalWebPage",
                           image=f"{BASE}/assets/images/conditions-hero.webp", breadcrumb_id=url + "#breadcrumb"),
        {**sc.breadcrumb([("Home", f"{BASE}/"), ("Conditions treated", None)]), "@id": url + "#breadcrumb"},
        {"@type": "ItemList", "name": "Conditions treated", "itemListElement": [
            {"@type": "ListItem", "position": i, "name": plain(n), "url": u} for i, (n, u) in enumerate(items, 1)]},
    ]
    head = sc.head(rel, "Conditions Treated | Village Naturopathy", desc, "conditions.html",
                   "/og/conditions.jpg", og_alt="Village Naturopathy, online naturopath for women",
                   ld_graph=sc.graph(nodes))
    blurbs = {
        "stress-anxiety-nervous-system": ("Stress &amp; nervous system", "Chronic stress isn&rsquo;t just mental. It disrupts sleep, digestion, hormones, immunity, and energy. We use evidence-based naturopathic strategies to calm the nervous system, rebuild resilience, and address the physical fallout of long-term stress."),
        "hormonal-imbalances-womens-health": ("Hormones", "Hormone issues are common but not normal. From painful periods to PMS and PMOS/PCOS, we use comprehensive testing and root-cause treatment to bring your hormones back into balance without masking symptoms."),
        "digestive-gut-health": ("Gut health", "A healthy gut is the foundation of overall health, affecting your hormones, mood, immunity, and energy. We use functional testing and targeted protocols to get your gut working properly again."),
        "fatigue-sleep-energy": ("Energy &amp; fatigue", "If you&rsquo;re tired all the time, running on coffee, or waking up unrefreshed, there&rsquo;s a reason. We investigate the root causes of fatigue and build a plan to restore sustainable energy."),
        "thyroid-autoimmune": ("Thyroid &amp; autoimmune", "Thyroid and autoimmune conditions are complex and deeply personal. We use comprehensive testing to understand what&rsquo;s driving your symptoms and build plans that support the underlying immune and metabolic picture."),
        "acne-hormonal-skin": ("Acne &amp; skin", "Persistent acne often reflects what&rsquo;s happening inside: hormones, blood sugar, the gut and stress. We look for the internal drivers rather than only suppressing symptoms."),
    }
    sections = ""
    for i, c in enumerate(CONDITIONS):
        eyebrow, blurb = blurbs[c["slug"]]
        bg = ' style="background:var(--cream-50)"' if i % 2 else ""
        cid = f"cond-{i}"
        sections += f'''    <section class="section"{bg} aria-labelledby="{cid}">
      <div class="container">
        <div class="conditions-block reveal">
          <div class="section-head">
            <p class="eyebrow">{eyebrow}</p>
            <h2 id="{cid}">{c["h1"]}</h2>
          </div>
          <div class="conditions-content">
            <p>{blurb}</p>
            <ul class="conditions-list">
{sc.conditions_list(c["conditions"])}
            </ul>
            <a class="btn btn--warm" href="{JANE_BOOK}" target="_blank" rel="noopener noreferrer">Book a consultation</a>
            <a class="btn btn--outline" href="conditions/{c["slug"]}/">Learn more</a>
          </div>
        </div>
      </div>
    </section>
'''
    main = f'''    <section class="page-hero" aria-labelledby="conditions-title">
      <div class="hero-bg">
        <img src="assets/images/conditions-hero.webp" alt="" width="1920" height="1080" fetchpriority="high">
      </div>
      <div class="hero-copy">
        <p class="eyebrow">Conditions treated</p>
        <h1 id="conditions-title">Root-cause naturopathic care for the conditions holding you back.</h1>
        <p class="lead">We treat the whole person, not just the diagnosis. Here are the most common conditions we work with, for patients across the UK and Ontario.</p>
      </div>
    </section>
{sections}
{sc.cta_banner(rel, eyebrow="Ready to get started?", heading="Don&rsquo;t see your condition listed? We may still be able to help.", body="Book your consultation and let&rsquo;s talk about what&rsquo;s going on. No obligation, no pressure.", button="Book a consultation", href=JANE_BOOK)}

    <section class="section" aria-label="Important information">
      <div class="container" style="max-width:720px"><p style="font-size:13px;color:var(--text-subtle);text-align:center">{sc.DISCLAIMER}</p></div>
    </section>'''
    return sc.page_shell(rel, head, main)


def write(path, content):
    full = os.path.join(SITE_ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)


def build():
    """Write all pages; returns [(path, lastmod-priority metadata)] for the sitemap."""
    out = []
    for page in SERVICES:
        write(f"services/{page['slug']}/index.html", render_page(page, "service"))
        write(f"services/{page['slug']}/index.md", md_for(page, "service"))
        out.append((f"services/{page['slug']}/", 0.9))
    for page in CONDITIONS:
        write(f"conditions/{page['slug']}/index.html", render_page(page, "condition"))
        write(f"conditions/{page['slug']}/index.md", md_for(page, "condition"))
        out.append((f"conditions/{page['slug']}/", 0.7))
    write("conditions.html", render_conditions_hub())
    out.append(("conditions.html", 0.8))
    return out


if __name__ == "__main__":
    for p, _ in build():
        print("  ", p)
