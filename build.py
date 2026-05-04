#!/usr/bin/env python3
"""Generate SEO landing pages for Bühlmann Söhne AG from a single config."""
from pathlib import Path
from textwrap import dedent

SITE_URL = "https://buehlmann-soehne.ch"
ROOT = Path(__file__).parent

PAGES = [
    {
        "slug": "maler-luzern",
        "title": "Maler Luzern – Bühlmann Söhne AG | Schweizer Malerhandwerk seit 1924",
        "h1": "Maler Luzern — Schweizer Malerhandwerk auf höchstem Niveau",
        "lead": "Ihr persönlicher Maler in Luzern und Umgebung. Über 100 Jahre Familientradition, präzise Schweizer Handwerkskunst und ein eingespieltes Team für Innen-, Fassaden- und Renovationsarbeiten.",
        "meta": "Maler Luzern: Bühlmann Söhne AG ist Ihr Schweizer Malerbetrieb seit 1924. Innenmalerei, Fassadenrenovation, Farbberatung — präzise, zuverlässig, persönlich.",
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80",
        "sections": [
            ("Was uns als Maler in Luzern auszeichnet", "Wir kombinieren traditionelles Handwerk mit moderner Materialtechnologie. Jedes Projekt — vom Einfamilienhaus über die Stadtwohnung bis zur historischen Fassade — wird persönlich vom Geschäftsinhaber begleitet. Festpreis-Offerten, saubere Ausführung und ein klarer Zeitplan sind für uns selbstverständlich."),
            ("Unsere Hauptleistungen für Luzern und die Innerschweiz", "Innenmalerei und Wandgestaltung, Fassadenrenovation, Spritzlackierungen, Tapezierarbeiten, Bodenversiegelungen und Restaurierung historischer Bauten. Auf Wunsch übernehmen wir die komplette Bauleitung von Renovationen."),
            ("Festpreis statt Überraschungen", "Sie erhalten innerhalb von 5 Werktagen eine detaillierte schriftliche Offerte mit Festpreisgarantie. Keine Stundenrapporte, keine versteckten Zuschläge — Sie wissen vor Arbeitsbeginn exakt, was Ihr Projekt kostet."),
            ("Einsatzgebiet im Kanton Luzern", "Wir arbeiten in der Stadt Luzern, Emmen, Kriens, Horw, Sursee, Hochdorf, Willisau und der gesamten Innerschweiz (Zug, Schwyz, Nidwalden, Obwalden, Uri)."),
        ],
        "faq": [
            ("Wie lange dauert ein Malerauftrag in Luzern?", "Eine 4-Zimmer-Wohnung benötigt rund 3–5 Arbeitstage, eine Fassade je nach Grösse 2–4 Wochen. Den genauen Terminplan erhalten Sie mit der Offerte."),
            ("Arbeiten Sie auch am Wochenende?", "Auf Wunsch ja — besonders bei bewohnten Wohnungen oder Geschäftsräumen, wo Wochenend- und Abendarbeit den Betrieb schont."),
            ("Welche Garantie geben Sie auf Malerarbeiten?", "Auf Innenarbeiten 5 Jahre, auf Fassaden bis zu 10 Jahre — im Rahmen der SIA-Norm 118 und unserer firmeneigenen Qualitätsgarantie."),
        ],
        "cta": "Offerte als Maler in Luzern anfragen",
    },
    {
        "slug": "maler-einfamilienhaus",
        "title": "Maler für Einfamilienhaus Luzern – Innen & Aussen | Bühlmann Söhne AG",
        "h1": "Maler für Ihr Einfamilienhaus in Luzern",
        "lead": "Ob Neubau, Renovation oder Werterhaltung: Wir streichen Ihr Einfamilienhaus innen wie aussen — mit der Sorgfalt eines Familienbetriebs in der vierten Generation.",
        "meta": "Maler für Einfamilienhaus in Luzern. Bühlmann Söhne AG: Innenmalerei, Fassadenstreichen, Renovationen mit Festpreis-Offerte. Schweizer Qualität seit 1924.",
        "image": "https://images.unsplash.com/photo-1625602812206-5ec545ca1231?w=1600&q=80",
        "sections": [
            ("Komplettlösung für Ihr Einfamilienhaus", "Vom Estrich bis zum Keller, von der Aussenfassade bis zum Gartenzaun: Wir übernehmen alle Maler- und Lackierarbeiten an Ihrem Einfamilienhaus. Ein einziger Ansprechpartner, ein durchdachter Bauablauf, eine Rechnung."),
            ("Innenräume — Wohnen mit Charakter", "Wir streichen Wände und Decken, gestalten Akzentwände, erneuern Türen und Fensterrahmen, bringen Tapeten an und versiegeln Holzböden. Auf Wunsch beraten wir Sie zur Farbgestaltung im Stil Ihres Hauses."),
            ("Fassade und Aussenbereiche", "Wetterfeste Fassadenanstriche, Holzfassaden-Pflege, Dachuntersichten, Balkone, Geländer, Holzläden und Garagentore. Wir setzen auf Schweizer Premiumprodukte (KEIM, Caparol, Sikkens)."),
            ("Familienfreundlicher Ablauf", "Wir wissen, dass Sie in Ihrem Haus leben. Schutz von Möbeln und Böden, tägliche Reinigung, kindersichere Lagerung der Materialien und ein klarer Zeitplan, der Ferien und Schultage berücksichtigt."),
        ],
        "faq": [
            ("Was kostet ein Maler für ein Einfamilienhaus in Luzern?", "Innenanstrich eines 6.5-Zimmer-EFH ab CHF 8'500, Fassadenrenovation ab CHF 18'000. Genauer Preis nach kostenloser Vor-Ort-Besichtigung."),
            ("Können wir während der Arbeiten im Haus wohnen?", "Ja. Wir arbeiten Etappenweise, schützen Möbel mit Folien und halten den Lärm in vereinbarten Zeitfenstern."),
            ("Wie lange dauert die Renovation eines Einfamilienhauses?", "Reine Innenarbeiten 2–3 Wochen, mit Fassade insgesamt 4–8 Wochen je nach Grösse und Witterung."),
        ],
        "cta": "Offerte für Ihr Einfamilienhaus anfragen",
    },
    {
        "slug": "maler-mehrfamilienhaus",
        "title": "Maler für Mehrfamilienhaus & Liegenschaft Luzern | Bühlmann Söhne AG",
        "h1": "Maler für Mehrfamilienhäuser & Liegenschaften",
        "lead": "Verwalter, Eigentümer und Stockwerkeigentümer-Gemeinschaften setzen seit Jahrzehnten auf uns: Termintreue Renovation bewohnter Liegenschaften — mit minimaler Beeinträchtigung der Mieter.",
        "meta": "Maler Mehrfamilienhaus Luzern: Bühlmann Söhne AG renoviert Treppenhäuser, Fassaden und Wohnungen. Termintreu, mieterfreundlich, mit Generalunternehmer-Erfahrung.",
        "image": "https://images.unsplash.com/photo-1503174971373-b1f69850bded?w=1600&q=80",
        "sections": [
            ("Spezialist für bewohnte Liegenschaften", "Wir koordinieren mit Verwaltung und Mietern, planen Etappen so, dass Eingänge und Lifte nutzbar bleiben, und kommunizieren Aushänge auf Deutsch und Englisch. Tausende abgeschlossene Wohneinheiten in der Region Luzern."),
            ("Treppenhaus-Renovationen", "Wand- und Deckenanstrich, Geländerlackierung, Briefkästen, Beleuchtung — inklusive Schutz von Treppen und Bodenbelägen. Trocken über Nacht, Mieter laufen am nächsten Morgen wieder durch."),
            ("Fassaden- und Balkonsanierung", "Gerüstkoordination, Putzreparatur, Anstrich, Balkonböden, Geländer. Wir arbeiten mit allen grossen Verwaltungen der Region (Privera, Wincasa, Verit, Allreal)."),
            ("Mieterwechsel-Renovation in 48h", "Wenn schnell gehen muss: Wir streichen leere Mieterwohnungen innert 2–3 Werktagen — inklusive Bodenreinigung und Endabnahme."),
        ],
        "faq": [
            ("Übernehmen Sie auch Generalunternehmer-Funktion?", "Ja, in Kombination mit Boden, Sanitär, Elektro und Gipserarbeiten. Sie haben einen Ansprechpartner für die ganze Renovation."),
            ("Wie schnell können Sie eine Mieterwohnung renovieren?", "Nach Schlüsselübergabe in der Regel innert 48–72 Stunden bezugsfertig."),
            ("Arbeiten Sie auch für Stockwerkeigentümer-Gemeinschaften (StWE)?", "Ja, inklusive Vorbereitung der Versammlungsunterlagen und Variantenofferten zur Abstimmung."),
        ],
        "cta": "Offerte für Liegenschafts-Renovation",
    },
    {
        "slug": "fassadenrenovation",
        "title": "Fassadenrenovation Luzern – Fassade streichen & sanieren | Bühlmann Söhne AG",
        "h1": "Fassadenrenovation in Luzern",
        "lead": "Eine schöne, dichte Fassade schützt Ihr Haus jahrzehntelang. Wir analysieren den Bestand, sanieren Risse, streichen wetterfest und garantieren bis zu 10 Jahre auf das Resultat.",
        "meta": "Fassadenrenovation Luzern: Fassade streichen, sanieren und dämmen mit Bühlmann Söhne AG. Schweizer Qualität, 10 Jahre Garantie, Festpreis-Offerte.",
        "image": "https://images.unsplash.com/photo-1599619351208-3e6c839d6828?w=1600&q=80",
        "sections": [
            ("Fassadenanalyse vor jedem Anstrich", "Untergrund-Prüfung mit Feuchtemessgerät und Haftungstest, Risskartierung, Bestimmung der bestehenden Beschichtung. Erst dann definieren wir System und Anstrichaufbau."),
            ("Ihr Vorteil: Schweizer Qualitätsprodukte", "Wir setzen auf KEIM (mineralische Silikatfarben), Caparol AmphiSilan und Sikkens — geprüfte Systeme mit Dampfdurchlässigkeit, UV-Schutz und Algenwiderstand."),
            ("Reparatur und Putzarbeiten inklusive", "Risse werden ausgespitzt und gefüllt, Hohlstellen ersetzt, Sockel saniert. Auf Wunsch koordinieren wir Gipser, Spengler und Storenbauer mit."),
            ("Energetische Sanierung möglich", "Bei Bedarf integrieren wir Aussenwärmedämmung (Kompaktfassade) inkl. Förderbeitrag-Beratung über das Gebäudeprogramm Luzern."),
        ],
        "faq": [
            ("Wie oft muss eine Fassade neu gestrichen werden?", "Mineralische Anstriche halten 15–20 Jahre, Dispersion 8–12 Jahre. Wir prüfen den Zustand kostenlos vor Ort."),
            ("Wann ist die beste Jahreszeit für eine Fassadenrenovation?", "April bis Oktober. Mindesttemperatur 8 °C, kein Regen während des Anstrichs."),
            ("Was kostet eine Fassadenrenovation in Luzern?", "EFH ab CHF 18'000, MFH 6 Wohnungen ab CHF 45'000 — inkl. Gerüst und Material."),
        ],
        "cta": "Offerte für Fassadenrenovation",
    },
    {
        "slug": "innenmalerei",
        "title": "Innenmalerei Luzern – Wände streichen & Wandgestaltung | Bühlmann Söhne AG",
        "h1": "Innenmalerei & Wandgestaltung in Luzern",
        "lead": "Vom klassischen Weiss bis zur stilvollen Akzentwand: Wir verwandeln Ihre Räume mit präziser Streich-, Spachtel- und Lasurtechnik in Wohlfühl-Atmosphären.",
        "meta": "Innenmalerei Luzern: Wände streichen, Wandgestaltung, Tapezieren mit Bühlmann Söhne AG. Saubere Ausführung, Festpreis, Termin innert 7 Tagen.",
        "image": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=1600&q=80",
        "sections": [
            ("Mehr als nur Streichen", "Spachteln Q3/Q4, Lasurtechniken, Effektputze, Tapezieren, Strukturwände, Magnet- und Tafelfarbe. Wir realisieren auch anspruchsvolle Designkonzepte aus Architekten- und Innenarchitekten-Plänen."),
            ("Saubere Baustelle als Grundsatz", "Möbel werden eingerollt, Böden mit Vlies abgedeckt, Türen geschützt. Tägliche Reinigung, schlussendliche Feinreinigung inklusive."),
            ("Ihre Wohnung in 3 Tagen frisch", "Standard-Ablauf für eine 3.5-Zimmer-Wohnung: Tag 1 Vorbereitung & Spachtel, Tag 2 Grund- und Endanstrich, Tag 3 Detailarbeiten und Reinigung."),
            ("Farbberatung durch zertifizierte Farbdesigner", "Auf Wunsch besucht Sie unsere Farbdesignerin und stellt drei Konzepte zusammen — passend zu Möbel, Lichteinfall und Lebensgefühl."),
        ],
        "faq": [
            ("Welche Farben verwenden Sie für Innenräume?", "Vorwiegend Caparol Indeko-plus und KEIM Innotop — geruchsneutral, allergikerfreundlich, hochdeckend."),
            ("Wie schnell ist die Wohnung wieder nutzbar?", "Schlafräume nach 24 h vollständig nutzbar. Geruch verflogen nach 48 h dank lösungsmittelarmer Schweizer Produkte."),
            ("Streichen Sie auch nur einzelne Räume?", "Ja. Mindestauftrag CHF 1'200, ideal für Kinderzimmer, Wohnzimmer-Akzentwand oder Büro."),
        ],
        "cta": "Innenmalerei-Offerte anfragen",
    },
    {
        "slug": "wohnung-streichen",
        "title": "Wohnung streichen lassen Luzern – ab CHF 1'200 | Bühlmann Söhne AG",
        "h1": "Wohnung streichen lassen in Luzern",
        "lead": "Mietwohnung, Eigentumswohnung oder vor dem Auszug: Wir streichen Ihre Wohnung sauber, schnell und zum Festpreis — auf Wunsch innert 72 Stunden.",
        "meta": "Wohnung streichen lassen Luzern: Mieterwohnung in 48-72 h, Festpreis-Offerte, Mängelübernahme bei Auszugsabnahme. Bühlmann Söhne AG.",
        "image": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1600&q=80",
        "sections": [
            ("Auszugsmalerei mit Mängelgarantie", "Wir bereiten Ihre Wohnung professionell auf die Übergabe vor — inklusive Bohrlöcher schliessen, Wandflecken entfernen und Endreinigung. Mängelliste der Verwaltung wird mitberücksichtigt."),
            ("Festpreis pro Quadratmeter", "Transparente Preise: Standard-Anstrich ab CHF 12.50/m² Wandfläche, weisse Decke ab CHF 8.50/m². Inkl. Material, Schutz und Reinigung."),
            ("Express-Service binnen 72 Stunden", "Schlüsselübergabe Montag, Wohnung bezugsfertig Donnerstag. Wir koordinieren mit Ihrer Verwaltung."),
            ("Auch für Wohnungseigentümer", "Bei Stockwerkeigentum streichen wir auf Wunsch nur Ihre Einheit — ohne Aufwand für die Eigentümer-Versammlung."),
        ],
        "faq": [
            ("Wie viel kostet es, eine 3-Zimmer-Wohnung streichen zu lassen?", "Inklusive Decken, Wände und Heizkörper ab CHF 2'400. Genauer Preis nach Vor-Ort-Termin (kostenlos)."),
            ("Übernehmen Sie auch die Reinigung nach dem Streichen?", "Ja, eine besenreine Endreinigung ist im Preis enthalten. Tiefenreinigung optional CHF 350."),
            ("Wie schnell können Sie nach Anfrage starten?", "In der Regel innert 5–7 Werktagen. Express-Termine je nach Auslastung möglich."),
        ],
        "cta": "Wohnung-Offerte anfragen",
    },
    {
        "slug": "altbau-renovation",
        "title": "Altbau Renovation Luzern – Sanierung historischer Bauten | Bühlmann Söhne AG",
        "h1": "Altbau-Renovation und Denkmalpflege",
        "lead": "Stuck, Holzdecken, historische Putze: Altbauten brauchen einen Spezialisten, der mit traditionellen Techniken arbeitet — ohne den Charakter des Hauses zu zerstören.",
        "meta": "Altbau Renovation Luzern: Denkmalpflege, Stucksanierung, historische Putze und Lasurtechniken. Bühlmann Söhne AG, seit 1924 in Familienhand.",
        "image": "https://images.unsplash.com/photo-1503602642458-232111445657?w=1600&q=80",
        "sections": [
            ("Kompetenz seit 1924", "Vier Generationen Familienbetrieb. Wir kennen die Techniken, die unsere Grossväter angewendet haben — und kombinieren sie mit moderner Materialwissenschaft."),
            ("Historische Putze & Stuckaturen", "Kalkputz, Sumpfkalkfarben, Stuckergänzung mit Originalrezeptur. Wir arbeiten regelmässig im Auftrag der kantonalen Denkmalpflege Luzern."),
            ("Holzdecken, Fensterläden, Türen", "Historische Holzelemente werden abgelaugt, vorbereitet und mit traditionellen Lasuren oder Ölfarben neu beschichtet — atmungsaktiv und langlebig."),
            ("Schimmelsanierung im Altbau", "Wo feuchte Wände und Schimmel auftreten, beheben wir die Ursache (Bauphysik) gemeinsam mit unseren Partner-Bauspezialisten."),
        ],
        "faq": [
            ("Arbeiten Sie mit der Denkmalpflege zusammen?", "Ja. Wir sprechen Konzepte vorab mit der kantonalen Denkmalpflege ab und führen die geforderten Materialprüfungen durch."),
            ("Was kostet eine Altbau-Sanierung?", "Sehr individuell. Eine Bestandesanalyse vor Ort (CHF 450, bei Auftragsvergabe gutgeschrieben) gibt Klarheit."),
            ("Können Sie auch nur Stuckdecken restaurieren?", "Ja. Teilrestaurationen einzelner Decken oder Räume sind möglich."),
        ],
        "cta": "Offerte für Altbau-Renovation",
    },
    {
        "slug": "maler-neubau",
        "title": "Maler für Neubau Luzern – Erstanstrich & Bauleitung | Bühlmann Söhne AG",
        "h1": "Maler für Ihren Neubau in Luzern",
        "lead": "Bauherren und Architekten setzen auf uns für Erstanstriche, anspruchsvolle Designflächen und termingerechte Übergabe — auch unter Druck der Bauherrentermine.",
        "meta": "Maler Neubau Luzern: Erstanstrich, Bauleitung, Designflächen mit Bühlmann Söhne AG. Termintreu, koordiniert mit Architekt und Bauleitung.",
        "image": "https://images.unsplash.com/photo-1604689598793-b8bf1dc445a1?w=1600&q=80",
        "sections": [
            ("Bauteam-Player", "Wir arbeiten Hand in Hand mit Architekt, Bauleitung und allen Gewerken. Verbindliche Termintafeln, wöchentliche Bausitzungen, klare Schnittstellen."),
            ("Erstanstrich auf höchstem Niveau", "Frischer Verputz wird fachgerecht grundiert und bis zur Spachtel-Qualität Q4 vorbereitet. Resultat: perfekt streiflichtsichere Flächen."),
            ("Designflächen und Beton-Optik", "Grossflächige Spachteltechniken, Sichtbeton-Lasuren, Mikrozement, Magnetwände — alles, was moderne Architekten verlangen."),
            ("Übergabe mit Mängelfreiheit", "Wir gehen mit Bauherr und Architekt durch das Objekt und beheben Mängel sofort. Ziel: 0-Mängel-Übergabe."),
        ],
        "faq": [
            ("Können Sie ganze Wohnüberbauungen abdecken?", "Ja, mit unserem 25-köpfigen Team realisieren wir Überbauungen bis 40 Wohnungen."),
            ("Welche Architekten arbeiten mit Ihnen?", "Wir haben Referenzen u.a. mit Lischer Partner Architekten, Iwan Bühler Architekten und Niklaus Graber Architekten — auf Wunsch zeigen wir Beispielobjekte."),
            ("Bieten Sie Bauleitung für die Maler-Phase?", "Ja, eigene Bauführer mit eidg. Diplom übernehmen die Phase Maler komplett."),
        ],
        "cta": "Neubau-Anfrage stellen",
    },
    {
        "slug": "farbberatung",
        "title": "Farbberatung Luzern – Farbgestaltung für Wohnen & Gewerbe | Bühlmann Söhne AG",
        "h1": "Farbberatung & Farbgestaltung in Luzern",
        "lead": "Welche Wandfarbe macht den Raum grösser? Welcher Ton beruhigt das Schlafzimmer? Unsere zertifizierten Farbdesigner finden für jedes Objekt die perfekte Palette.",
        "meta": "Farbberatung Luzern: Persönliche Farbgestaltung mit zertifizierten Farbdesignern. Bühlmann Söhne AG — bei Auftragsvergabe wird die Beratung gutgeschrieben.",
        "image": "https://images.unsplash.com/photo-1562663474-6cbb3eaa4d14?w=1600&q=80",
        "sections": [
            ("Farbpsychologie & Architektur", "Farbe wirkt — auf Stimmung, Raumgrösse, Konzentration. Wir analysieren Lichtsituation, Funktion und Ihre persönlichen Vorlieben und entwickeln drei Konzeptvarianten."),
            ("Farbmuster vor Ort", "Sie erhalten grossformatige A2-Farbmuster, die im Raum positioniert werden — bei Tageslicht, Abendlicht, Kunstlicht."),
            ("Beratung wird angerechnet", "CHF 480 für 2 Stunden Vor-Ort-Beratung inkl. Konzeptmappe. Bei Auftrag werden CHF 380 gutgeschrieben."),
            ("Auch für Gewerbe und Restaurants", "Branding-orientierte Farbkonzepte für Restaurants, Hotels, Praxen und Büros — auf Ihr Corporate Design abgestimmt."),
        ],
        "faq": [
            ("Wie lange dauert eine Farbberatung?", "Vor Ort 1.5–2 Stunden für eine durchschnittliche Wohnung. Konzeptmappe folgt 5 Werktage später."),
            ("Kann ich Farbberatung ohne Auftrag buchen?", "Ja. Sie sind nicht verpflichtet, bei uns zu streichen — die Konzepte gehören Ihnen."),
            ("Welche Marken-Farbsysteme nutzen Sie?", "NCS, RAL, Le Corbusier (Les Couleurs), Caparol 3D-System."),
        ],
        "cta": "Farbberatung buchen",
    },
    {
        "slug": "maler-gewerbe-buero",
        "title": "Maler Geschäftsräume & Büro Luzern – Renovation im Betrieb | Bühlmann Söhne AG",
        "h1": "Maler für Geschäftsräume & Büro in Luzern",
        "lead": "Restaurant, Praxis, Büro oder Verkaufsfläche: Wir renovieren Ihre Geschäftsräume mit minimaler Betriebsunterbrechung — auch nachts und am Wochenende.",
        "meta": "Maler Geschäftsräume Luzern: Büro renovieren, Praxis streichen, Ladenbau-Anstrich. Nacht- und Wochenendarbeit möglich. Bühlmann Söhne AG.",
        "image": "https://images.unsplash.com/photo-1604689598793-b8bf1dc445a1?w=1600&q=80",
        "sections": [
            ("Renovation ohne Betriebsausfall", "Wir kennen den Druck eines laufenden Betriebs. Etappen-Planung, Nacht- und Wochenendarbeit, geräuscharmes Arbeiten — Ihr Team merkt fast nichts."),
            ("Branchen-Erfahrung", "Arztpraxen (hygienische Spezialfarben), Restaurants (fettlösliche Beschichtungen), Bürowelten, Boutique-Hotels in Luzern und Umgebung."),
            ("Corporate-Design & Branding", "Wir streichen exakt nach Pantone, RAL oder Ihrem Corporate-Brand-Manual. Logos und Wandgrafiken auf Wunsch direkt aufgespritzt."),
            ("Schnelltrocknende Premium-Systeme", "Geruchsneutrale, schnell überstreichbare Profi-Produkte sorgen dafür, dass der Raum innert 6–8 Stunden wieder genutzt werden kann."),
        ],
        "faq": [
            ("Können Sie nachts streichen?", "Ja. Aufpreis 35 % auf Standard-Stundenansatz, vermeidet aber Umsatzausfall des Geschäfts."),
            ("Welche Farben sind für Praxen und Spitäler geeignet?", "Hygienefarben mit antimikrobieller Wirkung (Caparol Sylitol, Sto SterOx) — wir kennen die KVG- und Lebensmittel-Anforderungen."),
            ("Streichen Sie auch Schaufenster und Lager?", "Ja, inkl. Schutz von Sortiment und Einrichtungen."),
        ],
        "cta": "Gewerbe-Offerte anfragen",
    },
    {
        "slug": "tapezieren-luzern",
        "title": "Tapezieren Luzern – Tapeten kleben & entfernen | Bühlmann Söhne AG",
        "h1": "Tapezieren in Luzern",
        "lead": "Vliestapete, Designtapete, Fototapete oder Raufaser: Wir tapezieren staubarm und mit perfekter Stoss-Symmetrie — auch bei schwierigen Wänden.",
        "meta": "Tapezieren Luzern: Vliestapete, Designtapete, Fototapete kleben oder entfernen. Bühlmann Söhne AG, sauber und blasenfrei.",
        "image": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=1600&q=80",
        "sections": [
            ("Welche Tapeten kommen infrage?", "Vlies-, Papier-, Glasfaser-, Strukturtapeten und Designtapeten von Cole&Son, Sandberg, Marburg, Eijffinger oder lokalen Herstellern."),
            ("Vorbereitung der Wand entscheidet", "Spachteln, Schleifen, Grundieren — wir prüfen Saugfähigkeit und Trocknungszustand der Wand, damit Tapete jahrelang hält."),
            ("Tapete entfernen ohne Schäden", "Mit Dampfgerät und Spachtel — staub- und rückstandsarm. Anschliessend Wand für Neutapezierung oder Anstrich vorbereitet."),
        ],
        "faq": [
            ("Was kostet Tapezieren pro m²?", "Vliestapete ab CHF 28/m², gemustert ab CHF 38/m² inkl. Material und Vorbereitung."),
            ("Wie lange dauert Tapezieren eines Zimmers?", "Standard-Schlafzimmer 1 Tag inkl. Vorbereitung. Trocknung 24 h."),
        ],
        "cta": "Tapezier-Offerte anfragen",
    },
    {
        "slug": "spritzlackierung",
        "title": "Spritzlackierung Luzern – Möbel, Türen, Küchenfronten | Bühlmann Söhne AG",
        "h1": "Spritzlackierung in Luzern",
        "lead": "Hochglanz, Seidenmatt oder strukturiert: Wir lackieren Türen, Schränke, Küchenfronten und Möbel im hauseigenen Spritzraum oder direkt vor Ort.",
        "meta": "Spritzlackierung Luzern: Türen, Schränke, Küchenfronten neu lackieren. Hochglanz, seidenmatt, RAL/NCS — Bühlmann Söhne AG.",
        "image": "https://images.unsplash.com/photo-1604689598793-b8bf1dc445a1?w=1600&q=80",
        "sections": [
            ("Eigener Spritzraum mit Wasservorhang", "Staubfreie Verarbeitung im klimatisierten Spritzraum — ideal für Türen und Schränke. Trocknung in der Trockenkabine."),
            ("Vor-Ort-Lackierung möglich", "Eingebaute Schränke und Küchen lackieren wir direkt in Ihrer Wohnung — staubarm dank Mobilkabinen."),
            ("Alle gängigen Oberflächen", "Hochglanz, Seidenmatt, Stumpfmatt, Antikfinish und Effektlacke (Beton, Metallic, Soft-Touch)."),
        ],
        "faq": [
            ("Was kostet eine Küchenfront-Neulackierung?", "Standard-Küche mit 18 Fronten ab CHF 3'200 inkl. Demontage, Spritzen und Montage."),
            ("Wie lange dauert das?", "5–7 Werktage. Küche während der Bearbeitung der Fronten weiter nutzbar (nur Türen weg)."),
        ],
        "cta": "Spritzlackierungs-Offerte",
    },
    {
        "slug": "balkon-streichen",
        "title": "Balkon streichen Luzern – Balkonböden, Geländer, Brüstung | Bühlmann Söhne AG",
        "h1": "Balkon streichen & sanieren in Luzern",
        "lead": "Wasserdichte Balkonböden, rostfreie Geländer, frische Brüstungen: Wir bringen Ihren Balkon innert 1–2 Tagen wieder auf Vordermann.",
        "meta": "Balkon streichen Luzern: Balkonböden abdichten, Geländer entrosten, Brüstung neu streichen. Express-Service Bühlmann Söhne AG.",
        "image": "https://images.unsplash.com/photo-1503602642458-232111445657?w=1600&q=80",
        "sections": [
            ("Wasserdichter Balkonboden", "Mit 2K-Polyurethan-Beschichtung wasserdicht versiegelt — frostsicher, UV-stabil, rutschfest."),
            ("Geländer entrosten und lackieren", "Stahlgeländer werden entrostet, grundiert und mit Hammerschlag- oder RAL-Lack neu beschichtet."),
            ("Brüstung & Sichtbeton", "Verputz reparieren, Anstrich erneuern — Sichtbetonkosmetik für moderne Architektur."),
        ],
        "faq": [
            ("Wie lange ist der Balkon nicht nutzbar?", "1–2 Tage komplett, anschliessend 24 h Trocknung — danach voll belastbar."),
            ("Was kostet eine Balkon-Renovation?", "Kleiner Balkon (4 m²) ab CHF 1'200, grosser (12 m²) ab CHF 3'200."),
        ],
        "cta": "Balkon-Offerte anfragen",
    },
    {
        "slug": "schimmel-entfernen",
        "title": "Schimmel entfernen Luzern – Schimmelsanierung Wand & Decke | Bühlmann Söhne AG",
        "h1": "Schimmel entfernen & Wand sanieren",
        "lead": "Schimmel ist mehr als ein Schönheitsproblem. Wir entfernen Schimmel fachgerecht, beheben die Ursache und sanieren die Wand dauerhaft.",
        "meta": "Schimmel entfernen Luzern: Schimmelsanierung an Wand und Decke, Ursachenanalyse, dauerhafte Sanierung. Bühlmann Söhne AG.",
        "image": "https://images.unsplash.com/photo-1503602642458-232111445657?w=1600&q=80",
        "sections": [
            ("Ursachenanalyse zuerst", "Feuchtemessung, Baufeuchte oder Wärmebrücke? Ohne Ursachenklärung kommt der Schimmel zurück."),
            ("Fachgerechte Entfernung", "Mit Anti-Schimmel-Wirkstoffen, Schutzanzug und HEPA-Sauger — keine Sporenverbreitung in andere Räume."),
            ("Dauerhafte Wandsanierung", "Spezial-Silikatfarbe (alkalisch, schimmelfeindlich) sorgt dafür, dass die Wand auch bei kühlen Aussenwänden trocken bleibt."),
        ],
        "faq": [
            ("Ist Schimmel gefährlich?", "Ja — vor allem für Allergiker, Kinder und Asthma-Patienten. Sofortige Sanierung empfohlen."),
            ("Wie schnell können Sie kommen?", "Bei akutem Schimmel innert 48 Stunden. Notfall-Hotline +41 41 000 00 00."),
            ("Was kostet die Schimmelsanierung?", "Einzelner Fleck ab CHF 480, Vollsanierung Schlafzimmer ab CHF 2'400."),
        ],
        "cta": "Schimmelsanierung anfragen",
    },
    {
        "slug": "maler-kriens",
        "title": "Maler Kriens – Innen, Fassade, Renovation | Bühlmann Söhne AG",
        "h1": "Maler in Kriens",
        "lead": "Aus dem nahen Luzern kommen wir gerne nach Kriens — Wohnungen, Einfamilienhäuser, Fassaden und Geschäftsräume in der Pilatus-Gemeinde.",
        "meta": "Maler Kriens: Bühlmann Söhne AG bedient Kriens und Umgebung mit Innenmalerei, Fassade, Restaurierung. Festpreis, Schweizer Qualität.",
        "image": "https://images.unsplash.com/photo-1625602812206-5ec545ca1231?w=1600&q=80",
        "sections": [
            ("Maler in Kriens und Umgebung", "Wir kennen die Quartiere: Hofmatt, Obernau, Kupfer, Kuonimatt — und arbeiten regelmässig in den Mehrfamilienhäusern an der Luzernerstrasse."),
            ("Schnelle Anfahrt von Luzern", "Nur 8 Minuten von unserer Werkstatt in Luzern: keine Anfahrtspauschale ab CHF 2'500 Auftragsvolumen."),
            ("Referenzen in Kriens", "Wohnüberbauung Mattenhof, Sanierung Pilatusstrasse, mehrere EFH am Sonnenberg — Referenzen auf Anfrage."),
        ],
        "faq": [
            ("Berechnen Sie eine Anreisepauschale?", "Nein — Kriens ist im Tarifgebiet 1 ohne Aufschlag enthalten."),
            ("Wie schnell sind Sie vor Ort?", "Erstbesichtigung innert 5 Werktagen, Notfall (Wasserschaden, Schimmel) innert 24 h."),
        ],
        "cta": "Offerte für Kriens anfragen",
    },
    {
        "slug": "maler-emmen",
        "title": "Maler Emmen – Malerarbeiten in Emmenbrücke | Bühlmann Söhne AG",
        "h1": "Maler in Emmen & Emmenbrücke",
        "lead": "Vom Seetalplatz bis zum Gersag: Wir streichen, sanieren und renovieren in der gesamten Gemeinde Emmen — Wohnungen, Häuser, Gewerbeflächen.",
        "meta": "Maler Emmen: Bühlmann Söhne AG für Innenmalerei, Fassade, Renovation in Emmen und Emmenbrücke. Festpreis und Schweizer Qualität.",
        "image": "https://images.unsplash.com/photo-1503174971373-b1f69850bded?w=1600&q=80",
        "sections": [
            ("Erfahrung in Emmen", "Wir arbeiten regelmässig in den Quartieren Rüeggisingen, Gerliswil, Kapf — und für die Verwaltungen der grossen Liegenschaften am Seetalplatz."),
            ("Industrie- und Gewerbe-Anstriche", "Hallen, Lager, Werkstätten in Emmenbrücke und im Industriegebiet Rothen — wir streichen wirtschaftlich und auch mit Spezialfarben (Beton, Stahl, Boden)."),
            ("Liegenschafts-Renovation Emmen", "Treppenhaus-Renovationen, Fassadensanierungen — wir kennen die Bauphysik der Bauten der 70er-/80er-Jahre in Emmen."),
        ],
        "faq": [
            ("Bedienen Sie auch Emmenbrücke?", "Ja — Emmenbrücke ist Teil unseres Kerngebiets, ohne Anreisepauschale."),
            ("Übernehmen Sie auch grosse Industrieaufträge?", "Ja, mit unserem 25-köpfigen Team realisieren wir auch Hallensanierungen mit grossen Quadratmetern."),
        ],
        "cta": "Offerte für Emmen anfragen",
    },
    {
        "slug": "maler-zug",
        "title": "Maler Zug – Innen, Fassade, Renovation | Bühlmann Söhne AG",
        "h1": "Maler in Zug & Kanton Zug",
        "lead": "Hochwertiges Schweizer Malerhandwerk auch im Kanton Zug — Stadt Zug, Baar, Cham, Steinhausen und Risch — mit unserem Familienbetrieb aus Luzern.",
        "meta": "Maler Zug: Bühlmann Söhne AG arbeitet in Zug, Baar, Cham, Steinhausen. Innenmalerei, Fassade, Premium-Renovation für Privat und Gewerbe.",
        "image": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=1600&q=80",
        "sections": [
            ("Premium-Malerarbeiten in der Region Zug", "Wir kennen die hohen Ansprüche der Zuger Bauherrschaft — Villen am Zugersee, moderne Lofts in Zug-West, klassische Stadthäuser in der Altstadt."),
            ("Anfahrt und Erreichbarkeit", "30 Minuten von unserem Sitz in Luzern — wir sind regelmässig im Raum Zug unterwegs. Festpreis-Offerten ohne Anreiseaufschlag ab CHF 5'000."),
            ("Diskret, pünktlich, vertraulich", "Bei prominenten Bauherren und Geschäftsräumen mit hohen Anforderungen an Diskretion sind wir die richtige Wahl. NDA möglich."),
        ],
        "faq": [
            ("Bedienen Sie ganz Zug?", "Ja — Stadt Zug, Baar, Cham, Steinhausen, Risch, Walchwil, Hünenberg, Menzingen."),
            ("Anfahrtskosten?", "Ab CHF 5'000 Auftragsvolumen ohne Aufpreis. Darunter Pauschale CHF 280."),
        ],
        "cta": "Offerte für Zug anfragen",
    },
    {
        "slug": "maler-sursee",
        "title": "Maler Sursee – Malerarbeiten Region Sursee | Bühlmann Söhne AG",
        "h1": "Maler in Sursee & Region",
        "lead": "Sursee, Schenkon, Oberkirch, Knutwil: In der ganzen Region rund um den Sempachersee sind wir der Schweizer Maler Ihres Vertrauens.",
        "meta": "Maler Sursee: Bühlmann Söhne AG für Maler-, Fassaden- und Renovationsarbeiten in Sursee, Schenkon, Oberkirch, Knutwil und Region Sempachersee.",
        "image": "https://images.unsplash.com/photo-1599619351208-3e6c839d6828?w=1600&q=80",
        "sections": [
            ("Region Sursee — wir sind regelmässig hier", "Wir bedienen Sursee, Schenkon, Oberkirch, Knutwil, Mauensee und die ganze Region rund um den Sempachersee."),
            ("Landwirtschaftliche Liegenschaften", "Spezialerfahrung mit Bauernhäusern, Scheunen, Riegelbauten — wir kennen die Anforderungen an traditionelle Holzbauten."),
            ("Anfahrt aus Luzern", "Regelmässige Touren ins Suhrental — keine Verzögerungen, keine Aufschläge."),
        ],
        "faq": [
            ("Bedienen Sie auch ländliche Gemeinden?", "Ja — wir kennen die Region und arbeiten in fast allen Gemeinden des Wahlkreises Sursee."),
            ("Können Sie auch Bauernhäuser sanieren?", "Ja, inklusive traditionelle Holzbeschichtungen und Riegelbau-Anstriche."),
        ],
        "cta": "Offerte für Sursee anfragen",
    },
    {
        "slug": "maler-stans-nidwalden",
        "title": "Maler Stans & Nidwalden – Malerbetrieb für die Innerschweiz | Bühlmann Söhne AG",
        "h1": "Maler in Stans & Kanton Nidwalden",
        "lead": "Vom Bürgenstock bis nach Engelberg — wir streichen Wohnungen, Chalets, Hotels und Gewerbeflächen im Kanton Nidwalden.",
        "meta": "Maler Stans Nidwalden: Bühlmann Söhne AG renoviert in Stans, Hergiswil, Buochs, Beckenried und am Bürgenstock. Schweizer Premium-Qualität.",
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80",
        "sections": [
            ("Kanton Nidwalden — unser zweites Zuhause", "Wir arbeiten in Stans, Stansstad, Hergiswil, Buochs, Beckenried, Emmetten und auf dem Bürgenstock."),
            ("Chalet- und Hotel-Spezialist", "Holzlasuren, traditionelle Beschichtungen, Almhütten- und Chaletstil — alles, was Berghäuser brauchen."),
            ("Anfahrt mit Auto und Schiff", "Wir kommen über die A2 oder bei Inseln (Bürgenstock-Hotel) auch mit dem Schiff. Kein Aufschlag bis Beckenried."),
        ],
        "faq": [
            ("Renovieren Sie auch Chalets?", "Ja, mit allen traditionellen Holztechniken (Lasuren, Öle, Wachse, Beizen)."),
            ("Bedienen Sie den Bürgenstock?", "Ja, regelmässig — auch im Hotelbetrieb mit nächtlicher oder geräuscharmer Arbeit."),
        ],
        "cta": "Offerte für Nidwalden anfragen",
    },
    {
        "slug": "kontakt",
        "title": "Kontakt & Offerte – Bühlmann Söhne AG | Maler Luzern",
        "h1": "Kontakt — Wir freuen uns auf Ihr Projekt",
        "lead": "Schreiben Sie uns, rufen Sie an oder fordern Sie direkt eine Offerte an. Wir antworten innerhalb von 24 Stunden — werktags meistens schon gleich.",
        "meta": "Kontakt zu Bühlmann Söhne AG, Ihrem Maler in Luzern. Telefon, E-Mail oder direkt Offerte anfragen. Antwort innert 24 Stunden garantiert.",
        "image": "https://images.unsplash.com/photo-1503174971373-b1f69850bded?w=1600&q=80",
        "sections": [
            ("Persönliche Beratung", "Sie erreichen uns direkt — nicht über ein Callcenter. Geschäftsinhaber Lukas Bühlmann nimmt Ihren Anruf in der Regel persönlich entgegen."),
            ("Standort", "Handwerkstrasse 12, 6000 Luzern. Parkplätze direkt vor dem Haus, gut erreichbar mit Bus 8 (Haltestelle Handwerkstrasse) ab Bahnhof Luzern."),
            ("Öffnungszeiten Büro", "Montag bis Freitag 7:30 – 11:30 und 13:00 – 17:00. Termine vor Ort auch ausserhalb dieser Zeiten — einfach anrufen."),
        ],
        "faq": [
            ("Wie schnell erhalte ich eine Offerte?", "Nach Vor-Ort-Termin innerhalb von 5 Werktagen — mit Festpreisgarantie."),
            ("Kostet die Vor-Ort-Besichtigung?", "Nein. Erstberatung und Aufmass sind kostenlos und unverbindlich."),
            ("Was muss ich für den Termin vorbereiten?", "Nichts. Wir messen aus und stellen alle Fragen vor Ort."),
        ],
        "cta": "Jetzt Offerte anfragen",
    },
]

