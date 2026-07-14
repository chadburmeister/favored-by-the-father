#!/usr/bin/env python3
"""Static page generator for Favored by the Father Ministries.
Assembles shared header/footer around per-page content. Output: public/
Run: python3 build.py
"""
import json
import pathlib
import shutil

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "public"
SITE = "https://favoredbythefather.com"
CDN = "https://images.squarespace-cdn.com/content/v1/65faf99814900055181908ab"

IMG = {
    "logo": f"{CDN}/5c16df6c-f5f4-43f4-be13-173ed06b6ec8/logo.png?format=300w",
    "portrait": f"{CDN}/c40c6d1f-fc49-4ebd-afc0-bb3ebcc950c0/2026.02.01.jpg?format=1000w",
    "portrait_hat": "/PastorBrehon.jpeg",
    "hero_legacy": f"{CDN}/df7d89e0-4701-4433-a3b9-86415be84692/_Website+Homepage2e.png?format=1200w",
    "butterfly": f"{CDN}/4ff37526-3877-42b2-b292-79487046e568/Butterfly.jpg?format=800w",
    "music": f"{CDN}/0de7e1e1-362d-4af9-8e61-50af485c7f3d/Website+Music+Inspired+by+Ministry.png?format=800w",
    "church_hurt_song": f"{CDN}/bd646411-806b-4c16-9f11-8415795c6736/New+Release+Church+Hurt+Thumbnail+Song+Cover.png?format=800w",
    "brookside": f"{CDN}/ac03e005-4c8e-4d30-9d8f-5d4ed5b52c02/Brookside+A+Sacred+Haven.png?format=800w",
    "season5": f"{CDN}/92e5384c-e355-49ba-99b0-60c827479a24/Season+5+Newsletter+Image+on+LinkedIn+%281%29.png?format=800w",
    "smiles": f"{CDN}/03f96042-925c-4d85-b9f6-facc00ff4acd/SMILES+sail+at+sunset+2.2024-12-23.png?format=600w",
    "beyond": f"{CDN}/5ba44923-9971-4267-9c2a-36c0949c6d68/Cover+Beyond+Discipleship.from+Amazon+Q.jpg?format=600w",
    "blooming": f"{CDN}/ade487c7-930a-4874-b279-1f313c54e481/Cover+Soft+2026+Blooming.jpg?format=600w",
    "points1": f"{CDN}/ec35cce0-a58f-40f5-8432-8772a6894883/Points+Softcover2024.2.jpg?format=600w",
    "points2": f"{CDN}/e5b033d3-6ab6-4d0b-8f5f-9cb5151fea02/Points+Vol+2+Soft+Cover.jpg?format=600w",
    "persp_singles": f"{CDN}/39e2daff-e731-4c66-acdd-6626857772eb/Perspectives+Singles+Cover+1.png?format=600w",
    "unboxed100": f"{CDN}/03979347-e4a5-460c-a442-6604205e74af/100+Unboxed+Perspectives+Cover+eBook.png?format=600w",
    "church_hurt": f"{CDN}/71be1868-edcc-412e-a397-4b46fbd76f31/Church+Hurt+Hard+cover+Amazon.jpg?format=600w",
    "mending": f"{CDN}/92972f3a-1f4e-4250-b069-11f4bfb84522/Mending+the+Masterpiece+COVER+Amazon.jpg?format=600w",
    "cocoon": f"{CDN}/fe38cab0-af55-4f5e-9abd-b84a3aec166b/COCOON+1.jpg?format=600w",
    "retreat": f"{CDN}/2a67da61-d9e0-46ea-8bcc-3bedd9dd2af8/Fall+Spiritual+Retreat+3rd+Annual+2026.b.png?format=900w",
    "masterclass": f"{CDN}/429d9797-3e23-4c31-bd5c-c30e91daf227/Mini+Masterclass+Series+Cover+2.png?format=800w",
    "chatchew": f"{CDN}/3cafdf8f-75fe-4d8a-b6de-c3bec3296bfc/Chat+%26+Chew+Generic.png?format=800w",
    "firm": f"{CDN}/36d2e96c-0eb7-47e7-a753-d7f34573102f/Firm+Foundation+Logo.png?format=400w",
    "gg": f"{CDN}/986ded8d-7a0c-4aea-afba-d789bdec3ff5/GG+United+by+Love.png?format=400w",
    "retreat2025": f"{CDN}/2b67ddd9-6334-4157-900b-a72b6271d409/2025+Retreat+Discount+2-4-1-Deal.png?format=700w",
    "retreat2024": f"{CDN}/eec40e3c-9ebe-4729-9e98-842528e32861/1.jpg?format=700w",
    "elaines": f"{CDN}/08b376d1-d895-4b1e-9750-784ba117f36d/Elaines+Book+Signing+06-11+192153.png?format=700w",
    "charles": f"{CDN}/5bd416d5-766b-428f-95d4-4068a4ea73ea/CHARLES.jpg?format=700w",
    "masterclass2025": f"{CDN}/ff37d65f-c4c7-42c0-bbd8-ceead07f3f23/Mini+Masterclass+Cover.png?format=700w",
}

