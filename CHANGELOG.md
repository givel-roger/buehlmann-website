# Changelog

## v2.5.5 — 2026-07-27

- Mobile: Logo mittig zentriert, Menue-Knopf rechts (Desktop unveraendert: Logo links)


## v2.5.4 — 2026-07-27

- Mobile Abstaende allgemein reduziert (Abschnitts-Padding, Grid-Abstaende, Hero)
  responsiv gemacht: enger auf dem Handy, grosszuegig auf dem Desktop


## v2.5.3 — 2026-07-27

- Mobile: Logo und Kopfzeile kompakter (Logo 56px, Nav 80px), Desktop bleibt 200px;
  Mobile-Ansicht durchgeprueft (Menue, Farbstudie, Formular, Inhaltsblöcke)


## v2.5.2 — 2026-07-27

- Gerüst-Stockbild auf Fassaden-Seite und Malerei-Block "Aussen" ersetzt durch
  echtes Standbild aus dem Firmenvideo (Maler bei der Arbeit)


## v2.5.1 — 2026-07-27

- Kontaktformular zusaetzlich unten auf der Startseite (Abschnitt "Bereit fuer Ihr Projekt?")
- Formular als wiederverwendbare Funktion; Live-Test erfolgreich (Brevo akzeptiert, Sicherungskopie ok)


## v2.5.0 — 2026-07-27

- Echtes Kontaktformular: Backend (Node, Brevo) verschickt Anfragen serverseitig
  an info@bs-luzern.ch (Antworten-an = Besucher), plus Sicherungskopie auf dem Server
- Formular mit E-Mail-Feld, Bot-Schutz (Honeypot) und Erfolgs-/Fehlermeldung
- mailto-Formular abgeloest


## v2.4.4 — 2026-07-26

- Fax restlos entfernt (auch aus den unsichtbaren SEO-/Schema.org-Daten)


## v2.4.3 — 2026-07-26

- Kontakt-Hero: doppelte Telefonnummer entfernt, erster Knopf jetzt "E-Mail schreiben"
- Faxnummer überall entfernt (Footer + Kontaktseite)
- Unscharfes Fassadenfoto (520 px) im Referenzen-Hero und Malerei-Block "Aussen"
  ersetzt; Referenzen-Hero zeigt jetzt ein echtes, scharfes Standbild aus dem
  Firmenvideo (zwei Maler beim Streichen, 1920 px)

## v2.4.2 — 2026-07-26

- Hero-Video ausgewechselt: neue Version (55 s, 720p, 5.9 MB, stumm/faststart)
- Neues Ladevorschau-Bild direkt aus dem Video (echter Mitarbeiter im
  bs-luzern.ch-Shirt) statt Unsplash-Bild

## v2.4.1 — 2026-07-20

- Logo nochmals grösser (200 px Desktop, 112 px Handy), Nav-Höhe angepasst;
  auf allen Seiten identisch, bleibt scharf

## v2.4.0 — 2026-07-20

- Dockerisierung fürs Deployment: Dockerfile (nginx:alpine), docker-compose.yml
  (Container buehlmann-app auf 127.0.0.1:3016), nginx-Site-Config und deploy/deploy.sh
- Ziel: Server 2 (schulung-video, 204.168.145.158) als statischer nginx-Container

## v2.3.3 — 2026-07-20

- Logo in der Navigation grösser (180 px statt 130 px), Nav-Höhe angepasst;
  bleibt dank hochauflösender Logo-Datei (600x423) auch auf Retina scharf

## v2.3.2 — 2026-07-20

- Unpassendes Stockbild (amerikanisches Gebäude mit Bauarbeiter) ersetzt:
  Malerei-Seite "Aussen" und Referenzen-Hero zeigen jetzt das echte Firmenfoto
  mit eigenem Gerüst (assets/fassade.jpg)

## v2.3.1 — 2026-07-20

- Hero-Video: statt 16-Sekunden-Ausschnitt läuft jetzt das ganze Image-Video (61 s)
  im Hintergrund; neu mit ffmpeg komprimiert (720p, 7.5 MB — kleiner als der alte Ausschnitt)

## v2.3.0 — 2026-07-20

- Startseite: Image-Video läuft jetzt gross und vollflächig im Hintergrund des Heros
  (moderner Video-Slider), Titel und Kennzahlen in Weiss darüber, Loop neu in 720p (13 MB)
