#!/bin/bash
# build_image.sh — pack the lunchbox.
# Run it with: bash scripts/build_image.sh
set -euo pipefail

# If Docker is not installed, say so clearly and stop.
# We never pretend the image was built.
if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is not installed on this computer."
  echo "Please install Docker Desktop first, then run this script again."
  exit 1
fi

echo "Building Docker image shop-app:1.0.0 ..."
docker build -t shop-app:1.0.0 .
echo "Done. Image shop-app:1.0.0 is ready."