LINKS = {
    "email": "mailto:barbara@favoredbythefather.com",
    "donate": "https://buy.stripe.com/bIYcP60yOdzae4MdQT",
    "prayer": "https://pastorpurpose.com/",
    "calendly_general": "https://calendly.com/unboxedfavor/book-time-with-me",
    "calendly_haven": "https://calendly.com/unboxedfavor/haven4ravens-v",
    "calendly_group": "https://calendly.com/unboxedfavor/disciple-making-with-rev-dr-bb",
    "ios": "https://apps.apple.com/app/id1664953185",
    "android": "https://play.google.com/store/apps/details?id=com.inpeaceapp.favoredbythefatherministries.va",
    "youtube": "https://www.youtube.com/@favoredbythefatherministries",
    "podcast_playlist": "https://www.youtube.com/playlist?list=PLTpFdYsdDUf_94IQJGkv4bnCEQ_yIFtEy",
    "album_becoming": "https://youtube.com/playlist?list=PLTpFdYsdDUf9WvOMTqJzdYWcFlL9eR9eJ",
    "singles": "https://youtube.com/playlist?list=PLTpFdYsdDUf8UNVKAgOmuT3eLELTyQF-p",
    "appearances": "https://youtube.com/playlist?list=PLTpFdYsdDUf-nVrEWEOoKZEgC41K7X0ou",
    "eventbrite": "https://www.eventbrite.com/e/3rd-annual-fall-spiritual-retreat-tickets-1980435173917",
    "amazon_author": "https://www.amazon.com/s?k=Barbara+A.+F.+Brehon",
    "b_smiles": "https://www.amazon.com/Reach-SMILES-Developing-Disciples-Christlikeness/dp/B0DRZSFDQT",
    "b_beyond": "https://www.amazon.com/Beyond-Discipleship-Relationship-Developing-Intimacy/dp/1963565096",
    "b_blooming": "https://www.amazon.com/BLOOMING-CHRIST-Intimacy-Disciples-Christlikeness/dp/B0DRZTTJ33",
    "b_points1": "https://www.amazon.com/POINTS-PONDER-Devotional-Readings-Journaling/dp/B0DQJQKWST",
    "b_points2": "https://www.amazon.com/gp/product/B0F9DHTVY7",
    "b_persp_singles": "https://www.amazon.com/PERSPECTIVES-What-Singles-Really-Ministry/dp/B0FM33LHYH",
    "b_unboxed100": "https://www.amazon.com/100-UNBOXED-Perspectives-Reminiscences-Inspire/dp/B0G5JBDLX9",
    "b_church_hurt": "https://www.amazon.com/dp/B0H1RZXCKK",
    "b_mending": "https://www.amazon.com/Mending-Masterpiece-Discussion-Workbook-Perspectives/dp/B0H1S2F7B7",
    "b_cocoon": "https://www.amazon.com/Cocoon-Soar-Compilation-Unstoppable-Leaders/dp/B0G5T1V8DJ",
    "fb_ministry": "https://www.facebook.com/favored.by.the.father.ministries",
    "fb_firm": "https://www.facebook.com/groups/905844402777980/",
    "linkedin": "https://www.linkedin.com/in/barbara-a-f-brehon-favored",
    "linktree": "https://linktr.ee/favorbloom",
    "planu": "https://planuinc.com/about-us",
    "kingdom_women": "https://www.drsharonarrindell.com/",
    "empowerment": "https://www.bwrightjones.com/",
    "gg_united": "https://ggunitedbylove.com/",
    "ep_bloom": "https://youtu.be/sA-HtNiGANY",
    "ep_safe": "https://youtu.be/8-gti2LsJX4",
    "ep_falcon": "https://www.youtube.com/live/2DjdHEhSPqM",
    "ep_goodevil": "https://youtu.be/eUNpJf7FAdk",
    "ep_camp": "https://www.youtube.com/live/xLrwkZmJzjQ",
    "ep_authentic": "https://youtu.be/31ys1lFTxfQ",
}

