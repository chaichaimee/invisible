<p align="center">
  <img src="https://www.nvaccess.org/wp-content/uploads/2015/10/NVDA_logo_standard_transparent.png" alt="NVDA Logo" width="220">
</p>

# Invisible

<p align="center"><i>Beenden Sie das Durcheinander. Gestalten Sie die Stimme. Bestimmen Sie Ihr Surferlebnis selbst.</i></p>

<p align="center">
  <strong>Autor:</strong> Chai Chaimee<br>
  <strong>Repository:</strong> <a href="https://github.com/chaichaimee/invisible">github.com/chaichaimee/invisible</a>
</p>

---

## Warum sich mit lauten Webseiten zufriedengeben?

Moderne Websites sind voll von Wiederholungen, Sponsoren-Labels, Cookie-Hinweisen, Kommentar-Zählern, Seitenleisten und automatisch generiertem Ballast, den Screenreader immer und immer wieder vorlesen müssen.

**Invisible** gibt Ihnen die Kontrolle zurück.

Entscheiden Sie genau, welche Wörter, Sätze oder Muster NVDA komplett überspringen soll – oder ersetzen Sie sie leise durch etwas Kürzeres, Saubereres oder völlige Stille.

<br><br>

Dies ist nicht nur Filterung. Dies ist **persönliche Audio-Kuration** für das Web.

## Leistungsstark und doch elegant einfach

*   Text komplett ausblenden – NVDA verhält sich so, als ob er nie existiert hätte
*   Lästige Labels durch kurze Platzhalter ersetzen („Gesponsert · Anzeige“ → „überspringen“)
*   Regeln auf eine einzelne Seite, eine gesamte Domain oder komplexe URL-Muster (Regex) anwenden
*   Volle Unterstützung für reguläre Ausdrücke für chirurgische Präzision
*   Sofortiger Effekt – kein Neuladen der Seite erforderlich
*   Kontextsensitive Benutzeroberfläche: Doppeltipp-Geste öffnet „Seite hinzufügen“ mit bereits ausgefüllter aktueller URL
*   Unterstützung für Rechtsklick + Entf-Taste für schnelle Verwaltung
*   Portable .json-Dateien pro Seite – einfach zu sichern oder zu teilen

## In weniger als 30 Sekunden loslegen

1.  Gehen Sie auf eine beliebige Seite, auf der NVDA etwas liest, das Sie stummschalten oder ändern möchten.

2.  Drücken Sie **NVDA + Umschalt + W**<br><br>
    → Einmaliges Tippen → öffnet das Hauptverwaltungsfenster<br>
    → Doppeltippen (schnell) → öffnet den Dialog „Neue Seite hinzufügen“ mit bereits ausgefüllter aktueller URL

3.  Im Dialog **Seite hinzufügen**:<br><br>
    • Behalten oder bearbeiten Sie den Anzeigenamen<br>
    • Wählen Sie den Bereich:<br>
    &nbsp;&nbsp;– Nur einzelne Seite<br>
    &nbsp;&nbsp;– Gesamte Website (Domain)<br>
    &nbsp;&nbsp;– Regulärer Ausdruck (erweitertes URL-Matching)<br><br>
    Klicken Sie auf **Speichern**

4.  Jetzt befinden Sie sich im Regel-Manager der Seite:<br><br>
    • Geben Sie das Muster ein, das Sie anvisieren möchten<br>
    • Geben Sie den Ersetzungstext ein – oder lassen Sie ihn für komplette Stille leer<br>
    • Aktivieren Sie bei Bedarf „Als regulären Ausdruck verwenden“<br>
    • Klicken Sie auf **Hinzufügen** (oder **Aktualisieren** beim Bearbeiten)<br><br>
    Änderungen werden sofort wirksam – kehren Sie zum Surfen zurück und hören Sie zu.

<br>

Sie können jederzeit mit **NVDA + Umschalt + W** (einmaliges Tippen) zurückkehren, um Regeln zu bearbeiten, weitere hinzuzufügen, Einträge zu entfernen oder zwischen Seiten zu wechseln.

## Praxisbeispiele, die jeden Tag Zeit sparen

| Zielmuster | Ersetzung | Regex? | Was Sie stattdessen hören |
| :--- | :--- | :--- | :--- |
| Anzeige | (leer) | Nein | — komplett übersprungen — |
| Gesponsert | überspringen | Nein | „überspringen“ |
| · [0-9,]+ Kommentare? | (leer) | Ja | — keine Kommentarzähler — |
| Eilmeldung: | News: | Nein | Kürzer & sauberer |
| ^Cookie-Hinweis.*akzeptieren | (leer) | Ja | Banner-Text stummgeschaltet |

## Profi-Tipps für Power-User

*   Rechtsklick auf eine Seite oder einen Eintrag → Kontextmenü mit Bearbeiten / Entfernen
*   Drücken Sie die **Entf-Taste** auf einem ausgewählten Element für sofortige Entfernung
*   Verwendet „Literal Longest-First Matching“ → vermeidet Probleme mit Teilwörtern
*   Regeln aus einer anderen .json-Datei direkt in eine beliebige Seite importieren
*   Der Regex-Modus unterstützt Ersetzungsgruppen – sehr mächtig für dynamische Inhalte

<br><br>

## Mich unterstützen

Wenn dieses Tool Ihr Leben erleichtert hat, ziehen Sie in Erwägung, das nächste Update mit einer kleinen Spende zu unterstützen.

<br>

[<img src="https://img.shields.io/badge/Donate-Support%20Me-blue?style=for-the-badge&logo=stripe" alt="Support me">](https://buy.stripe.com/dRm9AU1xQ3Ds22N6VK1VK01)

<br>

Ihre Unterstützung bedeutet mir viel. Lassen Sie uns gemeinsam etwas Großartiges bauen.

<br>

<p align="center">© 2026 Chai Chaimee NVDA Add-on Veröffentlicht unter GNU</p>