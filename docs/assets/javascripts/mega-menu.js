/*
 * HMS Help — single "Modules ▾" dropdown that replaces the top tabs.
 *
 * Reads `window.HMS_NAV` (generated at build time from mkdocs.yml by
 * scripts/build-nav-data.py) and builds ONE dropdown trigger inside the
 * existing .md-tabs row. Clicking opens a wide multi-column panel that
 * lists every top-level section's pages.
 */
(function () {
  function siteRoot() {
    const link = document.querySelector('.md-tabs__link, .md-header__title a');
    if (!link) return '/';
    try {
      const u = new URL(link.href);
      const parts = u.pathname.split('/').filter(Boolean);
      if (parts.length === 0) return '/';
      return '/' + parts[0] + '/';
    } catch (e) {
      return '/';
    }
  }

  function abs(href) {
    if (!href) return '#';
    if (/^https?:/i.test(href)) return href;
    const root = siteRoot();
    return (root + href.replace(/^\//, '')).replace(/\/{2,}/g, '/');
  }

  function build() {
    // Material renders <nav class="md-tabs"><div class="md-grid"><ul class="md-tabs__list">…
    // Anchor inside the .md-grid so our button picks up the page's content
    // width and respects the left/right gutters.
    const tabs = document.querySelector('.md-tabs');
    if (!tabs) return;
    const grid = tabs.querySelector('.md-grid') || tabs;
    const data = window.HMS_NAV;
    if (!Array.isArray(data)) return;

    // Avoid rebuilding on instant-load page changes
    if (tabs.querySelector('.hms-mm-wrap')) return;

    // Wrapper holds the button + the absolutely-positioned panel
    const wrap = document.createElement('div');
    wrap.className = 'hms-mm-wrap';

    // The trigger button
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'hms-mm-trigger';
    btn.setAttribute('aria-haspopup', 'true');
    btn.setAttribute('aria-expanded', 'false');
    btn.innerHTML = '<span>☰ Modules</span><span class="hms-caret">▼</span>';
    wrap.appendChild(btn);

    // The panel
    const panel = document.createElement('div');
    panel.className = 'hms-mm-panel';
    const sections = document.createElement('div');
    sections.className = 'hms-mm-sections';
    panel.appendChild(sections);
    wrap.appendChild(panel);

    // Build each top-level section as a column
    data.forEach((node) => {
      // Skip "Home" — it has no children
      const isHome = (node.label || '').toLowerCase() === 'home';
      if (isHome && (!node.columns || node.columns.length === 0)) return;

      const sec = document.createElement('div');
      sec.className = 'hms-mm-section';

      // Section title — links to first leaf if available
      const firstLeaf = (node.columns || [])
        .flatMap((c) => c.items || [])
        .find((x) => x && x.href);
      let titleEl;
      if (firstLeaf) {
        titleEl = document.createElement('a');
        titleEl.href = abs(firstLeaf.href);
        titleEl.className = 'hms-mm-section-title is-link';
      } else {
        titleEl = document.createElement('span');
        titleEl.className = 'hms-mm-section-title';
      }
      titleEl.textContent = node.label;
      sec.appendChild(titleEl);

      // If the section has columns (sub-groups), render them.
      // Flatten — all leaves under one ul, with sub-group titles in between.
      (node.columns || []).forEach((col) => {
        if (col.label) {
          const sg = document.createElement('span');
          sg.className = 'hms-mm-subgroup-title';
          sg.textContent = col.label;
          sec.appendChild(sg);
        }
        const ul = document.createElement('ul');
        (col.items || []).forEach((leaf) => {
          const li = document.createElement('li');
          const a = document.createElement('a');
          a.href = abs(leaf.href);
          a.className = 'hms-mm-link';
          a.textContent = leaf.label;
          li.appendChild(a);
          ul.appendChild(li);
        });
        if (ul.childNodes.length) sec.appendChild(ul);
      });

      sections.appendChild(sec);
    });

    // Backdrop for outside-click close
    const backdrop = document.createElement('div');
    backdrop.className = 'hms-mm-backdrop';
    document.body.appendChild(backdrop);

    function open() {
      panel.classList.add('is-open');
      backdrop.classList.add('is-open');
      btn.classList.add('is-open');
      btn.setAttribute('aria-expanded', 'true');
    }
    function close() {
      panel.classList.remove('is-open');
      backdrop.classList.remove('is-open');
      btn.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
    }
    function toggle() {
      if (panel.classList.contains('is-open')) close(); else open();
    }
    btn.addEventListener('click', (e) => { e.stopPropagation(); toggle(); });
    backdrop.addEventListener('click', close);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') close();
    });
    panel.addEventListener('click', (e) => {
      // close on link click (so navigation feels snappy)
      if (e.target.closest('a')) close();
    });

    // Insert wrapper at the start of the grid (so it lines up with content).
    grid.insertBefore(wrap, grid.firstChild);
  }

  // Try every path so we don't miss the initial load:
  //   - document$ is a one-shot in some Material versions, so we ALSO call
  //     build() directly via DOMContentLoaded or immediately if already past.
  if (window.document$ && typeof window.document$.subscribe === 'function') {
    try { window.document$.subscribe(() => build()); } catch (e) {}
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    // DOM already parsed — schedule for the next tick so Material's tab DOM
    // has finished rendering before we look for .md-tabs.
    setTimeout(build, 0);
  }
})();
