#!/usr/bin/env python3
"""Generiert die Webseite der Bühlmann Söhne AG (bs-luzern.ch) aus einem Config.

Alle Firmendaten stammen von der bisherigen Webseite www.bs-luzern.ch.
Texte sind modernisiert, Fakten unverändert (Gründung 1935, Rothenbad 18 usw.).
"""
from pathlib import Path
from textwrap import dedent

VERSION = "2.6.2"
SITE_URL = "https://www.bs-luzern.ch"
ROOT = Path(__file__).parent

PHONE_DISPLAY = "041 269 88 50"
PHONE_LINK = "+41412698850"
EMAIL = "info@bs-luzern.ch"
ADDRESS = "Rothenbad 18"
CITY = "6015 Luzern"
MAPS_URL = "https://maps.google.com/?q=B%C3%BChlmann+S%C3%B6hne+AG,+Rothenbad+18,+6015+Luzern"

# Scharfe Bilder (Unsplash, visuell geprüft). Die Original-Fotos der alten Seite
# sind nur 520-600 px breit und werden darum nur klein (Karten) verwendet.
U = "https://images.unsplash.com/"
IMG_INNEN = U + "photo-1693985120993-e9b203ce7631?w=1600&q=80"          # Roller streicht Wand
IMG_GERUEST = U + "photo-1646608220368-c604d8e8130f?w=1600&q=80"        # Mann auf Geruest
IMG_ALTBAU = U + "photo-1626471671222-9d89fe4c2668?w=1600&q=80"         # Geruest an historischer Fassade
IMG_FARBEIMER = U + "photo-1652572036885-b5e9205dd847?w=1600&q=80"      # Farbeimer und Pinsel
IMG_ROLLER = U + "photo-1516962080544-eac695c93791?w=1600&q=80"         # Farbroller Nahaufnahme
IMG_ROLLER2 = U + "photo-1652829069862-87874e119527?w=1600&q=80"        # Roller Nahaufnahme 2
IMG_WEISSER_RAUM = U + "photo-1630699375895-fe5996d163ee?w=1600&q=80"   # frisch gestrichener Raum
IMG_HELLER_RAUM = U + "photo-1649083048381-520a5b3d91ff?w=1600&q=80"    # heller renovierter Raum
IMG_LUZERN = U + "photo-1477271706509-fecda7438b68?w=1600&q=80"         # Kapellbruecke Luzern
IMG_LUZERN_PANO = U + "photo-1664369081469-8a72d67d75ae?w=1600&q=80"    # Stadtpanorama Luzern
IMG_LUZERN_UFER = U + "photo-1690056072536-c48de99fef89?w=1600&q=80"    # Flussufer Luzern
IMG_MFH = U + "photo-1783282643449-5f026f572931?w=1600&q=80"            # MFH vor Bergkulisse
IMG_NEUBAU = U + "photo-1777669164326-7a4f6e09e7cc?w=1600&q=80"         # Neubau vor Bergen
IMG_SEEHAUS = U + "photo-1641938552237-ba43ad0b2a1d?w=1600&q=80"        # Dorf am See mit Pilatus
IMG_BERGDORF = U + "photo-1773529472042-ed4bc495eb05?w=1600&q=80"       # Bergdorf Innerschweiz

# ---------------------------------------------------------------------------
# Leistungs-Detailseiten (SEO-Landingpages)
# ---------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "innenmalerei",
        "nav": "Innenmalerei",
        "title": "Innenmalerei Luzern | Bühlmann Söhne AG, Maler seit 1935",
        "meta": "Malen, Spritzen und Tapezieren für jeden Innenraum in Luzern und der Innerschweiz. Von der denkmalgeschützten Stube bis zum modernen Büro. Tel. 041 269 88 50.",
        "h1": "Innenmalerei mit Liebe zum Detail",
        "lead": "Malen, Spritzen, Tapezieren: Mit Spachtel, Pinsel, Roller und Spritzpistole verschönern wir jeden Innenraum in Luzern und der Innerschweiz.",
        "image": "assets/arbeit-roller.jpg",
        "sections": [
            ("Jeder Raum hat seinen eigenen Charakter", "Ob denkmalgeschützte Ratsherrenstube, modernes Bürogebäude oder nüchterner Industriebau: Unsere Malerinnen und Maler gehen auf jeden Raum individuell ein und arbeiten sauber, präzise und termingerecht."),
            ("Das ganze Spektrum des Malerhandwerks", "Unsere Fachleute malen, marmorieren, maserieren, vergolden, stuckatieren, tapezieren und spritzlackieren. Durch laufende Weiterbildung sind sie stets auf dem neusten Stand der Technik."),
            ("Farbe nach Mass", "Mit unserem Mischcomputer treffen wir jeden Farbton exakt. Gerne beraten wir Sie bei der Farbwahl und zeigen Ihnen Varianten, bevor der erste Pinselstrich fällt."),
        ],
        "faq": [
            ("Arbeiten Sie auch in bewohnten Räumen?", "Ja. Wir decken sorgfältig ab, arbeiten sauber und hinterlassen die Räume besenrein."),
            ("Übernehmen Sie auch kleine Aufträge?", "Ja. Unser Kundendienst ist auf kleine, prompte Einsätze eingerichtet."),
            ("Beraten Sie bei der Farbwahl?", "Ja, die Farbberatung gehört bei uns selbstverständlich dazu."),
        ],
        "cta": "Offerte für Innenmalerei anfragen",
    },
    {
        "slug": "fassaden",
        "nav": "Fassaden",
        "title": "Fassadenrenovation Luzern | Bühlmann Söhne AG",
        "meta": "Fassaden streichen, renovieren und isolieren in Luzern. Eigene Roll- und Fassadengerüste, Farbstudien am Computer, Betonsanierung. Tel. 041 269 88 50.",
        "h1": "Fassaden, die Zeichen setzen",
        "lead": "Ob Holz, Beton, Naturstein, Verputz, Metall oder Kunststoff: Wir bearbeiten jede Fassade fachmännisch, mit eigenen Roll- und Fassadengerüsten.",
        "image": "assets/arbeit-fassade.jpg",
        "sections": [
            ("Ein neues Kleid für Ihr Gebäude", "Eine neue Fassade ist für unsere Fachleute eine kreative Herausforderung, die viel Gefühl für das Objekt und seine Umgebung voraussetzt. Wir nehmen uns diese Zeit."),
            ("Farbstudien am Computer", "Bevor wir loslegen, zeigen wir Ihnen Ihr Gebäude in verschiedenen Farbvarianten am Bildschirm. So sehen Sie alle Nuancen Ihres zukünftigen Objekts und haben die Qual der Wahl."),
            ("Alles aus einer Hand", "Eigene Gerüste, Maler- und Spritzarbeiten, Kunststoffputze, Betonsanierungen sowie Fassadenisolationen und -renovationen: Bei uns bekommen Sie die ganze Fassadenarbeit effizient aus einer Hand."),
            ("Langlebig und umweltbewusst", "Wir sorgen mit unserem guten Namen dafür, dass Ihre neue Fassade langlebig und farbbeständig ist und umweltgerechte Materialien zum Einsatz kommen."),
        ],
        "faq": [
            ("Haben Sie eigene Gerüste?", "Ja, wir verfügen über eigene Roll- und Fassadengerüste und können dadurch effizient und flexibel arbeiten."),
            ("Machen Sie auch Fassadenisolationen?", "Ja, Fassadenisolationen und -renovationen gehören zu unserem Kerngeschäft."),
            ("Kann ich die neue Fassadenfarbe vorher sehen?", "Ja, wir erstellen Farbstudien am Computer und zeigen Ihnen Ihr Gebäude in verschiedenen Varianten."),
        ],
        "cta": "Offerte für Fassadenarbeiten anfragen",
    },
    {
        "slug": "renovation",
        "nav": "Renovation",
        "title": "Renovation Luzern | Malerarbeiten mit Werterhalt | Bühlmann Söhne AG",
        "meta": "Renovationen mit Sorgfalt und Liebe zum Detail in Luzern. Malen, Tapezieren, Vergolden, Stuckatieren. Mit Werterhaltungs-Kundendienst. Tel. 041 269 88 50.",
        "h1": "Renovation mit Sorgfalt und Detailtreue",
        "lead": "Renovationsarbeiten verlangen gut ausgebildete Fachleute, Sorgfalt und Liebe zum Detail. Genau dafür stehen wir seit Jahrzehnten.",
        "image": "assets/arbeit-abdecken.jpg",
        "sections": [
            ("Vertrauen, über Jahrzehnte aufgebaut", "In diesem Bereich zählen wir auf eine treue, über Jahrzehnte sorgfältig aufgebaute Privatkundschaft. Diese Kundinnen und Kunden wissen: Bei uns ist ihr Zuhause in besten Händen."),
            ("Handwerk auf höchstem Niveau", "Unsere Mitarbeiter malen, marmorieren, maserieren, vergolden, stuckatieren, tapezieren und spritzlackieren. Weiterbildung hält sie auf dem neusten Stand, oft sogar einen Schritt voraus."),
            ("Service auch nach dem letzten Pinselstrich", "Sie profitieren nach Abschluss des Auftrags von unserem Werterhaltungs-Kundendienst, der Objektbetreuung und unserem Know-how. Garantie inbegriffen."),
        ],
        "faq": [
            ("Renovieren Sie auch bewohnte Wohnungen?", "Ja. Wir planen die Arbeiten mit Ihnen so, dass Sie möglichst wenig davon spüren."),
            ("Was ist der Werterhaltungs-Kundendienst?", "Wir betreuen Ihr Objekt auch nach der Renovation weiter und sorgen dafür, dass es seinen Wert behält."),
            ("Übernehmen Sie auch historische Techniken?", "Ja, von Marmorieren über Vergolden bis Stuckatieren beherrschen unsere Fachleute auch traditionelle Techniken."),
        ],
        "cta": "Offerte für Ihre Renovation anfragen",
    },
    {
        "slug": "neubau",
        "nav": "Neubau",
        "title": "Maler für Neubau Luzern | Bühlmann Söhne AG",
        "meta": "Malerarbeiten im Neubau: moderne Maschinen, eingespielte Fachkräfte und optimale Arbeitsorganisation. Referenzen in Luzern und der Innerschweiz. Tel. 041 269 88 50.",
        "h1": "Neubau: Präzision ab der ersten Schicht",
        "lead": "Ein Neubau ist für uns Herausforderung und Motivation zugleich: Sie als Kunde in allen Belangen zufriedenzustellen und unsere Referenzliste um ein weiteres Objekt zu bereichern.",
        "image": IMG_NEUBAU,
        "sections": [
            ("Erfahrung, die sich auszahlt", "Im Neubau ist der Wettbewerb intensiv. Sie profitieren von unserer grossen Erfahrung: moderne Maschinen, optimale Arbeitsorganisation und tüchtige Fachkräfte machen uns konkurrenzfähig, heute und in Zukunft."),
            ("Ein starker Partner für Architekten und Bauherren", "Wir arbeiten eng mit Architekten, Generalunternehmern und privaten Bauherren zusammen und halten Termine und Budgets zuverlässig ein."),
            ("Qualität vor Quantität", "Auch im Neubau gilt unser Leitgedanke: saubere, fachmännisch und termingerecht ausgeführte Arbeit, die den Wünschen der Auftraggeber gerecht wird."),
        ],
        "faq": [
            ("Arbeiten Sie mit Generalunternehmern zusammen?", "Ja, wir sind ein eingespielter Partner für Architekten, GU und Bauherrschaften."),
            ("Wie stellen Sie Termintreue sicher?", "Durch optimale Arbeitsorganisation, moderne Maschinen und ein eingespieltes Team."),
            ("Übernehmen Sie auch grosse Überbauungen?", "Ja, unsere Referenzen umfassen auch grosse Wohnüberbauungen in der Region."),
        ],
        "cta": "Offerte für Ihren Neubau anfragen",
    },
    {
        "slug": "umbau",
        "nav": "Umbau",
        "title": "Maler für Umbau Luzern | Bühlmann Söhne AG",
        "meta": "Umbau ohne unangenehme Überraschungen: vom Kostenvoranschlag bis zum letzten Pinselstrich in besten Händen. Tel. 041 269 88 50.",
        "h1": "Umbau ohne Nebengeräusche",
        "lead": "Mehr Platz, bessere Nutzung oder einfach Lust auf einen Tapetenwechsel: Beim Umbau sind Sie vom Kostenvoranschlag bis zum letzten Pinselstrich in besten Händen.",
        "image": "assets/arbeit-kueche.jpg",
        "sections": [
            ("Eingespieltes Mannschaftsspiel", "Hohe Flexibilität, Termintreue und das eingespielte Zusammenspiel mit unseren Partnerfirmen sorgen für einen Umbau-Ablauf ohne unangenehme Überraschungen."),
            ("Optimales Preis-Leistungs-Verhältnis", "Einer der Leitgedanken unserer Firma ist ein optimales Preis-Leistungs-Verhältnis. Das hat sich schon immer für beide Seiten gelohnt."),
            ("Alles koordiniert", "Dank unserer Erfahrung optimieren wir Abläufe und koordinieren die Arbeiten so, dass Ihr Umbau speditiv und sauber über die Bühne geht."),
        ],
        "faq": [
            ("Koordinieren Sie auch andere Handwerker?", "Wir arbeiten eng mit bewährten Partnerfirmen zusammen und stimmen die Abläufe untereinander ab."),
            ("Erhalte ich vorab einen Kostenvoranschlag?", "Ja, selbstverständlich. Sie wissen vor Baubeginn, womit Sie rechnen können."),
            ("Wie schnell können Sie starten?", "Rufen Sie uns an, wir finden gemeinsam den passenden Termin. Kleine Einsätze erledigen wir prompt."),
        ],
        "cta": "Offerte für Ihren Umbau anfragen",
    },
    {
        "slug": "spritzwerk",
        "nav": "Spritzwerk",
        "title": "Spritzwerk Luzern | Thermo-Lackierung | Bühlmann Söhne AG",
        "meta": "Eigenes Spritzwerk für Industrie- und Bauteile in Luzern: Jalousieläden, Türen und grossflächige Teile im Thermo-Lackier-Verfahren. Tel. 041 269 88 50.",
        "h1": "Unser eigenes Spritzwerk",
        "lead": "Mit unserer modernen Spritzanlage für Industrie- und Bauteile lackieren wir auch grossflächige Gegenstände wie Jalousieläden im Thermo-Lackier-Verfahren.",
        "image": IMG_FARBEIMER,
        "sections": [
            ("Perfekte Oberflächen", "Spritzlackierte Oberflächen sind gleichmässig, robust und wie neu. Türen, Läden, Möbelfronten und Bauteile erhalten bei uns eine makellose zweite Haut."),
            ("Thermo-Lackier-Verfahren", "Unsere Anlage beherrscht das Thermo-Lackier-Verfahren und verarbeitet auch grossflächige Teile wie Jalousieläden effizient und in gleichbleibender Qualität."),
            ("Für Private und Industrie", "Vom einzelnen Möbelstück bis zur Serie von Industrie-Bauteilen: Unser Spritzwerk steht Privatkunden und Firmen offen."),
        ],
        "faq": [
            ("Was kann man spritzlackieren lassen?", "Türen, Jalousieläden, Möbelfronten, Heizkörper und viele weitere Bau- und Industrieteile."),
            ("Muss ich die Teile selber bringen?", "Nach Absprache holen wir Teile ab und liefern sie fertig lackiert wieder aus."),
            ("Lackieren Sie auch Serien für Firmen?", "Ja, unsere Anlage ist auf Industrie- und Bauteile ausgelegt, auch in grösseren Stückzahlen."),
        ],
        "cta": "Offerte für Spritzarbeiten anfragen",
    },
    {
        "slug": "gipserei",
        "nav": "Gipserei",
        "title": "Kundengipserei Luzern | Verputz und Betonsanierung | Bühlmann Söhne AG",
        "meta": "Kundengipserei für kleine und mittlere Einsätze: Verputzarbeiten, Reparaturen und Betonsanierungen in Luzern. Prompt und unkompliziert. Tel. 041 269 88 50.",
        "h1": "Wir setzen Zeichen mit Gips",
        "lead": "Unsere Kundengipserei ist für Einsätze jeglicher Art ausgerüstet. Wir erledigen Ihre Aufträge prompt und unkompliziert.",
        "image": "assets/arbeit-fugen.jpg",
        "sections": [
            ("Kleine Einsätze, grosse Wirkung", "Risse, Löcher, beschädigte Ecken: Unsere Kundengipserei behebt Schäden schnell und sauber, bevor der Maler für das perfekte Finish sorgt."),
            ("Verputz- und Gipserarbeiten", "Wir führen Kundengipser- und Verputzarbeiten aller Art aus, innen wie aussen, und kombinieren sie auf Wunsch direkt mit den Malerarbeiten."),
            ("Betonsanierungen", "Auch Betonsanierungen gehören zu unserem Angebot. So bleibt die Bausubstanz Ihres Objekts langfristig gesund."),
        ],
        "faq": [
            ("Lohnt sich das auch für kleine Reparaturen?", "Ja, unsere Kundengipserei ist genau auf solche prompten, unkomplizierten Einsätze eingerichtet."),
            ("Machen Sie Gips- und Malerarbeiten aus einer Hand?", "Ja, das ist unsere Stärke: ein Ansprechpartner, ein Termin, ein sauberes Ergebnis."),
            ("Sanieren Sie auch Beton?", "Ja, Betonsanierungen führen wir fachmännisch durch, oft kombiniert mit Fassadenarbeiten."),
        ],
        "cta": "Offerte für Gipserarbeiten anfragen",
    },
]

