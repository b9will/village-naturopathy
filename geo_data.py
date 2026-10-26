# -*- coding: utf-8 -*-
"""Content for the UK location pages.

Rules for anything written here:
  * Virtual clinic. Never imply a physical clinic, address, or in-person visits in the UK.
  * Never describe the target audience as wealthy/affluent on the site.
  * Facts about places are limited to well-known geography (borough/council, postcode
    districts, parks, rivers, transport lines). No claims about local residents' health,
    and no invented patient stories.
  * Health language: "support", "care for", "work with". No cure/guarantee/outcome promises.
  * Never say "licensed in the UK". Naturopathy is not statutorily regulated in the UK;
    the accurate statement is "full member of the Association of Naturopathic Practitioners (UK)".
Strings are HTML (entities already encoded).
"""

# ----------------------------------------------------------------- focus areas
FOCUS = {
    "stress": {
        "name": "Stress, burnout &amp; anxiety",
        "service": "stress-anxiety",
        "blurb": "Nervous system regulation, sleep, nutrient status and cortisol patterns for people who feel wired but tired.",
    },
    "hormones": {
        "name": "Hormones, PMOS/PCOS &amp; cycles",
        "service": "hormone-balancing",
        "blurb": "PMS and PMDD, irregular or painful periods, PMOS/PCOS, endometriosis and hormonal acne, with DUTCH testing where it helps.",
    },
    "gut": {
        "name": "Gut health, IBS &amp; SIBO",
        "service": "gut-health",
        "blurb": "Bloating, reflux, IBS and SIBO, food sensitivities and the gut-hormone-mood connection.",
    },
    "fatigue": {
        "name": "Fatigue &amp; low energy",
        "service": "fatigue",
        "blurb": "Iron, B12, thyroid markers and cortisol, plus the sleep and stress patterns that keep energy low.",
    },
}

# ----------------------------------------------------------------- nations
NATIONS = {
    "scotland": {
        "name": "Scotland",
        "h1": "Online Naturopath in Scotland",
        "meta_title": "Online Naturopath in Scotland | Edinburgh, Glasgow, St Andrews | Village Naturopathy",
        "meta_desc": ("Virtual naturopathic care for women across Scotland, including Edinburgh, Glasgow and St Andrews. "
                      "Hormones, stress, gut health and fatigue with Dr. Heather Robinson, ND."),
        "quick": ("Dr. Heather Robinson, ND, sees patients across Scotland by secure video, so you can have a full "
                  "naturopathic consultation from Edinburgh, Glasgow, St Andrews or anywhere between. She is a full "
                  "member of the Association of Naturopathic Practitioners (UK)."),
        "intro": ("Scotland is well suited to virtual care. Distances are long, and many people split their week between "
                  "the Central Belt, the coast and the Highlands. A video consultation removes the travel, and all "
                  "testing and follow-ups can be arranged around your calendar. Whether you are in Edinburgh&rsquo;s "
                  "New Town, Glasgow&rsquo;s West End or a town on the east coast, the appointment is the same: a "
                  "75-minute conversation about your health history, then a plan built around you."),
        "cities": ["edinburgh", "glasgow"],
        "towns": ["st-andrews"],
        "faqs": [
            ("Can I see a naturopath online in Scotland?", "Yes. Dr. Heather Robinson, ND, sees patients across Scotland by secure video. You do not need to travel, and your first step is a free 15-minute discovery call."),
            ("Do you offer appointments in Edinburgh or Glasgow in person?", "No. Village Naturopathy is a virtual clinic, so all consultations take place online. That means the same care is available whether you live in a city, a town or a rural area."),
            ("How much does a naturopathic consultation cost in Scotland?", "The initial 75-minute consultation is &pound;200 and follow-ups are &pound;50&ndash;170 depending on length. The 15-minute discovery call is free."),
        ],
    },
    "northern-ireland": {
        "name": "Northern Ireland",
        "h1": "Online Naturopath in Northern Ireland",
        "meta_title": "Online Naturopath in Northern Ireland | Belfast & Holywood | Village Naturopathy",
        "meta_desc": ("Virtual naturopathic care for women across Northern Ireland, including Belfast and Holywood. "
                      "Hormones, stress, gut health and fatigue with Dr. Heather Robinson, ND."),
        "quick": ("Dr. Heather Robinson, ND, sees patients across Northern Ireland by secure video, including Belfast, "
                  "Holywood and the surrounding area. She is a full member of the Association of Naturopathic "
                  "Practitioners (UK), and the first step is a free 15-minute discovery call."),
        "intro": ("Naturopathic practitioners are not always easy to find outside the larger English cities. A virtual "
                  "clinic changes that: you get a full 75-minute consultation, a personalised plan and ongoing "
                  "follow-ups from your own home, whichever part of Northern Ireland you live in. Testing, where it "
                  "is useful, is discussed with you first so you know what is involved before you decide."),
        "cities": ["belfast"],
        "towns": [],
        "faqs": [
            ("Can I see a naturopath online in Northern Ireland?", "Yes. Dr. Heather Robinson, ND, sees patients across Northern Ireland by secure video. Start with a free 15-minute discovery call."),
            ("Is naturopathy regulated in Northern Ireland?", "Naturopathy is not statutorily regulated anywhere in the UK. Dr. Heather is a full member of the Association of Naturopathic Practitioners (UK) and is registered with the College of Naturopaths of Ontario, where naturopathic doctors are regulated."),
            ("How much does a naturopathic consultation cost?", "The initial 75-minute consultation is &pound;200 and follow-ups are &pound;50&ndash;170 depending on length. The 15-minute discovery call is free."),
        ],
    },
}