BUTTERFLY_SVG = """<svg width="30" height="26" viewBox="0 0 32 28" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M16 8C13 2.5 6.5 0.5 3 3C-0.5 5.5 1 12.5 5 15.5C2 17 1.5 21.5 4 24C6.7 26.7 12 25.5 14.5 21.5L16 18M16 8C19 2.5 25.5 0.5 29 3C32.5 5.5 31 12.5 27 15.5C30 17 30.5 21.5 28 24C25.3 26.7 20 25.5 17.5 21.5L16 18M16 8V18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>"""

BOOK_ICON = """<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>"""
PHONE_ICON = """<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/></svg>"""
MUSIC_ICON = """<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>"""
MIC_ICON = """<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0 0 14 0M12 19v3"/></svg>"""
HEART_ICON = """<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 14c1.5-1.4 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.1 3 5.5l7 7z"/></svg>"""
DOVE_ICON = """<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c-1 3-4 5-8 5 2 2 4 3 6 3-1 4-4 6-7 7 5 1 9 0 12-2s5-5 5-9c1 0 2-1 3-3-2 0-3 0-4-1-1-2-4-2-7 0z"/></svg>"""


# ---------------- Structured data (JSON-LD) ----------------
PERSON = {
    "@type": "Person",
    "@id": f"{SITE}/#barbara-brehon",
    "name": "Barbara A. F. Brehon",
    "alternateName": "Rev. Dr. Barbara A. F. Brehon",
    "honorificPrefix": "Rev. Dr.",
    "jobTitle": "Pastor, Author, Podcaster, Mentor",
    "description": "Pastor, bestselling author, podcaster, lyricist, and spiritual mentor. Founder of Favored by the Father Ministries, Associate Pastor of Beulah Baptist Church, and Adjunct Professor of Discipleship at the Virginia University of Lynchburg.",
    "image": f"{SITE}/PastorBrehon.jpeg",
    "url": f"{SITE}/about",
    "sameAs": [
        LINKS["linkedin"],
        LINKS["fb_ministry"],
        LINKS["youtube"],
        LINKS["linktree"],
    ],
    "worksFor": {"@id": f"{SITE}/#organization"},
}