# ---------------------------------------------------------------------------
# Regionen-Seiten (echte Standorte und Einzugsgebiet)
# ---------------------------------------------------------------------------
REGIONS = [
    {
        "slug": "maler-luzern",
        "name": "Luzern",
        "title": "Maler Luzern | Bühlmann Söhne AG, seit 1935",
        "meta": "Ihr Maler in Luzern seit 1935: Innenmalerei, Fassaden, Renovationen, Gipserei und Spritzwerk. Familienbetrieb in dritter Generation. Tel. 041 269 88 50.",
        "h1": "Ihr Maler in Luzern seit 1935",
        "lead": "Vom Firmensitz im Rothenbad in Luzern aus sind wir seit bald einem Jahrhundert für die Stadt und die Region im Einsatz.",
        "image": IMG_LUZERN,
        "body": [
            ("Verwurzelt in Luzern", "1935 an der Dammstrasse gegründet, heute im eigenen Betriebsgebäude im Rothenbad: Die Bühlmann Söhne AG ist seit drei Generationen fester Bestandteil des Luzerner Gewerbes. Spuren unserer Arbeit finden Sie in der ganzen Stadt, von der Altstadt bis zu modernen Überbauungen."),
            ("Schnell vor Ort", "Unser Standort nahe Seetalplatz bedeutet kurze Wege in alle Quartiere. Kleine Einsätze erledigt unser Kundendienst prompt und unkompliziert."),
            ("Alles aus einer Hand", "Innenmalerei, Fassaden, Gipserei, Spritzwerk: In Luzern bekommen Sie von uns das komplette Maler- und Gipserhandwerk aus einer Hand."),
        ],
    },
    {
        "slug": "maler-emmen",
        "name": "Emmen und Emmenbrücke",
        "title": "Maler Emmen und Emmenbrücke | Bühlmann Söhne AG",
        "meta": "Malerarbeiten in Emmen und Emmenbrücke: Der Betrieb der Bühlmann Söhne AG liegt direkt beim Seetalplatz. Tel. 041 269 88 50.",
        "h1": "Ihr Maler in Emmen und Emmenbrücke",
        "image": IMG_MFH,
        "lead": "Unser Betrieb liegt in Reussbühl, nur wenige Minuten vom Seetalplatz entfernt. Näher kann ein Maler kaum sein.",
        "body": [
            ("Ihr Nachbar im Rothenbad", "Von unserem Firmensitz an der Grenze zu Emmenbrücke sind wir in wenigen Minuten bei Ihnen. Das macht uns schnell, flexibel und günstig in der Anfahrt."),
            ("Für Private und Liegenschaftsverwaltungen", "Wir streichen Wohnungen, Treppenhäuser und Fassaden in Emmen und Emmenbrücke, für Eigentümer, Mieter und Verwaltungen."),
            ("Prompter Kundendienst", "Kleine Reparaturen und Auffrischungen erledigen wir unkompliziert. Ein Anruf genügt."),
        ],
    },
    {
        "slug": "maler-kriens",
        "name": "Kriens",
        "title": "Maler Kriens | Bühlmann Söhne AG",
        "meta": "Malerarbeiten in Kriens: Innenmalerei, Fassadenrenovationen und Gipserarbeiten vom Luzerner Traditionsbetrieb. Tel. 041 269 88 50.",
        "h1": "Ihr Maler in Kriens",
        "image": IMG_LUZERN_PANO,
        "lead": "Ob Wohnung, Einfamilienhaus oder Gewerbe: In Kriens sind wir seit Jahrzehnten regelmässig im Einsatz.",
        "body": [
            ("Kurze Wege, schnelle Termine", "Kriens erreichen wir von unserem Betrieb in Luzern in wenigen Minuten. Das gilt für grosse Renovationen genauso wie für kleine Kundendienst-Einsätze."),
            ("Erfahrung mit jedem Baustil", "Vom älteren Einfamilienhaus bis zur modernen Überbauung: Unsere Fachleute kennen die Bausubstanz der Region und wählen Material und Technik passend aus."),
            ("Fassaden mit Farbstudie", "Für Fassadenrenovationen in Kriens erstellen wir auf Wunsch Farbstudien am Computer, damit Sie das Ergebnis vorab sehen."),
        ],
    },
    {
        "slug": "maler-hergiswil",
        "name": "Hergiswil NW",
        "title": "Maler Hergiswil NW | Bühlmann Söhne AG",
        "meta": "Die Bühlmann Söhne AG ist mit einem Standort in Hergiswil NW präsent: Malerarbeiten innen und aussen für ganz Nidwalden. Tel. 041 269 88 50.",
        "h1": "Ihr Maler in Hergiswil und Nidwalden",
        "image": IMG_SEEHAUS,
        "lead": "Hergiswil ist einer unserer drei Standorte. Für Kundinnen und Kunden in Nidwalden sind wir darum besonders schnell zur Stelle.",
        "body": [
            ("Vor Ort in Hergiswil", "Neben Luzern und Alpnach ist Hergiswil NW einer unserer Standorte. Wir kennen die Häuser am See und am Berg und sind schnell bei Ihnen."),
            ("Innen und aussen", "Von der Innenmalerei über Tapezierarbeiten bis zur kompletten Fassadenrenovation erhalten Sie bei uns alles aus einer Hand."),
            ("Werterhalt am See", "Seelage und Wetter fordern die Gebäudehülle. Wir beraten Sie zu langlebigen, farbbeständigen und umweltgerechten Lösungen."),
        ],
    },
    {
        "slug": "maler-alpnach",
        "name": "Alpnach OW",
        "title": "Maler Alpnach OW | Bühlmann Söhne AG",
        "meta": "Die Bühlmann Söhne AG ist mit einem Standort in Alpnach OW präsent: Maler- und Gipserarbeiten für ganz Obwalden. Tel. 041 269 88 50.",
        "h1": "Ihr Maler in Alpnach und Obwalden",
        "image": IMG_BERGDORF,
        "lead": "Alpnach ist einer unserer drei Standorte. Obwaldner Kundinnen und Kunden profitieren von kurzen Wegen und promptem Service.",
        "body": [
            ("Vor Ort in Alpnach", "Neben Luzern und Hergiswil sind wir auch in Alpnach OW präsent. So sind wir in ganz Obwalden schnell und flexibel im Einsatz."),
            ("Vom Bauernhaus bis zum Neubau", "Unsere Fachleute beherrschen traditionelle Techniken genauso wie moderne Beschichtungen und werden jedem Objekt gerecht."),
            ("Maler und Gipser in einem", "Auch in Obwalden bieten wir Maler- und Kundengipserarbeiten kombiniert an. Das spart Ihnen Koordination, Zeit und Kosten."),
        ],
    },
]

