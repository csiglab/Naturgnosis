FROM python:3.12-slim
WORKDIR /srv
COPY bin/ bin/
COPY app/ app/
COPY spec/ spec/
COPY Makefile .
# Generated artifacts (indexes, layouts, derived views, polity manifest) are
# not committed — the image bakes them from the tracked sources. `production-view`
# runs first so landing-metrics (inside `index`) sees a fresh view.json.
RUN apt-get update \
 && apt-get install -y --no-install-recommends make \
 && make production-view \
 && make build \
 && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["sh", "-c", "python bin/sync.py --app-root /srv/app --port \"${PORT:-8000}\""]
