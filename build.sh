#!/usr/bin/env bash
# Regenerate all derived artifacts: graph layouts.
# (The old mkdocs build is gone; the served root is app/.)
set -eu

cd "$(dirname "$0")"

echo "Building Naturgnosis artifacts…"
make build

echo "Build complete."