NAV_LINKS = [
    ("index.html", "Home"),
    ("malerei.html", "Malerei"),
    ("referenzen.html", "Referenzen"),
    ("unternehmen.html", "Unternehmen"),
    ("jobs.html", "Jobs"),
    ("kontakt.html", "Kontakt"),
]

# ---------------------------------------------------------------------------
# Design-Bausteine
# ---------------------------------------------------------------------------
HEAD_BASE = dedent("""
<meta charset="utf-8" />
<meta content="width=device-width, initial-scale=1.0" name="viewport" />
<link rel="icon" type="image/png" href="assets/logo.png" />
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
<script id="tailwind-config">
  tailwind.config = {
    theme: { extend: {
      colors: {
        "ink": "#101c3d",
        "ink-soft": "#3d4763",
        "accent": "#fddc00",
        "accent-deep": "#e5c700",
        "paper": "#fcfcfa",
        "mist": "#f4f5f7",
        "line": "#e4e6eb",
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        display: ["Playfair Display", "Georgia", "serif"],
      },
    } },
  };
</script>
<style>
  body { font-family: "Inter", system-ui, sans-serif; }
  .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24; display: inline-block; line-height: 1; }
  .eyebrow { font-size: 13px; letter-spacing: 0.22em; text-transform: uppercase; font-weight: 600; }
  .accent-bar { display: inline-block; width: 56px; height: 4px; background: #fddc00; border-radius: 2px; }
  .card-lift { transition: transform .35s ease, box-shadow .35s ease; }
  .card-lift:hover { transform: translateY(-4px); box-shadow: 0 18px 40px -18px rgba(16,28,61,.25); }
  html { scroll-behavior: smooth; }
  a, button { -webkit-tap-highlight-color: transparent; }
  /* Logo: Einblenden, gelegentliches Winken, interaktiver Hover */
  @keyframes logo-in { 0% { opacity: 0; transform: translateY(-10px) rotate(-8deg); } 100% { opacity: 1; transform: translateY(0) rotate(0); } }
  @keyframes logo-wave { 0%, 86%, 100% { transform: rotate(0); } 88% { transform: rotate(-5deg); } 92% { transform: rotate(4deg); } 96% { transform: rotate(-2deg); } }
  .logo-anim { animation: logo-in .8s ease-out both, logo-wave 9s ease-in-out 3s infinite; transform-origin: 50% 80%; transition: transform .35s ease, filter .35s ease; cursor: pointer; }
  @media (hover: hover) {
    .logo-anim:hover { animation-play-state: paused, paused; transform: rotate(-5deg) scale(1.08); filter: drop-shadow(0 6px 14px rgba(16,28,61,.35)); }
  }
  /* Sanftes Einblenden beim Scrollen */
  .reveal { opacity: 0; transform: translateY(26px); transition: opacity .8s ease, transform .8s ease; }
  .reveal.visible { opacity: 1; transform: none; }
  @media (prefers-reduced-motion: reduce) { .reveal { opacity: 1; transform: none; transition: none; } }
  /* Farbstudie */
  .swatch { width: 44px; height: 44px; border-radius: 9999px; border: 3px solid #fff; box-shadow: 0 2px 8px rgba(16,28,61,.2); cursor: pointer; transition: transform .25s ease, box-shadow .25s ease; }
  .swatch:hover { transform: scale(1.15); }
  .swatch.aktiv { transform: scale(1.15); box-shadow: 0 0 0 3px #101c3d, 0 2px 8px rgba(16,28,61,.3); }
  #haus-fassade, #haus-giebel { transition: fill .5s ease; }
</style>
""").strip()


# Scroll-Einblendung: alle Sektionen und Seiten-Heros sanft einblenden
SCRIPTS = dedent("""
<script>
(function () {
  var els = Array.prototype.slice.call(document.querySelectorAll('section, body > header'));
  els.forEach(function (e) { e.classList.add('reveal'); });
  function check() {
    var limit = window.innerHeight * 0.92;
    els.forEach(function (e) {
      if (!e.classList.contains('visible') && e.getBoundingClientRect().top < limit) {
        e.classList.add('visible');
      }
    });
  }
  check();
  window.addEventListener('scroll', check, { passive: true });
  window.addEventListener('resize', check);
  setInterval(check, 600);
})();
</script>
""").strip()

# Interaktive Farbstudie: Haus per Klick umfaerben
FARBSTUDIE = dedent("""
<section class="bg-paper" id="farbstudie">
  <div class="max-w-6xl mx-auto px-6 py-14 md:py-20 grid md:grid-cols-2 gap-8 md:gap-14 items-center">
    <div>
      <span class="eyebrow text-ink-soft block mb-4">Zum Ausprobieren</span>
      <h2 class="font-display text-3xl md:text-4xl text-ink mb-5">Welche Farbe passt zu Ihrem Haus?</h2>
      <span class="accent-bar mb-6"></span>
      <p class="text-ink-soft text-[16px] leading-relaxed mb-8">Klicken Sie auf einen Farbton und sehen Sie sofort, wie die Fassade wirkt. Genau so erstellen wir professionelle Farbstudien am Computer, mit Ihrem Haus als Vorlage und allen Nuancen ab Bildschirm.</p>
      <div class="flex flex-wrap gap-3 mb-5" id="swatches" aria-label="Fassadenfarbe wählen"></div>
      <p class="text-[14px] text-ink-soft mb-9">Gewählter Farbton: <span id="farbname" class="font-semibold text-ink">Sonnengelb</span></p>
      <a href="kontakt.html" class="bg-ink text-white text-[13px] font-semibold tracking-[0.14em] uppercase px-7 py-4 rounded hover:bg-[#1a2a55] transition-colors inline-block">Farbstudie für mein Haus anfragen</a>
    </div>
    <div class="bg-mist border border-line rounded-lg p-6 md:p-10">
      <svg viewBox="0 0 480 340" role="img" aria-label="Haus mit wählbarer Fassadenfarbe" class="w-full h-auto">
        <ellipse cx="240" cy="320" rx="215" ry="14" fill="#e0e3e8"/>
        <polygon id="haus-giebel" points="240,52 100,140 380,140" fill="#E8C64B"/>
        <polygon points="240,40 82,140 98,140 240,52 382,140 398,140" fill="#3a4046"/>
        <rect id="haus-fassade" x="100" y="140" width="280" height="178" fill="#E8C64B"/>
        <rect x="100" y="140" width="280" height="8" fill="rgba(0,0,0,.08)"/>
        <rect x="126" y="166" width="52" height="62" rx="2" fill="#ffffff"/>
        <rect x="130" y="170" width="44" height="54" fill="#bcd6e8"/>
        <line x1="152" y1="170" x2="152" y2="224" stroke="#ffffff" stroke-width="3"/>
        <rect x="302" y="166" width="52" height="62" rx="2" fill="#ffffff"/>
        <rect x="306" y="170" width="44" height="54" fill="#bcd6e8"/>
        <line x1="328" y1="170" x2="328" y2="224" stroke="#ffffff" stroke-width="3"/>
        <rect x="126" y="248" width="52" height="62" rx="2" fill="#ffffff"/>
        <rect x="130" y="252" width="44" height="54" fill="#bcd6e8"/>
        <line x1="152" y1="252" x2="152" y2="306" stroke="#ffffff" stroke-width="3"/>
        <rect x="302" y="248" width="52" height="62" rx="2" fill="#ffffff"/>
        <rect x="306" y="252" width="44" height="54" fill="#bcd6e8"/>
        <line x1="328" y1="252" x2="328" y2="306" stroke="#ffffff" stroke-width="3"/>
        <rect x="216" y="238" width="48" height="80" rx="3" fill="#59616b"/>
        <circle cx="256" cy="280" r="3" fill="#fddc00"/>
        <rect x="212" y="70" width="18" height="42" fill="#59616b"/>
        <circle cx="412" cy="284" r="22" fill="#a9b7a0"/>
        <rect x="408" y="300" width="8" height="18" fill="#8a7a63"/>
        <circle cx="66" cy="292" r="16" fill="#a9b7a0"/>
      </svg>
    </div>
  </div>
</section>
<script>
(function () {
  var farben = [
    ["Altweiss", "#EAE4D6"], ["Sandbeige", "#D8C6A5"], ["Terracotta", "#C1713F"],
    ["Rosé", "#D6A99C"], ["Salbeigrün", "#A9B7A0"], ["Taubenblau", "#7F97AD"],
    ["Sonnengelb", "#E8C64B"], ["Graphit", "#555B63"]
  ];
  var wrap = document.getElementById('swatches');
  if (!wrap) return;
  farben.forEach(function (f, idx) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'swatch' + (f[0] === 'Sonnengelb' ? ' aktiv' : '');
    b.style.background = f[1];
    b.title = f[0];
    b.setAttribute('aria-label', 'Fassadenfarbe ' + f[0]);
    b.addEventListener('click', function () {
      document.getElementById('haus-fassade').setAttribute('fill', f[1]);
      document.getElementById('haus-giebel').setAttribute('fill', f[1]);
      document.getElementById('farbname').textContent = f[0];
      wrap.querySelectorAll('.swatch').forEach(function (s) { s.classList.remove('aktiv'); });
      b.classList.add('aktiv');
    });
    wrap.appendChild(b);
  });
})();
</script>
""").strip()