ORGANIZATION = {
    "@type": "Organization",
    "@id": f"{SITE}/#organization",
    "name": "Favored by the Father Ministries",
    "url": SITE,
    "logo": IMG["logo"],
    "image": f"{SITE}/PastorBrehon.jpeg",
    "description": "A church without walls founded in 2003 in Chesapeake, Virginia — nurturing souls and empowering individuals to grow in grace through digital discipleship, mentoring, books, music, and the UNBOXED on Purpose podcast.",
    "email": "barbara@favoredbythefather.com",
    "foundingDate": "2003-01",
    "founder": {"@id": f"{SITE}/#barbara-brehon"},
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Chesapeake",
        "addressRegion": "VA",
        "addressCountry": "US",
    },
    "sameAs": [
        LINKS["fb_ministry"],
        LINKS["youtube"],
        LINKS["linkedin"],
        LINKS["linktree"],
    ],
}

WEBSITE = {
    "@type": "WebSite",
    "@id": f"{SITE}/#website",
    "name": "Favored by the Father Ministries",
    "url": SITE,
    "publisher": {"@id": f"{SITE}/#organization"},
}

def _book(name, url, image, description):
    return {
        "@type": "Book",
        "name": name,
        "author": {"@id": f"{SITE}/#barbara-brehon"},
        "url": url,
        "image": image,
        "description": description,
        "bookFormat": "https://schema.org/Paperback",
        "inLanguage": "en",
    }

BOOKS_SCHEMA = {
    "@type": "ItemList",
    "name": "Books by Rev. Dr. Barbara A. F. Brehon",
    "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "item": bk}
        for i, bk in enumerate([
            _book("Reach Me with SMILES: A Handbook for Developing Disciple Makers", LINKS["b_smiles"], IMG["smiles"], "A practical guide to cultivating intentional, relational, and spiritually mature disciple makers using the SMILES model."),
            _book("Beyond Discipleship to Relationship: Developing Intimacy with the Lord", LINKS["b_beyond"], IMG["beyond"], "An invitation to move past surface-level discipleship into deep, Christ-centered relationship."),
            _book("Blooming for Christ: Growing Godly Intimacy", LINKS["b_blooming"], IMG["blooming"], "A nurturing exploration of spiritual growth and intimacy with God."),
            _book("Points to Ponder: Daily Devotionals and Journaling", LINKS["b_points1"], IMG["points1"], "Daily devotionals and journaling prompts to nurture spiritual growth."),
            _book("Points to Ponder: Daily Devotionals and Journaling, Volume 2", LINKS["b_points2"], IMG["points2"], "Fresh devotionals and prompts that deepen personal connection with the Lord."),
            _book("Perspectives: What Singles Really Want from Ministry and Life", LINKS["b_persp_singles"], IMG["persp_singles"], "Honest insight for ministries that long to serve singles well."),
            _book("100 UNBOXED Perspectives", LINKS["b_unboxed100"], IMG["unboxed100"], "The first 100 episodes of the UNBOXED on Purpose Podcast with cover art and episode summaries."),
            _book("Perspectives on Church Hurt", LINKS["b_church_hurt"], IMG["church_hurt"], "A compassionate, scripture-centered framework for healing from church hurt, grounded in a nationwide survey."),
            _book("Mending the Masterpiece: Discussion Workbook", LINKS["b_mending"], IMG["mending"], "The hands-on companion workbook to Perspectives on Church Hurt."),
            _book("From Cocoon to Soar", LINKS["b_cocoon"], IMG["cocoon"], "Anthology co-authored with 18 leaders, featuring chapters on emerging from darkness and the power of self-discovery."),
        ])
    ],
}

