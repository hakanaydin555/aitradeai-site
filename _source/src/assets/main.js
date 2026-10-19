/* AI Trade — site script (no cookies, no trackers) */
(function () {
  'use strict';
  var doc = document.documentElement;
  var pageLang = doc.getAttribute('lang') || 'en';

  function store(key, val) { try { if (val === undefined) return localStorage.getItem(key); localStorage.setItem(key, val); } catch (e) { return null; } }

  /* 1. Language: first visit to an English page from Turkey -> Turkish */
  var alt = document.querySelector('a[data-setlang="tr"]');
  if (pageLang === 'en' && alt && !store('at-lang')) {
    var langs = (navigator.languages || [navigator.language || '']).join(',').toLowerCase();
    var tz = '';
    try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch (e) {}
    if (/(^|,)tr/.test(langs) || tz === 'Europe/Istanbul') {
      location.replace(alt.getAttribute('href') + location.hash);
      return;
    }
  }
  document.querySelectorAll('[data-setlang]').forEach(function (a) {
    a.addEventListener('click', function () { store('at-lang', a.getAttribute('data-setlang')); });
  });

  /* 2. Mobile menu */
  var menuBtn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('a.navlink').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); });
    });
  }

  /* 3. Reveal on scroll, leak map loop, counters */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function countUp(el) {
    var end = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    if (reduce || !end) { el.textContent = end + suffix; return; }
    var t0 = null, dur = 1200;
    function step(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      var v = Math.round(end * (1 - Math.pow(1 - p, 3)));
      el.textContent = v.toLocaleString('en-US') + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var watched = document.querySelectorAll('.reveal, .stagger, .leakmap, [data-count]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        if (el.hasAttribute('data-count')) countUp(el); else el.classList.add('in');
        io.unobserve(el);
      });
    }, { threshold: 0.2 });
    watched.forEach(function (el) { io.observe(el); });
  } else {
    watched.forEach(function (el) { el.classList.add('in'); });
  }

  /* 4. Check-up form */
  var form = document.getElementById('checkup');
  if (!form) return;
  var steps = form.querySelectorAll('[data-step]');
  var bar = form.querySelector('.progress span');
  var label = form.querySelector('[data-steplabel]');
  var labelTpl = label ? label.getAttribute('data-steplabel') : 'Step {n} of 5';
  var backBtn = form.querySelector('.back');
  var head = form.querySelector('.progress-wrap');
  var answers = {};
  var current = 0;

  function show(i) {
    current = i;
    steps.forEach(function (s) { s.hidden = Number(s.getAttribute('data-step')) !== i; });
    var n = Math.min(i + 1, 5);
    if (bar) bar.style.width = (n * 20) + '%';
    if (label) label.textContent = labelTpl.replace('{n}', n);
    if (head) head.hidden = i >= 5;
    if (backBtn) backBtn.hidden = !(i > 0 && i < 5);
    var focusEl = steps[i] && steps[i].querySelector('h2');
    if (focusEl && i > 0) { focusEl.setAttribute('tabindex', '-1'); focusEl.focus({ preventScroll: true }); }
  }

  form.querySelectorAll('.opt').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var stepEl = btn.closest('[data-step]');
      var idx = Number(stepEl.getAttribute('data-step'));
      stepEl.querySelectorAll('.opt').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
      btn.setAttribute('aria-pressed', 'true');
      answers[idx] = { q: stepEl.getAttribute('data-q'), key: stepEl.getAttribute('data-key'), a: btn.textContent.trim() };
      setTimeout(function () { show(idx + 1); }, 180);
    });
  });
  if (backBtn) backBtn.addEventListener('click', function () { show(Math.max(0, current - 1)); });

  function val(name) { var el = form.elements[name]; return el ? String(el.value || '').trim() : ''; }
  function mark(name, bad) { var el = form.elements[name]; if (el) el.closest('.field').classList.toggle('invalid', bad); }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var okName = val('name').length > 1;
    var okMail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val('email'));
    var okCompany = val('company').length > 1;
    var consent = form.elements.consent && form.elements.consent.checked;
    mark('name', !okName); mark('email', !okMail); mark('company', !okCompany);
    var cbox = form.querySelector('.consent'); if (cbox) cbox.classList.toggle('invalid', !consent);
    if (!(okName && okMail && okCompany && consent)) return;
    if (val('website2')) { show(5); return; } /* honeypot: silently drop bots */

    var data = new URLSearchParams();
    data.append('lang', pageLang);
    data.append('page', location.pathname);
    Object.keys(answers).forEach(function (k) { data.append(answers[k].key, answers[k].a); });
    ['name', 'email', 'company', 'phone', 'note'].forEach(function (f) { data.append(f, val(f)); });

    var btn = form.querySelector('button[type="submit"]');
    var errBox = form.querySelector('.form-error');
    if (errBox) errBox.style.display = 'none';
    btn.disabled = true;

    var summary = form.querySelector('.summary-list');
    if (summary) {
      summary.innerHTML = '';
      Object.keys(answers).sort().forEach(function (k) {
        var p = document.createElement('p');
        p.textContent = answers[k].q + ': ' + answers[k].a;
        summary.appendChild(p);
      });
    }

    var endpoint = window.AT_FORM_ENDPOINT;
    if (!endpoint) { btn.disabled = false; show(5); return; } /* preview mode */
    fetch(endpoint, { method: 'POST', mode: 'no-cors', body: data })
      .then(function () { show(5); })
      .catch(function () { if (errBox) errBox.style.display = 'block'; })
      .then(function () { btn.disabled = false; });
  });

  var restart = form.querySelector('.restart');
  if (restart) restart.addEventListener('click', function () {
    answers = {}; form.reset();
    form.querySelectorAll('.opt').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
    show(0);
  });

  show(0);
})();