# ----------------------------------------------------------------- cities
CITIES = {
    "london": {
        "name": "London", "nation": "England", "nation_slug": None,
        "h1": "Online Naturopath in London",
        "meta_title": "Online Naturopath in London | Hormones, Stress, Gut & Fatigue | Village Naturopathy",
        "meta_desc": ("Virtual naturopathic doctor for women in London. Hormone health, PMOS/PCOS, burnout, gut health "
                      "and fatigue with Dr. Heather Robinson, ND. Free discovery call."),
        "quick": ("Village Naturopathy is a virtual clinic seeing patients across London by secure video. Dr. Heather "
                  "Robinson, ND, a full member of the Association of Naturopathic Practitioners (UK), offers a "
                  "75-minute initial consultation (&pound;200) focused on hormones, stress and burnout, gut health and "
                  "fatigue, with DUTCH hormone testing and blood work where they are useful."),
        "postcodes": "all London postcode districts",
        "intro": [
            "London asks a lot of your body. Long commutes, back-to-back meetings, late dinners, little daylight in winter and a social calendar that never quite switches off all leave their mark on sleep, digestion and hormones. If you have been told your blood tests are &lsquo;normal&rsquo; while you still feel exhausted, wired at night or unwell around your cycle, you are not imagining it.",
            "Virtual care fits a London week. There is no clinic to get across the city to, and appointments can sit around a working day or a school run. Dr. Heather&rsquo;s approach is root-cause and personalised: a full history, comprehensive testing where it is useful, and a plan you can realistically follow.",
        ],
        "topics": ["hormone-balancing", "pmos-pcos", "stress-burnout", "gut-health", "fatigue", "dutch-test"],
        "faqs": [
            ("Can I see a naturopath online in London?", "Yes. Dr. Heather Robinson, ND, sees patients across London by secure video. There is no need to travel to a clinic. Start with a free 15-minute discovery call, then book a 75-minute initial consultation if you would like to go ahead."),
            ("Is Dr. Heather based in London?", "No. Village Naturopathy is a virtual clinic, and every consultation takes place online. London patients receive the same care as patients anywhere in the UK."),
            ("How much does a naturopath cost in London?", "The initial 75-minute consultation is &pound;200 and follow-up appointments are &pound;50&ndash;170 depending on length. The 15-minute discovery call is free. Any testing is optional and discussed with you before you decide."),
            ("Do you offer DUTCH hormone testing for patients in London?", "Where DUTCH testing is useful, Dr. Heather explains how it works, what it measures and the cost before you decide. It is optional and recommended case by case."),
            ("Is naturopathy regulated in the UK?", "Naturopathy is not statutorily regulated in the UK. Dr. Heather is a full member of the Association of Naturopathic Practitioners (UK) and is registered with the College of Naturopaths of Ontario, where naturopathic doctors are regulated. She is fully insured."),
        ],
    },
    "edinburgh": {
        "name": "Edinburgh", "nation": "Scotland", "nation_slug": "scotland",
        "h1": "Online Naturopath in Edinburgh",
        "meta_title": "Online Naturopath in Edinburgh | Hormones, Stress & Gut Health | Village Naturopathy",
        "meta_desc": ("Virtual naturopathic doctor for women in Edinburgh. Hormone health, PMOS/PCOS, burnout, gut health "
                      "and fatigue with Dr. Heather Robinson, ND. Free discovery call."),
        "quick": ("Village Naturopathy is a virtual clinic seeing patients across Edinburgh by secure video. Dr. "
                  "Heather Robinson, ND, a full member of the Association of Naturopathic Practitioners (UK), offers a "
                  "75-minute initial consultation (&pound;200) for hormones, stress and burnout, gut health and "
                  "fatigue, with testing such as DUTCH where it is useful."),
        "postcodes": "EH postcodes across the city",
        "intro": [
            "Edinburgh combines demanding professional life with long, dark winters and a lot of walking up and down hills. Many people here balance careers in law, finance, medicine, education and the university sector with family life, and the result can be a body that is running on adrenaline and coffee through January.",
            "Naturopathic practitioners are not always easy to find close to home. A virtual clinic means you can have a full consultation from your own living room, with follow-ups that fit around your week, and a plan built around your history rather than a generic protocol.",
        ],
        "topics": ["dutch-test"],
        "faqs": [
            ("Can I see a naturopath online in Edinburgh?", "Yes. Dr. Heather Robinson, ND, sees patients across Edinburgh and the Lothians by secure video. Start with a free 15-minute discovery call."),
            ("Do you have a clinic in Edinburgh?", "No. Village Naturopathy is a virtual clinic. All consultations take place by secure video, so you can attend from home or work."),
            ("How much does a naturopathic consultation cost in Edinburgh?", "The initial 75-minute consultation is &pound;200 and follow-ups are &pound;50&ndash;170 depending on length. The 15-minute discovery call is free."),
            ("Can I get DUTCH hormone testing in Edinburgh?", "Where it is useful, Dr. Heather can recommend DUTCH testing and will explain how it works and what it costs before you decide. It is optional and recommended case by case."),
        ],
    },
    "glasgow": {
        "name": "Glasgow", "nation": "Scotland", "nation_slug": "scotland",
        "h1": "Online Naturopath in Glasgow",
        "meta_title": "Online Naturopath in Glasgow | Hormones, Stress & Gut Health | Village Naturopathy",
        "meta_desc": ("Virtual naturopathic doctor for women in Glasgow and the West of Scotland. Hormone health, burnout, "
                      "gut health and fatigue with Dr. Heather Robinson, ND. Free discovery call."),
        "quick": ("Village Naturopathy is a virtual clinic seeing patients across Glasgow and the west of Scotland by "
                  "secure video. Dr. Heather Robinson, ND, a full member of the Association of Naturopathic "
                  "Practitioners (UK), offers a 75-minute initial consultation (&pound;200) for hormones, stress and "
                  "burnout, gut health and fatigue."),
        "postcodes": "G postcodes across Glasgow and the surrounding towns",
        "intro": [
            "Glasgow is a city of hospitals, universities, creative industries and long commutes along the M8 and into the suburbs. If your days involve shift patterns, long hours or heavy caring responsibilities, sleep, digestion and hormones are often the first things to slip.",
            "With virtual care, you can book from the West End, from Bearsden or Newton Mearns, or from anywhere else in the west of Scotland, without adding another journey to your week.",
        ],
        "topics": ["dutch-test"],
        "faqs": [
            ("Can I see a naturopath online in Glasgow?", "Yes. Dr. Heather Robinson, ND, sees patients across Glasgow and the west of Scotland by secure video. Start with a free 15-minute discovery call."),
            ("Do you have a clinic in Glasgow?", "No. Village Naturopathy is a virtual clinic. All consultations take place by secure video."),
            ("How much does a naturopathic consultation cost in Glasgow?", "The initial 75-minute consultation is &pound;200 and follow-ups are &pound;50&ndash;170 depending on length. The 15-minute discovery call is free."),
            ("Can I get DUTCH hormone testing in Glasgow?", "Where it is useful, Dr. Heather can recommend DUTCH testing and will explain how it works and what it costs before you decide. It is optional and recommended case by case."),
        ],
    },
    "belfast": {
        "name": "Belfast", "nation": "Northern Ireland", "nation_slug": "northern-ireland",
        "h1": "Online Naturopath in Belfast",
        "meta_title": "Online Naturopath in Belfast | Hormones, Stress & Gut Health | Village Naturopathy",
        "meta_desc": ("Virtual naturopathic doctor for women in Belfast and Northern Ireland. Hormone health, burnout, gut "
                      "health and fatigue with Dr. Heather Robinson, ND. Free discovery call."),
        "quick": ("Village Naturopathy is a virtual clinic seeing patients across Belfast and Northern Ireland by "
                  "secure video. Dr. Heather Robinson, ND, a full member of the Association of Naturopathic "
                  "Practitioners (UK), offers a 75-minute initial consultation (&pound;200) for hormones, stress and "
                  "burnout, gut health and fatigue."),
        "postcodes": "BT postcodes across Belfast and the surrounding area",
        "intro": [
            "Belfast has a strong professional and academic community, with big employers in health, law, technology and education. Busy working weeks, family commitments and the commute along the M2, the Lagan towpath or the Belfast Lough shore can leave little time to look after your own health.",
            "A virtual clinic removes the travel entirely. You get a full naturopathic consultation, a clear plan and follow-ups from home, with testing discussed first so you know what is involved.",
        ],
        "topics": ["dutch-test"],
        "faqs": [
            ("Can I see a naturopath online in Belfast?", "Yes. Dr. Heather Robinson, ND, sees patients across Belfast and Northern Ireland by secure video. Start with a free 15-minute discovery call."),
            ("Do you have a clinic in Belfast?", "No. Village Naturopathy is a virtual clinic. All consultations take place by secure video."),
            ("How much does a naturopathic consultation cost in Belfast?", "The initial 75-minute consultation is &pound;200 and follow-ups are &pound;50&ndash;170 depending on length. The 15-minute discovery call is free."),
            ("Can I get DUTCH hormone testing in Belfast?", "Where it is useful, Dr. Heather can recommend DUTCH testing and will explain how it works and what it costs before you decide. It is optional and recommended case by case."),
        ],
    },
}

