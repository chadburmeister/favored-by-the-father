BODY = """
<!-- HERO -->
<section class="hero on-dark">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">A Church Without Walls &middot; Est. 2003</span>
      <h1>Favored <span class="script" style="font-size:0.85em">by the</span> Father <span style="display:block;font-size:0.55em;letter-spacing:0.04em;margin-top:0.3rem;color:var(--lavender)">Ministries</span></h1>
      <p class="lede">Nurturing souls and empowering individuals to grow. Through digital discipleship and fellowship, we help you — and the ministry you serve — increase effectiveness for Kingdom building.</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="#devotional">Get the Free Daily Devotional</a>
        <a class="btn btn-outline" href="{LINKS[podcast_playlist]}" target="_blank" rel="noopener">Listen to the Podcast</a>
        <a class="btn btn-outline" href="/events#bible-institute">Bible Institute</a>
      </div>
      <p class="hero-verse">"Grow in the grace and knowledge of our Lord and Savior Jesus Christ." <br><strong>— 2 Peter 3:18 NLT</strong></p>
    </div>
    <div class="hero-portrait reveal">
      <img src="{IMG[portrait_hat]}" alt="Rev. Dr. Barbara A. F. Brehon" width="800" height="800">
    </div>
  </div>
</section>

<!-- WHAT WE DO -->
<section>
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">What We Do</span>
      <h2>Every season of your walk, <span class="script" style="font-size:1.1em">nurtured</span></h2>
      <p>From daily devotionals in your pocket to sacred one-on-one mentoring, every ministry stream flows toward one purpose: helping you grow your relationship with the Lord and with others.</p>
    </div>
    <div class="grid-3">
      <article class="card reveal">
        <div style="height:150px;display:flex;align-items:center;justify-content:center;margin-bottom:1.2rem;background:linear-gradient(135deg,var(--lavender-soft),rgba(201,182,228,0.3));border-radius:12px">
          <img src="{IMG[app_icon]}" alt="Favored by the Father app icon" style="height:110px;width:110px;border-radius:24px;box-shadow:var(--shadow-md)" loading="lazy">
        </div>
        <h3>Digital Discipleship App</h3>
        <p>A free download designed to connect, engage, and help you grow from wherever you are — daily devotionals, prayer requests, Bible study, multiple Bible versions, and more.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="{LINKS[ios]}" target="_blank" rel="noopener">iOS</a>
          <a class="btn btn-sm btn-outline-dark" href="{LINKS[android]}" target="_blank" rel="noopener">Android</a>
        </div>
      </article>
      <article class="card reveal">
        <div style="display:flex;gap:0.5rem;margin-bottom:1.2rem;height:150px;border-radius:12px;overflow:hidden">
          <img src="{IMG[b_home_cover]}" alt="Start at Home book cover" style="flex:1;min-width:0;height:100%;object-fit:cover;border-radius:8px" loading="lazy">
          <img src="{IMG[b_ella_cover]}" alt="Ella's Perspectives book cover" style="flex:1;min-width:0;height:100%;object-fit:cover;border-radius:8px" loading="lazy">
          <img src="{IMG[b_points3_cover]}" alt="Points to Ponder Volume 3 cover" style="flex:1;min-width:0;height:100%;object-fit:cover;border-radius:8px" loading="lazy">
          <img src="{IMG[church_hurt]}" alt="Perspectives on Church Hurt cover" style="flex:1;min-width:0;height:100%;object-fit:cover;border-radius:8px" loading="lazy">
        </div>
        <h3>Books &amp; Resources</h3>
        <p>Bestselling books, devotionals, and workbooks — plus ministry consultants available for mini masterclasses, book talks, preaching, teaching, seminars, webinars, and podcasts.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="/books">Browse the Books</a>
          <a class="btn btn-sm btn-outline-dark" href="{LINKS[calendly_general]}" target="_blank" rel="noopener">Make a Request</a>
        </div>
      </article>
      <article class="card reveal">
        <div style="border-radius:12px;overflow:hidden;margin-bottom:1.2rem;height:150px">
          <img src="{IMG[music_singles]}" alt="Favored by the Father Singles Collection — songs born in prayer, teaching, and revelation" style="width:100%;height:100%;object-fit:cover" loading="lazy">
        </div>
        <h3>Music Inspired by Ministry</h3>
        <p>Experience the journey from page to melody. <em>Here, in the Becoming</em> — a landmark album inspired by Dr. Brehon's books — guides, comforts, and inspires through life's seasons.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="/podcast#music">Explore the Music</a>
        </div>
      </article>
      <article class="card reveal">
        <div style="border-radius:12px;overflow:hidden;margin-bottom:1.2rem;height:150px">
          <img src="{IMG[season5]}" alt="UNBOXED on Purpose Podcast — Season 5" style="width:100%;height:100%;object-fit:cover" loading="lazy">
        </div>
        <h3>UNBOXED on Purpose Podcast</h3>
        <p>Real, unfiltered conversations that inspire deeper faith, self-discovery, and the courage to walk boldly in your God-gifted purpose.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="/podcast">About the Podcast</a>
          <a class="btn btn-sm btn-outline-dark" href="{LINKS[podcast_playlist]}" target="_blank" rel="noopener">View Episodes</a>
        </div>
      </article>
      <article class="card reveal">
        <div style="border-radius:12px;overflow:hidden;margin-bottom:1.2rem;height:150px">
          <img src="{IMG[brookside]}" alt="Brookside — A Sacred Haven" style="width:100%;height:100%;object-fit:cover" loading="lazy">
        </div>
        <h3>Mentoring &amp; Sacred Spaces</h3>
        <p>Brookside virtual mentoring and Haven for Ravens — safe, confidential spaces where those who feed others can breathe and be nurtured themselves.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="/mentoring">Find Your Haven</a>
        </div>
      </article>
      <article class="card reveal">
        <div style="height:150px;display:flex;align-items:center;justify-content:center;margin-bottom:1.2rem;background:var(--ivory-warm);border-radius:12px">
          <img src="{IMG[prayer_logo]}" alt="Community of Prayer Circle logo" style="height:120px;width:120px;object-fit:contain" loading="lazy">
        </div>
        <h3>Community of Prayer</h3>
        <p>Sincere prayer is the purest way to converse with God. Open your heart, share your prayer request, and pray for others on our virtual wall.</p>
        <div class="card-links">
          <a class="btn btn-sm btn-royal" href="{LINKS[prayer]}" target="_blank" rel="noopener">Make a Prayer Request</a>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- SCRIPTURE BAND -->
<section class="panel-dark section-tight on-dark">
  <div class="container">
    <blockquote class="scripture">
      "Be transformed by the renewing of your mind."
      <cite>Romans 12:2</cite>
    </blockquote>
  </div>
</section>

<!-- FREE 7-DAY DEVOTIONAL -->
<section class="leadmagnet" id="devotional">
  <div class="container">
    <div class="leadmagnet-card reveal">
      <div class="leadmagnet-cover">
        <img src="{IMG[points1]}" alt="Points to Ponder — Daily Devotionals and Journaling book cover" loading="lazy">
      </div>
      <div>
        <span class="eyebrow">Free Gift</span>
        <h2>Begin with 7 days of <span class="script" style="font-size:1.1em">grace</span></h2>
        <p style="color:var(--ink-soft)">Receive a free 7-day devotional excerpt from <em>Points to Ponder: Daily Devotionals and Journaling</em> — one scripture-centered reading and journaling prompt each morning, delivered to your inbox.</p>
        <ul class="leadmagnet-list">
          <li>Seven daily readings drawn from the bestselling devotional</li>
          <li>A reflection prompt to journal with the Lord each day</li>
          <li>A gentle on-ramp to the full Points to Ponder journey</li>
        </ul>
        <div class="btn-row" style="margin-top:0">
          <a class="btn btn-gold" href="mailto:info@favoredbythefather.com?subject=Please%20send%20my%20free%207-Day%20Devotional&amp;body=Hi%2C%0A%0APlease%20send%20the%20free%207-day%20devotional%20excerpt%20from%20Points%20to%20Ponder%20to%20this%20email%20address.%0A%0A%28Sent%20from%20favoredbythefather.com%29">Send Me the Devotional</a>
          <a class="btn btn-outline-dark" href="/books">Explore the Full Book</a>
        </div>
        <p style="font-size:0.8rem;color:var(--ink-soft);margin-top:1rem">One email with your 7-day excerpt — no spam, ever.</p>
      </div>
    </div>
  </div>
</section>

<!-- FEATURED: NEW RELEASE -->
<section>
  <div class="container grid-2" style="align-items:center">
    <div class="media-frame reveal">
      <img src="{IMG[church_hurt]}" alt="Perspectives on Church Hurt book cover" loading="lazy">
    </div>
    <div class="reveal">
      <span class="eyebrow">Available Now</span>
      <h2>Perspectives on Church&nbsp;Hurt</h2>
      <p style="color:var(--ink-soft)">Grounded in a nationwide survey on the profound impact of church hurt, this compassionate, scripture-centered framework helps restore trust, foster spiritual growth, and rebuild deep intimacy with the Lord. Perfect for personal reflection, leadership development, or small groups — with a hands-on companion workbook, <em>Mending the Masterpiece</em>.</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="{LINKS[b_church_hurt]}" target="_blank" rel="noopener">Get the Book</a>
        <a class="btn btn-outline-dark" href="{LINKS[b_mending]}" target="_blank" rel="noopener">Companion Workbook</a>
        <a class="btn btn-outline-dark" href="/books">All Books</a>
      </div>
    </div>
  </div>
</section>

<!-- MEET DR. BREHON -->
<section class="panel-warm">
  <div class="container grid-2" style="align-items:center">
    <div class="reveal">
      <span class="eyebrow">Visionary Servant Leader</span>
      <h2>Rev. Dr. Barbara A. F. Brehon</h2>
      <p>A spiritual bodybuilder, pastor, preacher, teacher, mentor, bestselling author, podcaster, lyricist, song producer, and public speaker — driven by a deep passion for guiding others toward healing, purpose, and spiritual growth.</p>
      <div class="badge-row">
        <span class="badge">Pastor</span><span class="badge">Bestselling Author</span><span class="badge">Podcaster</span><span class="badge">Mentor</span><span class="badge">Lyricist</span>
      </div>
      <div class="btn-row">
        <a class="btn btn-gold" href="/about">Her Story &amp; Our Beliefs</a>
      </div>
    </div>
    <div class="glass reveal">
      <blockquote class="scripture" style="margin:0;text-align:left">
        "Jesus grew in wisdom and in stature and in favor with God and all the people."
        <cite style="text-align:left">Luke 2:52 NLT — Our Mission's Foundation</cite>
      </blockquote>
    </div>
  </div>
</section>

<!-- UPCOMING EVENT -->
<section>
  <div class="container grid-2" style="align-items:center">
    <div class="reveal">
      <span class="eyebrow">Events 2026</span>
      <h2>3rd Annual Fall <span class="script" style="font-size:1.1em">Spiritual</span> Retreat</h2>
      <p style="color:var(--ink-soft)"><strong>November 5–6, 2026 · Thursday–Friday</strong><br>Williamsburg Christian Retreat Center<br>9275 Barnes Road, Toano, VA 23168</p>
      <p style="color:var(--ink-soft)">A getaway of spiritual teaching, meditation, and connection with nature — designed to provide respite and nurture for those who constantly pour into others. Space is limited and the early-bird phase has already sold out.</p>
      <p data-countdown-wrap style="margin:1.2rem 0 0"><span class="countdown-chip">Registration closes Nov 1 — <strong data-countdown="2026-11-01">limited time</strong> left</span></p>
      <div class="btn-row">
        <a class="btn btn-gold" href="{LINKS[eventbrite]}" target="_blank" rel="noopener">Reserve Your Place</a>
        <a class="btn btn-outline-dark" href="/events">All Events &amp; Masterclasses</a>
      </div>
    </div>
    <div class="media-frame reveal">
      <img src="{IMG[retreat]}" alt="3rd Annual Fall Spiritual Retreat 2026 flyer" loading="lazy">
    </div>
  </div>
</section>

<!-- TESTIMONIAL TEASER -->
<section class="section-tight" style="background:var(--ivory-warm)">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Voices of Transformation</span>
      <h2>"A safe place to be encouraged and uplifted"</h2>
      <p>Hear from those who found healing, renewal, and clarity through the Haven — then share your own journey.</p>
      <div class="btn-row" style="justify-content:center">
        <a class="btn btn-royal" href="/testimonials">Read the Testimonials</a>
      </div>
    </div>
  </div>
</section>
"""
