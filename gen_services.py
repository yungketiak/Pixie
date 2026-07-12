#!/usr/bin/env python3
# Generates the 4 PIXIE³ service landing pages from one template.
import json, os

OUT = "/sessions/zealous-gifted-hopper/mnt/outputs/site"

FOOTER_LINKS = """        <li><a href="works.html">Our Works</a></li>
        <li><a href="process.html">Process</a></li>
        <li><a href="faq.html">FAQ</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="hotel-virtual-tour.html">Hotel Tours</a></li>
        <li><a href="event-venue-virtual-tour.html">Venue Tours</a></li>
        <li><a href="retail-virtual-tour.html">Retail Tours</a></li>
        <li><a href="office-virtual-tour.html">Office Tours</a></li>
        <li><a href="https://instagram.com/pixiecube.space" target="_blank" rel="noopener">Instagram</a></li>"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="https://pixiecube.space/{slug}" />
  <meta property="og:image" content="https://pixiecube.space/assets/room-scan.jpg" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="canonical" href="https://pixiecube.space/{slug}" />
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23212431'/%3E%3Crect x='22' y='22' width='56' height='56' fill='%23EA5C1F'/%3E%3C/svg%3E" />

  <script type="application/ld+json">
{jsonld}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Mono:wght@300;400;500&family=Outfit:wght@300;400;500;600&family=Silkscreen:wght@400;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />

  <style>
    .svc-intro {{ background: var(--navy-mid); }}
    .svc-intro-grid {{
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 4rem;
      align-items: center;
    }}
    .svc-intro-copy p {{ color: var(--mist); font-size: 0.97rem; line-height: 1.8; margin-bottom: 1.4rem; }}
    .svc-intro-visual {{ aspect-ratio: 16/11; }}
    .svc-benefits {{ background: var(--navy); }}
    .svc-title {{ font-size: clamp(1.8rem, 3.5vw, 3rem); margin-bottom: 3rem; }}
    .svc-uses {{ background: var(--navy-mid); }}
    .use-row {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 2rem;
    }}
    .use {{
      border-left: 2px solid var(--amber);
      padding-left: 1.2rem;
      transition: transform 0.3s var(--ease-out-expo);
    }}
    .use:hover {{ transform: translateX(4px); }}
    .use-title {{
      font-family: var(--ff-display);
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--white);
      margin-bottom: 0.4rem;
    }}
    .use-desc {{ font-size: 0.86rem; color: var(--mist); line-height: 1.6; }}
    @media (max-width: 900px) {{
      .svc-intro-grid {{ grid-template-columns: 1fr; gap: 2.5rem; }}
    }}
  </style>
</head>
<body>

  <nav aria-label="Main navigation">
    <a href="index.html" class="logo">PIXIE<sup>3</sup></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu">Menu</button>
    <ul class="nav-links" id="nav-menu">
      <li><a href="index.html">Home</a></li>
      <li><a href="works.html">Our Works</a></li>
      <li><a href="process.html">Process</a></li>
      <li><a href="faq.html">FAQ</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
    <a href="contact.html" class="nav-cta">Get a Quote</a>
  </nav>

  <header class="page-hero">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
  </header>

  <section class="svc-intro" aria-labelledby="intro-heading">
    <div class="section-inner">
      <div class="svc-intro-grid">
        <div class="svc-intro-copy reveal">
          <h2 class="display-title svc-title" id="intro-heading">{intro_title}</h2>
          {intro_paras}
          <a href="works.html" class="btn-ghost">Walk Through a Live Tour →</a>
        </div>
        <div class="frame svc-intro-visual reveal">
          <span class="corner tl" aria-hidden="true"></span>
          <img src="assets/{img}" alt="{img_alt}" loading="lazy" />
          <span class="corner br" aria-hidden="true"></span>
          <span class="badge">{img_badge}</span>
        </div>
      </div>
    </div>
  </section>

  <section class="svc-benefits" aria-labelledby="benefits-heading">
    <div class="section-inner">
      <p class="eyebrow reveal">Why it works</p>
      <h2 class="display-title svc-title reveal" id="benefits-heading">{benefits_title}</h2>
      <div class="card-grid" role="list">
{benefit_cards}
      </div>
    </div>
  </section>

  <section class="svc-uses" aria-labelledby="uses-heading">
    <div class="section-inner">
      <p class="eyebrow reveal">Where it goes to work</p>
      <h2 class="display-title svc-title reveal" id="uses-heading">One scan. <em>Everywhere it matters.</em></h2>
      <div class="use-row">
{uses}
      </div>
    </div>
  </section>

  <section class="cta-band" aria-labelledby="cta-heading">
    <div class="section-inner">
      <h2 class="cta-title" id="cta-heading">{cta_title}</h2>
      <p class="cta-sub">{cta_sub}</p>
      <div class="cta-actions">
        <a href="contact.html" class="btn-primary">Get a Fixed Quote →</a>
        <a href="process.html" class="btn-ghost">See the Process</a>
      </div>
    </div>
  </section>

  <footer>
    <div class="footer-inner">
      <div class="footer-logo">PIXIE<sup>3</sup></div>
      <ul class="footer-links">
{footer_links}
      </ul>
      <div class="footer-legal">
        © 2026 PIXIE³. Malaysia.<br>
        Powered by Matterport.
      </div>
    </div>
  </footer>

  <script src="site.js"></script>
</body>
</html>
"""

