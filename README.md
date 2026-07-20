# Bühlmann Söhne AG — Website (bs-luzern.ch)

Statische Webseite für die Bühlmann Söhne AG, Malerei und Gipserei in Luzern seit 1935.
Alle Inhalte (Firmendaten, Texte, Fotos) basieren auf der bisherigen Webseite www.bs-luzern.ch.

## Struktur

- **`index.html`** — Startseite (heller, edler Auftritt, Slogan «Wir setzen Zeichen mit Farbe»)
- **`malerei.html`** — Leistungsübersicht (Innen, Aussen, Spritzwerk, Gipserei)
- **7 Leistungs-Seiten** — innenmalerei, fassaden, renovation, neubau, umbau, spritzwerk, gipserei
- **5 Regionen-Seiten** — maler-luzern, maler-emmen, maler-kriens, maler-hergiswil, maler-alpnach
- **`unternehmen.html`** — Zahlen/Fakten, Geschichte-Timeline (1935 bis 2008), Leitbild
- **`referenzen.html`** — echte Projektfotos
- **`jobs.html`** — Stelle Maler/in EFZ 100% + Lehrstellen-Hinweis
- **`kontakt.html`** — Rothenbad 18, 6015 Luzern, Tel. 041 269 88 50
- **`sitemap.xml`** + **`robots.txt`** — für Google
- **`assets/`** — Logo und Original-Fotos der alten Webseite

## Lokaler Server

```bash
python3 -m http.server 4321 --directory .
# → http://localhost:4321
```

## Seiten neu generieren

Inhalte werden in `build.py` gepflegt (SERVICES, REGIONS, Seiten-Funktionen). Danach:

```bash
python3 build.py
```

Das überschreibt alle generierten `*.html` (ausser `code.html`, altes Stitch-Original mit veralteten Angaben).

## SEO

Jede Seite hat eigenen Title, Meta-Description, Canonical, Open Graph, Schema.org
(LocalBusiness, FAQPage auf Leistungs-Seiten, JobPosting auf der Jobs-Seite).

## Tech-Stack

Statisches HTML, Tailwind (CDN), Fonts Inter + Playfair Display, Material Symbols.
Kein Build-Tool nötig, Deploy = Dateien auf einen Webserver kopieren.