def nav_html(active: str) -> str:
    items = []
    for href, label in NAV_LINKS:
        slug = href.replace(".html", "")
        cls = "text-ink font-semibold border-b-2 border-accent pb-0.5" if active == slug else "text-ink-soft hover:text-ink transition-colors"
        items.append(f'<a class="text-[15px] {cls}" href="{href}">{label}</a>')
    return "\n        ".join(items)


def mobile_nav_html(active: str) -> str:
    items = []
    for href, label in NAV_LINKS:
        slug = href.replace(".html", "")
        cls = "text-ink font-semibold" if active == slug else "text-ink-soft"
        items.append(f'<a class="py-2.5 text-[16px] border-b border-line {cls}" href="{href}">{label}</a>')
    return "\n          ".join(items)


def header_html(active: str) -> str:
    return dedent(f"""
    <div class="bg-ink text-white/90 text-[13px]">
      <div class="max-w-6xl mx-auto px-6 flex justify-between items-center h-9">
        <span class="hidden sm:block tracking-wide">Wir setzen Zeichen mit Farbe · Luzern · Hergiswil NW · Alpnach OW</span>
        <span class="flex items-center gap-5">
          <a href="tel:{PHONE_LINK}" class="hover:text-accent transition-colors flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px]">call</span>{PHONE_DISPLAY}</a>
          <a href="mailto:{EMAIL}" class="hidden md:flex hover:text-accent transition-colors items-center gap-1.5"><span class="material-symbols-outlined text-[16px]">mail</span>{EMAIL}</a>
        </span>
      </div>
    </div>
    <nav class="sticky top-0 z-50 bg-white border-b border-line shadow-sm">
      <div class="relative max-w-6xl mx-auto px-6 flex items-center justify-between h-28 md:h-52 gap-6">
        <a href="index.html" class="flex items-center shrink-0 absolute left-1/2 -translate-x-1/2 md:static md:left-auto md:translate-x-0">
          <img src="assets/logo.png" alt="Bühlmann Söhne AG, Maler und Gipser in Luzern" class="h-20 md:h-[200px] w-auto logo-anim" />
        </a>
        <div class="hidden md:flex items-center gap-7">
        {nav_html(active)}
        </div>
        <div class="flex items-center gap-3 ml-auto md:ml-0">
          <a href="kontakt.html" class="hidden sm:block bg-ink text-white text-[13px] font-semibold tracking-[0.14em] uppercase px-5 py-3 rounded hover:bg-[#1a2a55] transition-colors whitespace-nowrap">Offerte anfragen</a>
          <button type="button" class="md:hidden p-2 text-ink" aria-label="Menü öffnen" onclick="document.getElementById('mobilemenu').classList.toggle('hidden')">
            <span class="material-symbols-outlined text-[28px]">menu</span>
          </button>
        </div>
      </div>
      <div id="mobilemenu" class="hidden md:hidden border-t border-line bg-white">
        <div class="max-w-6xl mx-auto px-6 py-4 flex flex-col gap-1">
          {mobile_nav_html(active)}
          <a href="kontakt.html" class="mt-3 bg-ink text-white text-center text-[13px] font-semibold tracking-[0.14em] uppercase px-5 py-3.5 rounded">Offerte anfragen</a>
        </div>
      </div>
    </nav>
    """).strip()


def footer_html() -> str:
    service_links = "".join(
        f'<li><a class="hover:text-ink transition-colors" href="{s["slug"]}.html">{s["nav"]}</a></li>' for s in SERVICES
    )
    region_links = "".join(
        f'<li><a class="hover:text-ink transition-colors" href="{r["slug"]}.html">Maler {r["name"]}</a></li>' for r in REGIONS
    )
    return dedent(f"""
    <footer class="bg-mist border-t border-line">
      <div class="max-w-6xl mx-auto px-6 py-16 grid grid-cols-1 md:grid-cols-4 gap-10">
        <div>
          <img src="assets/logo.png" alt="Bühlmann Söhne AG" class="h-16 w-auto mb-5" />
          <p class="text-ink-soft text-[15px] leading-relaxed">Malerei und Gipserei in Luzern seit 1935. Familienbetrieb in dritter Generation.</p>
          <p class="mt-4 text-[13px] text-ink-soft italic">«Wir setzen Zeichen mit Farbe»</p>
        </div>
        <div>
          <h4 class="eyebrow text-ink mb-5">Leistungen</h4>
          <ul class="space-y-2.5 text-ink-soft text-[15px]">{service_links}</ul>
        </div>
        <div>
          <h4 class="eyebrow text-ink mb-5">Einsatzgebiet</h4>
          <ul class="space-y-2.5 text-ink-soft text-[15px]">{region_links}</ul>
        </div>
        <div>
          <h4 class="eyebrow text-ink mb-5">Kontakt</h4>
          <ul class="space-y-2.5 text-ink-soft text-[15px]">
            <li class="font-semibold text-ink">Bühlmann Söhne AG</li>
            <li>{ADDRESS}, {CITY}</li>
            <li><a href="tel:{PHONE_LINK}" class="hover:text-ink">Tel. {PHONE_DISPLAY}</a></li>
            <li><a href="mailto:{EMAIL}" class="hover:text-ink">{EMAIL}</a></li>
            <li><a href="{MAPS_URL}" target="_blank" rel="noopener" class="underline decoration-accent decoration-2 underline-offset-4 hover:text-ink">Auf Google Maps zeigen</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-line">
        <div class="max-w-6xl mx-auto px-6 py-5 flex flex-col md:flex-row justify-between items-center gap-3 text-[13px] text-ink-soft">
          <span>v{VERSION}</span>
          <span>© 2026 Bühlmann Söhne AG · {ADDRESS} · {CITY}</span>
          <span class="flex items-center gap-1.5"><span class="material-symbols-outlined text-[16px] text-ink">verified</span>Schweizer Handwerk seit 1935</span>
        </div>
      </div>
    </footer>
    """).strip()


def schema_org(page_url: str, extra: str = "") -> str:
    return (
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@graph":[{"@type":"LocalBusiness","@id":"' + SITE_URL + '/#org",'
        '"name":"Bühlmann Söhne AG","image":"' + SITE_URL + '/assets/logo.png","logo":"' + SITE_URL + '/assets/logo.png",'
        '"slogan":"Wir setzen Zeichen mit Farbe",'
        '"telephone":"+41 41 269 88 50","email":"' + EMAIL + '",'
        '"url":"' + page_url + '",'
        '"address":{"@type":"PostalAddress","streetAddress":"' + ADDRESS + '","addressLocality":"Luzern","postalCode":"6015","addressCountry":"CH"},'
        '"areaServed":["Luzern","Emmen","Kriens","Hergiswil","Alpnach","Nidwalden","Obwalden","Innerschweiz"],'
        '"foundingDate":"1935","founder":{"@type":"Person","name":"Harry Bühlmann"},'
        '"employee":{"@type":"Person","name":"Patrick Bühlmann","jobTitle":"Geschäftsführer"},'
        '"numberOfEmployees":{"@type":"QuantitativeValue","value":13}}'
        + ("," + extra if extra else "") + "]}"
        "</script>"
    )


def page_shell(slug: str, title: str, meta: str, og_image: str, body: str, extra_schema: str = "") -> str:
    page_url = f"{SITE_URL}/" if slug == "index" else f"{SITE_URL}/{slug}.html"
    return dedent(f"""<!DOCTYPE html>
<html lang="de">
<head>
{HEAD_BASE}
<title>{title}</title>
<meta name="description" content="{meta}" />
<link rel="canonical" href="{page_url}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{meta}" />
<meta property="og:image" content="{og_image if og_image.startswith("http") else SITE_URL + "/" + og_image}" />
<meta property="og:url" content="{page_url}" />
<meta name="robots" content="index, follow" />
{schema_org(page_url, extra_schema)}
</head>
<body class="bg-paper text-ink antialiased">
{header_html(slug)}
{body}
{footer_html()}
{SCRIPTS}
</body>
</html>""").strip()


def hero_light(eyebrow: str, h1: str, lead: str, image: str, cta_label: str, cta_href: str = "kontakt.html") -> str:
    """Heller, edler Seiten-Hero: Text links, Bild rechts."""
    return dedent(f"""
    <header class="bg-paper">
      <div class="max-w-6xl mx-auto px-6 pt-12 pb-12 md:pt-24 md:pb-20 grid md:grid-cols-2 gap-12 items-center">
        <div>
          <span class="eyebrow text-ink-soft block mb-4">{eyebrow}</span>
          <h1 class="font-display text-4xl md:text-5xl leading-[1.12] text-ink mb-6">{h1}</h1>
          <span class="accent-bar mb-6"></span>
          <p class="text-ink-soft text-lg leading-relaxed mb-9 max-w-xl">{lead}</p>
          <div class="flex flex-wrap gap-4">
            <a href="{cta_href}" class="bg-ink text-white text-[13px] font-semibold tracking-[0.14em] uppercase px-7 py-4 rounded hover:bg-[#1a2a55] transition-colors">{cta_label}</a>
            <a href="tel:{PHONE_LINK}" class="border border-line bg-white text-ink text-[13px] font-semibold tracking-[0.14em] uppercase px-7 py-4 rounded hover:border-ink transition-colors flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">call</span>{PHONE_DISPLAY}</a>
          </div>
        </div>
        <div class="relative">
          <div class="absolute -top-4 -left-4 w-full h-full rounded-lg bg-accent/25" aria-hidden="true"></div>
          <img src="{image}" alt="{h1}" class="relative rounded-lg shadow-xl w-full aspect-[4/3] object-cover" />
        </div>
      </div>
    </header>
    """).strip()


def cta_section(title: str) -> str:
    return dedent(f"""
    <section class="bg-ink text-white">
      <div class="max-w-4xl mx-auto px-6 py-14 md:py-20 text-center">
        <h2 class="font-display text-3xl md:text-4xl mb-5">{title}</h2>
        <p class="text-white/75 text-lg mb-9">Rufen Sie uns an oder schreiben Sie uns. Wir beraten Sie gerne persönlich.</p>
        <div class="flex flex-wrap gap-4 justify-center">
          <a href="tel:{PHONE_LINK}" class="bg-accent text-ink text-[13px] font-semibold tracking-[0.14em] uppercase px-8 py-4 rounded hover:bg-accent-deep transition-colors flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">call</span>{PHONE_DISPLAY}</a>
          <a href="kontakt.html" class="border border-white/30 text-white text-[13px] font-semibold tracking-[0.14em] uppercase px-8 py-4 rounded hover:bg-white/10 transition-colors">Kontaktformular</a>
        </div>
      </div>
    </section>
    """).strip()


