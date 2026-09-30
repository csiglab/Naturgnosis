PYTHON ?= python3
# Datasets (CouchDB-backed). Production is a derived view, not a dataset —
# see the production-view target below.
MODULES := social research nation technique epistemica nature

.PHONY: help build index notes-index qa-index search-index universal-index landing-metrics production-view seed serve dev deploy-local deploy-server clean

help:
	@echo "build         regenerate notes + qa + universal index + graph layouts (+ universal graph)"
	@echo "index         rebuild all indexes (notes + qa + search + universal)"
	@echo "notes-index   rebuild app/note/data/index.json from app/note/data/"
	@echo "qa-index      rebuild app/qa/data/qa-index.json from app/qa/data/qa.json"
	@echo "search-index  rebuild app/data/search-index.json (needs notes-index first)"
	@echo "universal-index rebuild app/data/universal-graph.json + universal-layout.json (view-only Graphive)"
	@echo "landing-metrics rebuild app/data/landing-metrics.json (per-module counts for the hub)"
	@echo "production-view rebuild app/production/data/view.json (derived view over social)"
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