EVENT_SCHEMA = {
    "@type": "Event",
    "name": "3rd Annual Fall Spiritual Retreat",
    "description": "A Christian spiritual retreat in Williamsburg, Virginia — spiritual teaching, meditation, and connection with nature, designed to provide respite and nurture for those who constantly pour into others. Registration closes November 1, 2026.",
    "startDate": "2026-11-05",
    "endDate": "2026-11-06",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "eventStatus": "https://schema.org/EventScheduled",
    "image": IMG["retreat"],
    "location": {
        "@type": "Place",
        "name": "Williamsburg Christian Retreat Center",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "9275 Barnes Road",
            "addressLocality": "Toano",
            "addressRegion": "VA",
            "postalCode": "23168",
            "addressCountry": "US",
        },
    },
    "organizer": {"@id": f"{SITE}/#organization"},
    "performer": {"@id": f"{SITE}/#barbara-brehon"},
    "offers": {
        "@type": "Offer",
        "url": LINKS["eventbrite"],
        "price": "250.00",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "validThrough": "2026-11-01",
    },
}

FAQ_SCHEMA = {
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in [
            ("When and where is the 3rd Annual Fall Spiritual Retreat?",
             "Thursday, November 5 (4:00 PM) through Friday, November 6, 2026 (11:00 AM EST) at the Williamsburg Christian Retreat Center, 9275 Barnes Road, Toano, VA 23168."),
            ("What is included in retreat registration?",
             "Regular Registration includes lodging, meals, snacks, retreat materials, and all sessions. Day-only options include the sessions and materials for that day."),
            ("How much does the retreat cost?",
             "Regular Registration is $250, Day 1 only is $165, and Day 2 only is $95, plus Eventbrite processing fees. Rates increase by phase and the early-bird rate has sold out."),
            ("When does registration close?",
             "All registration options close November 1, 2026. Space is limited."),
            ("What activities are included?",
             "Spiritual teaching, meditation, peaceful nature walks, campfire fellowship, and unhurried time to reflect and connect."),
            ("Can mentors and mentees attend together?",
             "Yes — mentor and mentee teams are warmly welcomed."),
            ("What is the refund policy?",
             "Tickets are non-refundable. Questions may be emailed to barbara@favoredbythefather.com."),
        ]
    ],
}

PODCAST_SCHEMA = {
    "@type": "PodcastSeries",
    "name": "UNBOXED on Purpose",
    "description": "Real, unfiltered conversations that inspire deeper faith, self-discovery, and the courage to walk boldly in your God-gifted purpose. Hosted by Rev. Dr. Barbara A. F. Brehon.",
    "url": LINKS["podcast_playlist"],
    "image": IMG["season5"],
    "author": {"@id": f"{SITE}/#barbara-brehon"},
    "publisher": {"@id": f"{SITE}/#organization"},
}

def page_schema(canonical, title, description, extra=None):
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    if canonical != "/":
        crumbs.append({"@type": "ListItem", "position": 2, "name": title.split(" | ")[0].split(" — ")[0], "item": SITE + canonical})
    graph = [
        WEBSITE,
        ORGANIZATION,
        PERSON,
        {
            "@type": "WebPage",
            "@id": SITE + canonical + "#webpage",
            "url": SITE + canonical,
            "name": title,
            "description": description,
            "isPartOf": {"@id": f"{SITE}/#website"},
            "about": {"@id": f"{SITE}/#organization"},
            "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": crumbs},
        },
    ]
    if extra:
        graph.extend(extra if isinstance(extra, list) else [extra])
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)

def header(active: str) -> str:
    return f"""<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="/">
      <img src="{IMG['logo']}" alt="Favored by the Father Ministries logo" width="90" height="52" loading="eager">
      <span class="brand-text">
        <span class="brand-name">Favored by the Father</span>
        <span class="brand-tag">Ministries</span>
      </span>
    </a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="main-nav" aria-label="Primary">
      <a href="/about">About</a>
      <a href="/books">Books</a>
      <a href="/podcast">Podcast &amp; Music</a>
      <a href="/mentoring">Mentoring</a>
      <a href="/events">Events</a>
      <a href="/testimonials">Testimonials</a>
      <a href="/contact">Contact</a>
      <a class="nav-cta" href="{LINKS['donate']}" target="_blank" rel="noopener">Donate</a>
    </nav>
  </div>
</header>"""