def contact_form(fid: str = "kontaktform") -> str:
    """Wiederverwendbares Kontaktformular (sendet an /api/kontakt)."""
    sid = fid + "-status"
    return dedent(f"""
    <form id="{fid}" class="bg-white border border-line rounded-lg p-8 space-y-5">
      <p class="text-[14px] text-ink-soft">Wir melden uns so rasch wie möglich bei Ihnen zurück.</p>
      <div>
        <label class="block text-[14px] font-semibold text-ink mb-1.5" for="{fid}-name">Name*</label>
        <input required id="{fid}-name" name="name" type="text" autocomplete="name" class="w-full rounded border-line focus:border-ink focus:ring-accent" />
      </div>
      <div>
        <label class="block text-[14px] font-semibold text-ink mb-1.5" for="{fid}-email">E-Mail*</label>
        <input required id="{fid}-email" name="email" type="email" autocomplete="email" class="w-full rounded border-line focus:border-ink focus:ring-accent" />
      </div>
      <div>
        <label class="block text-[14px] font-semibold text-ink mb-1.5" for="{fid}-tel">Telefon</label>
        <input id="{fid}-tel" name="tel" type="tel" autocomplete="tel" class="w-full rounded border-line focus:border-ink focus:ring-accent" />
      </div>
      <div>
        <label class="block text-[14px] font-semibold text-ink mb-1.5" for="{fid}-msg">Nachricht*</label>
        <textarea required id="{fid}-msg" name="msg" rows="5" class="w-full rounded border-line focus:border-ink focus:ring-accent"></textarea>
      </div>
      <input type="text" name="website" tabindex="-1" autocomplete="off" class="hidden" aria-hidden="true" />
      <button type="submit" class="bg-ink text-white text-[13px] font-semibold tracking-[0.14em] uppercase px-7 py-4 rounded hover:bg-[#1a2a55] transition-colors w-full">Nachricht senden</button>
      <p id="{sid}" class="text-[14px] hidden" role="status"></p>
    </form>
    <script>
    (function () {{
      var f = document.getElementById('{fid}');
      if (!f) return;
      var s = document.getElementById('{sid}');
      f.addEventListener('submit', function (e) {{
        e.preventDefault();
        var btn = f.querySelector('button[type=submit]');
        btn.disabled = true; btn.textContent = 'Wird gesendet …';
        s.className = 'text-[14px] text-ink-soft'; s.textContent = '';
        var data = {{ name: f.name.value, email: f.email.value, tel: f.tel.value, msg: f.msg.value, website: f.website.value }};
        fetch('/api/kontakt', {{ method: 'POST', headers: {{ 'content-type': 'application/json' }}, body: JSON.stringify(data) }})
          .then(function (r) {{ return r.json().then(function (j) {{ return {{ ok: r.ok, j: j }}; }}); }})
          .then(function (res) {{
            if (res.ok && res.j.ok) {{
              f.reset();
              s.className = 'text-[14px] text-green-700 font-semibold';
              s.textContent = 'Vielen Dank! Ihre Nachricht ist bei uns eingegangen.';
            }} else {{
              s.className = 'text-[14px] text-red-600 font-semibold';
              s.textContent = (res.j && res.j.error) || 'Es ist ein Fehler aufgetreten. Bitte rufen Sie uns an: {PHONE_DISPLAY}.';
            }}
          }})
          .catch(function () {{
            s.className = 'text-[14px] text-red-600 font-semibold';
            s.textContent = 'Verbindung fehlgeschlagen. Bitte rufen Sie uns an: {PHONE_DISPLAY}.';
          }})
          .finally(function () {{ btn.disabled = false; btn.textContent = 'Nachricht senden'; }});
      }});
    }})();
    </script>
    """).strip()


# ---------------------------------------------------------------------------
# Startseite
# ---------------------------------------------------------------------------
def index_page() -> str:
    service_cards = [
        ("Innenmalerei", "innenmalerei.html", "format_paint", "Malen, Spritzen und Tapezieren für jeden Innenraum, vom Altbau bis zum Büro."),
        ("Fassaden", "fassaden.html", "apartment", "Renovation und Isolation jeder Fassade, mit eigenen Gerüsten und Farbstudien am Computer."),
        ("Renovation", "renovation.html", "history_edu", "Sorgfalt und Liebe zum Detail, inklusive Werterhaltungs-Kundendienst mit Garantie."),
        ("Neubau und Umbau", "neubau.html", "domain_add", "Eingespielter Partner für Architekten, Generalunternehmer und private Bauherren."),
        ("Spritzwerk", "spritzwerk.html", "airline_seat_flat", "Eigene Spritzanlage für Bauteile und Jalousieläden im Thermo-Lackier-Verfahren."),
        ("Gipserei", "gipserei.html", "handyman", "Kundengipserei für prompte Einsätze, Verputzarbeiten und Betonsanierungen."),
    ]
    cards_html = "\n".join(
        f'<a href="{href}" class="card-lift bg-white border border-line rounded-lg p-8 block group">'
        f'<span class="material-symbols-outlined text-4xl text-ink mb-5">{icon}</span>'
        f'<h3 class="font-display text-xl text-ink mb-3">{title}</h3>'
        f'<p class="text-ink-soft text-[15px] leading-relaxed mb-5">{desc}</p>'
        f'<span class="text-[13px] font-semibold tracking-[0.14em] uppercase text-ink border-b-2 border-accent pb-1">Mehr erfahren</span>'
        f'</a>'
        for title, href, icon, desc in service_cards
    )

    refs = [
        ("assets/referenz-ueberbauung.jpg", "Wohnüberbauung, Neubau"),
        ("assets/referenz-altstadt.jpg", "Stadthaus Luzern, Fassade"),
        ("assets/referenz-wohnung.jpg", "Wohnungsrenovation"),
    ]
    refs_html = "\n".join(
        f'<figure class="card-lift rounded-lg overflow-hidden bg-white border border-line">'
        f'<img src="{img}" alt="{cap}" class="w-full aspect-[4/3] object-cover" />'
        f'<figcaption class="px-5 py-4 text-[14px] text-ink-soft">{cap}</figcaption>'
        f'</figure>'
        for img, cap in refs
    )

    body = dedent(f"""
    <header class="relative min-h-[82vh] flex items-center overflow-hidden bg-ink">
      <video class="absolute inset-0 w-full h-full object-cover" autoplay muted loop playsinline preload="metadata" poster="assets/hero-poster.jpg" aria-label="Einblick in die Arbeit der Bühlmann Söhne AG">
        <source src="assets/hero-loop.mp4" type="video/mp4" />
      </video>
      <div class="absolute inset-0 bg-gradient-to-r from-ink/85 via-ink/55 to-ink/25" aria-hidden="true"></div>
      <div class="relative max-w-6xl mx-auto px-6 py-24 w-full">
        <div class="max-w-2xl">
          <span class="eyebrow text-accent block mb-5">Malerei und Gipserei in Luzern · seit 1935</span>
          <h1 class="font-display text-5xl md:text-6xl leading-[1.08] text-white mb-7">Wir setzen Zeichen mit&nbsp;Farbe.</h1>
          <span class="accent-bar mb-7"></span>
          <p class="text-white/85 text-lg leading-relaxed mb-10 max-w-xl">Familienbetrieb in dritter Generation. Malerarbeiten innen und aussen, Kundengipserei und eigenes Spritzwerk, in Luzern, Hergiswil NW und Alpnach OW.</p>
          <div class="flex flex-wrap gap-4">
            <a href="kontakt.html" class="bg-accent text-ink text-[13px] font-semibold tracking-[0.14em] uppercase px-8 py-4 rounded hover:bg-accent-deep transition-colors shadow-xl">Offerte anfragen</a>
            <a href="malerei.html" class="border border-white/40 text-white text-[13px] font-semibold tracking-[0.14em] uppercase px-8 py-4 rounded hover:bg-white/10 transition-colors">Unsere Leistungen</a>
          </div>
          <div class="mt-12 grid grid-cols-3 gap-6 max-w-md">
            <div><span class="font-display text-3xl text-white block">1935</span><span class="text-[13px] text-white/70">gegründet</span></div>
            <div><span class="font-display text-3xl text-white block">3.</span><span class="text-[13px] text-white/70">Generation</span></div>
            <div><span class="font-display text-3xl text-white block">13</span><span class="text-[13px] text-white/70">Mitarbeitende</span></div>
          </div>
        </div>
      </div>
    </header>

    <section class="bg-mist border-y border-line">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20">
        <div class="text-center mb-8 md:mb-12">
          <span class="eyebrow text-ink-soft block mb-3">Unsere Leistungen</span>
          <h2 class="font-display text-3xl md:text-4xl text-ink">Das komplette Maler- und Gipserhandwerk</h2>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
          {cards_html}
        </div>
      </div>
    </section>

    <section class="bg-paper">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20 grid md:grid-cols-2 gap-8 md:gap-14 items-center">
        <div class="relative order-2 md:order-1">
          <img src="assets/arbeit-roller.jpg" alt="Maler der Bühlmann Söhne AG bei der Arbeit" class="rounded-lg shadow-lg w-full aspect-[4/3] object-cover" />
          <img src="assets/referenz-altstadt.jpg" alt="Referenzobjekt in der Stadt Luzern" class="hidden md:block absolute -bottom-8 -right-8 w-56 rounded-lg shadow-xl border-4 border-white" />
        </div>
        <div class="order-1 md:order-2">
          <span class="eyebrow text-ink-soft block mb-4">Unternehmen</span>
          <h2 class="font-display text-3xl md:text-4xl text-ink mb-5">Drei Generationen Handwerk</h2>
          <span class="accent-bar mb-6"></span>
          <p class="text-ink-soft text-[16px] leading-relaxed mb-4">1935 von Harry Bühlmann in einer einfachen Garage an der Dammstrasse gegründet, ist die Bühlmann Söhne AG heute ein moderner Betrieb im eigenen Gebäude im Rothenbad, Luzern.</p>
          <p class="text-ink-soft text-[16px] leading-relaxed mb-8">Geschäftsführer Patrick Bühlmann führt das Unternehmen mit 10 Malern und 3 Mitarbeitenden in der Administration. Moderne Maschinen und ein umfangreicher Wagenpark sorgen für effizientes Arbeiten. Und weil uns der Nachwuchs wichtig ist, bilden wir regelmässig Malerlehrlinge aus.</p>
          <a href="unternehmen.html" class="text-[13px] font-semibold tracking-[0.14em] uppercase text-ink border-b-2 border-accent pb-1">Geschichte und Leitbild</a>
        </div>
      </div>
    </section>

    <section class="bg-ink text-white overflow-hidden">
      <div class="max-w-4xl mx-auto px-6 py-14 md:py-20 text-center flex flex-col items-center">
        <span class="eyebrow text-accent block mb-6 text-lg md:text-2xl tracking-[0.4em]">Sponsor</span>
        <div class="bg-white rounded-2xl p-6 md:p-8 flex items-center justify-center w-44 h-44 md:w-56 md:h-56 mb-8">
          <img src="assets/fcl-logo.png" alt="FC Luzern" class="w-full h-full object-contain" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" />
          <span class="material-symbols-outlined text-ink" style="display:none;font-size:120px;">sports_soccer</span>
        </div>
        <h2 class="font-display text-3xl md:text-5xl leading-[1.1] mb-5">Stolzer Sponsor des FC&nbsp;Luzern</h2>
        <span class="accent-bar mb-6"></span>
        <p class="text-white/80 text-lg leading-relaxed max-w-xl">Als Luzerner Familienbetrieb stehen wir hinter dem FC Luzern, mit Herzblut und Farbe.</p>
      </div>
    </section>

    {FARBSTUDIE}

    <section class="bg-paper border-y border-line">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20">
        <div class="flex flex-wrap items-end justify-between gap-6 mb-8 md:mb-12">
          <div>
            <span class="eyebrow text-ink-soft block mb-3">Referenzen</span>
            <h2 class="font-display text-3xl md:text-4xl text-ink">Spuren unserer Arbeit</h2>
          </div>
          <a href="referenzen.html" class="text-[13px] font-semibold tracking-[0.14em] uppercase text-ink border-b-2 border-accent pb-1">Alle Referenzen</a>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
          {refs_html}
        </div>
      </div>
    </section>

    <section class="bg-paper">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20 grid md:grid-cols-2 gap-8 md:gap-14 items-center">
        <div>
          <span class="eyebrow text-ink-soft block mb-4">Einsatzgebiet</span>
          <h2 class="font-display text-3xl md:text-4xl text-ink mb-5">Drei Standorte, eine Region</h2>
          <span class="accent-bar mb-6"></span>
          <p class="text-ink-soft text-[16px] leading-relaxed mb-8">Von Luzern, Hergiswil NW und Alpnach OW aus sind wir in der ganzen Innerschweiz im Einsatz. Spuren unserer Arbeit finden sich auf Fassaden und in Wohn- und Geschäftsräumen der ganzen Region.</p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <a href="maler-luzern.html" class="bg-white border border-line rounded px-5 py-4 flex justify-between items-center hover:border-ink transition-colors"><span class="font-semibold text-[15px]">Maler Luzern</span><span class="material-symbols-outlined text-[18px]">arrow_forward</span></a>
            <a href="maler-emmen.html" class="bg-white border border-line rounded px-5 py-4 flex justify-between items-center hover:border-ink transition-colors"><span class="font-semibold text-[15px]">Maler Emmen</span><span class="material-symbols-outlined text-[18px]">arrow_forward</span></a>
            <a href="maler-kriens.html" class="bg-white border border-line rounded px-5 py-4 flex justify-between items-center hover:border-ink transition-colors"><span class="font-semibold text-[15px]">Maler Kriens</span><span class="material-symbols-outlined text-[18px]">arrow_forward</span></a>
            <a href="maler-hergiswil.html" class="bg-white border border-line rounded px-5 py-4 flex justify-between items-center hover:border-ink transition-colors"><span class="font-semibold text-[15px]">Maler Hergiswil NW</span><span class="material-symbols-outlined text-[18px]">arrow_forward</span></a>
            <a href="maler-alpnach.html" class="bg-white border border-line rounded px-5 py-4 flex justify-between items-center hover:border-ink transition-colors"><span class="font-semibold text-[15px]">Maler Alpnach OW</span><span class="material-symbols-outlined text-[18px]">arrow_forward</span></a>
          </div>
        </div>
        <div class="bg-mist border border-line rounded-lg p-10">
          <span class="eyebrow text-ink-soft block mb-4">Jobs</span>
          <h3 class="font-display text-2xl text-ink mb-4">Wir suchen dich: Maler/in EFZ, 100 %</h3>
          <p class="text-ink-soft text-[15px] leading-relaxed mb-6">Kleines Team, familiärer Stil, vielseitige Aufgaben in Kundenmalerei, Renovation und Neubau. Per sofort oder nach Vereinbarung.</p>
          <a href="jobs.html" class="bg-ink text-white text-[13px] font-semibold tracking-[0.14em] uppercase px-6 py-3.5 rounded inline-block hover:bg-[#1a2a55] transition-colors">Zur Stellenanzeige</a>
          <p class="text-[13px] text-ink-soft mt-5">Wir bilden ausserdem regelmässig Malerlehrlinge aus.</p>
        </div>
      </div>
    </section>

    <section id="kontakt" class="bg-mist border-y border-line">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20 grid md:grid-cols-2 gap-12 items-start">
        <div>
          <span class="eyebrow text-ink-soft block mb-4">Kontakt</span>
          <h2 class="font-display text-3xl md:text-4xl text-ink mb-5">Bereit für Ihr Projekt?</h2>
          <span class="accent-bar mb-6"></span>
          <p class="text-ink-soft text-[16px] leading-relaxed mb-8">Schreiben Sie uns direkt oder rufen Sie an. Kostenlose Vor-Ort-Besichtigung und persönliche Beratung.</p>
          <div class="space-y-3">
            <a href="tel:{PHONE_LINK}" class="flex items-center gap-3 text-ink hover:text-ink-soft"><span class="material-symbols-outlined">call</span><span class="font-semibold">{PHONE_DISPLAY}</span></a>
            <a href="mailto:{EMAIL}" class="flex items-center gap-3 text-ink hover:text-ink-soft"><span class="material-symbols-outlined">mail</span><span class="font-semibold">{EMAIL}</span></a>
            <div class="flex items-center gap-3 text-ink-soft"><span class="material-symbols-outlined">location_on</span><span>{ADDRESS}, {CITY}</span></div>
          </div>
        </div>
        <div>
          {contact_form("homeform")}
        </div>
      </div>
    </section>

    {cta_section("Wir freuen uns auf Sie")}
    """).strip()

    return page_shell(
        "index",
        "Maler Luzern | Bühlmann Söhne AG | Malerei und Gipserei seit 1935",
        "Bühlmann Söhne AG: Maler und Gipser in Luzern seit 1935. Innenmalerei, Fassaden, Renovation, Neubau, Spritzwerk. Standorte Luzern, Hergiswil NW, Alpnach OW. Tel. 041 269 88 50.",
        "assets/hero-farben.jpg",
        body,
    )


