# Notes corpus

Long-form notes for the Naturgnosis note module (`/note/`): catalog at
`/note/`, single-note viewer at `/note/note.html?n=<path>`. This directory
is the **source of truth** — hand-edited markdown, never machine-edited.
After any change, rebuild the search index and commit it:

```sh
python bin/build_note_index.py
```

## Format

- A **note** is a markdown file (`*.md`), rendered on the fly by the viewer.
  No metadata required: the title comes from the first `# ` heading (else
  the filename); the top-level directory is the section.
- A **live note** is a self-contained, hand-authored HTML page (`*.html`)
  with bespoke interactivity and its own scripts. Served as-is, never
  rendered through the viewer; the catalog still indexes it (title,
  headings, text) and links straight to the page with a `live` chip.
  No CDN libraries allowed in live notes.

## Naming convention

Note paths (directories and `.md`/`.html` filenames) must be:

- **ASCII** only — `a-z`, `0-9`, `-` (no accents, spaces, underscores, dots
  beyond the `.md`/`.html` extension)
- **lowercase** — never capitals
- **kebab-case** — words separated by `-`

Examples: `social-space-overview.md`, `technique-glossary.md`.
Non-markdown assets (images, code samples) may live beside notes and are
exempt from the filename rule, but directories always follow it.

`bin/build_note_index.py` validates every note path and prints warnings for
violations; warnings never fail the build. Keep the output warning-free.

## Pins

Catalog pins (starred notes) are server-side, stored as a single `pins`
document in the `naturgnosis` CouchDB database via `GET/POST
/note/api/pins` (see `bin/sync.py`). The catalog hides pin UI when the API
is unreachable (e.g. `sync.py --no-couch`).