FOOTER = f"""<section class="footer-cta section-tight">
  <div class="container">
    <div class="divider-butterfly">{BUTTERFLY_SVG}</div>
    <h2>Flutter freely out of confining dark boxes.<br><span class="script" style="font-size:1.2em">Be UNBOXED on purpose.</span></h2>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-gold" href="{LINKS['calendly_general']}" target="_blank" rel="noopener">Make an Appointment</a>
      <a class="btn btn-outline" href="{LINKS['donate']}" target="_blank" rel="noopener">Give &amp; Support</a>
    </div>
  </div>
</section>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <h4>Favored by the Father Ministries</h4>
        <p>A church without walls since 2003 — nurturing souls and empowering individuals to grow in grace through digital discipleship and fellowship. Chesapeake, Virginia.</p>
        <p><a href="{LINKS['email']}">barbara@favoredbythefather.com</a></p>
      </div>
      <div>
        <h4>Explore</h4>
        <a href="/about">About &amp; Beliefs</a>
        <a href="/books">Books by Dr.&nbsp;Brehon</a>
        <a href="/#devotional">Free 7-Day Devotional</a>
        <a href="/podcast">UNBOXED Podcast</a>
        <a href="/mentoring">Mentoring &amp; Brookside</a>
      </div>
      <div>
        <h4>Connect</h4>
        <a href="/events">Events &amp; Retreat</a>
        <a href="/testimonials">Testimonials</a>
        <a href="{LINKS['prayer']}" target="_blank" rel="noopener">Prayer Request</a>
        <a href="{LINKS['donate']}" target="_blank" rel="noopener">Donate</a>
      </div>
      <div>
        <h4>Follow</h4>
        <a href="{LINKS['youtube']}" target="_blank" rel="noopener">YouTube</a>
        <a href="{LINKS['fb_ministry']}" target="_blank" rel="noopener">Facebook</a>
        <a href="{LINKS['linkedin']}" target="_blank" rel="noopener">LinkedIn</a>
        <a href="{LINKS['linktree']}" target="_blank" rel="noopener">Linktree</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Favored by the Father Ministries. All rights reserved.</span>
      <span>"Grow in grace… and remain favored by the Father." — 2&nbsp;Peter&nbsp;3:18</span>
    </div>
  </div>
</footer>
<script src="/main.js?v=3" defer></script>"""

def page(*, filename: str, title: str, description: str, body: str, canonical: str, extra_schema=None) -> None:
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://favoredbythefather.com{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{SITE + IMG['portrait_hat']}">
  <meta property="og:url" content="https://favoredbythefather.com{canonical}">
  <meta property="og:site_name" content="Favored by the Father Ministries">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{SITE + IMG['portrait_hat']}">
  <script type="application/ld+json">{page_schema(canonical, title, description, extra_schema)}</script>
  <link rel="icon" href="{IMG['logo']}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Great+Vibes&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css?v=3">
