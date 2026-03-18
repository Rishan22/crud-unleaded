#!/bin/bash
set -e

if ! command -v docker >/dev/null; then
  echo "Docker missing. Install required."
  exit 1
fi

python3 scripts/configure.py
python3 scripts/build.py

docker compose -f docker/docker-compose.yml up -d

echo "Running at http://localhost:8080"
