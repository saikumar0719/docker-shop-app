#!/bin/bash
# run_app.sh — open the lunchbox and run the app.
# Run it with: bash scripts/run_app.sh
# Expected output: Raw orders: 11, Clean orders: 8, Total sales: 10550.00
set -euo pipefail

# If Docker is not installed, say so clearly and stop.
if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is not installed on this computer."
  echo "Please install Docker Desktop first, then run this script again."
  exit 1
fi

echo "Running Docker image shop-app:1.0.0 ..."
docker run --rm shop-app:1.0.0
