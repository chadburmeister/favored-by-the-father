// Favored by the Father Ministries — shared behavior
(function () {
  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Mark current page in nav
  var path = location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.main-nav a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (!href) return;
    var clean = href.replace('.html', '').replace(/\/$/, '');
    if (clean === '' || clean === 'index') clean = '/';
    if (clean.charAt(0) !== '/') clean = '/' + clean;
    if (clean === path || (path === '/' && clean === '/')) {
      if (!a.classList.contains('nav-cta')) a.setAttribute('aria-current', 'page');
    }
  });

  // Reveal on scroll
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('visible'); });
  }

  // Current year in footer
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();

// Countdown chips — <element data-countdown="YYYY-MM-DD"> shows whole days remaining
(function () {
  var els = document.querySelectorAll('[data-countdown]');
  for (var i = 0; i < els.length; i++) {
    var el = els[i];
    var target = new Date(el.getAttribute('data-countdown') + 'T23:59:59-05:00');
    var days = Math.ceil((target.getTime() - Date.now()) / 86400000);
    if (days > 0) {
      el.textContent = days + (days === 1 ? ' day' : ' days');
    } else {
      var wrap = el.closest ? el.closest('[data-countdown-wrap]') : null;
      if (wrap) wrap.style.display = 'none';
      else el.textContent = 'almost no time';
    }
  }
})();