- Separater Abschnitt "Ein Blick in unsere Arbeit" samt 32-MB-Video entfernt

## v2.2.1 — 2026-07-20

- Malerei-Seite, Block "Aussen": unpassendes Stockbild (Arbeiter in heruntergekommener
  Gasse) ersetzt durch Gerüst an historischer Fassade; Bild ganz aus dem Pool entfernt

## v2.2.0 — 2026-07-20

Image-Video der Firma eingebaut (Original 148 MB, fürs Web komprimiert mit avconvert):

- Hero der Startseite: 16-Sekunden-Loop als moderner Video-Slider
  (assets/hero-loop.mp4, 8.3 MB, stumm, automatisch, mit Poster-Fallback)
- Neuer Abschnitt "Ein Blick in unsere Arbeit": ganzes Video (61 s) mit Ton
  und Play-Steuerung (assets/imagevideo.mp4, 32 MB, lädt erst beim Abspielen)

## v2.1.0 — 2026-07-20

Echte Arbeitsfotos der Firma eingebaut (WeTransfer vom 20.07.2026, 1920x1080, scharf):

- Jobs: Teamfoto (zwei Maler beim Streichen) statt Stockbild
- Innenmalerei: echter Maler mit Roller als Hero, auch auf der Startseite (Drei Generationen)
- Renovation: sorgfältiges Abdecken; Umbau: Küche schützen; Gipserei: Fugen-Detailarbeit
- Unternehmen: Firmenwagen mit BS-Logo und Abdeck-Foto statt Stockbilder
- Referenzen: unscharfe Spritzwerk-Kachel (520px) durch scharfes Arbeitsfoto ersetzt
- Zwei private Fotos (Stadionbesuch) bewusst nicht verwendet

## v2.0.1 — 2026-07-20

- Navigation: Text neben dem Logo entfernt (Firmenname steht im Logo selber)
- Logo auf maximale scharfe Grösse gebracht (130 px, Original-Auflösung der Logo-Datei)

## v2.0.0 — 2026-07-20

Kompletter Neuaufbau mit echten Firmendaten von www.bs-luzern.ch.

### Inhalte
- Alle Firmendaten korrigiert: Gründung 1935 (Harry Bühlmann), heute Patrick Bühlmann
  in dritter Generation, Rothenbad 18, 6015 Luzern, Tel. 041 269 88 50, info@bs-luzern.ch,
  13 Mitarbeitende, Standorte Luzern / Hergiswil NW / Alpnach OW
- Erfundene Inhalte der Vorversion entfernt (fiktives Portfolio, Blog, falsche Garantien,
  falsche Adresse und Telefonnummer)
- Neue Seitenstruktur: Home, Malerei, 7 Leistungs-Seiten (Innenmalerei, Fassaden,
  Renovation, Neubau, Umbau, Spritzwerk, Gipserei), 5 Regionen-Seiten (Luzern, Emmen,
  Kriens, Hergiswil, Alpnach), Unternehmen (Geschichte-Timeline 1935-2008, Leitbild),
  Referenzen (echte Projektfotos), Jobs (Maler/in EFZ 100% + Lehrstellen), Kontakt
- Slogan «Wir setzen Zeichen mit Farbe» übernommen

### Design
- Neues, helles und edles Design: Playfair Display + Inter, Navy/Gelb nach Logo,
  schlanke Navigation mit Kontaktleiste, Mobile-Menü
- Logo gross (120 px) mit Animation: Einschwenken, periodisches Winken, Hover-Effekt
- Interaktive Farbstudie: Haus mit 8 anklickbaren Fassadenfarben (Home + Fassaden-Seite)
- Sanfte Einblend-Animationen beim Scrollen (mit reduced-motion-Unterstützung)

### Bilder
- Original-Fotos der alten Seite übernommen (Referenzen), aber nur in kleinen Karten,
  wo sie scharf wirken (Quelldateien sind nur 520-600 px)
- Alle grossen Bilder durch geprüfte, scharfe Unsplash-Aufnahmen ersetzt
  (Unsplash-Lizenz, kommerzielle Nutzung erlaubt)

### SEO
- Pro Seite: Title, Meta-Description, Canonical, Open Graph
- Schema.org: LocalBusiness (echte Daten), FAQPage, JobPosting
- sitemap.xml und robots.txt für bs-luzern.ch

## v1.0.0 — vorher

Erste Version mit 20 SEO-Landingpages (Platzhalter-Inhalte).
