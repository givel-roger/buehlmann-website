#!/usr/bin/env bash
# Deploy der Bühlmann-Webseite auf Server 2 (schulung-video, 204.168.145.158)
# Statische Seite als nginx-Docker-Container auf 127.0.0.1:3016.
# Reihenfolge: erst GitHub (manuell), dann dieses Skript.
set -euo pipefail

SERVER="schulung-video"
REMOTE="/opt/buehlmann"
LOCAL="$(cd "$(dirname "$0")/.." && pwd)"

echo "==> Dateien nach $SERVER:$REMOTE synchronisieren (ohne .git)"
ssh "$SERVER" "mkdir -p $REMOTE"
rsync -az --delete \
  --exclude '.git' --exclude 'screen.png' \
  "$LOCAL"/ "$SERVER:$REMOTE"/

echo "==> Container bauen und starten"
ssh "$SERVER" "cd $REMOTE && docker compose up -d --build"

echo "==> Health-Check"
ssh "$SERVER" "sleep 2; curl -sf -o /dev/null -w 'HTTP %{http_code}\n' http://127.0.0.1:3016/ && echo OK"

echo "==> Fertig. Reverse-Proxy/SSL separat via nginx-Site + certbot einrichten."
