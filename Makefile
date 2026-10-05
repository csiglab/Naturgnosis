PYTHON ?= python3
# Datasets (CouchDB-backed). Production is a derived view, not a dataset —
# see the production-view target below.
MODULES := social research nation technique epistemica nature

.PHONY: help build index notes-index qa-index search-index universal-index landing-metrics production-view epistecnica-export seed serve dev deploy-local deploy-server clean

# Epistecnica migration export (tecnica + epistemica graph deltas since a commit).
EPISTECNICA ?= ../Epistecnica
SINCE ?=
DATASET ?= all
OUT ?= /tmp/epistecnica-migration.json

help:
	@echo "build         regenerate notes + qa + universal index + graph layouts (+ universal graph)"
	@echo "index         rebuild all indexes (notes + qa + search + universal)"
	@echo "notes-index   rebuild app/note/data/index.json from app/note/data/"
	@echo "qa-index      rebuild app/qa/data/qa-index.json from app/qa/data/qa.json"
	@echo "search-index  rebuild app/data/search-index.json (needs notes-index first)"
	@echo "universal-index rebuild app/data/universal-graph.json + universal-layout.json (view-only Graphive)"
	@echo "landing-metrics rebuild app/data/landing-metrics.json (per-module counts for the hub)"
	@echo "production-view rebuild app/production/data/view.json (derived view over social)"
	@echo "epistecnica-export export Epistecnica tecnica + epistemica graph deltas since SINCE (needs SINCE=<commit>)"
	@echo "seed          push app/*/data/data.json into CouchDB"
	@echo "serve         run the sync server (needs CouchDB + .env)"
	@echo "dev           run the sync server offline (--no-couch)"
	@echo "deploy-local  compose up couchdb + app, then seed"
	@echo "deploy-server pull the GHCR image and run it"

build: index production-view
	@for m in $(MODULES); do \
		if [ -s app/$$m/data/data.json ]; then \
			$(PYTHON) bin/layout.py --data-file app/$$m/data/data.json \
				--layout-file app/$$m/data/layout.json 2>/dev/null || \
			echo "layout: skipped $$m"; \
		fi; \
	done

index: notes-index qa-index search-index universal-index landing-metrics

notes-index:
	$(PYTHON) bin/build_note_index.py

qa-index:
	$(PYTHON) bin/build_qa_index.py

search-index: notes-index qa-index
	$(PYTHON) bin/build_search_index.py

universal-index:
	$(PYTHON) bin/build_universal_index.py

landing-metrics: notes-index qa-index
	$(PYTHON) bin/build_landing_metrics.py

production-view:
	$(PYTHON) bin/build_production_view.py

epistecnica-export:
	@if [ -z "$(SINCE)" ]; then echo "usage: make epistecnica-export SINCE=<commit> [EPISTECNICA=../Epistecnica] [DATASET=all|tecnica|epistemica] [OUT=/tmp/epistecnica-migration.json]"; exit 1; fi
	$(PYTHON) bin/extract_migration.py --since $(SINCE) --epistecnica $(EPISTECNICA) --dataset $(DATASET) --out $(OUT)
	@echo "migration JSON: $(OUT)"
	@$(PYTHON) -c "import json; d=json.load(open('$(OUT)')); print('result: %d node(s) to migrate' % len(d['items'])); print('\n'.join('  %s: %d added, %d modified' % (k, v['added'], v['modified']) for k, v in d['datasets'].items()))"

seed:
	$(PYTHON) bin/seed_couchdb.py

serve:
	$(PYTHON) bin/sync.py

dev:
	$(PYTHON) bin/sync.py --no-couch

deploy-local:
	bash deploy/deploy_local.sh

deploy-server:
	./deploy/deploy_server.sh

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -r {} +