# ---------------------------------------------------------------------------
# Malerei-Übersicht
# ---------------------------------------------------------------------------
def malerei_page() -> str:
    blocks = [
        ("Innen", "assets/team-streichen.jpg", "Malen, Spritzen, Tapezieren: Mit Spachtel, Pinsel, Spritzpistole und Tapetenbürste verschönern wir jeden Innenraum. Ob denkmalgeschützte Ratsherrenstube, modernes Bürogebäude oder Industriebau.", "innenmalerei.html"),
        ("Aussen", "assets/arbeit-fassade.jpg", "Ob Holz, Beton, Naturstein, Verputz, Metall oder Kunststoff: Wir bearbeiten jede Fassade fachmännisch. Eigene Roll- und Fassadengerüste machen uns schnell und flexibel.", "fassaden.html"),
        ("Unser Spritzwerk", IMG_FARBEIMER, "Mit unserer modernen Spritzanlage für Industrie- und Bauteile lackieren wir auch grossflächige Gegenstände wie Jalousieläden im Thermo-Lackier-Verfahren.", "spritzwerk.html"),
        ("Kundengipserei", IMG_ROLLER, "Unsere Kundengipserei ist für Einsätze jeglicher Art ausgerüstet. Verputzarbeiten und Betonsanierungen erledigen wir prompt und unkompliziert.", "gipserei.html"),
    ]
    blocks_html = "\n".join(
        f'<div class="grid md:grid-cols-2 gap-10 items-center {"md:[direction:rtl]" if i % 2 else ""}">'
        f'<div class="[direction:ltr]"><img src="{img}" alt="{title}, Bühlmann Söhne AG" class="rounded-lg shadow-lg w-full aspect-[16/9] object-cover" /></div>'
        f'<div class="[direction:ltr]">'
        f'<h2 class="font-display text-2xl md:text-3xl text-ink mb-4">{title}</h2>'
        f'<span class="accent-bar mb-5"></span>'
        f'<p class="text-ink-soft text-[16px] leading-relaxed mb-6">{desc}</p>'
        f'<a href="{href}" class="text-[13px] font-semibold tracking-[0.14em] uppercase text-ink border-b-2 border-accent pb-1">Mehr erfahren</a>'
        f'</div></div>'
        for i, (title, img, desc, href) in enumerate(blocks)
    )

    detail_links = "\n".join(
        f'<a href="{s["slug"]}.html" class="bg-white border border-line rounded px-5 py-4 flex justify-between items-center hover:border-ink transition-colors"><span class="font-semibold text-[15px]">{s["nav"]}</span><span class="material-symbols-outlined text-[18px]">arrow_forward</span></a>'
        for s in SERVICES
    )

    body = dedent(f"""
    {hero_light("Malerei", "Seit über 90 Jahren Farbe im Alltag", "Spuren unserer Arbeit finden Sie in der ganzen Schweiz, auf Gebäudefassaden ebenso wie in Wohn- und Geschäftsräumen. Traditionelles Handwerk, kombiniert mit zukunftsorientierten Techniken und neuen Werkstoffen.", "assets/hero-farben.jpg", "Offerte anfragen")}

    <section class="bg-mist border-y border-line">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20 space-y-14 md:space-y-20">
        {blocks_html}
      </div>
    </section>

    <section class="bg-paper">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20">
        <div class="text-center mb-10">
          <span class="eyebrow text-ink-soft block mb-3">Kompetente Mitarbeitende</span>
          <h2 class="font-display text-3xl text-ink mb-5">Qualität vor Quantität</h2>
          <p class="text-ink-soft text-[16px] leading-relaxed max-w-3xl mx-auto">Unser Team umfasst kompetente Fachleute für Neu- und Umbauten sowie Renovationen im Innen- und Aussenbereich. Dank laufender Weiterbildung sind unsere Mitarbeitenden stets auf dem neusten Stand der Technik. Die Nachwuchsförderung ist uns seit jeher ein wichtiges Anliegen: Wir bilden regelmässig Malerlehrlinge aus.</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 max-w-4xl mx-auto">
          {detail_links}
        </div>
      </div>
    </section>

    {cta_section("Welches Projekt dürfen wir für Sie umsetzen?")}
    """).strip()

    return page_shell(
        "malerei",
        "Malerei Luzern | Innen, Aussen, Spritzwerk, Gipserei | Bühlmann Söhne AG",
        "Das komplette Maler- und Gipserhandwerk in Luzern: Innenmalerei, Fassaden, Spritzwerk und Kundengipserei. Seit über 90 Jahren. Tel. 041 269 88 50.",
        "assets/hero-farben.jpg",
        body,
    )