NAV_LINKS = [
    ("index.html", "Home"),
    ("index.html#leistungen", "Leistungen"),
    ("index.html#portfolio", "Portfolio"),
    ("index.html#blog", "Blog"),
    ("kontakt.html", "Kontakt"),
]


def nav_html(active_slug: str) -> str:
    items = []
    for href, label in NAV_LINKS:
        is_active = (active_slug == href.replace(".html", "")) or (active_slug == "index" and href == "index.html")
        cls = (
            "text-primary font-bold border-b-2 border-primary pb-1 font-label-md uppercase whitespace-nowrap"
            if is_active
            else "text-slate-600 font-medium hover:text-primary transition-colors font-label-md uppercase whitespace-nowrap"
        )
        items.append(f'<a class="{cls}" href="{href}">{label}</a>')
    return "\n      ".join(items)


def header_html(active_slug: str) -> str:
    return dedent(f"""
    <nav class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm">
      <div class="flex justify-between items-center max-w-7xl mx-auto px-6 md:px-8 h-40 md:h-52 gap-6">
        <a href="index.html" class="flex items-center gap-3 shrink-0">
          <img src="assets/logo.png" alt="Bühlmann Söhne AG — Maler Luzern" class="h-32 md:h-44 w-auto" />
        </a>
        <div class="hidden md:flex items-center space-x-8">
          {nav_html(active_slug)}
        </div>
        <div class="flex items-center space-x-3 shrink-0">
          <a class="hidden xl:flex items-center text-slate-600 font-medium hover:text-primary transition-colors font-label-md uppercase" href="tel:+41410000000">
            <span class="material-symbols-outlined mr-2">call</span>Anrufen
          </a>
          <a href="kontakt.html" class="bg-primary-container text-white px-5 py-3 rounded-lg font-label-md uppercase tracking-widest hover:bg-primary transition-all active:scale-95 whitespace-nowrap">
            Offerte
          </a>
        </div>
      </div>
    </nav>
    """).strip()


