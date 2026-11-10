# Metin2 Singleplayer - Übersetzungen der Community

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | **Deutsch** | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Dieses Repository enthält die Texte von **Metin2 Singleplayer** - den
Spielclient, die Namen von Gegenständen und Monstern, die Meldungen des
Servers, die Quests, den Chat der Bots, den Windows-Launcher und das klassische Webpanel -, damit
Spieler das Spiel in ihre eigene Sprache übersetzen können. Es enthält nur
Übersetzungen, keinen Spielcode.

Jeder Pull Request wird automatisch geprüft, und angenommene Übersetzungen
kommen in den folgenden Versionen ins Spiel.

## Was hier liegt

| Ordner | Inhalt |
|---|---|
| `template/` | alle Texte des Spiels, die Spalte `translation` leer. Der Start einer neuen Sprache. |
| `de/` `fr/` `pt/` `ro/` `tr/` | die Sprachen, die das Spiel schon hat, mit ihrer aktuellen Übersetzung: korrigiere sie und ergänze, was fehlt (Zeilen mit `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | neue Sprachen, vollständig mit KI-Hilfe übersetzt: Muttersprachler, bitte korrigiert, was falsch klingt. |
| `en_US/` | amerikanisches Englisch: der englische Ausgangstext (britische Schreibweise) in US-Schreibweise (color, armor, defense...). |
| `tools/validate.py` | die Prüfung, die jeder Pull Request durchläuft. |

Englisch ist die Quelle, Polnisch steht zum Vergleich daneben; keine der
beiden hat einen eigenen Ordner.

Jeder Sprachordner enthält dieselben CSV-Dateien, in Teile geschnitten, damit
GitHub sie anzeigen und bearbeiten kann (höchstens 700 Zeilen pro Datei):

| Dateien | Inhalt |
|---|---|
| `1_klient_NN.csv` | der Client: Fenster, Schaltflächen, Tooltips, Fertigkeiten, Regeln |
| `2_przedmioty_potwory_NN.csv` | Namen von Gegenständen und Monstern, Beschreibungen von Gegenständen |
| `3_gra_serwer_NN.csv` | die eigenen Meldungen des Servers (Chat, Systemzeilen) |
| `4_questy_NN.csv` | die Dialoge der Quests |
| `5_boty_czat_NN.csv` | der Chat der Bots, das Gerede der Monster, die Sätze des Servers |
| `6_launcher_NN.csv` | der Windows-Launcher |
| `7_panel_NN.csv` | das klassische Webpanel (das Admin-Panel auf Port 7788, im Browser) |

Jede Datei hat die Spalten:

| Spalte | |
|---|---|
| `id` | der Schlüssel der Zeile. **Niemals ändern.** |
| `english` | der zu übersetzende Text. **Niemals ändern.** |
| `polski` | derselbe Text auf Polnisch, zum Vergleich (kann leer sein). |
| `translation` | **deine Übersetzung - die einzige Spalte, die du bearbeitest.** Leer = das Spiel zeigt das Englische. |
| `notes` | wo der Text zu sehen ist, was erhalten bleiben muss, eine Längengrenze. |
| `status` | `new` (nicht übersetzt), `done` (übersetzt), `check` (wie das Englische - prüfe es). Du darfst ihn auf `done` setzen. |

## So übersetzt du

### A. Im Browser (kleine Änderungen)

1. Öffne die Datei, z. B. [`de/1_klient_01.csv`](de/1_klient_01.csv). GitHub
   zeigt sie als Tabelle; mit dem Suchfeld darüber findest du eine Zeile.
2. Klicke auf den Stift (**Edit this file**). Beim ersten Mal legt GitHub
   eine Kopie (einen Fork) für dich an.
3. Ändere nur die Spalte `translation` der gewünschten Zeilen. Ein Text mit
   Komma, Anführungszeichen oder Zeilenumbruch steht in doppelten
   Anführungszeichen (`"so, wie hier"`); ein Anführungszeichen darin wird
   doppelt geschrieben (`""`).
4. Klicke auf **Commit changes...**, dann **Propose changes**, dann **Create
   pull request**. Schreib in einem Satz, was du übersetzt hast.

### B. In einer Tabellenkalkulation (viele Zeilen)

1. Lade die Dateien herunter (Datei öffnen, **Download raw file**; oder der
   grüne Knopf **Code**, **Download ZIP**, für alles).
2. Öffne sie in einer Tabellenkalkulation:
   - **Google Sheets**: Datei > Importieren > Hochladen. Funktioniert ohne Einstellungen.
   - **LibreOffice Calc**: Datei öffnen; Zeichensatz **UTF-8**, Trennzeichen
     **Komma** wählen und die Spalten auf **Text** stellen.
   - **Excel**: die Datei nicht doppelklicken (Excel würde die Buchstaben
     falsch lesen). Nimm Daten > Aus Text/CSV, Dateiursprung **65001: Unicode
     (UTF-8)**, Trennzeichen **Komma**. Speichere als **CSV UTF-8 (durch
     Trennzeichen getrennt)**.
3. Fülle die Spalte `translation` aus. Benenne die Dateien nicht um, füge
   keine Spalten hinzu und entferne keine, ändere `id` und `english` nicht.
   Sortieren und Filtern ist in Ordnung.
4. Speichere als CSV (UTF-8, kommagetrennt) unter demselben Namen.
5. Öffne auf GitHub den Sprachordner, **Add file > Upload files**, zieh deine
   Dateien hinein, dann **Propose changes** und **Create pull request**.

Du musst nicht alles auf einmal übersetzen - schick, was du hast.

## Regeln

1. **Nur die Spalte `translation`.** `id` und `english` bleiben, wie sie
   sind; die Prüfung lehnt eine Datei ab, in der sie geändert wurden.
2. **Behalte jede Variable und jeden Code genau wie im Englischen, in
   derselben Reihenfolge** - das Spiel setzt sie ein:
   - printf-Variablen: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... und `%%` (ein Prozentzeichen);
   - Platzhalter: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` ist ein Zeilenumbruch im Questfenster; `[WAIT]`, `[DELAY value;5]`,
     `[COLOR r;1|g;0|b;0]` sind seine Befehle;
   - Farben `|cffff0000` ... `|r`, Links `|H` ... `|h`, `|E` ... `|e`.

   Du darfst sie innerhalb des Satzes verschieben, wie es deine Sprache
   braucht, aber Variablen der `%`-Art müssen in derselben Reihenfolge
   bleiben. Ein Text in Klammern wie `[Guild]` oder `[PT]` ist normaler
   Text: übersetze ihn.
3. **Buchstaben.** Das Spiel zeichnet jede Sprache in einer Windows-Codepage,
   daher können nur deren Buchstaben angezeigt werden - keine Emoji, keine
   Symbole wie `→` oder `✓`:

   | Codepage | Sprachen | Buchstaben |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (lateinisch), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (kyrillisch) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Rumänisch: Die Codepage hat nur **ş ţ mit Cedille**, nicht ș ț mit
   Komma. Der Launcher (`6_launcher_*`) ist ein eigenes Windows-Programm und
   nimmt jeden Buchstaben. Ebenso das Webpanel (`7_panel_*`), eine Seite im
   Browser: beide sind **UTF-8**, jeder Buchstabe jeder Sprache.
4. **Der Chat der Bots** (Zeilen, deren Notes „ASCII letters only“ sagen):
   Die Bots tippen wie Spieler, in einfachen Buchstaben a-z ohne Akzente.
5. **Länge.** Wo die Notes „max N characters“ sagen, hat das Spiel keinen
   Platz für mehr.
6. **Zeilenumbrüche** nur, wo das Englische sie hat oder die Notes „new lines
   allowed“ sagen.
7. **Das Webpanel** (`7_panel_*`): Seine Texte landen in einer Webseite, also
   behalte die HTML-Tags des Englischen genau so bei (`<b>`, `</b>`,
   `<a href="...">`, `<br>` und die Platzhalter im Stil `<number>` in spitzen
   Klammern) und füge kein eigenes `<`, `>` oder `javascript:` hinzu. Seine
   Variablen sind `%s`, `%d`, `%(name)s` und `{name}`; ein benanntes `%(name)s`
   darf verschoben werden. Ein `%` mit folgendem Leerzeichen (`25% a character`)
   ist ein Prozentzeichen. Eine Sprache mit mindestens einem übersetzten
   Panel-Text erscheint in der Sprachauswahl des Panels; was nicht übersetzt
   ist, erscheint auf Englisch.

## Eine neue Sprache

1. Kopiere den ganzen Ordner `template/` in einen Ordner mit dem
   zweibuchstabigen ISO-639-1-Code deiner Sprache (`hu`, `es`, `cs`, `pl`... -
   siehe [die Liste](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Das geht auch in einer Tabellenkalkulation: `template/` herunterladen,
   übersetzen und die Dateien in den neuen Ordner hochladen (**Add file >
   Upload files**, `xx/` vor den Namen schreiben, um den Ordner anzulegen).
2. Übersetze und öffne einen Pull Request.

Eine neue Sprache braucht etwas Arbeit im Spiel, bevor Spieler sie wählen
können (Sprachen außerhalb der Codepage 1250 brauchen auch einen neuen
Client), daher kann sie einige Versionen nach der ersten Übersetzung kommen.

## Die Prüfung

Jeder Pull Request führt `tools/validate.py` aus (GitHub Actions). Sie meldet
an der gefundenen Zeile:

- eine `id`, die nicht in `template/` steht, oder doppelt vorkommt;
- eine geänderte Spalte `english`;
- andere Variablen, Platzhalter, Tags oder Farbcodes als im Englischen;
- im Blatt des Webpanels andere HTML-Tags als im Englischen oder ein
  eigenes `<`, `>` oder `javascript:`;
- einen Buchstaben außerhalb der Codepage der Sprache, einen Tabulator, ein
  Steuerzeichen, einen Zeilenumbruch, wo keiner erlaubt ist, einen zu langen
  Text.

Nur die Zeilen, die dein Pull Request geändert hat, werden beurteilt;
Probleme, die schon in den Dateien waren, werden gezählt, aber nicht dir
angelastet. Selbst ausführen (Python 3, nichts zu installieren):
`python tools/validate.py de`.

## Lizenz

Mit dem Öffnen eines Pull Requests stimmst du zu, dass deine Übersetzung in
Metin2 Singleplayer verwendet und unter denselben Bedingungen wie das Projekt
geteilt wird: [CC BY-NC-ND 4.0](LICENSE). Mitwirkende werden im Projekt
genannt. Metin2 selbst und seine Originaltexte gehören Ymir Interactive und
Webzen.
