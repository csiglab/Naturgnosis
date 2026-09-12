# Phrases Catalog

> Aphorisms, proverbs, maxims and locutions worth keeping — curated for resonance with episteme and
> technique: how reality is navigated, named, and acted upon.

## Storage model

- **Source of truth: CouchDB**, `dataset=phrases` (one document per phrase, namespaced
  `phrases:<id>` inside the `naturgnosis` database), written through the standard sync API.
- **Disk mirror:** `app/phrases/data/data.json` — rewritten by the sync server after each save, so
  the static catalog and fresh bootstraps work without CouchDB.
- **Seed:** generated once from the Notion exports by `bin/import_phrases.py`; raw exports are
  archival in `app/phrases/import/` — do not edit.

Phrase nodes reuse the Naturgnosis node model:

| Field | Usage for a phrase |
| ----- | ------------------ |
| `id` | slug of the phrase |
| `name` | the phrase itself |
| `category` | always `Phrase` |
| `description` | meaning, commentary, translation notes |
| `tags` | free-form curation tags |
| `specific` | `{language, translation}` |
| `metadata` | `{source, imported, edited}` |
| `references` | source URLs |

## UI

- **Catalog** `app/phrases/web/index.html` — card grid, client-side search over name/meaning/tags;
  loads `/api/graph?dataset=phrases`, falls back to the static mirror.
- **Editor** `app/phrases/web/edit.html` — list + form (phrase, meaning, language, translation,
  tags, references); saves via `POST /api/graph/save` (`{dataset:'phrases', nodes:[…], delete_ids?}`),
  which upserts into CouchDB and re-mirrors `data.json`.

## Operations

```sh
python bin/import_phrases.py           # one-shot seed from Notion exports
python bin/seed_couchdb.py --dataset phrases   # (re)push the mirror into CouchDB
```

## Conventions

- Keep the original language of the phrase in `name`; translation goes in `specific.translation`.
- Tags in English, lowercase.