def card(num, icon, title, line):
    return f"""        <article class="card reveal" role="listitem">
          <div class="card-num">{num}</div>
          <span class="card-icon" aria-hidden="true">{icon}</span>
          <div class="card-title">{title}</div>
          <p class="card-line">{line}</p>
        </article>"""

def use(title, desc):
    return f"""        <div class="use reveal">
          <div class="use-title">{title}</div>
          <p class="use-desc">{desc}</p>
        </div>"""

def jsonld(name, slug, svc_desc, page_name):
    d = {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Service",
          "name": name,
          "serviceType": "Matterport 3D virtual tour production",
          "description": svc_desc,
          "url": f"https://pixiecube.space/{slug}",
          "areaServed": { "@type": "Country", "name": "Malaysia" },
          "provider": {
            "@type": "LocalBusiness",
            "@id": "https://pixiecube.space/#business",
            "name": "PIXIE³",
            "url": "https://pixiecube.space/",
            "email": "hello@pixiecube.space",
            "telephone": "+60145845034",
            "address": { "@type": "PostalAddress", "streetAddress": "Plaza KLTS", "addressLocality": "Kuala Lumpur", "postalCode": "53000", "addressCountry": "MY" },
            "geo": { "@type": "GeoCoordinates", "latitude": 3.2035407, "longitude": 101.7034491 },
            "sameAs": ["https://instagram.com/pixiecube.space"]
          }
        },
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://pixiecube.space/" },
            { "@type": "ListItem", "position": 2, "name": page_name, "item": f"https://pixiecube.space/{slug}" }
          ]
        }
      ]
    }
    return json.dumps(d, indent=2, ensure_ascii=False)