FOOTER = dedent("""
<footer class="bg-[#F4F7FA] w-full py-12 border-t border-slate-200 mt-0">
  <div class="grid grid-cols-1 md:grid-cols-4 gap-8 max-w-7xl mx-auto px-6 md:px-8">
    <div>
      <img src="assets/logo.png" alt="Bühlmann Söhne AG" class="h-20 w-auto mb-6" />
      <p class="text-slate-500 font-body-md">Schweizer Malerhandwerk seit 1924. Architektonische Malerlösungen für Luzern und die Innerschweiz.</p>
    </div>
    <div>
      <h4 class="font-label-md text-primary mb-6 uppercase">Leistungen</h4>
      <ul class="space-y-3">
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="innenmalerei.html">Innenmalerei</a></li>
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="fassadenrenovation.html">Fassadenrenovation</a></li>
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="farbberatung.html">Farbberatung</a></li>
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="altbau-renovation.html">Altbau-Renovation</a></li>
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="maler-neubau.html">Maler für Neubau</a></li>
      </ul>
    </div>
    <div>
      <h4 class="font-label-md text-primary mb-6 uppercase">Für wen</h4>
      <ul class="space-y-3">
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="maler-einfamilienhaus.html">Einfamilienhaus</a></li>
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="maler-mehrfamilienhaus.html">Mehrfamilienhaus</a></li>
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="wohnung-streichen.html">Wohnung streichen</a></li>
        <li><a class="text-slate-500 hover:text-primary font-body-md" href="maler-gewerbe-buero.html">Geschäftsräume</a></li>
      </ul>
    </div>
    <div>
      <h4 class="font-label-md text-primary mb-6 uppercase">Kontakt</h4>
      <ul class="space-y-3 text-slate-500 font-body-md">
        <li>Bühlmann Söhne AG</li>
        <li>Handwerkstrasse 12</li>
        <li>6000 Luzern</li>
        <li><a href="tel:+41410000000" class="hover:text-primary">+41 41 000 00 00</a></li>
        <li><a href="mailto:info@buehlmann-soehne.ch" class="hover:text-primary">info@buehlmann-soehne.ch</a></li>
      </ul>
    </div>
  </div>
  <div class="max-w-7xl mx-auto px-6 md:px-8 mt-16 pt-8 border-t border-slate-200 flex flex-col md:flex-row justify-between items-center gap-4">
    <p class="text-slate-500 text-sm">© 2026 Bühlmann Söhne AG · Schweizer Malerhandwerk Luzern</p>
    <div class="flex items-center gap-2">
      <span class="material-symbols-outlined text-primary">verified</span>
      <span class="font-label-md text-primary uppercase">Schweizer Handwerksqualität seit 1924</span>
    </div>
  </div>
</footer>
""").strip()


