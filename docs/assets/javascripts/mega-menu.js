/*
 * HMS Help — Mega-menu builder.
 *
 * On every page load, for each top-level tab in `.md-tabs__list`, find the
 * corresponding section in the in-page nav drawer (`.md-sidebar--primary
 * .md-nav__list`) and clone its second-level structure into a dropdown
 * panel anchored under the tab.
 *
 * No build-time changes needed — works against the standard Material
 * navigation output.
 */
(function () {
  function build() {
    const tabsList = document.querySelector('.md-tabs__list');
    if (!tabsList) return; // tabs hidden (mobile) — nothing to do

    // Sidebar nav — Material renders the full nav tree here at every page.
    const sidebar = document.querySelector('.md-sidebar--primary .md-nav--primary > .md-nav__list');
    if (!sidebar) return;

    const tabs = tabsList.querySelectorAll(':scope > .md-tabs__item');

    tabs.forEach((tab) => {
      // Skip if we already built one for this tab
      if (tab.querySelector('.hms-mm')) return;

      const tabLink = tab.querySelector('.md-tabs__link');
      if (!tabLink) return;
      const label = (tabLink.textContent || '').trim();

      // Locate the matching top-level <li> in the sidebar by visible label.
      const sideItems = sidebar.querySelectorAll(':scope > .md-nav__item');
      let match = null;
      sideItems.forEach((li) => {
        const itemLabel =
          (li.querySelector(':scope > label, :scope > a')?.textContent || '').trim();
        if (itemLabel === label) match = li;
      });
      if (!match) return;

      // Pull the nested nav (level-2 + level-3 lists)
      const nestedNav = match.querySelector(':scope > nav.md-nav');
      if (!nestedNav) return; // no children — skip (single-page tab)

      const groups = nestedNav.querySelectorAll(':scope > ul.md-nav__list > li.md-nav__item');
      if (!groups.length) return;

      // Build columns
      const panel = document.createElement('div');
      panel.className = 'hms-mm';
      const grid = document.createElement('div');
      grid.className = 'hms-mm-grid';
      panel.appendChild(grid);

      groups.forEach((g) => {
        const col = document.createElement('div');
        col.className = 'hms-mm-col';

        // Column title — either a section <label> or the leaf <a>
        const titleEl = g.querySelector(':scope > label, :scope > a');
        if (titleEl) {
          const t = document.createElement('span');
          t.className = 'hms-mm-col-title';
          t.textContent = (titleEl.textContent || '').trim();
          col.appendChild(t);
        }

        // Links under the section (descend one or two levels)
        const links = g.querySelectorAll(':scope > nav.md-nav a.md-nav__link');
        if (links.length) {
          const ul = document.createElement('ul');
          links.forEach((a) => {
            const li = document.createElement('li');
            const na = document.createElement('a');
            na.href = a.href;
            na.textContent = (a.textContent || '').trim();
            li.appendChild(na);
            ul.appendChild(li);
          });
          col.appendChild(ul);
        } else if (g.querySelector(':scope > a')) {
          // Leaf item without nested nav — wrap it as a single-link column
          const a = g.querySelector(':scope > a');
          const ul = document.createElement('ul');
          const li = document.createElement('li');
          const na = document.createElement('a');
          na.href = a.href;
          na.textContent = (a.textContent || '').trim();
          li.appendChild(na);
          ul.appendChild(li);
          col.appendChild(ul);
        }

        grid.appendChild(col);
      });

      // Anchor the panel inside the tab item so positioning is relative
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

  // Material uses instant loading — re-run after each navigation
  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(() => build());
  } else {
    document.addEventListener('DOMContentLoaded', build);
  }
})();
