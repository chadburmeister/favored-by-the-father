BODY = """
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Events 2026</span>
    <h1>Gather, <span class="script" style="font-size:1.05em">grow,</span> and be renewed</h1>
    <p>Mini masterclasses, book talks, group sessions, and the annual Fall Spiritual Retreat — spaces designed for reflection, refocus, and intentional growth.</p>
  </div>
</section>

<!-- RETREAT (FLAGSHIP) -->
<section>
  <div class="container grid-2" style="align-items:center">
    <div class="media-frame reveal">
      <img src="{IMG[retreat]}" alt="3rd Annual Fall Spiritual Retreat 2026 flyer" loading="eager">
    </div>
    <div class="reveal">
      <span class="eyebrow">Flagship Gathering</span>
      <h2>3rd Annual Fall Spiritual Retreat</h2>
      <div class="event-card" style="margin:1.4rem 0">
        <div class="event-date">
          <div class="month">Nov</div>
          <div class="day">5–6</div>
          <div class="month">2026</div>
        </div>
        <div>
          <p style="color:var(--ink-soft);margin:0"><strong>Thursday – Friday</strong><br>
          Williamsburg Christian Retreat Center<br>
          9275 Barnes Road, Toano, VA 23168</p>
        </div>
      </div>
      <p style="color:var(--ink-soft)">A getaway filled with spiritual teaching, meditation, and connection with nature — designed to provide respite and nurture for those who constantly pour into others. Mentor and mentee teams welcomed.</p>
      <p style="color:var(--ink-soft)"><strong>Registration includes lodging, meals, snacks, retreat materials, and all sessions.</strong> Space is limited, rates increase by phase, and the early-bird phase has already sold out.</p>
      <p data-countdown-wrap style="margin:0 0 1.2rem"><span class="countdown-chip">Registration closes Nov 1 — <strong data-countdown="2026-11-01">limited time</strong> left</span></p>
      <div class="btn-row">
        <a class="btn btn-gold" href="{LINKS[eventbrite]}" target="_blank" rel="noopener">Reserve Now on Eventbrite</a>
        <a class="btn btn-outline-dark" href="#pricing">Pricing &amp; FAQ</a>
      </div>
    </div>
  </div>
</section>

<!-- RETREAT PRICING -->
<section class="section-tight" id="pricing" style="background:var(--ivory-warm)">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Simple, Transparent Pricing</span>
      <h2>Choose your <span class="script" style="font-size:1.1em">retreat</span> experience</h2>
      <p>Every option includes retreat materials and that day's sessions. The full experience adds overnight lodging, meals, and snacks.</p>
    </div>
    <div class="price-grid">
      <article class="price-card featured reveal">
        <span class="price-flag">Full Experience</span>
        <div class="price-tier">Regular Registration</div>
        <div class="price-amount"><sup>$</sup>250</div>
        <div class="price-note">+ processing fee</div>
        <p class="price-desc">Both days with overnight stay — lodging, meals, snacks, retreat materials, and every session from Thursday 4&nbsp;PM through Friday 11&nbsp;AM.</p>
        <a class="btn btn-gold" href="{LINKS[eventbrite]}" target="_blank" rel="noopener">Reserve Your Place</a>
      </article>
      <article class="price-card reveal">
        <div class="price-tier">Day 1 Only</div>
        <div class="price-amount"><sup>$</sup>165</div>
        <div class="price-note">+ processing fee</div>
        <p class="price-desc">Thursday, November 5 — the opening teaching, evening fellowship, and campfire gathering.</p>
        <a class="btn btn-outline-dark" href="{LINKS[eventbrite]}" target="_blank" rel="noopener">Register for Day 1</a>
      </article>
      <article class="price-card reveal">
        <div class="price-tier">Day 2 Only</div>
        <div class="price-amount"><sup>$</sup>95</div>
        <div class="price-note">+ processing fee</div>
        <p class="price-desc">Friday, November 6 — morning teaching, meditation, and closing sessions through 11&nbsp;AM.</p>
        <a class="btn btn-outline-dark" href="{LINKS[eventbrite]}" target="_blank" rel="noopener">Register for Day 2</a>
      </article>
    </div>
    <p class="price-fine">Checkout is securely handled on Eventbrite. Tickets are non-refundable. All registration closes November&nbsp;1,&nbsp;2026.</p>
  </div>
</section>

<!-- RETREAT FAQ -->
<section class="section-tight" style="background:var(--white)">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Good to Know</span>
      <h2>Retreat questions, <span class="script" style="font-size:1.1em">answered</span></h2>
    </div>
    <div class="faq reveal">
      <details class="faq-item">
        <summary>When and where is the retreat?</summary>
        <p>Thursday, November 5 (4:00 PM) through Friday, November 6, 2026 (11:00 AM EST) at the Williamsburg Christian Retreat Center, 9275 Barnes Road, Toano, VA 23168.</p>
      </details>
      <details class="faq-item">
        <summary>What is included in my registration?</summary>
        <p>Regular Registration includes lodging, meals, snacks, retreat materials, and all sessions. Day-only options include the sessions and materials for that day.</p>
      </details>
      <details class="faq-item">
        <summary>How much does it cost?</summary>
        <p>Regular Registration is $250, Day 1 only is $165, and Day 2 only is $95, plus Eventbrite processing fees. Rates increase by phase — the early-bird rate has already sold out, so today's rate is the best remaining price.</p>
      </details>
      <details class="faq-item">
        <summary>When does registration close?</summary>
        <p>All registration options close November 1, 2026 — and space is limited, so earlier is better.</p>
      </details>
      <details class="faq-item">
        <summary>What will we actually do?</summary>
        <p>Spiritual teaching, meditation, peaceful nature walks, campfire fellowship, and unhurried time to breathe, reflect, and connect with the Lord and with like-minded friends.</p>
      </details>
      <details class="faq-item">
        <summary>Can I come with my mentor or mentee?</summary>
        <p>Yes — mentor and mentee teams are warmly welcomed. The retreat is designed for those who pour into others, together.</p>
      </details>
      <details class="faq-item">
        <summary>What is the refund policy?</summary>
        <p>Tickets are non-refundable. If you have questions before registering, email <a href="mailto:barbara@favoredbythefather.com">barbara@favoredbythefather.com</a>.</p>
      </details>
    </div>
  </div>
</section>

<!-- MASTERCLASS + CHAT & CHEW -->
<section class="panel-dark on-dark">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Ongoing in 2026</span>
      <h2>Teaching Experiences</h2>
    </div>
    <article class="glass reveal" style="border:1.5px solid rgba(227,197,101,0.5);margin-bottom:1.8rem">
      <span class="eyebrow" style="color:var(--gold-soft)">New &mdash; Enrolling Now</span>
      <h3 style="font-size:1.6rem">Favored by the Father Bible Institute</h3>
      <p>Join Rev. Dr. Barbara A. F. Brehon for the Favored by the Father Bible Institute &mdash; an immersive teaching series where she guides you through the spiritual insights and practical applications found in her published works. Secure your spot for this transformative, paid experience today by registering through our official Eventbrite page.</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="{LINKS[eventbrite_org]}" target="_blank" rel="noopener">Register on Eventbrite</a>
        <a class="btn btn-outline" href="/books">Explore the Books</a>
      </div>
    </article>
    <div class="grid-2">
      <article class="glass reveal">
        <div class="media-frame" style="margin-bottom:1.4rem"><img src="{IMG[masterclass]}" alt="Mini Masterclass Series" loading="lazy"></div>
        <h3>Mini Masterclass Series</h3>
        <p>Focused, 45-minute teaching experiences designed to create space for reflection, refocus, and intentional growth. More than a lecture — thoughtful engagement, practical insight, and spiritual grounding, tailored to help you grow in God's grace.</p>
        <div class="btn-row">
          <a class="btn btn-sm btn-gold" href="{LINKS[calendly_group]}" target="_blank" rel="noopener">Book 45 min – 3 hours</a>
          <a class="btn btn-sm btn-outline" href="mailto:barbara@favoredbythefather.com">Email Questions</a>
        </div>
      </article>
      <article class="glass reveal">
        <div class="media-frame" style="margin-bottom:1.4rem"><img src="{IMG[chatchew]}" alt="Chat and Chew book talks" loading="lazy"></div>
        <h3>Chat &amp; Chew</h3>
        <p>Book talks and signings tailored to meet your needs — available upon request. Topics we tailor to your context include:</p>
        <div class="badge-row">
          <span class="badge">Emerging from Darkness</span><span class="badge">Discipleship</span><span class="badge">Developing Disciple Makers</span><span class="badge">Intimacy with the Lord</span><span class="badge">Spiritual Growth</span><span class="badge">Self-Care</span><span class="badge">Placing Priorities</span><span class="badge">Spiritual Gifts</span>
        </div>
        <div class="btn-row">
          <a class="btn btn-sm btn-gold" href="{LINKS[calendly_general]}" target="_blank" rel="noopener">Request a Book Talk</a>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- PAST EVENTS -->
<section>
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Our Journey</span>
      <h2>Past Events &amp; <span class="script" style="font-size:1.1em">Photo</span> Gallery</h2>
      <p>A look back at where the Lord has taken this ministry.</p>
    </div>
    <div class="grid-3">
      <article class="card reveal">
        <div class="media-frame" style="margin-bottom:1.2rem"><img src="{IMG[retreat2025]}" alt="2025 Fall Spiritual Retreat" loading="lazy"></div>
        <h3 style="font-size:1.1rem">2nd Annual Fall Spiritual Retreat — 2025</h3>
        <p>Williamsburg Christian Retreat Center, Toano, VA.</p>
      </article>
      <article class="card reveal">
        <div class="media-frame" style="margin-bottom:1.2rem"><img src="{IMG[masterclass2025]}" alt="Mini Masterclass Series 2025" loading="lazy"></div>
        <h3 style="font-size:1.1rem">Mini Masterclass Series — 2025</h3>
        <p>Growing in God's grace, one focused session at a time.</p>
      </article>
      <article class="card reveal">
        <div class="media-frame" style="margin-bottom:1.2rem"><img src="{IMG[retreat2024]}" alt="Fall Spiritual Retreat 2024" loading="lazy"></div>
        <h3 style="font-size:1.1rem">Fall Spiritual Retreat — 2024</h3>
        <p>November 14–15, 2024 · Williamsburg Christian Retreat Center.</p>
      </article>
      <article class="card reveal">
        <div class="media-frame" style="margin-bottom:1.2rem"><img src="{IMG[elaines]}" alt="Book signing at Elaine's, Alexandria VA" loading="lazy"></div>
        <h3 style="font-size:1.1rem">Book Signing at Elaine's — 2024</h3>
        <p>June 30, 2024 · 208 Queen St., Alexandria, VA.</p>
      </article>
      <article class="card reveal">
        <div class="media-frame" style="margin-bottom:1.2rem"><img src="{IMG[charles]}" alt="Book signing at 2nd and Charles, Richmond VA" loading="lazy"></div>
        <h3 style="font-size:1.1rem">2nd &amp; Charles Bookstore — 2024</h3>
        <p>July 12, 2024 · 9004 West Broad Street, Richmond, VA.</p>
      </article>
      <article class="card reveal" style="justify-content:center;text-align:center">
        <h3 style="font-size:1.1rem">Your event could be next</h3>
        <p>Invite Dr. Brehon to preach, teach, or lead a masterclass.</p>
        <div class="card-links" style="justify-content:center">
          <a class="btn btn-sm btn-gold" href="{LINKS[calendly_general]}" target="_blank" rel="noopener">Start the Conversation</a>
        </div>
      </article>
    </div>
  </div>
</section>
"""