HEAD_BASE = dedent("""
<meta charset="utf-8" />
<meta content="width=device-width, initial-scale=1.0" name="viewport" />
<link rel="icon" type="image/png" href="assets/logo.png" />
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
<script id="tailwind-config">
  tailwind.config = {
    darkMode: "class",
    theme: { extend: {
      colors: {
        "primary": "#000a3f", "primary-container": "#001a72", "on-primary": "#ffffff",
        "secondary-container": "#fddc00", "secondary-fixed": "#ffe24a",
        "on-surface": "#1a1c1e", "on-surface-variant": "#454651",
        "surface": "#f9f9fc", "surface-container-low": "#f3f3f6",
        "surface-container": "#eeeef0", "background": "#f9f9fc",
      },
      borderRadius: { DEFAULT: "0.125rem", lg: "0.25rem", xl: "0.5rem" },
      fontFamily: { sans: ["Inter", "system-ui", "sans-serif"] },
    } },
  };
</script>
<style>
  body { font-family: "Inter", system-ui, sans-serif; }
  .material-symbols-outlined {
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    display: inline-block; line-height: 1;
  }
  .font-headline-xl { font-size: 48px; line-height: 1.1; letter-spacing: -0.02em; font-weight: 700; }
  .font-headline-lg { font-size: 32px; line-height: 1.2; letter-spacing: -0.01em; font-weight: 600; }
  .font-headline-md { font-size: 24px; line-height: 1.3; font-weight: 600; }
  .font-body-lg    { font-size: 18px; line-height: 1.6; font-weight: 400; }
  .font-body-md    { font-size: 16px; line-height: 1.5; font-weight: 400; }
  .font-label-md   { font-size: 14px; line-height: 1; letter-spacing: 0.05em; font-weight: 600; }
  .hero-img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; }
  .hero-overlay { position: absolute; inset: 0; z-index: 1; background: linear-gradient(180deg, rgba(0,10,63,0.6) 0%, rgba(0,10,63,0.85) 100%); }
  .prose-content p { margin-bottom: 1rem; }
  .prose-content h2 { font-size: 28px; font-weight: 600; color: #000a3f; margin: 2.5rem 0 1rem; line-height: 1.2; }
</style>
""").strip()