# ----------------------------------------------------------------- areas
# local: one factual, hand-written paragraph. angle: three conditional, non-claiming bullets.
AREAS = [
    # ---------------- London
    {"slug": "kensington", "city": "london", "name": "Kensington", "council": "Royal Borough of Kensington and Chelsea",
     "postcodes": "W8, W14 and SW7", "nearby": ["chelsea", "notting-hill", "chiswick"],
     "local": "Kensington sits in west London between Hyde Park, Kensington Gardens and Holland Park, with the museum quarter to the south and Kensington High Street at its centre. It is well connected by the District, Circle and Piccadilly lines, which makes for long journeys across town to almost anywhere else.",
     "focus": ["stress", "hormones", "fatigue"],
     "angle": ["If your working week runs from the City or the West End to Kensington and back again, the cumulative strain on sleep and stress hormones is worth looking at properly.",
               "If cycles have become irregular, painful or hard to predict, a full hormone and nutrient picture can show what is behind it.",
               "If you wake unrefreshed even after a full night, iron, B12, thyroid markers and cortisol are a sensible place to start."]},
    {"slug": "chelsea", "city": "london", "name": "Chelsea", "council": "Royal Borough of Kensington and Chelsea",
     "postcodes": "SW3 and SW10", "nearby": ["kensington", "notting-hill", "putney"],
     "local": "Chelsea runs from the King&rsquo;s Road and Sloane Square down to the Chelsea Embankment on the Thames. Its mix of busy streets and quiet residential squares means a lot of people work from home or hybrid, with the long hours at a screen that come with it.",
     "focus": ["hormones", "stress", "gut"],
     "angle": ["If PMS, painful periods or hormonal acne are still part of your month, testing and a cycle-aligned plan can add clarity.",
               "If screen-heavy days leave you tense, tired and unable to switch off in the evening, nervous system support can help.",
               "If bloating, reflux or food sensitivities are getting in the way of work lunches and dinners out, a structured gut assessment is a good first step."]},
    {"slug": "notting-hill", "city": "london", "name": "Notting Hill", "council": "Royal Borough of Kensington and Chelsea",
     "postcodes": "W11 and W2", "nearby": ["kensington", "marylebone", "chiswick"],
     "local": "Notting Hill is known for Portobello Road, Westbourne Grove and the long stretches of Ladbroke Grove, with Holland Park and Hyde Park close by. It is home to many people in creative, media and self-employed work, where irregular hours and no clear off-switch are common.",
     "focus": ["stress", "hormones", "gut"],
     "angle": ["If freelance or creative work means irregular hours, skipped meals and poor sleep, regulating the nervous system and blood sugar is often where we begin.",
               "If you are coming off hormonal contraception or want to understand your natural cycle, a clear plan and testing can help.",
               "If your digestion is unpredictable, SIBO and food sensitivities are worth ruling in or out."]},
    {"slug": "marylebone", "city": "london", "name": "Marylebone", "council": "City of Westminster",
     "postcodes": "W1U, W1G and NW1", "nearby": ["st-johns-wood", "primrose-hill", "notting-hill"],
     "local": "Marylebone lies north of Oxford Street, with Marylebone High Street at its heart, Regent&rsquo;s Park to the north and Baker Street running through it. Many people live and work within a short walk, so days can blur into one another without much outdoor time.",
     "focus": ["stress", "fatigue", "hormones"],
     "angle": ["If the day starts early and ends late, a plan that protects sleep and stabilises energy is worth building into your routine.",
               "If tiredness hangs around despite normal basic blood tests, a closer look at iron, B12, thyroid and cortisol can find what standard panels miss.",
               "If your cycle changes with stress or travel, tracking and testing can show which hormones are involved."]},
    {"slug": "st-johns-wood", "city": "london", "name": "St John&rsquo;s Wood", "council": "City of Westminster and the London Borough of Camden",
     "postcodes": "NW8", "nearby": ["primrose-hill", "marylebone", "hampstead"],
     "local": "St John&rsquo;s Wood sits just north of Regent&rsquo;s Park, a leafy part of NW8 with Abbey Road and Lord&rsquo;s Cricket Ground nearby, served by the Jubilee line. Family life and a steady commute to central London are common.",
     "focus": ["hormones", "stress", "fatigue"],
     "angle": ["If you are thinking about fertility or have recently come off the pill, preconception hormone and nutrient support can be a good place to start.",
               "If school runs, work and caring responsibilities leave you running on empty, a realistic, sustainable plan matters more than a perfect one.",
               "If you are exhausted in the afternoon every day, blood sugar and iron status are common contributors worth checking."]},
    {"slug": "hampstead", "city": "london", "name": "Hampstead", "council": "London Borough of Camden",
     "postcodes": "NW3", "nearby": ["highgate", "primrose-hill", "st-johns-wood"],
     "local": "Hampstead sits on the edge of Hampstead Heath, with Hampstead Village, the Northern line and a strong local culture of walking and outdoor swimming. It is a part of north London that many people stay in for years.",
     "focus": ["stress", "hormones", "gut"],
     "angle": ["If you walk the Heath to decompress but still cannot switch off at night, the issue may be more physiological than behavioural.",
               "If your cycle has changed in your thirties or forties, hormone testing and a good history can help you understand what is going on.",
               "If gut symptoms flare around stress or travel, a structured assessment can identify the drivers."]},
    {"slug": "highgate", "city": "london", "name": "Highgate", "council": "London Borough of Camden, Haringey and Islington",
     "postcodes": "N6", "nearby": ["hampstead", "islington", "primrose-hill"],
     "local": "Highgate is a hilltop village in north London beside Hampstead Heath and Waterlow Park, with Highgate Wood close by. The Northern line and the hill itself make getting anywhere a longer trip than it looks on the map.",
     "focus": ["hormones", "fatigue", "stress"],
     "angle": ["If PMS or heavy periods are affecting work and family plans, a hormone and iron assessment is a useful place to start.",
               "If energy slumps every afternoon, nutrient status, thyroid markers and sleep quality are worth a closer look.",
               "If anxiety has crept in alongside a demanding schedule, we can look at the physical contributors as well as the situational ones."]},
    {"slug": "primrose-hill", "city": "london", "name": "Primrose Hill", "council": "London Borough of Camden and the City of Westminster",
     "postcodes": "NW1 and NW8", "nearby": ["st-johns-wood", "hampstead", "marylebone"],
     "local": "Primrose Hill is a compact village-like neighbourhood north of Regent&rsquo;s Park, with Primrose Hill itself, Regent&rsquo;s Park Road and Camden within a short walk. Many people work from home, in media, design or the arts.",
     "focus": ["stress", "gut", "hormones"],
     "angle": ["If working from home has blurred the line between work and rest, rebuilding sleep and stress rhythms is a good starting point.",
               "If you eat in a rush or at odd times and your gut protests, a structured look at digestion can bring clarity.",
               "If your periods or moods shift across the month, a cycle-aligned plan and testing may help."]},
    {"slug": "islington", "city": "london", "name": "Islington", "council": "London Borough of Islington",
     "postcodes": "N1 and N5", "nearby": ["highgate", "primrose-hill", "city-and-canary-wharf"],
     "local": "Islington covers the Angel, Upper Street, Canonbury and Highbury, with the Regent&rsquo;s Canal on one side and the City on the other. It is close enough to the City for many people to commute in on foot, by bike or by Victoria and Northern line.",
     "focus": ["stress", "hormones", "gut"],
     "angle": ["If a demanding job in the City or tech leaves you wired at night and flat in the morning, nervous system support and sleep strategies can help.",
               "If PMS or PMDD is a regular monthly disruption, there are nutritional and botanical strategies worth discussing.",
               "If IBS-type symptoms follow stressful weeks, the gut-brain connection is part of the picture."]},
    {"slug": "richmond", "city": "london", "name": "Richmond", "council": "London Borough of Richmond upon Thames",
     "postcodes": "TW9 and TW10", "nearby": ["wimbledon", "putney", "chiswick"],
     "local": "Richmond sits on the Thames in south-west London, beside Richmond Park and close to Kew Gardens. Many people commute into central London on the District line and National Rail, and put in long days on top of family life.",
     "focus": ["hormones", "fatigue", "stress"],
     "angle": ["If you are navigating fertility, pregnancy planning or the postpartum period, nutrient and hormone support can make a real difference to how you feel.",
               "If you are tired despite getting to bed on time, thyroid markers, iron and B12 can help explain why.",
               "If the commute and the school run leave no time for yourself, a short, realistic plan is more useful than a long list."]},
    {"slug": "wimbledon", "city": "london", "name": "Wimbledon", "council": "London Borough of Merton",
     "postcodes": "SW19", "nearby": ["putney", "richmond", "clapham"],
     "local": "Wimbledon spans Wimbledon Village, Wimbledon Common and the town centre, with the District line and Thameslink linking it to central London. The Common is a major green space in south-west London, much used for running and walking.",
     "focus": ["stress", "hormones", "gut"],
     "angle": ["If training, work and family leave your body under constant load, recovery and cortisol rhythm deserve attention.",
               "If your cycle changes with training or stress, a hormone and nutrient picture can help distinguish the causes.",
               "If bloating or reflux shows up during busy periods, a gut assessment is a good first step."]},
    {"slug": "putney", "city": "london", "name": "Putney", "council": "London Borough of Wandsworth",
     "postcodes": "SW15", "nearby": ["wimbledon", "clapham", "richmond"],
     "local": "Putney lies on the south bank of the Thames, with Putney Bridge, the riverside, Putney Heath and the start of the Boat Race course. It is a popular area for runners, rowers and commuters on the District line.",
     "focus": ["hormones", "fatigue", "gut"],
     "angle": ["If you are active but your energy, cycle or recovery are not what they should be, hormones and nutrient status are a good place to look.",
               "If tiredness lingers after training or a busy week, iron, B12 and thyroid markers are worth checking.",
               "If your digestion is unpredictable around events, travel or stress, a structured gut review can help."]},
    {"slug": "clapham", "city": "london", "name": "Clapham", "council": "London Borough of Lambeth and the London Borough of Wandsworth",
     "postcodes": "SW4 and SW11", "nearby": ["putney", "wimbledon", "dulwich"],
     "local": "Clapham is centred on Clapham Common in south-west London, with the Northern line and Overground connecting it to the City and West End. Busy social lives, long working days and a lot of time spent commuting are common.",
     "focus": ["stress", "gut", "hormones"],
     "angle": ["If a full social calendar and a demanding job leave you tired but wired, nervous system regulation is a good place to start.",
               "If bloating or irregular digestion follows busy weeks, we can look at the physical and lifestyle triggers.",
               "If hormonal acne or irregular cycles are an ongoing frustration, there are root-cause options to explore."]},
    {"slug": "dulwich", "city": "london", "name": "Dulwich", "council": "London Borough of Southwark",
     "postcodes": "SE21 and SE22", "nearby": ["clapham", "blackheath", "islington"],
     "local": "Dulwich is a village-like part of south-east London around Dulwich Village, Dulwich Park and the Picture Gallery, served by National Rail rather than the Tube. Longer commutes make a flexible, home-based form of care particularly useful.",
     "focus": ["fatigue", "hormones", "stress"],
     "angle": ["If the commute leaves you drained before the day has even started, a closer look at sleep, iron and thyroid function can help.",
               "If you are considering pregnancy or managing the months after birth, nutrient and hormone support is often a priority.",
               "If anxiety or low mood have crept in, we can explore the physical contributors alongside the situational ones."]},
    {"slug": "blackheath", "city": "london", "name": "Blackheath", "council": "Royal Borough of Greenwich and the London Borough of Lewisham",
     "postcodes": "SE3", "nearby": ["dulwich", "city-and-canary-wharf", "clapham"],
     "local": "Blackheath is a village on the edge of an open heath in south-east London, close to Greenwich and the Thames, with National Rail services into central London and Canary Wharf. Family life and a long commute are common here.",
     "focus": ["fatigue", "hormones", "gut"],
     "angle": ["If you are tired after a long commute and a full evening, nutrient status and sleep quality deserve a proper look.",
               "If cycles or PMS have changed after pregnancy, a hormone-focused assessment can bring clarity.",
               "If digestion flares with stress, a structured gut review can help you identify triggers."]},
    {"slug": "chiswick", "city": "london", "name": "Chiswick", "council": "London Borough of Hounslow",
     "postcodes": "W4", "nearby": ["richmond", "kensington", "notting-hill"],
     "local": "Chiswick sits on the Thames in west London around Chiswick High Road, Chiswick House and the riverside at Strand-on-the-Green. It is served by the District line and National Rail, and many people here run their own business or work in media.",
     "focus": ["stress", "hormones", "fatigue"],
     "angle": ["If self-employment means working most evenings, building structure around sleep and stress can make a big difference.",
               "If hormonal symptoms are affecting your work or family life, testing and a careful history can show where to focus.",
               "If you feel tired most of the time, a look at iron, B12, thyroid and cortisol is a good first step."]},
    {"slug": "city-and-canary-wharf", "city": "london", "name": "the City &amp; Canary Wharf", "council": "City of London and the London Borough of Tower Hamlets",
     "postcodes": "EC1&ndash;EC4 and E14", "nearby": ["islington", "blackheath", "dulwich"],
     "local": "The City of London and Canary Wharf are the capital&rsquo;s two financial districts, with long working hours, early starts and heavy time pressure. Many people here travel in from across London and the south-east, so a clinic you can attend from home is often the only realistic option.",
     "focus": ["stress", "fatigue", "gut"],
     "angle": ["If you work long hours under constant pressure, burnout, disrupted sleep and cortisol patterns are worth looking at together.",
               "If you feel permanently tired despite &lsquo;normal&rsquo; results, a more detailed look at iron, B12, thyroid and cortisol can help.",
               "If stress shows up in your gut, structured testing and nutrition support can reduce the guesswork."]},

    # ---------------- Edinburgh
    {"slug": "new-town", "city": "edinburgh", "name": "Edinburgh New Town", "council": "City of Edinburgh Council",
     "postcodes": "EH1, EH2 and EH3", "nearby": ["stockbridge", "morningside", "cramond-and-barnton"],
     "local": "Edinburgh&rsquo;s New Town is a UNESCO World Heritage Site of Georgian streets and gardens, with George Street, Queen Street Gardens and Princes Street at its heart. It is the commercial and legal centre of the city, with long working days and little green space close to hand.",
     "focus": ["stress", "fatigue", "hormones"],
     "angle": ["If you work in law, finance or the public sector and long days leave you drained, burnout and sleep patterns are worth looking at.",
               "If you are tired in a way that rest does not fix, a close look at iron, B12, thyroid and cortisol can help.",
               "If your cycle or hormones have changed in your thirties or forties, a clear history and testing can guide the plan."]},
    {"slug": "stockbridge", "city": "edinburgh", "name": "Stockbridge", "council": "City of Edinburgh Council",
     "postcodes": "EH3 and EH4", "nearby": ["new-town", "cramond-and-barnton", "morningside"],
     "local": "Stockbridge is a village-style neighbourhood next to the Water of Leith, with independent shops, a Sunday market and the Royal Botanic Garden nearby. It sits within walking distance of the New Town and Inverleith Park.",
     "focus": ["hormones", "gut", "stress"],
     "angle": ["If PMS, heavy periods or hormonal acne are affecting your month, hormone testing and a cycle-aligned plan can help.",
               "If you eat well but still struggle with bloating or reflux, a structured gut assessment is a good first step.",
               "If stress and poor sleep are making everything feel harder, nervous system support can be a starting point."]},
    {"slug": "morningside", "city": "edinburgh", "name": "Morningside &amp; Bruntsfield", "council": "City of Edinburgh Council",
     "postcodes": "EH10", "nearby": ["new-town", "stockbridge", "cramond-and-barnton"],
     "local": "Morningside and Bruntsfield form a residential part of south Edinburgh along Morningside Road and around Bruntsfield Links, with the Braid Hills close by. Family life and a short commute into the city centre are typical here.",
     "focus": ["fatigue", "hormones", "stress"],
     "angle": ["If family life, work and long Edinburgh winters leave you flat, vitamin D, iron and B12 are worth checking with a naturopath alongside your GP.",
               "If you are managing fertility, pregnancy planning or postpartum recovery, nutrient and hormone support can help.",
               "If anxiety or low mood have taken hold, we can look at the physical drivers as well as the situational ones."]},
    {"slug": "cramond-and-barnton", "city": "edinburgh", "name": "Cramond &amp; Barnton", "council": "City of Edinburgh Council",
     "postcodes": "EH4", "nearby": ["stockbridge", "new-town", "morningside"],
     "local": "Cramond is a coastal village on the Firth of Forth with the Cramond Island causeway and the River Almond, while Barnton is a residential area to the west. Many people here commute into the city or over the Forth.",
     "focus": ["stress", "fatigue", "gut"],
     "angle": ["If a long commute and a full week leave you depleted, sleep and stress physiology are worth a closer look.",
               "If you wake tired and run on caffeine, iron, B12 and thyroid markers can help explain why.",
               "If digestive symptoms follow stress, a structured review of gut health may help."]},

    # ---------------- Glasgow
    {"slug": "west-end", "city": "glasgow", "name": "Glasgow West End", "council": "Glasgow City Council",
     "postcodes": "G11 and G12", "nearby": ["bearsden", "newton-mearns"],
     "local": "Glasgow&rsquo;s West End includes Hillhead, Hyndland, Partick and Kelvinbridge, centred on Byres Road, Kelvingrove Park and the University of Glasgow. Many residents work in the university, the NHS, law, media and the creative sector.",
     "focus": ["stress", "hormones", "gut"],
     "angle": ["If academic, clinical or creative work leaves you tense and short of sleep, nervous system and nutrient support can help.",
               "If your cycle or PMS symptoms are hard to live with, hormone testing and a plan may bring clarity.",
               "If IBS-type symptoms are part of your week, structured testing and nutrition can reduce the guesswork."]},
    {"slug": "bearsden", "city": "glasgow", "name": "Bearsden &amp; Milngavie", "council": "East Dunbartonshire Council",
     "postcodes": "G61 and G62", "nearby": ["west-end", "newton-mearns"],
     "local": "Bearsden and Milngavie are suburban towns north-west of Glasgow, with Mugdock Country Park and the start of the West Highland Way at Milngavie. The train line into Glasgow Queen Street makes the commute straightforward but long.",
     "focus": ["fatigue", "hormones", "stress"],
     "angle": ["If the commute and the school run leave you tired by mid-afternoon, nutrient status and sleep deserve attention.",
               "If cycles have changed or you are planning a family, hormone and nutrient support can be a sensible start.",
               "If anxiety is part of a busy family life, we can look at physical contributors alongside the practical ones."]},
    {"slug": "newton-mearns", "city": "glasgow", "name": "Newton Mearns", "council": "East Renfrewshire Council",
     "postcodes": "G77", "nearby": ["west-end", "bearsden"],
     "local": "Newton Mearns is a large suburb south of Glasgow in East Renfrewshire, with Rouken Glen Park nearby and road and rail links into the city. Family life and school runs shape much of the week.",
     "focus": ["hormones", "stress", "fatigue"],
     "angle": ["If PMS, painful periods or irregular cycles are on your mind, a careful history and testing can help you understand what is going on.",
               "If a busy household leaves no time to rest, a short plan you can realistically follow is the aim.",
               "If you feel permanently tired, a closer look at iron, B12 and thyroid markers is a good first step."]},
    # ---------------- St Andrews
    {"slug": "st-andrews", "city": None, "nation": "scotland", "name": "St Andrews", "council": "Fife Council",
     "postcodes": "KY16", "nearby": [],
     "local": "St Andrews is a university town on the Fife coast, famous for the Old Course and the University of St Andrews, with the East Sands and West Sands beaches on its doorstep. The nearest large clinics are in Dundee or Edinburgh, so online care saves a lot of travel.",
     "focus": ["stress", "hormones", "fatigue"],
     "angle": ["If academic or clinical work leaves you stretched, burnout and sleep patterns are worth a proper look.",
               "If your cycle, mood or skin are changing, hormone testing and a careful history can show what is behind it.",
               "If tiredness is constant, iron, B12 and thyroid markers are a sensible place to start."]},

    # ---------------- Belfast
    {"slug": "malone-and-stranmillis", "city": "belfast", "name": "Malone &amp; Stranmillis", "council": "Belfast City Council",
     "postcodes": "BT9", "nearby": ["holywood"],
     "local": "Malone Road and Stranmillis lie in south Belfast around the Botanic Gardens, Queen&rsquo;s University and the Lagan towpath. Many residents work in health, law, education and the university sector.",
     "focus": ["stress", "hormones", "gut"],
     "angle": ["If clinical, legal or academic work leaves you stretched, nervous system and sleep support can help.",
               "If your cycle or PMS symptoms are affecting work and home life, hormone testing and a plan may help.",
               "If bloating, reflux or IBS-type symptoms are hard to pin down, a structured gut review can clarify the picture."]},
    {"slug": "holywood", "city": "belfast", "name": "Holywood &amp; Cultra", "council": "Ards and North Down Borough Council",
     "postcodes": "BT18", "nearby": ["malone-and-stranmillis"],
     "local": "Holywood and Cultra sit on the south shore of Belfast Lough in County Down, with the Ulster Folk Museum at Cultra and the Belfast&ndash;Bangor railway line. Many people commute into Belfast, with a full day of work and travel.",
     "focus": ["fatigue", "hormones", "stress"],
     "angle": ["If the commute and a full week leave you running on empty, sleep, nutrient status and cortisol are worth looking at.",
               "If fertility, pregnancy or the postpartum period is on your mind, nutrient and hormone support can help.",
               "If anxiety or stress are affecting your routine, we can explore the physical contributors with you."]},
]

