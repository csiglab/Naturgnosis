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
  the filename); the top-level directory is the section. Optional tags go
  in `---` front matter (same style as Epistecnica; only `tags: [...]` is
  read, everything else ignored):
  ```md
  ---
  tags: [social-space, method]
  ---
  ```
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

Canonical slug (Epistecnica parity): NFKD-normalize to ASCII, lowercase,
every run of non-alphanumeric characters becomes a single `-`, trim
leading/trailing `-`; collisions get a `-2`, `-3`, … suffix. Never run
`bin/slugify_files.py` (underscore rule) on this directory.

`bin/build_note_index.py` validates every note path and tag, prints
warnings with the suggested normalized form for violations, and never
fails the build. Keep the output warning-free.

## Pins

Catalog pins (starred notes) are server-side, stored as a single `pins`
document in the `naturgnosis` CouchDB database via `GET/POST
/note/api/pins` (see `bin/sync.py`). The catalog hides pin UI when the API
is unreachable (e.g. `sync.py --no-couch`).