# ---------------------------------------------------------------------------
# Leistungs-Detailseite
# ---------------------------------------------------------------------------
def service_page(s: dict) -> str:
    sections_html = "\n".join(
        f'<section class="mb-8 md:mb-12"><h2 class="font-display text-2xl md:text-3xl text-ink mb-4">{t}</h2><p class="text-ink-soft text-[16px] leading-relaxed">{b}</p></section>'
        for t, b in s["sections"]
    )
    faq_html = "\n".join(
        f'<details class="bg-white border border-line rounded-lg px-6 py-5 mb-3 group">'
        f'<summary class="font-semibold text-ink cursor-pointer list-none flex justify-between items-center gap-4">{q}<span class="material-symbols-outlined group-open:rotate-180 transition-transform shrink-0">expand_more</span></summary>'
        f'<p class="text-ink-soft text-[15px] leading-relaxed mt-4">{a}</p></details>'
        for q, a in s["faq"]
    )
    faq_schema = (
        '{"@type":"FAQPage","mainEntity":['
        + ",".join(
            '{"@type":"Question","name":"' + q + '","acceptedAnswer":{"@type":"Answer","text":"' + a + '"}}'
            for q, a in s["faq"]
        )
        + "]}"
    )

    farbstudie = FARBSTUDIE if s["slug"] == "fassaden" else ""
    body = dedent(f"""
    {hero_light("Bühlmann Söhne AG · Luzern", s["h1"], s["lead"], s["image"], "Offerte anfragen")}

    <section class="bg-mist border-y border-line">
      <div class="max-w-3xl mx-auto px-6 py-14 md:py-20">
        {sections_html}
      </div>
    </section>

    {farbstudie}

    <section class="bg-paper">
      <div class="max-w-3xl mx-auto px-6 py-14 md:py-20">
        <h2 class="font-display text-3xl text-ink mb-8 text-center">Häufige Fragen</h2>
        {faq_html}
      </div>
    </section>

    {cta_section(s["cta"])}
    """).strip()

    return page_shell(s["slug"], s["title"], s["meta"], s["image"], body, faq_schema)


# ---------------------------------------------------------------------------
# Regionen-Seite
# ---------------------------------------------------------------------------
def region_page(r: dict) -> str:
    sections_html = "\n".join(
        f'<section class="mb-8 md:mb-12"><h2 class="font-display text-2xl md:text-3xl text-ink mb-4">{t}</h2><p class="text-ink-soft text-[16px] leading-relaxed">{b}</p></section>'
        for t, b in r["body"]
    )
    body = dedent(f"""
    {hero_light("Einsatzgebiet · " + r["name"], r["h1"], r["lead"], r.get("image", IMG_GERUEST), "Offerte anfragen")}

    <section class="bg-mist border-y border-line">
      <div class="max-w-3xl mx-auto px-6 py-14 md:py-20">
        {sections_html}
      </div>
    </section>

    {cta_section("Ihr Malerprojekt in " + r["name"] + "?")}
    """).strip()
    return page_shell(r["slug"], r["title"], r["meta"], r.get("image", IMG_GERUEST), body)


# ---------------------------------------------------------------------------
# Unternehmen
# ---------------------------------------------------------------------------
def unternehmen_page() -> str:
    timeline = [
        ("1935", "Firmengründung durch Harry Bühlmann an der Dammstrasse in Luzern, in einer einfachen Garagenunterkunft."),
        ("1940", "Umzug an die Weisenstrasse. Nach dem Krieg floriert die Bauwirtschaft, das Team wächst auf 15 Mitarbeitende."),
        ("1965", "Bezug des neuen Domizils an der Friedbergstrasse 1a: eine damals hochmoderne Malerwerkstatt."),
        ("1969", "Gründung der Abteilung Schriftenmalerei, mit erfolgreichen Synergien zur Malerei."),
        ("1980", "Übernahme durch die zweite Generation: die Söhne von Harry Bühlmann führen den Betrieb weiter."),
        ("1997", "Gründung der Bühlmann Söhne AG. Die dritte Generation wird auf die Nachfolge vorbereitet."),
        ("2000", "Umzug in den modernen Neubau im Rothenbad in Reussbühl, den heutigen Firmensitz."),
        ("2006", "Fokussierung auf die Kernkompetenzen: Kundendienst, Renovation, Fassade, Neubau und Umbau."),
        ("2008", "Patrick Bühlmann erwirbt die Bühlmann Söhne AG und die Liegenschaft Rothenbad 18."),
    ]
    timeline_html = "\n".join(
        f'<div class="relative pl-10 pb-10 border-l-2 border-line last:pb-0">'
        f'<span class="absolute -left-[11px] top-0 w-5 h-5 rounded-full bg-accent border-4 border-white shadow"></span>'
        f'<span class="font-display text-xl text-ink block mb-1.5">{year}</span>'
        f'<p class="text-ink-soft text-[15px] leading-relaxed">{text}</p></div>'
        for year, text in timeline
    )

    facts = [
        ("Gründung", "1935"),
        ("Rechtsform", "Aktiengesellschaft"),
        ("Geschäftsführer", "Patrick Bühlmann"),
        ("Sitz", f"{ADDRESS}, {CITY}"),
        ("Standorte", "Luzern, Hergiswil NW, Alpnach OW"),
        ("Team", "10 Maler, 3 Administration"),
    ]
    facts_html = "\n".join(
        f'<div class="bg-white border border-line rounded-lg px-6 py-5"><span class="eyebrow text-ink-soft block mb-1.5">{k}</span><span class="font-semibold text-ink text-[15px]">{v}</span></div>'
        for k, v in facts
    )

    leitbild = [
        ("Wir gestalten für Ihre Zukunft", "Wir sind ein unabhängiges, regional verankertes Familienunternehmen im Malergewerbe und stolz auf unsere Arbeit. Wir arbeiten innovativ, kompetent und qualitätsbewusst."),
        ("Unsere Kunden sind unsere Arbeitgeber", "Wir legen grossen Wert auf Kundennähe, Lieferbereitschaft und Flexibilität. In Baumalerei und Kundengipserei erbringen wir technologisch fortschrittliche Gesamtleistungen in optimaler Qualität, mit umweltgerechten Massnahmen."),
        ("Wir gestalten mit Menschen für Mitmenschen", "Wir sorgen für Arbeitsbedingungen, die Leistung, Sicherheit und persönliche Entfaltung fördern. Unsere Mitarbeitenden werden aktiv ins Unternehmensgeschehen einbezogen, denn sie sind der Schlüssel zu unserem Erfolg."),
    ]
    leitbild_html = "\n".join(
        f'<div class="bg-white border border-line rounded-lg p-8"><h3 class="font-display text-xl text-ink mb-4">{t}</h3><p class="text-ink-soft text-[15px] leading-relaxed">{b}</p></div>'
        for t, b in leitbild
    )

    body = dedent(f"""
    {hero_light("Unternehmen", "Ein Familienbetrieb in dritter Generation", "Seit 1935 steht der Name Bühlmann in Luzern für sauberes Maler- und Gipserhandwerk. Heute führt Patrick Bühlmann den Betrieb mit 13 Mitarbeitenden im eigenen Gebäude im Rothenbad.", IMG_LUZERN_PANO, "Kontakt aufnehmen")}

    <section class="bg-mist border-y border-line">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20">
        <h2 class="font-display text-3xl text-ink mb-10 text-center">Zahlen und Fakten</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 max-w-4xl mx-auto">
          {facts_html}
        </div>
      </div>
    </section>

    <section class="bg-paper">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20 grid md:grid-cols-2 gap-16">
        <div>
          <span class="eyebrow text-ink-soft block mb-3">Geschichte</span>
          <h2 class="font-display text-3xl text-ink mb-10">Von der Garage zum Neubau</h2>
          {timeline_html}
        </div>
        <div>
          <span class="eyebrow text-ink-soft block mb-3">Betrieb</span>
          <h2 class="font-display text-3xl text-ink mb-10">Modern und dynamisch</h2>
          <img src="assets/firmenwagen.jpg" alt="Firmenwagen der Bühlmann Söhne AG" class="rounded-lg shadow-lg w-full aspect-[16/9] object-cover mb-6" />
          <p class="text-ink-soft text-[15px] leading-relaxed mb-4">Unser moderner Betrieb sowie der umfangreiche Maschinen- und Wagenpark bieten den Mitarbeitenden optimale Arbeitsbedingungen und ermöglichen eine effiziente Arbeitsweise.</p>
          <img src="assets/arbeit-abdecken.jpg" alt="Sorgfältiges Abdecken vor dem Streichen" class="rounded-lg shadow-lg w-full aspect-[16/9] object-cover mb-6" />
          <p class="text-ink-soft text-[15px] leading-relaxed">Dank laufender Weiterbildung sind unsere Fachleute stets auf dem neusten Stand der Technik. Und weil uns der Nachwuchs am Herzen liegt, bilden wir regelmässig Malerlehrlinge aus.</p>
        </div>
      </div>
    </section>

    <section class="bg-mist border-y border-line">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20">
        <div class="text-center mb-8 md:mb-12">
          <span class="eyebrow text-ink-soft block mb-3">Unternehmensleitbild</span>
          <h2 class="font-display text-3xl text-ink">Wofür wir stehen</h2>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
          {leitbild_html}
        </div>
      </div>
    </section>

    {cta_section("Lernen Sie uns persönlich kennen")}
    """).strip()

    return page_shell(
        "unternehmen",
        "Unternehmen | Bühlmann Söhne AG Luzern, seit 1935",
        "Die Bühlmann Söhne AG ist ein Luzerner Familienbetrieb in dritter Generation: gegründet 1935, heute geführt von Patrick Bühlmann mit 13 Mitarbeitenden.",
        IMG_LUZERN_PANO,
        body,
    )


# ---------------------------------------------------------------------------
# Referenzen
# ---------------------------------------------------------------------------
def referenzen_page() -> str:
    refs = [
        ("assets/referenz-ueberbauung.jpg", "Wohnüberbauung", "Neubau: Malerarbeiten innen und aussen in einer modernen Überbauung."),
        ("assets/referenz-altstadt.jpg", "Stadthaus Luzern", "Fassadenrenovation eines historischen Stadthauses mit viel Liebe zum Detail."),
        ("assets/referenz-stadthaus.jpg", "Geschäftshaus Luzern", "Komplette Fassadenrenovation an zentraler Lage."),
        ("assets/referenz-wohnung.jpg", "Wohnungsrenovation", "Helle, frisch gestrichene Räume, sauber und termingerecht übergeben."),
        ("assets/referenz-geschaeft.jpg", "Geschäftsräume", "Malerarbeiten in modernen Verkaufs- und Ausstellungsflächen."),
        ("assets/arbeit-kueche.jpg", "Sauberes Arbeiten", "Abdecken, schützen, streichen: So sieht Sorgfalt bei uns aus."),
    ]
    refs_html = "\n".join(
        f'<figure class="card-lift rounded-lg overflow-hidden bg-white border border-line">'
        f'<img src="{img}" alt="{t}" class="w-full aspect-[4/3] object-cover" />'
        f'<figcaption class="px-6 py-5"><span class="font-display text-lg text-ink block mb-1">{t}</span><span class="text-[14px] text-ink-soft leading-relaxed">{d}</span></figcaption>'
        f'</figure>'
        for img, t, d in refs
    )
    body = dedent(f"""
    {hero_light("Referenzen", "Spuren unserer Arbeit", "Auf Gebäudefassaden ebenso wie in Wohn- und Geschäftsräumen: Eine Auswahl von Projekten aus Luzern und der Innerschweiz.", "assets/referenz-hero.jpg", "Offerte anfragen")}

    <section class="bg-mist border-y border-line">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20">
        <div class="grid md:grid-cols-3 gap-6">
          {refs_html}
        </div>
      </div>
    </section>

    {cta_section("Ihr Projekt als nächste Referenz?")}
    """).strip()
    return page_shell(
        "referenzen",
        "Referenzen | Bühlmann Söhne AG, Maler Luzern",
        "Referenzprojekte der Bühlmann Söhne AG: Fassadenrenovationen, Wohnungsrenovationen, Neubauten und Geschäftsräume in Luzern und der Innerschweiz.",
        "assets/referenz-hero.jpg",
        body,
    )


