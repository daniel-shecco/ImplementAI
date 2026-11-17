// Mobile navigation
const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.nav-links');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
}

// Reveal on scroll
const io = 'IntersectionObserver' in window
  ? new IntersectionObserver(entries => entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: 0.12 })
  : null;
document.querySelectorAll('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('in'));

// Contact forms: no backend yet, so we open the visitor's mail client with the details pre-filled.
// To use a form service (e.g. Formspree, Netlify Forms), set data-endpoint on the <form>.
const CONTACT_EMAIL = 'hello@implementai.example';
document.querySelectorAll('form[data-contact]').forEach(form => {
  form.addEventListener('submit', async e => {
    e.preventDefault();
    const data = new FormData(form);
    const success = form.querySelector('.form-success');
    const endpoint = form.dataset.endpoint;

    if (endpoint) {
      try {
        const res = await fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
        if (!res.ok) throw new Error();
        form.reset();
        if (success) success.style.display = 'block';
        return;
      } catch { /* fall through to mailto */ }
    }

    const lines = [];
    for (const [k, v] of data.entries()) if (k !== 'consent' && v) lines.push(`${k}: ${v}`);
    const subject = encodeURIComponent(form.dataset.subject || 'Enquiry via website');
    window.location.href = `mailto:${CONTACT_EMAIL}?subject=${subject}&body=${encodeURIComponent(lines.join('\n'))}`;
    if (success) success.style.display = 'block';
  });
});

document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
