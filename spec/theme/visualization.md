# Treemap Pattern — Naturgnosis Visualization Spec

> The general treemap pattern, binding on every treemap in the project
> (live catalogs, technique trees, the notes treemap, and any future one).
> A treemap here is always a **drill-down navigator**, never a static collage:
> first level visible at load, one click per level deeper, breadcrumb always
> available to climb back out. Parent spec: `spec/theme/README.md`
> (Oxford Common Room tokens, three voices of type, matte over neon,
> progressive disclosure).

## Structural Rules (binding)

1. **First level first.** On load the treemap shows exactly one level
   (the roots). No two-level flat mash: children appear only after drilling.
2. **One click deeper.** Clicking a block with children re-layouts the canvas
   into that node's children. Clicking a leaf performs the leaf action
   (catalog deep link, node select) instead of drilling.
3. **Breadcrumb always visible.** Every drill state shows the path
   (`root › … › current`) with each ancestor clickable; `Esc` returns to root.
   Reference: `renderCrumb` in `app/data/live/catalog-viewer.js`,
   `renderTmCrumb` in the marketing practice tree.
4. **Children partition the parent.** Child areas must sum to the parent area.
   Facets that overlap (e.g. one note carrying many tags) are normalized to
   partition the parent; labels always show true counts, never scaled ones.
5. **Squarified layout.** Rectangles packed by the squarify algorithm
   (aspect ratios kept near 1); 1–2px gutters; `devicePixelRatio` scaling.
6. **Metric toggle labeled with units** wherever two weights exist
   (e.g. note *count* vs *words*); the toggle states the active metric.

## Label Rules (binding)

7. **Thresholds.** Title line only when the rect fits it (`w > 56`, `h > 30`
   scale); count second line only when `h > 48`. Overlong labels truncate
   with `…` measured against rect width — never overflow, never wrap.
8. **Three voices.** Titles in the display voice, counts/metadata in mono
   (`JetBrains Mono`); tooltips carry path + count + the click action.
9. **Hover = brighten + tip.** Hovered rect brightens (or gilds at selection);
   tooltip shows label, true count, and what a click will do.

## Color Rules (binding)

10. **Hue sustained through depth.** A branch keeps its section hue at every
    level (parent translucent ≈0.28, children solid ≈0.7); never recolor
    children by an unrelated scheme.
11. **Matte fills, ink chosen per theme.** Muted fills per the theme accents;
    label ink near-black on light fills in dark mode and theme text in
    light mode. Selection/hover uses the copper gilt, sparingly.

## Click-Through Rules (binding)

12. **Every leaf resolves somewhere.** Treemap leaves deep-link into their
    home surface pre-filtered: notes catalog (`?section=`/`?tag=`), shared
    viewer (`#<id>`), technique nodes (`?node=`), good producers (`?id=`).
    A treemap whose leaves go nowhere is unfinished.

## Conformant Implementations

- `app/data/live/catalog-viewer.js` — squarified, one level per drill,
  breadcrumb, collapsed-to-first-level start (HS, NAICS, product taxonomy).
- Marketing practice tree treemap — squarified, drill path, breadcrumb,
  label thresholds with counts.
- `app/note/data/meta/notes-treemap.html` — sections to top tags,
  count/words toggle, catalog click-through.