</head>
<body>
{header(canonical)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>
"""
    OUT.mkdir(exist_ok=True)
    (OUT / filename).write_text(html)
    print(f"wrote public/{filename} ({len(html)} bytes)")


# Import page bodies
from pages_home import BODY as home_body
from pages_about import BODY as about_body
from pages_books import BODY as books_body
from pages_podcast import BODY as podcast_body
from pages_mentoring import BODY as mentoring_body
from pages_events import BODY as events_body
from pages_testimonials import BODY as testimonials_body
from pages_contact import BODY as contact_body

ctx = {"IMG": IMG, "LINKS": LINKS, "BUTTERFLY_SVG": BUTTERFLY_SVG,
       "BOOK_ICON": BOOK_ICON, "PHONE_ICON": PHONE_ICON, "MUSIC_ICON": MUSIC_ICON,
       "MIC_ICON": MIC_ICON, "HEART_ICON": HEART_ICON, "DOVE_ICON": DOVE_ICON}

page(filename="index.html", canonical="/",
     title="Favored by the Father Ministries | Spiritual Growth, Discipleship & Christian Mentoring",
     description="A church without walls founded in 2003 in Chesapeake, Virginia. Grow in grace with Rev. Dr. Barbara A. F. Brehon through discipleship books, the UNBOXED on Purpose podcast, Christian mentoring, spiritual retreats, and music inspired by ministry.",
     body=home_body.format(**ctx))
page(filename="about.html", canonical="/about",
     title="Rev. Dr. Barbara A. F. Brehon — Pastor, Author & Christian Mentor | About Favored by the Father Ministries",
     description="Meet Rev. Dr. Barbara A. F. Brehon: Virginia pastor, bestselling Christian author, UNBOXED on Purpose podcast host, and spiritual mentor. Learn the foundation, purpose, motto, and mission of Favored by the Father Ministries.",
     body=about_body.format(**ctx))
page(filename="books.html", canonical="/books",
     title="Christian Books on Discipleship, Daily Devotionals & Healing from Church Hurt | Rev. Dr. Barbara A. F. Brehon",
     description="Bestselling Christian books by Rev. Dr. Barbara A. F. Brehon: developing disciple makers (Reach Me with SMILES), intimacy with the Lord, daily devotionals, and Perspectives on Church Hurt — a scripture-centered guide to healing from church hurt.",
     body=books_body.format(**ctx), extra_schema=BOOKS_SCHEMA)
page(filename="podcast.html", canonical="/podcast",
     title="UNBOXED on Purpose — Christian Podcast on Faith & Purpose | Plus Music Inspired by Ministry",
     description="Listen to UNBOXED on Purpose, a Christian podcast of real, unfiltered conversations about faith, purpose, and breaking free — plus Here, in the Becoming, the gospel album inspired by Dr. Brehon's books.",
     body=podcast_body.format(**ctx), extra_schema=PODCAST_SCHEMA)
page(filename="mentoring.html", canonical="/mentoring",
     title="Christian Mentoring & Spiritual Direction — Brookside and Haven for Ravens | Favored by the Father Ministries",
     description="One-on-one Christian mentoring and spiritual direction, virtual or in person. Brookside scripture-centered mentoring, Haven for Ravens respite for pastors, caregivers and leaders, and a community prayer circle.",
     body=mentoring_body.format(**ctx))
page(filename="events.html", canonical="/events",
     title="Christian Spiritual Retreat in Virginia — Nov 5–6, 2026 | Events & Masterclasses",
     description="Join the 3rd Annual Fall Spiritual Retreat, November 5–6, 2026 at Williamsburg Christian Retreat Center in Toano, Virginia — plus the Mini Masterclass Series, Chat & Chew book talks, and group teaching sessions.",
     body=events_body.format(**ctx), extra_schema=[EVENT_SCHEMA, FAQ_SCHEMA])
page(filename="testimonials.html", canonical="/testimonials",
     title="Testimonials — Christian Mentoring & Retreat Stories | Favored by the Father Ministries",
     description="Real stories of healing, renewal, and spiritual transformation from Haven for Ravens, Brookside mentoring, and the ministry of Rev. Dr. Barbara A. F. Brehon.",
     body=testimonials_body.format(**ctx))
page(filename="contact.html", canonical="/contact",
     title="Contact, Prayer Requests & Booking | Favored by the Father Ministries",
     description="Contact Rev. Dr. Barbara A. F. Brehon: book a speaking engagement, mentoring session, or podcast appearance, share a prayer request, download the free ministry app, or give to support the ministry.",
     body=contact_body.format(**ctx))

# Copy static assets into the output directory
for static in ("styles.css", "main.js", "404.html", "robots.txt", "sitemap.xml", "PastorBrehon.jpeg"):
    shutil.copy(ROOT / static, OUT / static)
print("done — output in public/")
