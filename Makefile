PYTHON ?= python3
MODULES := social production research nation

.PHONY: help build seed serve dev deploy-local deploy-server clean

help:
	@echo "build         regenerate graph layouts"
	@echo "seed          push app/*/data/data.json into CouchDB"
	@echo "serve         run the sync server (needs CouchDB + .env)"
	@echo "dev           run the sync server offline (--no-couch)"
	@echo "deploy-local  compose up couchdb + app, then seed"
	@echo "deploy-server pull the GHCR image and run it"

build:
	@for m in $(MODULES); do \
		if [ -s app/$$m/data/data.json ]; then \
			$(PYTHON) bin/layout.py --data-file app/$$m/data/data.json \
				--layout-file app/$$m/data/layout.json 2>/dev/null || \
			echo "layout: skipped $$m"; \
		fi; \
	done

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
