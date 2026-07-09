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
      <p style="color:var(--ink-soft)"><strong>All registration options close November 1, 2026.</strong></p>
      <div class="btn-row">
        <a class="btn btn-gold" href="{LINKS[eventbrite]}" target="_blank" rel="noopener">Reserve Now on Eventbrite</a>
      </div>
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