# ----------------------------------------------------------------- topic pages
# kind: "london" topics are served at /uk/london/<slug>/ ; "dutch" is also city-level.
TOPICS = {
    "hormone-balancing": {
        "name": "Hormone Balancing", "service": "hormone-balancing",
        "h1": "Hormone Balancing Naturopath in London",
        "meta_title": "Hormone Balancing Naturopath London | Village Naturopathy",
        "meta_desc": ("Online naturopath in London for hormone health: PMS and PMDD, irregular periods, endometriosis "
                      "and hormonal acne. Free discovery call."),
        "quick": ("Village Naturopathy offers online hormone-focused naturopathic care for women in London. After a "
                  "75-minute consultation with Dr. Heather Robinson, ND, you receive a personalised plan that can "
                  "include nutrition, targeted supplementation, botanical medicine and, where it is useful, DUTCH "
                  "hormone testing and blood work."),
        "sections": [
            ("What hormone-focused naturopathic care looks like",
             ["Hormone symptoms rarely have a single cause. Cycles are influenced by stress, sleep, blood sugar, thyroid function, gut health, nutrient status and the way your body clears hormones. A naturopathic assessment looks at those together instead of treating each symptom in isolation.",
              "Dr. Heather starts with a detailed history: your cycle, symptoms, contraceptive history, stress load and goals. From there she recommends testing only where it will change the plan, and builds a programme of nutrition, targeted supplements, botanical medicine and lifestyle support."]),
            ("Common reasons London patients get in touch",
             ["PMS and PMDD that disrupt work and home life, irregular, heavy or painful periods, PMOS/PCOS, endometriosis, hormonal acne, post-pill syndrome and fertility support. Many arrive after being told their standard blood results are fine, and still know that something is off.",
              "The plan is personalised, so a cycle-tracking approach for one person may look quite different from the approach for someone else, even if the label on the symptoms is the same."]),
            ("Testing, if it helps",
             ["Comprehensive blood work and DUTCH hormone testing can give a clearer picture of sex hormones, cortisol patterns and hormone metabolites. Testing is never required to start care. Dr. Heather recommends it case by case and explains the cost and logistics first."]),
        ],
        "faqs": [
            ("Can a naturopath help with irregular or painful periods?", "Naturopathic care can look at what is driving cycle changes, from nutrient status and blood sugar to stress and inflammation, and build a plan to support a healthier cycle. It works alongside, not instead of, your GP."),
            ("Do you offer online hormone consultations in London?", "Yes. All appointments are by secure video, so you can attend from home or work anywhere in London."),
            ("Do I need to stop the pill to see you?", "Not necessarily. Dr. Heather works with wherever you are, including if you are considering coming off hormonal contraception."),
            ("How much does it cost?", "The initial 75-minute consultation is &pound;200 and follow-ups are &pound;50&ndash;170. The 15-minute discovery call is free."),
        ],
    },
    "pmos-pcos": {
        "name": "PMOS/PCOS", "service": "hormone-balancing",
        "h1": "PMOS/PCOS Naturopath in London",
        "meta_title": "PMOS/PCOS Naturopath London | Village Naturopathy",
        "meta_desc": ("Online naturopath in London for PMOS/PCOS (Polyendocrine Metabolic Ovarian Syndrome). Insulin, "
                      "inflammation and cycle support. Free discovery call."),
        "quick": ("PMOS (Polyendocrine Metabolic Ovarian Syndrome) is the updated name for PCOS. Village Naturopathy "
                  "offers online naturopathic support for PMOS/PCOS in London, looking at insulin and blood sugar, "
                  "inflammation, androgens, stress and cycle patterns with a personalised plan from Dr. Heather "
                  "Robinson, ND."),
        "sections": [
            ("PMOS or PCOS: what is the difference?",
             ["PCOS (polycystic ovary syndrome) has recently been renamed PMOS, Polyendocrine Metabolic Ovarian Syndrome, to reflect that the condition is not just about the ovaries. It involves metabolic, hormonal and often inflammatory factors, and people now search for both names. This site uses PMOS/PCOS for that reason."]),
            ("How a naturopathic approach works",
             ["The drivers of PMOS/PCOS vary: insulin resistance and blood sugar swings, raised androgens, chronic inflammation, gut health and stress can all play a part. Dr. Heather takes a thorough history, recommends testing where useful and builds a plan around nutrition, supplements, botanical medicine and lifestyle changes you can sustain.",
              "Care is complementary and works alongside your GP or specialist. Many people also use the <a href=\"/programs/pmos-playbook/\">PMOS Playbook</a>, a self-guided 90-day plan, alongside one-to-one care."]),
            ("What to expect from your first appointment",
             ["Your first consultation is 75 minutes by secure video. You will cover your cycle history, symptoms, nutrition, stress, sleep and medication, and leave with an outline of the next steps. Testing is optional and recommended case by case."]),
        ],
        "faqs": [
            ("Can naturopathy help with PMOS/PCOS?", "Naturopathic treatment focuses on insulin regulation, reducing inflammation and supporting hormone balance through nutrition, botanicals and lifestyle changes, addressing the root drivers rather than only the symptoms."),
            ("Is PMOS the same as PCOS?", "PMOS (Polyendocrine Metabolic Ovarian Syndrome) is the updated name for PCOS. People now search both names."),
            ("Do I need testing before booking?", "No. Testing is not required to start care. Dr. Heather recommends it case by case, based on your individual needs."),
            ("Do you offer PMOS/PCOS appointments online in London?", "Yes, all consultations are by secure video."),
        ],
    },
    "stress-burnout": {
        "name": "Stress &amp; Burnout", "service": "stress-anxiety",
        "h1": "Burnout &amp; Stress Naturopath in London",
        "meta_title": "Burnout & Stress Naturopath London | Village Naturopathy",
        "meta_desc": ("Online naturopath in London for burnout, chronic stress, anxiety and low mood. Nervous system, "
                      "sleep and hormone support. Free discovery call."),
        "quick": ("Village Naturopathy offers online naturopathic care for burnout, chronic stress, anxiety and low mood "
                  "for people in London. Dr. Heather Robinson, ND, looks at your nervous system, sleep, hormones, gut "
                  "and nutrient status, then builds a personalised plan that fits a demanding London schedule."),
        "sections": [
            ("When stress becomes your baseline",
             ["London rewards people who keep going. After enough years of early starts, late evenings and constant availability, being tired, tense and slightly on edge starts to feel normal. But persistent stress affects sleep, digestion, hormones and mood, and those effects can be investigated and supported."]),
            ("How we approach burnout and stress",
             ["Dr. Heather combines a thorough history with the physical contributors: blood sugar, nutrient status, cortisol patterns, thyroid function and gut health. The plan usually includes nutrition, targeted supplementation, botanical medicine, nervous system regulation techniques and realistic changes to your routine.",
              "She is also a Certified HeartMath Practitioner and integrates those techniques where they are useful."]),
            ("Working with your GP",
             ["Naturopathic care is complementary. If you are also seeing a GP or therapist, Dr. Heather is happy to work alongside them. If your mood is very low or you are struggling to cope, please contact your GP or a crisis service as well."]),
        ],
        "faqs": [
            ("Can a naturopath help with burnout?", "Naturopathic care can look at how long-term stress has affected your sleep, hormones, nervous system and nutrient levels, then build a plan to help you rebuild your energy step by step."),
            ("Do you offer online appointments in London?", "Yes, all consultations are by secure video, so you can attend from home or work."),
            ("How long does it take to see a difference?", "It depends on you. Many people notice some changes within a few weeks, and a full plan usually runs three to six months."),
            ("How much does it cost?", "The initial 75-minute consultation is &pound;200, follow-ups are &pound;50&ndash;170, and the discovery call is free."),
        ],
    },
    "gut-health": {
        "name": "Gut Health", "service": "gut-health",
        "h1": "Gut Health Naturopath in London",
        "meta_title": "Gut Health Naturopath London | Village Naturopathy",
        "meta_desc": ("Online naturopath in London for IBS, SIBO, bloating, reflux and food sensitivities. GI-MAP and "
                      "SIBO testing where useful. Free discovery call."),
        "quick": ("Village Naturopathy offers online naturopathic care for IBS, SIBO, bloating, reflux and food "
                  "sensitivities in London. Dr. Heather Robinson, ND, reviews your digestive history in a 75-minute "
                  "consultation and, where useful, recommends GI-MAP stool analysis or SIBO breath testing to guide "
                  "a tailored plan."),
        "sections": [
            ("Why the gut is often the missing link",
             ["Your gut influences hormones, immunity, mood and energy, and it is itself influenced by stress, sleep, medication and diet. If you have cut out foods, tried supplements and still bloat after meals, the cause may be more specific than a single trigger."]),
            ("How we investigate",
             ["Dr. Heather starts with your history, symptoms, diet, stress and medication. Where testing will change the plan, she may recommend GI-MAP stool analysis, SIBO breath testing or food sensitivity panels, and always explains the process and cost first.",
              "The plan is phased: remove triggers, replace what is missing, support beneficial bacteria and repair the gut lining with nutrition, botanicals and nutraceuticals."]),
            ("Alongside medical care",
             ["Gut symptoms can sometimes signal conditions that need medical assessment. If you have blood in your stool, unexplained weight loss, persistent vomiting or severe pain, please see your GP promptly. Naturopathic care is complementary to medical care."]),
        ],
        "faqs": [
            ("Can a naturopath help with IBS or SIBO?", "Naturopathic care looks for what is driving your symptoms, whether that is bacterial overgrowth, low stomach acid, stress or food triggers, and builds a plan using nutrition, botanicals and nutraceuticals. SIBO breath testing is available when it is useful."),
            ("Do I need a GI-MAP test?", "Not everyone needs testing. It is recommended based on your symptoms and history."),
            ("Do you offer online gut health consultations in London?", "Yes, all consultations are by secure video."),
            ("How much does it cost?", "The initial 75-minute consultation is &pound;200, follow-ups are &pound;50&ndash;170, and the discovery call is free."),
        ],
    },
    "fatigue": {
        "name": "Fatigue", "service": "fatigue",
        "h1": "Fatigue Naturopath in London",
        "meta_title": "Fatigue Naturopath London | Village Naturopathy",
        "meta_desc": ("Online naturopath in London for persistent fatigue, low iron and B12, post-viral fatigue and burnout. "
                      "Dr. Heather Robinson, ND. Free discovery call."),
        "quick": ("Village Naturopathy offers online naturopathic care for persistent fatigue in London. Dr. Heather "
                  "Robinson, ND, combines a full history with key lab markers, such as iron, B12, thyroid markers and "
                  "cortisol, to find what is draining your energy and builds a personalised plan."),
        "sections": [
            ("Always tired, but your labs are &lsquo;normal&rsquo;?",
             ["Standard blood tests check only a few markers, and reference ranges are broad. A naturopathic assessment looks more closely at nutrient status, thyroid function, hormones and cortisol, alongside your sleep, stress and lifestyle."]),
            ("Common contributors",
             ["Low iron or B12, thyroid imbalance, blood sugar swings, long-term stress, poor sleep, post-viral recovery and hormone changes are among the most common contributors to fatigue. Iron and B12 deficiencies are especially easy to overlook in women with heavy periods, plant-based diets or digestive issues."]),
            ("Your plan",
             ["Dr. Heather starts with the most foundational causes identified through your history and labs, then layers on support using nutrition, supplementation, botanical medicine and lifestyle changes. Follow-ups adapt to your progress."]),
        ],
        "faqs": [
            ("Why am I always tired even though my blood work is normal?", "Standard blood work often checks only a few markers, and &lsquo;normal&rsquo; ranges are broad. A closer look at nutrient status, thyroid function, hormones and cortisol, alongside sleep and stress, may find what is draining your energy."),
            ("Can low iron or B12 cause fatigue?", "Yes. Iron and B12 deficiencies are among the most common and most overlooked causes of fatigue."),
            ("Do you offer online appointments in London?", "Yes, all consultations are by secure video."),
            ("When should I see my GP?", "If your fatigue is sudden, severe or comes with other worrying symptoms, see your GP promptly. Naturopathic care is complementary to medical care."),
        ],
    },
}