pages = [
  {
    "slug": "hotel-virtual-tour.html",
    "title": "Hotel Virtual Tour Malaysia — Matterport 3D Scanning for Hotels & Resorts | PIXIE³",
    "og_title": "Hotel Virtual Tours Malaysia | PIXIE³",
    "desc": "Matterport 3D virtual tours for hotels and resorts in Malaysia. Let guests walk through rooms, suites and amenities before booking — on your website, OTAs and Google. Fixed quotes via WhatsApp.",
    "eyebrow": "Hotels & Resorts",
    "h1": "Let guests check in — <em>before they book.</em>",
    "lede": "A Matterport 3D virtual tour puts your rooms, lobby, pool and ballroom in front of guests worldwide — an immersive walkthrough that photos and videos can't match.",
    "intro_title": "The room sells itself. <em>Show it.</em>",
    "intro_paras": """<p>Guests booking a hotel in Malaysia compare dozens of options in minutes. Static photos all look the same — a live 3D walkthrough of your actual suite, captured in 4K, is what stops the scroll and builds the confidence to book direct.</p>
          <p>PIXIE³ scans your rooms, F&amp;B outlets, spa, pool deck and event spaces into one seamless tour you can embed on your website, share with corporate clients, and publish to your Google Business Profile.</p>""",
    "img": "room-scan.jpg",
    "img_alt": "Matterport 3D virtual tour of a hotel room in Kuala Lumpur, Malaysia",
    "img_badge": "Hotel suite · KL",
    "benefits_title": "Why hotels invest in <strong>virtual tours.</strong>",
    "benefit_cards": [
      ("01","🛏️","Drive direct bookings","Guests who walk the actual room book with confidence — and book direct instead of through commission-heavy OTAs."),
      ("02","🌏","Sell to overseas markets","International guests and travel agents tour your property from anywhere, any time zone, without a famil trip."),
      ("03","💍","Win events & weddings","Planners shortlist your ballroom and function rooms remotely — fewer site visits, faster confirmations."),
      ("04","📍","Stand out on Google","Publish the tour to your Google Business Profile so your listing outshines every competitor's photo gallery."),
    ],
    "uses": [
      ("Website & booking engine","Embed the tour beside your room types to lift conversion where it counts."),
      ("OTA & travel-agent kits","Send one link that shows everything — no more heavy photo decks."),
      ("Sales & MICE proposals","Attach walkthroughs of function spaces to every corporate pitch."),
      ("Social media","Dollhouse reveals and room fly-throughs make scroll-stopping content."),
    ],
    "cta_title": "Ready to show your property <em>properly?</em>",
    "cta_sub": "WhatsApp us your property type and room count — we'll come back with a fixed quote, usually within the hour.",
  },
  {
    "slug": "event-venue-virtual-tour.html",
    "title": "Event Venue Virtual Tour Malaysia — 3D Walkthroughs for Ballrooms & Event Spaces | PIXIE³",
    "og_title": "Event Venue Virtual Tours Malaysia | PIXIE³",
    "desc": "Matterport 3D virtual tours for event venues, ballrooms and convention spaces in Malaysia. Give planners a photorealistic virtual site inspection with real measurements — book more events, faster.",
    "eyebrow": "Event Venues",
    "h1": "Every planner's site visit — <em>without the visit.</em>",
    "lede": "Give event planners a photorealistic, measurable 3D walkthrough of your ballroom, hall or convention space — the virtual site inspection that gets you shortlisted first.",
    "intro_title": "Planners decide fast. <em>Be explorable.</em>",
    "intro_paras": """<p>Event planners juggle venues across the city and country — the venue they can inspect at 11pm from their laptop has the edge. A Matterport tour lets them walk your space, check ceiling heights, sight lines and floor dimensions with built-in measurement tools, and visualise their setup before they ever call you.</p>
          <p>PIXIE³ captures your ballrooms, breakout rooms, pre-function areas, loading access and parking flow into one connected tour your sales team can send with every proposal.</p>""",
    "img": "dollhouse.jpg",
    "img_alt": "Matterport dollhouse 3D model used for virtual event venue site inspection in Malaysia",
    "img_badge": "Dollhouse view",
    "benefits_title": "Why venues win more events with <strong>3D tours.</strong>",
    "benefit_cards": [
      ("01","📐","Real measurements","Planners measure stage, seating and rigging clearances directly inside the tour — Matterport captures true dimensions."),
      ("02","⚡","Faster confirmations","Cut the site-visit bottleneck. Shortlisting happens online; visits become final confirmations, not first looks."),
      ("03","🌐","Reach outstation clients","KL venue, Penang client? International conference organisers? They inspect your venue without flights."),
      ("04","🗓️","Sell dates year-round","Your venue is dressed and lit perfectly in the tour — even when it's mid-teardown in real life."),
    ],
    "uses": [
      ("Sales proposals","Every quotation goes out with a walkthrough link attached."),
      ("Venue-finder listings","Stand out on venue marketplaces with an interactive tour."),
      ("Floorplan planning","Planners map layouts against the real space, reducing surprises."),
      ("Vendor coordination","AV, decor and catering teams scope the space remotely before setup day."),
    ],
    "cta_title": "Make your venue the <em>easy yes.</em>",
    "cta_sub": "Tell us about your ballroom or event space on WhatsApp — fixed quote, fast turnaround, zero disruption to your event calendar.",
  },
  {
    "slug": "retail-virtual-tour.html",
    "title": "Retail & F&B Virtual Tour Malaysia — 360° Store & Restaurant Tours | PIXIE³",
    "og_title": "Retail & F&B Virtual Tours Malaysia | PIXIE³",
    "desc": "Matterport 3D virtual tours for retail stores, cafés and restaurants in Malaysia. Show your atmosphere and layout online, boost your Google Maps listing, and turn browsers into walk-ins.",
    "eyebrow": "Retail & F&B",
    "h1": "Your atmosphere is the product. <em>Put it online.</em>",
    "lede": "A 360° virtual tour lets customers step inside your store, café or restaurant from Google Maps, Instagram or your website — and decide to visit before they've left the couch.",
    "intro_title": "Foot traffic starts <em>online.</em>",
    "intro_paras": """<p>Most customers check a store or restaurant online before visiting. Photos show dishes and products — a virtual tour shows the vibe: the lighting, the layout, the seating, the space itself. That's what converts a browser into a walk-in.</p>
          <p>PIXIE³ captures your outlet in 4K and delivers a tour you can embed on your website, link in your Instagram bio, and publish to your Google Business Profile — so customers searching nearby can literally walk in from the map.</p>""",
    "img": "room-scan.jpg",
    "img_alt": "4K Matterport 360 virtual tour capture for retail and F&B spaces in Malaysia",
    "img_badge": "4K capture",
    "benefits_title": "Why retail &amp; F&amp;B outlets go <strong>3D.</strong>",
    "benefit_cards": [
      ("01","🗺️","Own your Google listing","Tours published to Google make your listing dramatically more engaging than competitors' static photos."),
      ("02","🪑","Show the experience","Customers see the ambience and seating before choosing you for a date, meeting or gathering."),
      ("03","📸","Content that compounds","4K stills and fly-through clips from the scan feed your socials for months."),
      ("04","🏬","Franchise & investor ready","Show prospective franchisees and landlords your concept and fit-out standard remotely."),
    ],
    "uses": [
      ("Google Maps & Search","Appear richer than competitors right where customers decide."),
      ("Instagram bio link","One tap from your profile into your space."),
      ("Website & delivery pages","Give online customers a reason to visit in person."),
      ("New outlet launches","Build hype by letting followers explore before opening day."),
    ],
    "cta_title": "Let customers walk in <em>from anywhere.</em>",
    "cta_sub": "WhatsApp us your outlet size and location — we'll quote fixed, scan around your operating hours, and have you live in days.",
  },
  {
    "slug": "office-virtual-tour.html",
    "title": "Office & Showroom Virtual Tour Malaysia — Corporate 3D Digital Twins | PIXIE³",
    "og_title": "Office & Corporate Virtual Tours Malaysia | PIXIE³",
    "desc": "Matterport 3D virtual tours and digital twins for offices, showrooms and corporate facilities in Malaysia. Virtual onboarding, remote presentations, leasing and facility documentation.",
    "eyebrow": "Corporate Spaces",
    "h1": "Your facility, presenting itself — <em>24/7.</em>",
    "lede": "Digitise your office, showroom or facility into a Matterport digital twin — an always-on walkthrough for clients, recruits, tenants and stakeholders anywhere in the world.",
    "intro_title": "A digital twin works <em>around the clock.</em>",
    "intro_paras": """<p>Corporate spaces are built to impress — but only the people who physically visit. A 3D digital twin puts your headquarters, showroom or facility in front of overseas clients, remote hires and prospective tenants with the same impact as a guided walkthrough.</p>
          <p>PIXIE³ scans your space with Matterport precision — including floorplans and measurements — delivering a tour that slots into pitch decks, onboarding portals, leasing listings and facility documentation.</p>""",
    "img": "dollhouse.jpg",
    "img_alt": "Matterport digital twin dollhouse view of a corporate space in Malaysia",
    "img_badge": "Digital twin",
    "benefits_title": "Why companies build <strong>digital twins.</strong>",
    "benefit_cards": [
      ("01","🤝","Impress remote clients","Walk international partners through your HQ or showroom without anyone boarding a flight."),
      ("02","🧑‍💻","Onboard & recruit","Show candidates and new hires the workplace before day one — a modern-employer signal."),
      ("03","🏗️","Lease space faster","Serviced offices and landlords let tenants inspect units remotely, shortening leasing cycles."),
      ("04","📋","Document the facility","Accurate as-built records with measurements — useful for renovation, insurance and compliance."),
    ],
    "uses": [
      ("Pitch decks & proposals","A live walkthrough link that sets your company apart."),
      ("Careers & onboarding","Embed the office tour on your careers page."),
      ("Leasing & listings","Property listings with 3D tours get more qualified enquiries."),
      ("Renovation planning","Contractors quote from the digital twin, not repeat site visits."),
    ],
    "cta_title": "Put your space to <em>work.</em>",
    "cta_sub": "Tell us about your office, showroom or facility — we'll scan around your working hours and deliver in days.",
  },
]

os.makedirs(OUT, exist_ok=True)
for p in pages:
    page_name = p["eyebrow"]
    html = TEMPLATE.format(
        title=p["title"], desc=p["desc"], og_title=p["og_title"], slug=p["slug"],
        jsonld=jsonld(p["og_title"].split(" | ")[0], p["slug"], p["desc"], page_name),
        eyebrow=p["eyebrow"], h1=p["h1"], lede=p["lede"],
        intro_title=p["intro_title"], intro_paras=p["intro_paras"],
        img=p["img"], img_alt=p["img_alt"], img_badge=p["img_badge"],
        benefits_title=p["benefits_title"],
        benefit_cards="\n\n".join(card(*c) for c in p["benefit_cards"]),
        uses="\n\n".join(use(*u) for u in p["uses"]),
        cta_title=p["cta_title"], cta_sub=p["cta_sub"],
        footer_links=FOOTER_LINKS,
    )
    with open(os.path.join(OUT, p["slug"]), "w") as f:
        f.write(html)
    print(f"wrote {p['slug']} ({len(html)} bytes)")