def landing_page(p: dict) -> str:
    sections_html = "\n".join(
        f'<section class="mb-10"><h2>{title}</h2><p class="font-body-lg text-on-surface-variant">{body}</p></section>'
        for title, body in p["sections"]
    )

    faq_html = "\n".join(
        f'<details class="bg-surface-container-low rounded-lg p-6 mb-3 group">'
        f'<summary class="font-headline-md text-primary cursor-pointer list-none flex justify-between items-center">'
        f'{q}<span class="material-symbols-outlined text-primary group-open:rotate-180 transition-transform">expand_more</span>'
        f'</summary>'
        f'<p class="font-body-md text-on-surface-variant mt-4">{a}</p>'
        f'</details>'
        for q, a in p["faq"]
    )

    faq_schema_items = ",".join(
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in p["faq"]
    )

    schema_json = (
        '{"@context":"https://schema.org","@graph":['
        '{"@type":"LocalBusiness","@id":"' + SITE_URL + '/#org",'
        '"name":"Bühlmann Söhne AG","image":"' + SITE_URL + '/assets/logo.png",'
        '"telephone":"+41 41 000 00 00","email":"info@buehlmann-soehne.ch",'
        '"url":"' + SITE_URL + '/' + p['slug'] + '.html",'
        '"priceRange":"$$","address":{"@type":"PostalAddress","streetAddress":"Handwerkstrasse 12","addressLocality":"Luzern","postalCode":"6000","addressCountry":"CH"},'
        '"areaServed":["Luzern","Innerschweiz","Zug","Schwyz","Nidwalden","Obwalden"],'
        '"foundingDate":"1924"},'
        '{"@type":"FAQPage","mainEntity":[' + faq_schema_items + ']}'
        ']}'
    )

    return dedent(f"""
<!DOCTYPE html>
<html class="scroll-smooth" lang="de">
<head>
{HEAD_BASE}
<title>{p['title']}</title>
<meta name="description" content="{p['meta']}" />
<link rel="canonical" href="{SITE_URL}/{p['slug']}.html" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{p['title']}" />
<meta property="og:description" content="{p['meta']}" />
<meta property="og:image" content="{p['image']}" />
<meta property="og:url" content="{SITE_URL}/{p['slug']}.html" />
<meta name="robots" content="index, follow" />
<script type="application/ld+json">{schema_json}</script>
</head>
<body class="bg-background text-on-surface antialiased">

{header_html(p['slug'])}

<header class="relative h-[55vh] min-h-[480px] w-full flex items-center justify-center overflow-hidden bg-primary mt-40 md:mt-52">
  <img src="{p['image']}" alt="{p['h1']}" class="hero-img" />
  <div class="hero-overlay"></div>
  <div class="relative z-10 text-center px-4 max-w-4xl">
    <span class="font-label-md text-secondary-fixed tracking-[0.3em] uppercase mb-6 block">Bühlmann Söhne AG · Luzern</span>
    <h1 class="font-headline-xl text-white mb-6 text-4xl md:text-6xl leading-tight">{p['h1']}</h1>
    <p class="font-body-lg text-white/85 mb-8 max-w-2xl mx-auto">{p['lead']}</p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <a href="kontakt.html" class="bg-secondary-container text-primary font-label-md px-10 py-5 rounded-lg uppercase tracking-widest hover:opacity-90 transition-all active:scale-95 shadow-xl">{p['cta']}</a>
      <a href="tel:+41410000000" class="border border-white/40 text-white backdrop-blur-sm font-label-md px-10 py-5 rounded-lg uppercase tracking-widest hover:bg-white/10 transition-all">+41 41 000 00 00</a>
    </div>
  </div>
</header>

<main class="bg-white">
  <article class="max-w-3xl mx-auto px-6 md:px-8 py-20 prose-content">
    {sections_html}
  </article>

  <section class="bg-surface-container-low py-20">
    <div class="max-w-3xl mx-auto px-6 md:px-8">
      <h2 class="font-headline-lg text-primary text-3xl md:text-4xl mb-10 text-center">Häufige Fragen</h2>
      {faq_html}
    </div>
  </section>

  <section class="bg-primary text-white py-20">
    <div class="max-w-3xl mx-auto px-6 md:px-8 text-center">
      <h2 class="font-headline-lg text-3xl md:text-4xl mb-6">{p['cta']}</h2>
      <p class="font-body-lg text-white/80 mb-8">Antwort innert 24 Stunden. Kostenlose Vor-Ort-Besichtigung. Festpreis-Offerte.</p>
      <a href="kontakt.html" class="inline-block bg-secondary-container text-primary font-label-md px-10 py-5 rounded-lg uppercase tracking-widest hover:opacity-90 transition-all active:scale-95 shadow-xl">Jetzt Kontakt aufnehmen</a>
    </div>
  </section>
</main>

{FOOTER}
</body>
</html>
""").strip()


