<div align="center">
  <img src="https://www.nvaccess.org/wp-content/uploads/2015/10/NVDA_logo_standard_transparent.png" alt="NVDA Logo" width="220">
</div>

# Invisible

*Stille den Ballast. Formen Sie die Stimme. Beherrschen Sie Ihr Surferlebnis.*

**Autor:** Chai Chaimee  
**Repository:** [github.com/chaichaimee/invisible](https://github.com/chaichaimee/invisible)

---

## Warum sich mit lauten Webseiten abfinden?

Moderne Websites sind voller Wiederholungen, Sponsorenhinweise, Cookie-Meldungen, Kommentarzahlen, Seitenleisten und automatisch generiertem Füllmaterial, das Screenreader immer wieder vorlesen müssen — wieder und wieder.

**Invisible** gibt Ihnen die Kontrolle zurück.

Entscheiden Sie genau, welche Wörter, Phrasen oder Muster NVDA komplett überspringen soll — oder leise durch etwas Kürzeres, Sauberes oder völlig Stilles ersetzen soll.

Dies ist nicht nur Filterung. Dies ist **persönliche Audiokuration** für das Web.

## Leistungsstark und dennoch elegant einfach

- Text komplett ausblenden — NVDA verhält sich, als hätte er nie existiert
- Störende Bezeichnungen durch kurze Platzhalter ersetzen („Sponsored · Advertisement“ → „skip“)
- Regeln auf eine einzelne Seite, eine gesamte Domain oder komplexe URL-Muster (Regex) anwenden
- Vollständige Unterstützung für reguläre Ausdrücke für chirurgische Präzision
- Sofortige Wirkung — kein Neuladen der Seite nötig
- Kontextsensitive Oberfläche: Doppel-Tipp-Geste öffnet „Add Site“ mit aktueller URL vorausgefüllt
- Rechtsklick + Entf-Taste für schnelle Verwaltung
- Portable .json-Dateien pro Site — einfach sichern oder teilen

## In unter 30 Sekunden starten

1. Gehen Sie zu einer beliebigen Seite, auf der NVDA etwas vorliest, das Sie stummschalten oder ändern möchten.

2. Drücken Sie **NVDA + Shift + W**  
   - Einzelner Tipp → öffnet das Hauptverwaltungsfenster  
   - Doppeltipp (schnell) → öffnet „Neue Site hinzufügen“ mit aktueller URL bereits eingefügt

3. Im Dialog **Site hinzufügen**:  
   - Anzeigenamen beibehalten oder bearbeiten  
   - Umfang wählen:  
     - Nur einzelne Seite  
     - Gesamte Website (Domain)  
     - Regulärer Ausdruck (erweiterte URL-Übereinstimmung)  
   - Klicken Sie auf **Speichern**

4. Nun befinden Sie sich im Regel-Manager der Site:  
   - Geben Sie das zu treffende Muster ein  
   - Ersetzungstext eingeben — oder leer lassen für vollständige Stille  
   - „Als regulären Ausdruck verwenden“ aktivieren, wenn nötig  
   - Auf **Hinzufügen** (oder **Aktualisieren** beim Bearbeiten) klicken  
   Änderungen wirken sofort — zurück zum Surfen und Zuhören.

Sie können jederzeit mit **NVDA+Shift+W** (einzelner Tipp) zurückkehren, um zu bearbeiten, weitere Regeln hinzuzufügen, Einträge zu entfernen oder zwischen Sites zu wechseln.

## Realwelt-Beispiele, die jeden Tag Zeit sparen

| Zielmuster                  | Ersetzung     | Regex? | Was Sie stattdessen hören      |
|-----------------------------|---------------|--------|--------------------------------|
| Advertisement               | (leer)        | Nein   | — komplett übersprungen —      |
| Sponsored                   | skip          | Nein   | „skip“                         |
| · [0-9,]+ comments?         | (leer)        | Ja     | — keine Kommentarzahlen —      |
| Breaking News:              | News:         | Nein   | Kürzer & sauberer              |
| ^Cookie notice.*accept      | (leer)        | Ja     | Bannermeldung stummgeschaltet  |

## Pro-Tipps für Power-User

- Rechtsklick auf Site oder Eintrag → Kontextmenü mit Bearbeiten / Entfernen
- Entf-Taste auf ausgewähltem Element für sofortiges Entfernen drücken
- Längste-wörtliche-Zuerst-Abgleich verwenden → vermeidet Teilwort-Probleme
- Regeln aus einer anderen .json-Datei direkt in eine Site importieren
- Regex-Modus unterstützt Ersetzungsgruppen — sehr mächtig für dynamischen Inhalt

## Das Projekt unterstützen

Wenn Invisible Ihr tägliches Surferlebnis verbessert hat, denken Sie darüber nach, die Weiterentwicklung zu unterstützen.

[**Spenden via GitHub Sponsors**](https://github.com/chaichaimee)

---

© 2026 Chai Chaimee · Invisible NVDA Add-on · Veröffentlicht unter GNU GPL v2+