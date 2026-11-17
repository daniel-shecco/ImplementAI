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
    const fmt = n => '€' + Math.round(n).toLocaleString('en-US');
    const run = () => {
      // Assumption: AI assistant recovers ~60% of missed enquiries and saves ~60% of admin hours.
      const recovered = calls.value * 0.6 * value.value * 52 / 12;
      const saved = hours.value * 0.6;
      lbl('calls').textContent = calls.value;
      lbl('value').textContent = fmt(value.value);
      lbl('hours').textContent = hours.value + ' h';
      out.textContent = fmt(recovered);
      outH.textContent = Math.round(saved * 4.3) + ' h';
    };
    [calls, value, hours].forEach(i => i.addEventListener('input', run)); run();
  });

  // Forms: mailto fallback until a form backend is configured via data-endpoint.
  const EMAIL = 'hello@implementai.example';
  $$('form[data-contact]').forEach(form => form.addEventListener('submit', async e => {
    e.preventDefault();
    const data = new FormData(form), ok = $('.form-ok', form);
    if (form.dataset.endpoint) {
      try {
        const r = await fetch(form.dataset.endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
        if (r.ok) { form.reset(); if (ok) ok.hidden = false; return; }
      } catch {}
    }
    const body = [...data.entries()].filter(([k, v]) => k !== 'consent' && v).map(([k, v]) => `${k}: ${v}`).join('\n');
    location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(form.dataset.subject || 'Website enquiry')}&body=${encodeURIComponent(body)}`;
    if (ok) ok.hidden = false;
  }));

  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
