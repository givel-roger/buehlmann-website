# Bühlmann Söhne AG — Website

Statische Webseite für die Bühlmann Söhne AG, Schweizer Malerbetrieb in Luzern seit 1924.

## Struktur

- **`index.html`** — Startseite mit Video-Hero
- **20 SEO-Landingpages** — eine Seite pro Suchbegriff (z.B. "Maler Einfamilienhaus", "Fassadenrenovation Luzern", "Maler Zug")
- **`sitemap.xml`** + **`robots.txt`** — für Google-Indexierung
- **`assets/logo.png`** — offizielles BS-Logo
- **`build.py`** — Generator-Skript: erstellt alle Seiten konsistent aus einem Config

## Lokaler Server

```bash
python3 -m http.server 4321 --directory .
# → http://localhost:4321
```

oder via npx:

```bash
npx http-server . -p 4321 -c-1
```

## Pages neu generieren

Inhalte werden in `build.py` (Variable `PAGES`) gepflegt. Nach Anpassung:

```bash
python3 build.py
```

Das überschreibt alle `*.html` ausser `code.html` (Stitch-Original).

## Tech-Stack

- Tailwind CSS via CDN
- Google Fonts (Inter)
- Material Symbols
- Pexels-Video im Hero (Drohnenflug Schweizer Alpen)
- Unsplash-Bilder für Services & Portfolio

## Keyword-Pages (Auswahl)

| Slug | Suchbegriff |
|------|-------------|
| `maler-luzern` | Maler Luzern |
| `maler-einfamilienhaus` | Maler für Einfamilienhaus |
| `maler-mehrfamilienhaus` | Maler für Mehrfamilienhaus |
| `fassadenrenovation` | Fassadenrenovation Luzern |
| `innenmalerei` | Innenmalerei Luzern |
| `wohnung-streichen` | Wohnung streichen lassen |
| `altbau-renovation` | Altbau Renovation |
| `maler-neubau` | Maler für Neubau |
| `farbberatung` | Farbberatung Luzern |
| `maler-gewerbe-buero` | Maler Geschäftsräume / Büro |
| `tapezieren-luzern` | Tapezieren Luzern |
| `spritzlackierung` | Spritzlackierung |
| `balkon-streichen` | Balkon streichen |
| `schimmel-entfernen` | Schimmel entfernen |
| `maler-kriens` | Maler Kriens |
| `maler-emmen` | Maler Emmen |
| `maler-zug` | Maler Zug |
| `maler-sursee` | Maler Sursee |
| `maler-stans-nidwalden` | Maler Stans / Nidwalden |
| `kontakt` | Kontakt & Offerte |

Jede Landingpage enthält:
- H1 mit Ziel-Keyword
- Meta-Title & -Description
- Strukturierter Content (Sections + FAQ)
- Schema.org `LocalBusiness` + `FAQPage`
- Internal Linking via Footer + Service-Grid auf Startseite
- CTA zu `kontakt.html`

## Lizenz

© Bühlmann Söhne AG, 2026. Alle Rechte vorbehalten.