DUTCH = {
    "name": "DUTCH hormone test",
    "sections": [
        ("What the DUTCH test is",
         ["DUTCH stands for Dried Urine Test for Comprehensive Hormones. You collect small dried urine samples at home on filter paper, usually four samples across a day, and send them to the laboratory. It measures sex hormones such as oestrogen, progesterone and testosterone, plus their metabolites, and the daily pattern of cortisol.",
          "Some versions of the test also look at markers linked to melatonin, oxidative stress, and certain B vitamins. A DUTCH report adds detail to your history. It does not diagnose a condition on its own, and results are always interpreted alongside your symptoms and other tests."]),
        ("When it can be useful",
         ["Dr. Heather may recommend DUTCH testing when cycles are irregular or difficult, when symptoms suggest a hormone pattern that blood tests do not explain, when you are coming off hormonal contraception, or when cortisol rhythm looks relevant to sleep and energy. It is never required to start care."]),
        ("How it works with Village Naturopathy",
         ["Testing starts with a conversation. Dr. Heather explains what the test would add, how the kit reaches you, what it costs and what to do on the day, before you decide. Results are reviewed with you in a follow-up appointment and fed into your plan."]),
    ],
    "faqs": [
        ("What is a DUTCH test?", "DUTCH (Dried Urine Test for Comprehensive Hormones) is a home test that measures sex hormones, cortisol patterns and hormone metabolites from dried urine samples collected over a day."),
        ("Do I need a DUTCH test to start?", "No. Testing is not required to start care. Dr. Heather recommends it case by case, based on your individual needs."),
        ("Can I do a DUTCH test at home in the UK?", "DUTCH is a home collection test. Dr. Heather will explain how the kit reaches you and what to do before you decide to order it."),
        ("Does a DUTCH test diagnose a condition?", "No. It adds detail to your history and is interpreted alongside your symptoms and other tests. It does not diagnose a condition on its own."),
        ("How much does it cost?", "The initial 75-minute consultation is &pound;200 and follow-ups are &pound;50&ndash;170. Dr. Heather will explain the cost of any recommended testing before you decide."),
    ],
}
