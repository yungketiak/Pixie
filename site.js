/* PIXIE³ — shared behaviour */

// theme toggle (light ⇄ dark)
const themeBtn = document.querySelector('.theme-toggle');
function applyTheme(t) {
  document.documentElement.setAttribute('data-theme', t);
  if (themeBtn) {
    themeBtn.textContent = t === 'dark' ? '☀' : '☾';
    themeBtn.setAttribute('aria-label', t === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
  }
  try { localStorage.setItem('pixie-theme', t); } catch (e) {}
}
if (themeBtn) {
  themeBtn.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    applyTheme(cur === 'dark' ? 'light' : 'dark');
  });
  // sync button glyph with theme set by the head snippet
  applyTheme(document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light');
}

// mobile menu toggle
const toggle = document.querySelector('.nav-toggle');
const menu = document.querySelector('.nav-links');
if (toggle && menu) {
  toggle.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

// scroll-reveal
const reveals = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window && reveals.length) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  reveals.forEach((el, i) => {
    el.style.transitionDelay = `${(i % 4) * 0.08}s`;
    io.observe(el);
  });
} else {
  reveals.forEach(el => el.classList.add('in'));
}
