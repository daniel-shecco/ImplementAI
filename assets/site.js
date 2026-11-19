// Shared behaviour for the design mockups: nav, reveal-on-scroll, tabs, ROI calculator, forms.
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // Mobile nav
  const toggle = $('.nav-toggle'), menu = $('.nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', () => toggle.setAttribute('aria-expanded', String(menu.classList.toggle('open'))));
    $$('a', menu).forEach(a => a.addEventListener('click', () => menu.classList.remove('open')));
  }

  // Header shadow on scroll
  const header = $('.header');
  const onScroll = () => header && header.classList.toggle('scrolled', scrollY > 12);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Reveal
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    $$('.reveal').forEach(el => io.observe(el));
  } else $$('.reveal').forEach(el => el.classList.add('in'));

  // Tabs
  $$('[data-tabs]').forEach(root => {
    const tabs = $$('[role="tab"]', root), panels = $$('[role="tabpanel"]', root);
    tabs.forEach((t, i) => t.addEventListener('click', () => {
      tabs.forEach((x, j) => x.setAttribute('aria-selected', String(i === j)));
      panels.forEach((p, j) => p.hidden = i !== j);
    }));
  });

  // ROI calculator
  $$('[data-roi]').forEach(root => {
    const calls = $('[name="calls"]', root), value = $('[name="value"]', root), hours = $('[name="hours"]', root);
    const out = $('[data-roi-out]', root), outH = $('[data-roi-hours]', root);
    const lbl = n => $(`[data-for="${n}"]`, root);
    const de = (document.documentElement.lang || '').startsWith('de');
    const group = n => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, de ? '.' : ',');
    const fmt = n => de ? '€ ' + group(n) : '€' + group(n);
    const hrs = n => Math.round(n) + (de ? ' Std.' : ' h');
    const run = () => {
      // Assumption: AI assistant recovers ~60% of missed enquiries and saves ~60% of admin hours.
      const recovered = calls.value * 0.6 * value.value * 52 / 12;
      const saved = hours.value * 0.6;
      lbl('calls').textContent = calls.value;
      lbl('value').textContent = fmt(value.value);
      lbl('hours').textContent = hrs(hours.value);
      out.textContent = fmt(recovered);
      outH.textContent = hrs(saved * 4.3);
    };
    [calls, value, hours].forEach(i => i.addEventListener('input', run)); run();
  });

  // Forms: sent to the Google Apps Script web app (operations/apps-script/Code.gs), which writes them
  // into the "ImplementAI – Pilot applications" Google Sheet and sends the confirmation email.
  // Until FORM_ENDPOINT is set, or if sending fails, the visitor's email app opens instead.
  const FORM_ENDPOINT = '';               // Apps Script web app URL (.../exec), see operations/SETUP.md
  const EMAIL = 'hello@implementai.example';
  const utm = new URLSearchParams(location.search);
  $$('form[data-contact]').forEach(form => form.addEventListener('submit', async e => {
    e.preventDefault();
    const data = new FormData(form), ok = $('.form-ok', form), btn = $('button[type="submit"]', form);
    const endpoint = form.dataset.endpoint || FORM_ENDPOINT;
    if (endpoint) {
      const params = new URLSearchParams(data);
      params.set('form', form.dataset.form || 'contact');
      params.set('lang', document.documentElement.lang || 'en');
      params.set('page', location.pathname.split('/').pop() || 'index.html');
      ['utm_source', 'utm_medium', 'utm_campaign'].forEach(k => utm.get(k) && params.set(k, utm.get(k)));
      if (btn) btn.disabled = true;
      try {
        // Apps Script sends no CORS headers, so the response is opaque; only a network error means failure.
        await fetch(endpoint, { method: 'POST', mode: 'no-cors', body: params });
        form.reset();
        if (ok) { ok.textContent = ok.dataset.sent || ok.textContent; ok.hidden = false; }
        return;
      } catch { /* fall back to email below */ }
      finally { if (btn) btn.disabled = false; }
    }
    const body = [...data.entries()].filter(([k, v]) => !['consent', 'website'].includes(k) && v).map(([k, v]) => `${k}: ${v}`).join('\n');
    location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(form.dataset.subject || 'Website enquiry')}&body=${encodeURIComponent(body)}`;
    if (ok) ok.hidden = false;
  }));

  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
