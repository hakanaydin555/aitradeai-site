/* AI Trade — site script (no cookies, no trackers) */
(function () {
  'use strict';
  var doc = document.documentElement;
  var pageLang = doc.getAttribute('lang') || 'en';

  function store(key, val) { try { if (val === undefined) return localStorage.getItem(key); localStorage.setItem(key, val); } catch (e) { return null; } }

  /* 1. Language: English for everyone; the TR link switches manually */
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

  /* 3b. Scroll-linked flow: process line, case dots, floating button */
  var plists = document.querySelectorAll('.plist');
  var fab = document.querySelector('.fab');
  var ticking = false;
  function onScroll() {
    ticking = false;
    var vh = window.innerHeight;
    plists.forEach(function (pl) {
      var r = pl.getBoundingClientRect();
      var p = Math.max(0, Math.min(1, (vh * 0.7 - r.top) / r.height));
      pl.style.setProperty('--p', reduce ? 1 : p.toFixed(3));
      pl.querySelectorAll('.prow').forEach(function (row) {
        row.classList.toggle('on', reduce || row.getBoundingClientRect().top < vh * 0.7);
      });
    });
    if (fab) {
      fab.classList.toggle('show', window.scrollY > vh * 0.6);
      var hideOn = document.querySelectorAll('#estimate .calc, #contact');
      var over = false;
      hideOn.forEach(function (el) { var r = el.getBoundingClientRect(); if (r.top < vh && r.bottom > vh - 120) over = true; });
      fab.classList.toggle('hide', over);
    }
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();
  var track = document.querySelector('.case-track');
  var dots = document.querySelectorAll('.case-dots span');
  if (track && dots.length) {
    track.addEventListener('scroll', function () {
      var cards = track.children, best = 0, bestD = Infinity;
      for (var i = 0; i < cards.length; i++) {
        var d = Math.abs(cards[i].getBoundingClientRect().left - track.getBoundingClientRect().left);
        if (d < bestD) { bestD = d; best = i; }
      }
      dots.forEach(function (dt, i) { dt.classList.toggle('on', i === best); });
    }, { passive: true });
  }

  /* 3c. Work carousel */
  document.querySelectorAll('[data-carousel]').forEach(function (box) {
    var track = box.querySelector('.work-track');
    var cards = track.children;
    var dots = box.querySelectorAll('.work-dots button');
    var prev = box.querySelector('.work-prev');
    var next = box.querySelector('.work-next');
    function current() {
      var best = 0, bestD = Infinity, left = track.getBoundingClientRect().left;
      for (var i = 0; i < cards.length; i++) {
        var d = Math.abs(cards[i].getBoundingClientRect().left - left - parseFloat(getComputedStyle(track).paddingLeft));
        if (d < bestD) { bestD = d; best = i; }
      }
      return best;
    }
    function update() {
      var i = track.scrollLeft + track.clientWidth >= track.scrollWidth - 5 ? cards.length - 1 : current();
      dots.forEach(function (d, j) { if (j === i) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current'); });
      if (prev) prev.disabled = track.scrollLeft < 5;
      if (next) next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 5;
    }
    function go(i) {
      i = Math.max(0, Math.min(cards.length - 1, i));
      track.scrollTo({ left: cards[i].offsetLeft - cards[0].offsetLeft, behavior: reduce ? 'auto' : 'smooth' });
    }
    dots.forEach(function (d, j) { d.addEventListener('click', function () { go(j); }); });
    if (prev) prev.addEventListener('click', function () { go(current() - 1); });
    if (next) next.addEventListener('click', function () { go(current() + 1); });
    track.addEventListener('scroll', function () { requestAnimationFrame(update); }, { passive: true });
    window.addEventListener('resize', update);
    update();
  });


  /* 3c2. Flow cards: play each card's animation only while it is visible */
  var flowCards = document.querySelectorAll('.flows .flow');
  if (flowCards.length && 'IntersectionObserver' in window) {
    var fio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { en.target.classList.toggle('play', en.isIntersecting); });
    }, { threshold: 0.55 });
    flowCards.forEach(function (c) { fio.observe(c); });
  } else { flowCards.forEach(function (c) { c.classList.add('play'); }); }

  /* 3d. Profit-leak estimator (all assumptions visible on the page) */
  document.querySelectorAll('[data-calc]').forEach(function (box) {
    var lang = box.getAttribute('data-lang');
    var loc = lang === 'tr' ? 'tr-TR' : 'en-US';
    var cuUrl = box.getAttribute('data-cu');
    var cta = box.querySelector('.cx-cta');
    var cur = { get value() { var r = box.querySelector('input[name="cur"]:checked'); return r ? r.value : ''; } };
    function num(name) {
      var el = box.querySelector('input[name="' + name + '"]');
      var v = String(el.value || '');
      if (el.getAttribute('data-kind') === 'money') v = v.replace(/[^\d]/g, '');
      else v = v.replace(',', '.').replace(/[^\d.]/g, '');
      var n = parseFloat(v);
      return isNaN(n) ? 0 : n;
    }
    function money(n, compact) {
      n = Math.round(n);
      if (compact && lang === 'tr') {
        var f1 = new Intl.NumberFormat(loc, { maximumFractionDigits: 1 });
        if (n >= 1e9) return cur.value + f1.format(n / 1e9) + ' milyar';
        if (n >= 1e6) return cur.value + f1.format(n / 1e6) + ' milyon';
        if (n >= 1e4) return cur.value + new Intl.NumberFormat(loc).format(Math.round(n / 1e3)) + ' bin';
        return cur.value + new Intl.NumberFormat(loc).format(n);
      }
      return cur.value + new Intl.NumberFormat(loc, compact ? { notation: 'compact', maximumFractionDigits: 1 } : { maximumFractionDigits: 0 }).format(n);
    }
    function range(a, b) { return money(a, true) + ' – ' + money(b, true); }
    function out(k, t) { var el = box.querySelector('[data-out="' + k + '"]'); if (el && el.textContent !== t) { el.textContent = t; el.classList.remove('cx-flash'); void el.offsetWidth; el.classList.add('cx-flash'); } }
    var fteH = parseFloat(box.getAttribute('data-fte')) || 40;
    var dayH = lang === 'tr' ? 9 : 8;
    var tDays = box.getAttribute('data-t-days'), tFte = box.getAttribute('data-t-fte'), tHours = box.getAttribute('data-t-hours');
    function mid(r) { return (r[0] + r[1]) / 2; }
    function calc() {
      var rev = num('rev'), ads = num('ads'), disc = Math.min(num('disc'), 100) / 100, ret = Math.min(num('ret'), 100) / 100,
          logi = Math.min(num('logi'), 100) / 100, hrs = num('hrs');
      var camp = [rev * disc * 0.015 * 12, rev * disc * 0.04 * 12];
      var ad = [ads * 0.05 * 12, ads * 0.12 * 12];
      var rets = [rev * ret * 0.10 * 0.15 * 12, rev * ret * 0.20 * 0.15 * 12];
      var lg = [rev * logi * 0.05 * 12, rev * logi * 0.10 * 12];
      var tot = [camp[0] + ad[0] + rets[0] + lg[0], camp[1] + ad[1] + rets[1] + lg[1]];
      out('camp', money(mid(camp), true)); out('ad', money(mid(ad), true)); out('rets', money(mid(rets), true)); out('logi', money(mid(lg), true));
      var segs = { camp: mid(camp), ad: mid(ad), logi: mid(lg), rets: mid(rets) };
      box.querySelectorAll('[data-seg]').forEach(function (el) { el.style.flexGrow = Math.max(segs[el.getAttribute('data-seg')], 0); });
      out('total', money(mid(tot), true));
      var tEl0 = box.querySelector('[data-out="total"]'); if (tEl0) tEl0.setAttribute('data-raw', mid(tot));
      out('range', range(tot[0], tot[1]));
      var wk = hrs * 0.5;
      var f1 = new Intl.NumberFormat(loc, { maximumFractionDigits: 1 });
      out('time', tHours.replace('{h}', f1.format(Math.round(wk))));
      out('eq', tDays.replace('{d}', f1.format(wk / dayH)) + ' · ' + tFte.replace('{f}', f1.format(wk / fteH)));
      box.querySelectorAll('[data-cur]').forEach(function (p) { p.textContent = cur.value; });
      var sum = lang === 'tr'
        ? 'Ciro ' + money(rev) + '/ay, reklam ' + money(ads) + '/ay, indirimli pay %' + num('disc') + ', iade %' + num('ret') + ', kargo/elleçleme %' + num('logi') + ', manuel iş ' + hrs + ' saat/hafta → tahmini kâr ≈' + money(mid(tot), true) + '/yıl (' + range(tot[0], tot[1]) + '), ≈' + Math.round(wk) + ' saat/hafta'
        : 'Revenue ' + money(rev) + '/mo, ads ' + money(ads) + '/mo, discounted ' + num('disc') + '%, returns ' + num('ret') + '%, shipping/fulfilment ' + num('logi') + '%, manual work ' + hrs + ' h/week → est. profit ≈' + money(mid(tot), true) + '/yr (' + range(tot[0], tot[1]) + '), ≈' + Math.round(wk) + ' h/week';
      if (cta) cta.href = cuUrl + '?calc=' + encodeURIComponent(sum);
    }
    box.querySelectorAll('input').forEach(function (el) {
      el.addEventListener('input', calc);
      if (el.getAttribute('data-kind') === 'money') el.addEventListener('blur', function () {
        var n = parseInt(String(el.value).replace(/[^\d]/g, ''), 10);
        el.value = isNaN(n) ? '' : new Intl.NumberFormat(loc).format(n);
      });
    });
    box.querySelectorAll('input[name="cur"]').forEach(function (r) { r.addEventListener('change', calc); });
    var outBox = box.querySelector('.cx-out'), go = box.querySelector('.cx-go');
    if (go) go.addEventListener('click', function () {
      calc();
      var first = outBox.classList.contains('pre');
      outBox.classList.remove('pre'); box.classList.add('done');
      var tEl = box.querySelector('[data-out="total"]');
      if (first && tEl && !reduce) {
        var target = parseFloat(tEl.getAttribute('data-raw')) || 0, t0 = null;
        (function step(t) { if (!t0) t0 = t; var k = Math.min((t - t0) / 900, 1); tEl.textContent = money(target * (1 - Math.pow(1 - k, 3)), true); if (k < 1) requestAnimationFrame(step); })(performance.now());
      }
      if (window.innerWidth < 861) outBox.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    });
    box.querySelectorAll('input[type="range"]').forEach(function (r) {
      var v = box.querySelector('[data-val="' + r.name + '"]');
      function show() { if (v) v.textContent = new Intl.NumberFormat(loc, { maximumFractionDigits: 1 }).format(parseFloat(r.value)); }
      r.addEventListener('input', show); show();
    });
    calc();
  });

  /* 4. Check-up form */
  var form = document.getElementById('checkup');
  if (!form) return;
  var steps = form.querySelectorAll('[data-step]');
  var bar = form.querySelector('.progress span');
  var label = form.querySelector('[data-steplabel]');
  var labelTpl = label ? label.getAttribute('data-steplabel') : 'Step {n} of {t}';
  var total = steps.length - 1; /* question + contact steps; last step is the thank-you screen */
  var backBtn = form.querySelector('.back:not(.restart)');
  var head = form.querySelector('.progress-wrap');
  var answers = {};
  var current = 0;
  var calcNote = '';
  try { calcNote = (new URLSearchParams(location.search).get('calc') || '').slice(0, 400); } catch (e) {}
  if (calcNote) { var cb = document.querySelector('.cu-calc'); if (cb) cb.classList.add('on'); var et = document.querySelector('.est-try'); if (et) et.hidden = true; }

  function show(i) {
    current = i;
    steps.forEach(function (s) { s.hidden = Number(s.getAttribute('data-step')) !== i; });
    var n = Math.min(i + 1, total);
    if (bar) bar.style.width = (n / total * 100) + '%';
    if (label) label.textContent = labelTpl.replace('{n}', n).replace('{t}', total);
    if (head) head.hidden = i >= total;
    if (backBtn) backBtn.hidden = !(i > 0 && i < total);
    var focusEl = steps[i] && steps[i].querySelector('h2');
    if (focusEl && i > 0) { focusEl.setAttribute('tabindex', '-1'); focusEl.focus({ preventScroll: true }); }
  }

  form.querySelectorAll('.opt').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var stepEl = btn.closest('[data-step]');
      var idx = Number(stepEl.getAttribute('data-step'));
      if (stepEl.hasAttribute('data-multi')) {
        btn.setAttribute('aria-pressed', btn.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
        var on = stepEl.querySelectorAll('.opt[aria-pressed="true"]');
        var a = [], ii = [];
        on.forEach(function (b) { a.push(b.textContent.trim()); ii.push(b.getAttribute('data-i')); });
        if (on.length) answers[idx] = { q: stepEl.getAttribute('data-q'), key: stepEl.getAttribute('data-key'), a: a.join(', '), i: ii.join(',') };
        else delete answers[idx];
        stepEl.querySelector('.multi-next').disabled = !on.length;
        return;
      }
      stepEl.querySelectorAll('.opt').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
      btn.setAttribute('aria-pressed', 'true');
      answers[idx] = { q: stepEl.getAttribute('data-q'), key: stepEl.getAttribute('data-key'), a: btn.textContent.trim(), i: btn.getAttribute('data-i') };
      setTimeout(function () { show(idx + 1); }, 180);
    });
  });
  form.querySelectorAll('.multi-next').forEach(function (b) {
    b.addEventListener('click', function () { show(Number(b.closest('[data-step]').getAttribute('data-step')) + 1); });
  });
  if (backBtn) backBtn.addEventListener('click', function () { show(Math.max(0, current - 1)); });

  function val(name) { var el = form.elements[name]; return el ? String(el.value || '').trim() : ''; }
  function mark(name, bad) { var el = form.elements[name]; if (el) el.closest('.field').classList.toggle('invalid', bad); }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var okName = val('name').length > 1;
    var mail = val('email').toLowerCase();
    var okMail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mail);
    var okWeb = /^[^\s]+\.[a-z]{2,}([\/?#][^\s]*)?$/i.test(val('website').replace(/^https?:\/\//i, ''));
    var okCompany = val('company').length > 1;
    var consent = form.elements.consent && form.elements.consent.checked;
    mark('name', !okName); mark('email', !okMail); mark('company', !okCompany); mark('website', !okWeb);
    var cbox = form.querySelector('.consent'); if (cbox) cbox.classList.toggle('invalid', !consent);
    if (!(okName && okMail && okCompany && okWeb && consent)) {
      var bad = form.querySelector('.field.invalid input'); if (bad) bad.focus();
      return;
    }
    if (val('website2')) { show(total); return; } /* honeypot: silently drop bots */

    var data = new URLSearchParams();
    data.append('lang', pageLang);
    data.append('page', location.pathname);
    Object.keys(answers).forEach(function (k) { data.append(answers[k].key, answers[k].a); data.append(answers[k].key + '_i', answers[k].i); });
    ['name', 'email', 'company', 'phone', 'website'].forEach(function (f) { data.append(f, val(f)); });
    data.append('note', val('note') + (calcNote ? (val('note') ? '\n\n' : '') + '[' + (pageLang === 'tr' ? 'Hesaplayıcı' : 'Calculator') + '] ' + calcNote : ''));

    var btn = form.querySelector('button[type="submit"]');
    var errBox = form.querySelector('.form-error');
    if (errBox) errBox.style.display = 'none';
    btn.disabled = true;

    var summary = form.querySelector('.summary-list');
    if (summary) {
      summary.innerHTML = '';
      Object.keys(answers).sort().forEach(function (k) {
        var p = document.createElement('p');
        p.textContent = answers[k].q.replace(/[?:]\s*$/, '') + ': ' + answers[k].a;
        summary.appendChild(p);
      });
    }

    var endpoint = window.AT_FORM_ENDPOINT;
    if (!endpoint) { btn.disabled = false; show(total); return; } /* preview mode */
    fetch(endpoint, { method: 'POST', mode: 'no-cors', body: data })
      .then(function () { show(total); })
      .catch(function () { if (errBox) errBox.style.display = 'block'; })
      .then(function () { btn.disabled = false; });
  });

  var restart = form.querySelector('.restart');
  if (restart) restart.addEventListener('click', function () {
    answers = {}; form.reset();
    form.querySelectorAll('.opt').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
    form.querySelectorAll('.multi-next').forEach(function (b) { b.disabled = true; });
    show(0);
  });

  show(0);
})();
