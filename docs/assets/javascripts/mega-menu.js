/*
 * HMS Help — Mega-menu builder.
 *
 * Reads `window.HMS_NAV` (generated at build time from mkdocs.yml by
 * scripts/build-nav-data.py) and attaches a multi-column dropdown panel
 * to each top tab — works on every page, regardless of which tab is
 * currently lifted in the sidebar.
 */
(function () {
  function siteRoot() {
    // Detect the base URL prefix from any md-tabs__link, falling back to '/'
    const link = document.querySelector('.md-tabs__link, .md-header__title a');
    if (!link) return '/';
    try {
      const u = new URL(link.href);
      // Strip the last path segment so we get the project root
      const parts = u.pathname.split('/').filter(Boolean);
      // For project pages (mtsoft2.github.io/HMS-HELP/...), root is /HMS-HELP/
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
    const tabsList = document.querySelector('.md-tabs__list');
    if (!tabsList) return;
    const data = window.HMS_NAV;
    if (!Array.isArray(data)) return;

    const tabs = tabsList.querySelectorAll(':scope > .md-tabs__item');
    tabs.forEach((tab) => {
      if (tab.querySelector('.hms-mm')) return;
      const tabLink = tab.querySelector('.md-tabs__link');
      if (!tabLink) return;
      const label = (tabLink.textContent || '').trim();

      const node = data.find((d) => d.label === label);
      if (!node || !node.columns || node.columns.length === 0) return;

      const panel = document.createElement('div');
      panel.className = 'hms-mm';
      const grid = document.createElement('div');
      grid.className = 'hms-mm-grid';
      panel.appendChild(grid);

      node.columns.forEach((col) => {
        const colEl = document.createElement('div');
        colEl.className = 'hms-mm-col';
        if (col.label) {
          const t = document.createElement('span');
          t.className = 'hms-mm-col-title';
          t.textContent = col.label;
          colEl.appendChild(t);
        }
        const ul = document.createElement('ul');
        (col.items || []).forEach((leaf) => {
          const li = document.createElement('li');
          const a = document.createElement('a');
          a.href = abs(leaf.href);
          a.textContent = leaf.label;
          li.appendChild(a);
          ul.appendChild(li);
        });
        colEl.appendChild(ul);
        grid.appendChild(colEl);
      });

      tab.appendChild(panel);

      // Tap-to-open on touch devices
      tabLink.addEventListener('click', (e) => {
        if (window.matchMedia('(hover: none)').matches) {
          e.preventDefault();
          tab.classList.toggle('hms-mm-open');
        }
      });
    });

    // Close any open panel on outside click (touch)
    document.addEventListener('click', (e) => {
      document.querySelectorAll('.md-tabs__item.hms-mm-open').forEach((t) => {
        if (!t.contains(e.target)) t.classList.remove('hms-mm-open');
      });
    });
  }

  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(() => build());
  } else {
    document.addEventListener('DOMContentLoaded', build);
  }
})();
