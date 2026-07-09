BODY = """
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Contact</span>
    <h1>We'd love to <span class="script" style="font-size:1.05em">hear</span> from you</h1>
    <p>Questions, booking requests, prayer needs, or a story to share — every message is welcome.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid-3">
      <article class="card reveal">
        <div class="card-icon">{HEART_ICON}</div>
        <h3 style="font-size:1.25rem">Email the Ministry</h3>
        <p>The fastest way to reach Rev. Dr. Brehon for questions, media, speaking, and everything else.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-gold" href="mailto:barbara@favoredbythefather.com">barbara@favoredbythefather.com</a>
        </div>
      </article>
      <article class="card reveal">
        <div class="card-icon">{DOVE_ICON}</div>
        <h3 style="font-size:1.25rem">Prayer Requests</h3>
        <p>Share your prayer request and pray for others on the virtual prayer wall.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="{LINKS[prayer]}" target="_blank" rel="noopener">Make a Prayer Request</a>
        </div>
      </article>
      <article class="card reveal">
        <div class="card-icon">{MIC_ICON}</div>
        <h3 style="font-size:1.25rem">Book Time with Dr. Brehon</h3>
        <p>Appointments, book talks, podcast guests, and consultations — pick a time that works.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="{LINKS[calendly_general]}" target="_blank" rel="noopener">Make an Appointment</a>
        </div>
      </article>
      <article class="card reveal">
        <div class="card-icon">{BOOK_ICON}</div>
        <h3 style="font-size:1.25rem">Mentoring Sessions</h3>
        <p>Brookside virtual mentoring and Haven for Ravens sessions, in person or virtual.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="{LINKS[calendly_haven]}" target="_blank" rel="noopener">Schedule a Session</a>
        </div>
      </article>
      <article class="card reveal">
        <div class="card-icon">{PHONE_ICON}</div>
        <h3 style="font-size:1.25rem">Take Us Anywhere</h3>
        <p>Download the free ministry app — devotionals, prayer, Bible study, and more.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="{LINKS[ios]}" target="_blank" rel="noopener">iOS</a>
          <a class="btn btn-sm btn-outline-dark" href="{LINKS[android]}" target="_blank" rel="noopener">Android</a>
        </div>
      </article>
      <article class="card reveal">
        <div class="card-icon">{HEART_ICON}</div>
        <h3 style="font-size:1.25rem">Giving</h3>
        <p>Help us continually provide our virtual services. Any amount defrays monthly costs — we thank you in advance.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-gold" href="{LINKS[donate]}" target="_blank" rel="noopener">Make a Donation</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="panel-dark on-dark section-tight">
  <div class="container" style="text-align:center">
    <div class="section-head center reveal">
      <span class="eyebrow">Stay Connected</span>
      <h2>Follow the <span class="script" style="font-size:1.1em">journey</span></h2>
      <p>Sermons, podcasts, music playlists, and ministry updates.</p>
    </div>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-outline" href="{LINKS[youtube]}" target="_blank" rel="noopener">YouTube</a>
      <a class="btn btn-outline" href="{LINKS[fb_ministry]}" target="_blank" rel="noopener">Facebook</a>
      <a class="btn btn-outline" href="{LINKS[linkedin]}" target="_blank" rel="noopener">LinkedIn</a>
      <a class="btn btn-outline" href="{LINKS[linktree]}" target="_blank" rel="noopener">Linktree</a>
    </div>
  </div>
</section>
"""