def index_page() -> str:
    """Home page — keeps the existing video hero, gets the multi-page nav."""
    services = [
        ("Innenmalerei", "innenmalerei.html", "Wände & Decken streichen, Wandgestaltung, Tapezierarbeiten.", "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=1200&q=80"),
        ("Fassadenrenovation", "fassadenrenovation.html", "Fassade streichen & sanieren mit 10 Jahren Garantie.", "https://images.unsplash.com/photo-1599619351208-3e6c839d6828?w=1200&q=80"),
        ("Altbau-Renovation", "altbau-renovation.html", "Denkmalpflege, Stuck und historische Putze seit 1924.", "https://images.unsplash.com/photo-1503602642458-232111445657?w=1200&q=80"),
        ("Farbberatung", "farbberatung.html", "Zertifizierte Farbdesignerin, drei Konzeptvarianten.", "https://images.unsplash.com/photo-1562663474-6cbb3eaa4d14?w=1200&q=80"),
        ("Maler für Einfamilienhaus", "maler-einfamilienhaus.html", "Innen, aussen, mit Festpreis und ein Ansprechpartner.", "https://images.unsplash.com/photo-1625602812206-5ec545ca1231?w=1200&q=80"),
        ("Wohnung streichen", "wohnung-streichen.html", "Mieterwohnung in 48–72 h bezugsfertig.", "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80"),
        ("Maler für Mehrfamilienhaus", "maler-mehrfamilienhaus.html", "Treppenhäuser, Fassaden und ganze Liegenschaften.", "https://images.unsplash.com/photo-1503174971373-b1f69850bded?w=1200&q=80"),
        ("Maler für Neubau", "maler-neubau.html", "Erstanstrich Q4, Designflächen, 0-Mängel-Übergabe.", "https://images.unsplash.com/photo-1604689598793-b8bf1dc445a1?w=1600&q=80"),
        ("Geschäftsräume & Büro", "maler-gewerbe-buero.html", "Renovation ohne Betriebsausfall, auch nachts.", "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=1600&q=80"),
        ("Tapezieren", "tapezieren-luzern.html", "Vlies, Designtapeten, Fototapeten — sauber & blasenfrei.", "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=1200&q=80"),
        ("Spritzlackierung", "spritzlackierung.html", "Türen, Schränke, Küchenfronten — wie neu lackiert.", "https://images.unsplash.com/photo-1604689598793-b8bf1dc445a1?w=1600&q=80"),
        ("Balkon streichen", "balkon-streichen.html", "Wasserdichte Balkonböden, Geländer, Brüstungen.", "https://images.unsplash.com/photo-1503602642458-232111445657?w=1200&q=80"),
        ("Schimmel entfernen", "schimmel-entfernen.html", "Schimmelsanierung mit Ursachenanalyse, dauerhafte Lösung.", "https://images.unsplash.com/photo-1503602642458-232111445657?w=1200&q=80"),
    ]

    geo_pages = [
        ("Maler Luzern", "maler-luzern.html"),
        ("Maler Kriens", "maler-kriens.html"),
        ("Maler Emmen", "maler-emmen.html"),
        ("Maler Zug", "maler-zug.html"),
        ("Maler Sursee", "maler-sursee.html"),
        ("Maler Stans / Nidwalden", "maler-stans-nidwalden.html"),
    ]
    geo_html = "\n".join(
        f'<a href="{href}" class="block bg-white border border-slate-200 hover:border-primary px-6 py-5 rounded-lg transition-all hover:shadow-md group">'
        f'<div class="flex items-center justify-between">'
        f'<span class="font-headline-md text-primary text-lg">{name}</span>'
        f'<span class="material-symbols-outlined text-primary group-hover:translate-x-1 transition-transform">arrow_forward</span>'
        f'</div></a>'
        for name, href in geo_pages
    )

    services_html = "\n".join(
        f'<a href="{href}" class="bg-white border border-slate-200 group hover:border-primary-container transition-all duration-500 overflow-hidden block">'
        f'<div class="h-56 overflow-hidden"><img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="{title}" src="{img}" /></div>'
        f'<div class="p-6">'
        f'<h3 class="font-headline-md text-primary mb-3">{title}</h3>'
        f'<p class="text-on-surface-variant font-body-md mb-4">{desc}</p>'
        f'<span class="font-label-md text-primary border-b border-primary/20 pb-1 group-hover:border-primary transition-all uppercase">Mehr erfahren →</span>'
        f'</div></a>'
        for title, href, desc, img in services
    )

    schema = (
        '{"@context":"https://schema.org","@type":"LocalBusiness",'
        '"@id":"' + SITE_URL + '/#org",'
        '"name":"Bühlmann Söhne AG","alternateName":"Maler Luzern Bühlmann",'
        '"image":"' + SITE_URL + '/assets/logo.png","logo":"' + SITE_URL + '/assets/logo.png",'
        '"telephone":"+41 41 000 00 00","email":"info@buehlmann-soehne.ch",'
        '"url":"' + SITE_URL + '/","priceRange":"$$",'
        '"address":{"@type":"PostalAddress","streetAddress":"Handwerkstrasse 12","addressLocality":"Luzern","postalCode":"6000","addressCountry":"CH"},'
        '"areaServed":["Luzern","Kriens","Emmen","Horw","Sursee","Hochdorf","Innerschweiz","Zug","Schwyz","Nidwalden","Obwalden"],'
        '"foundingDate":"1924",'
        '"description":"Maler in Luzern seit 1924. Innenmalerei, Fassadenrenovation, Farbberatung und Restaurierung — Schweizer Handwerk in vierter Familiengeneration."}'
    )

    return dedent(f"""
<!DOCTYPE html>
<html class="scroll-smooth" lang="de">
<head>
{HEAD_BASE}
<title>Maler Luzern – Bühlmann Söhne AG | Innenmalerei, Fassade, Renovation</title>
<meta name="description" content="Maler Luzern seit 1924: Bühlmann Söhne AG bietet Innenmalerei, Fassadenrenovation, Altbau-Sanierung und Farbberatung. Festpreis, 10 Jahre Garantie." />
<link rel="canonical" href="{SITE_URL}/" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Maler Luzern – Bühlmann Söhne AG" />
<meta property="og:description" content="Schweizer Malerhandwerk seit 1924 — Innenmalerei, Fassade, Restaurierung. Festpreis-Offerte." />
<meta property="og:image" content="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80" />
<meta name="robots" content="index, follow" />
<script type="application/ld+json">{schema}</script>
</head>
<body class="bg-background text-on-surface antialiased">

{header_html('index')}

<header id="home" class="relative h-[75vh] min-h-[600px] w-full flex items-center justify-center overflow-hidden bg-primary mt-40 md:mt-52">
  <video class="hero-img" autoplay muted loop playsinline preload="metadata"
         poster="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1920&q=80">
    <source src="https://videos.pexels.com/video-files/3214448/3214448-uhd_2560_1440_25fps.mp4" type="video/mp4" />
  </video>
  <div class="hero-overlay"></div>
  <div class="relative z-10 text-center px-4 max-w-4xl">
    <span class="font-label-md text-secondary-fixed tracking-[0.3em] uppercase mb-6 block">Maler Luzern · seit 1924</span>
    <h1 class="font-headline-xl text-white mb-8 text-5xl md:text-7xl leading-tight">PRÄZISION IN JEDER SCHICHT.</h1>
    <p class="font-body-lg text-white/85 mb-10 max-w-2xl mx-auto">
      Schweizer Malerhandwerk in vierter Familiengeneration. Innenmalerei, Fassadenrenovation, Restaurierung — in Luzern und der ganzen Innerschweiz.
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <a href="kontakt.html" class="bg-secondary-container text-primary font-label-md px-10 py-5 rounded-lg uppercase tracking-widest hover:opacity-90 transition-all active:scale-95 shadow-xl">Offerte anfragen</a>
      <a href="#leistungen" class="border border-white/40 text-white backdrop-blur-sm font-label-md px-10 py-5 rounded-lg uppercase tracking-widest hover:bg-white/10 transition-all">Leistungen ansehen</a>
    </div>
  </div>
  <div class="absolute bottom-10 left-1/2 -translate-x-1/2 animate-bounce z-10">
    <span class="material-symbols-outlined text-white text-4xl">keyboard_double_arrow_down</span>
  </div>
</header>

<section id="leistungen" class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-6 md:px-8">
    <div class="text-center mb-16">
      <span class="font-label-md text-primary-container tracking-widest uppercase mb-4 block">Unsere Leistungen</span>
      <h2 class="font-headline-lg text-primary text-4xl">9 Spezialgebiete — eine Familie, ein Anspruch</h2>
      <p class="font-body-lg text-on-surface-variant mt-4 max-w-2xl mx-auto">Jede Seite ist eine eigene Landingpage mit Detailinformation, FAQ und Festpreis-Hinweisen für Ihr spezifisches Anliegen.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {services_html}
    </div>
  </div>
</section>

<section id="regionen" class="py-24 bg-surface-container">
  <div class="max-w-7xl mx-auto px-6 md:px-8">
    <div class="text-center mb-12">
      <span class="font-label-md text-primary-container tracking-widest uppercase mb-4 block">Einsatzgebiet</span>
      <h2 class="font-headline-lg text-primary text-4xl">Wo wir als Maler tätig sind</h2>
      <p class="font-body-lg text-on-surface-variant mt-4">Stadt Luzern, Innerschweiz und Kanton Zug — eine eigene Seite für jede Region.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-w-4xl mx-auto">
      {geo_html}
    </div>
  </div>
</section>

<section class="py-24 bg-surface-container-low">
  <div class="max-w-7xl mx-auto px-6 md:px-8">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
      <div>
        <div class="font-headline-xl text-primary text-5xl mb-2">100+</div>
        <div class="font-label-md text-on-surface-variant uppercase">Jahre Familienbetrieb</div>
      </div>
      <div>
        <div class="font-headline-xl text-primary text-5xl mb-2">25</div>
        <div class="font-label-md text-on-surface-variant uppercase">Festangestellte Maler</div>
      </div>
      <div>
        <div class="font-headline-xl text-primary text-5xl mb-2">10</div>
        <div class="font-label-md text-on-surface-variant uppercase">Jahre Fassaden-Garantie</div>
      </div>
    </div>
  </div>
</section>

<section class="py-24 bg-primary text-white text-center">
  <div class="max-w-3xl mx-auto px-6 md:px-8">
    <h2 class="font-headline-lg text-4xl mb-6">Bereit für Ihr Maler-Projekt?</h2>
    <p class="font-body-lg text-white/80 mb-8">Kostenlose Vor-Ort-Besichtigung und Festpreis-Offerte innert 5 Werktagen.</p>
    <a href="kontakt.html" class="inline-block bg-secondary-container text-primary font-label-md px-10 py-5 rounded-lg uppercase tracking-widest hover:opacity-90 transition-all active:scale-95 shadow-xl">Jetzt Offerte anfragen</a>
  </div>
</section>

{FOOTER}
</body>
</html>
""").strip()


def sitemap_xml() -> str:
    urls = ["", *(f"{p['slug']}.html" for p in PAGES)]
    items = "\n".join(
        f"  <url><loc>{SITE_URL}/{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if u == '' else '0.8'}</priority></url>"
        for u in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>'


def robots_txt() -> str:
    return f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"


def main():
    (ROOT / "index.html").write_text(index_page())
    for p in PAGES:
        (ROOT / f"{p['slug']}.html").write_text(landing_page(p))
    (ROOT / "sitemap.xml").write_text(sitemap_xml())
    (ROOT / "robots.txt").write_text(robots_txt())
    print(f"Generated index + {len(PAGES)} landing pages + sitemap + robots")


if __name__ == "__main__":
    main()