# ---------------------------------------------------------------------------
# Jobs
# ---------------------------------------------------------------------------
def jobs_page() -> str:
    aufgaben = ["Malerarbeiten im Innen- und Aussenbereich", "Kundenmalerei und Renovationen", "Neubauten"]
    profil = [
        "Abgeschlossene Ausbildung als Maler/in EFZ oder gleichwertige Qualifikation",
        "Gute Deutschkenntnisse",
        "Körperliche Belastbarkeit",
        "Zuverlässigkeit und Verantwortungsbewusstsein",
        "Flexibilität und effiziente Arbeitsweise",
        "Teamfähigkeit und Kundenorientierung",
        "Führerschein der Kategorie B",
    ]
    wir_bieten = [
        "Verantwortungsvolle, interessante und abwechslungsreiche Tätigkeit",
        "Kollegiales Arbeitsklima mit familiärem Stil",
        "Gute Lage nahe Seetalplatz",
    ]

    def ul(items):
        return "".join(f'<li class="flex gap-3 items-start"><span class="material-symbols-outlined text-[18px] text-accent-deep mt-0.5">check_circle</span><span>{i}</span></li>' for i in items)

    job_schema = (
        '{"@type":"JobPosting","title":"Maler/in EFZ 100%","employmentType":"FULL_TIME",'
        '"description":"Malerarbeiten im Innen- und Aussenbereich, Kundenmalerei, Renovationen und Neubauten bei der Bühlmann Söhne AG in Luzern.",'
        '"datePosted":"2026-07-20",'
        '"hiringOrganization":{"@type":"Organization","name":"Bühlmann Söhne AG","sameAs":"' + SITE_URL + '"},'
        '"jobLocation":{"@type":"Place","address":{"@type":"PostalAddress","streetAddress":"' + ADDRESS + '","addressLocality":"Luzern","postalCode":"6015","addressCountry":"CH"}}}'
    )

    body = dedent(f"""
    {hero_light("Jobs", "Wir suchen dich!", "Wir sind ein typisches kleineres KMU mit familiärem Stil: viel Freiraum, vielseitige Aufgaben und ein Team, in dem Mitdenken und Mitwirken zählen.", "assets/team-streichen.jpg", "Jetzt bewerben")}

    <section class="bg-mist border-y border-line">
      <div class="max-w-4xl mx-auto px-6 py-14 md:py-20">
        <div class="bg-white border border-line rounded-lg p-8 md:p-12 shadow-sm">
          <div class="flex flex-wrap items-center justify-between gap-4 mb-8 pb-8 border-b border-line">
            <div>
              <h2 class="font-display text-3xl text-ink mb-2">Maler/in EFZ, 100 %</h2>
              <p class="text-ink-soft text-[15px]">Per sofort oder nach Vereinbarung · Luzern (nähe Seetalplatz)</p>
            </div>
            <a href="mailto:{EMAIL}?subject=Bewerbung%20Maler%2Fin%20100%25" class="bg-ink text-white text-[13px] font-semibold tracking-[0.14em] uppercase px-6 py-3.5 rounded hover:bg-[#1a2a55] transition-colors">Jetzt bewerben</a>
          </div>
          <div class="grid md:grid-cols-3 gap-10 text-[15px] text-ink-soft leading-relaxed">
            <div>
              <h3 class="font-display text-lg text-ink mb-4">Deine Aufgaben</h3>
              <ul class="space-y-3">{ul(aufgaben)}</ul>
            </div>
            <div>
              <h3 class="font-display text-lg text-ink mb-4">Das bringst du mit</h3>
              <ul class="space-y-3">{ul(profil)}</ul>
            </div>
            <div>
              <h3 class="font-display text-lg text-ink mb-4">Wir bieten</h3>
              <ul class="space-y-3">{ul(wir_bieten)}</ul>
            </div>
          </div>
          <div class="mt-10 pt-8 border-t border-line">
            <p class="text-ink-soft text-[15px] leading-relaxed">Konnten wir dich begeistern? Dann freuen wir uns auf deine vollständigen Bewerbungsunterlagen per E-Mail an <a href="mailto:{EMAIL}" class="font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4">{EMAIL}</a>.</p>
          </div>
        </div>

        <div class="mt-8 bg-white border border-line rounded-lg p-8 flex flex-wrap items-center justify-between gap-4">
          <div>
            <h3 class="font-display text-xl text-ink mb-1.5">Lehrstelle als Maler/in EFZ</h3>
            <p class="text-ink-soft text-[15px]">Wir bilden regelmässig Malerlehrlinge aus. Interessiert an einer Schnupperlehre? Melde dich bei uns.</p>
          </div>
          <a href="mailto:{EMAIL}?subject=Schnupperlehre%20Maler%2Fin" class="border border-line text-ink text-[13px] font-semibold tracking-[0.14em] uppercase px-6 py-3.5 rounded hover:border-ink transition-colors">Schnupperlehre anfragen</a>
        </div>
      </div>
    </section>

    {cta_section("Fragen zur Stelle? Ruf uns an.")}
    """).strip()

    return page_shell(
        "jobs",
        "Jobs | Maler/in EFZ 100% | Bühlmann Söhne AG Luzern",
        "Die Bühlmann Söhne AG in Luzern sucht eine/n Maler/in EFZ (100%), per sofort oder nach Vereinbarung. Familiäres KMU nahe Seetalplatz. Jetzt bewerben!",
        "assets/team-streichen.jpg",
        body,
        job_schema,
    )


# ---------------------------------------------------------------------------
# Kontakt
# ---------------------------------------------------------------------------
def kontakt_page() -> str:
    body = dedent(f"""
    {hero_light("Kontakt", "Wir freuen uns auf Ihr Projekt", "Rufen Sie uns an, schreiben Sie uns oder besuchen Sie uns im Rothenbad in Luzern. Wir beraten Sie gerne persönlich.", IMG_LUZERN_UFER, "E-Mail schreiben", "mailto:" + EMAIL)}

    <section class="bg-mist border-y border-line">
      <div class="max-w-6xl mx-auto px-6 py-14 md:py-20 grid md:grid-cols-2 gap-8 md:gap-12">
        <div>
          <h2 class="font-display text-2xl text-ink mb-8">So erreichen Sie uns</h2>
          <div class="space-y-4">
            <div class="bg-white border border-line rounded-lg px-6 py-5 flex items-start gap-4">
              <span class="material-symbols-outlined text-ink mt-0.5">location_on</span>
              <div><span class="font-semibold text-ink block mb-0.5">Bühlmann Söhne AG</span><span class="text-ink-soft text-[15px]">{ADDRESS}, {CITY}</span><br /><a href="{MAPS_URL}" target="_blank" rel="noopener" class="text-[14px] font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4">Route auf Google Maps</a></div>
            </div>
            <div class="bg-white border border-line rounded-lg px-6 py-5 flex items-start gap-4">
              <span class="material-symbols-outlined text-ink mt-0.5">call</span>
              <div><span class="font-semibold text-ink block mb-0.5">Telefon</span><a href="tel:{PHONE_LINK}" class="text-ink-soft text-[15px] hover:text-ink">{PHONE_DISPLAY}</a></div>
            </div>
            <div class="bg-white border border-line rounded-lg px-6 py-5 flex items-start gap-4">
              <span class="material-symbols-outlined text-ink mt-0.5">mail</span>
              <div><span class="font-semibold text-ink block mb-0.5">E-Mail</span><a href="mailto:{EMAIL}" class="text-ink-soft text-[15px] hover:text-ink">{EMAIL}</a></div>
            </div>
            <div class="bg-white border border-line rounded-lg px-6 py-5 flex items-start gap-4">
              <span class="material-symbols-outlined text-ink mt-0.5">place</span>
              <div><span class="font-semibold text-ink block mb-0.5">Standorte</span><span class="text-ink-soft text-[15px]">Luzern · Hergiswil NW · Alpnach OW</span></div>
            </div>
          </div>
        </div>
        <div>
          <h2 class="font-display text-2xl text-ink mb-8">Nachricht schreiben</h2>
          {contact_form("kontaktform")}
        </div>
      </div>
    </section>
    """).strip()

    return page_shell(
        "kontakt",
        "Kontakt | Bühlmann Söhne AG, Rothenbad 18, 6015 Luzern",
        "Kontakt zur Bühlmann Söhne AG in Luzern: Rothenbad 18, 6015 Luzern. Telefon 041 269 88 50, info@bs-luzern.ch. Standorte Luzern, Hergiswil NW, Alpnach OW.",
        IMG_LUZERN_UFER,
        body,
    )


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def main() -> None:
    pages = {"index.html": index_page(), "malerei.html": malerei_page(), "unternehmen.html": unternehmen_page(),
             "referenzen.html": referenzen_page(), "jobs.html": jobs_page(), "kontakt.html": kontakt_page()}
    for s in SERVICES:
        pages[f"{s['slug']}.html"] = service_page(s)
    for r in REGIONS:
        pages[f"{r['slug']}.html"] = region_page(r)

    # Alte, nicht mehr generierte Seiten entfernen (fiktive Inhalte)
    obsolete = [
        "leistungen.html", "portfolio.html", "blog.html", "altbau-renovation.html", "balkon-streichen.html",
        "farbberatung.html", "fassadenrenovation.html", "maler-einfamilienhaus.html", "maler-gewerbe-buero.html",
        "maler-mehrfamilienhaus.html", "maler-neubau.html", "maler-stans-nidwalden.html", "maler-sursee.html",
        "maler-zug.html", "schimmel-entfernen.html", "spritzlackierung.html", "tapezieren-luzern.html",
        "wohnung-streichen.html",
    ]
    for name in obsolete:
        f = ROOT / name
        if f.exists():
            f.unlink()

    for name, html in pages.items():
        (ROOT / name).write_text(html + "\n", encoding="utf-8")

    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{n}" for n in sorted(pages) if n != "index.html"]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
    sitemap += "</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")

    print(f"Generiert: {len(pages)} Seiten + sitemap.xml + robots.txt (v{VERSION})")


if __name__ == "__main__":
    main()
