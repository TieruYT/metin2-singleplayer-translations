# Metin2 Singleplayer - vertalingen van de community

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | **Nederlands** | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Deze repository bevat de teksten van **Metin2 Singleplayer** - de spelclient,
de namen van voorwerpen en monsters, de berichten van de server, de quests,
de chat van de bots, de Windows-launcher en het klassieke webpaneel - zodat spelers het spel in hun
eigen taal kunnen vertalen. Hij bevat alleen vertalingen: geen spelcode.

Elke pull request wordt automatisch gecontroleerd, en geaccepteerde
vertalingen komen in de volgende versies in het spel.

## Wat staat hier

| map | inhoud |
|---|---|
| `template/` | alle teksten van het spel, met de kolom `translation` leeg. Het begin van een nieuwe taal. |
| `de/` `fr/` `pt/` `ro/` `tr/` | de talen die het spel al heeft, met hun huidige vertaling: verbeter die en vul aan wat ontbreekt (rijen met `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | nieuwe talen, volledig vertaald met hulp van AI: moedertaalsprekers, verbeter wat niet goed klinkt. |
| `en_US/` | Amerikaans Engels: de Engelse brontekst (Britse spelling) in Amerikaanse spelling (color, armor, defense...). |
| `tools/validate.py` | de controle die elke pull request doorloopt. |

Engels is de bron en Pools staat ernaast als referentie; geen van beide heeft
een eigen map.

Elke taalmap bevat dezelfde CSV-bestanden, opgedeeld in stukken zodat GitHub
ze kan tonen en bewerken (maximaal 700 rijen per bestand):

| bestanden | inhoud |
|---|---|
| `1_klient_NN.csv` | de client: vensters, knoppen, tooltips, vaardigheden, regels |
| `2_przedmioty_potwory_NN.csv` | namen van voorwerpen en monsters, beschrijvingen van voorwerpen |
| `3_gra_serwer_NN.csv` | de eigen berichten van de server (chat, systeemregels) |
| `4_questy_NN.csv` | de dialogen van de quests |
| `5_boty_czat_NN.csv` | de chat van de bots, het gebabbel van monsters, de zinnen van de server |
| `6_launcher_NN.csv` | de Windows-launcher |
| `7_panel_NN.csv` | het klassieke webpaneel (het beheerpaneel op poort 7788, in de browser) |

Elk bestand heeft de kolommen:

| kolom | |
|---|---|
| `id` | de sleutel van de rij. **Nooit wijzigen.** |
| `english` | de tekst om te vertalen. **Nooit wijzigen.** |
| `polski` | dezelfde tekst in het Pools, als referentie (mag leeg zijn). |
| `translation` | **jouw vertaling - de enige kolom die je bewerkt.** Leeg = het spel toont het Engels. |
| `notes` | waar de tekst te zien is, wat behouden moet blijven, een lengtegrens. |
| `status` | `new` (niet vertaald), `done` (vertaald), `check` (hetzelfde als het Engels - controleer het). Je mag hem op `done` zetten. |

## Zo vertaal je

### A. In de browser (kleine wijzigingen)

1. Open het bestand, bijv. [`nl/1_klient_01.csv`](nl/1_klient_01.csv). GitHub
   toont het als tabel; gebruik het zoekveld erboven om een rij te vinden.
2. Klik op het potlood (**Edit this file**). De eerste keer maakt GitHub een
   kopie (een fork) voor je.
3. Wijzig alleen de kolom `translation` van de rijen die je wilt. Een tekst
   met een komma, een aanhalingsteken of een regeleinde staat tussen dubbele
   aanhalingstekens (`"zoals, hier"`); een aanhalingsteken erin schrijf je
   dubbel (`""`).
4. Klik op **Commit changes...**, dan **Propose changes**, dan **Create pull
   request**. Zeg in één zin wat je hebt vertaald.

### B. In een spreadsheet (veel rijen)

1. Download de bestanden (open een bestand, **Download raw file**; of de
   groene knop **Code**, **Download ZIP**, voor alles).
2. Open ze in een spreadsheet:
   - **Google Spreadsheets**: Bestand > Importeren > Uploaden. Werkt zonder
     instellingen.
   - **LibreOffice Calc**: open het bestand; kies tekenset **UTF-8**,
     scheidingsteken **komma** en zet de kolommen op **Tekst**.
   - **Excel**: dubbelklik het bestand niet (Excel zou de letters verkeerd
     lezen). Gebruik Gegevens > Van tekst/CSV, bestandsoorsprong **65001:
     Unicode (UTF-8)**, scheidingsteken **Komma**. Sla op als **CSV UTF-8
     (door komma's gescheiden)**.
3. Vul de kolom `translation` in. Hernoem de bestanden niet, voeg geen
   kolommen toe of verwijder ze niet, en wijzig `id` en `english` niet.
   Sorteren en filteren is prima.
4. Sla op als CSV (UTF-8, kommagescheiden) onder dezelfde naam.
5. Open op GitHub de taalmap, **Add file > Upload files**, sleep je bestanden
   erin, dan **Propose changes** en **Create pull request**.

Je hoeft niet alles in één keer te vertalen - stuur wat je hebt.

## Regels

1. **Alleen de kolom `translation`.** `id` en `english` blijven zoals ze
   zijn; de controle weigert een bestand waarin ze zijn gewijzigd.
2. **Behoud elke variabele en elke code precies zoals in het Engels, in
   dezelfde volgorde** - het spel vult ze in:
   - printf-variabelen: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... en `%%` (een procentteken);
   - plaatshouders: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` is een regeleinde in een questvenster; `[WAIT]`,
     `[DELAY value;5]`, `[COLOR r;1|g;0|b;0]` zijn de opdrachten ervan;
   - kleuren `|cffff0000` ... `|r`, links `|H` ... `|h`, `|E` ... `|e`.

   Je mag ze in de zin verplaatsen zoals je taal dat nodig heeft, maar
   variabelen van het type `%` moeten in dezelfde volgorde blijven. Een tekst
   tussen vierkante haken zoals `[Guild]` of `[PT]` is gewone tekst: vertaal
   hem.
3. **Letters.** Het spel tekent elke taal in een Windows-codetabel, dus
   alleen de letters daarvan kunnen worden getoond - geen emoji, geen symbolen
   zoals `→` of `✓`:

   | codetabel | talen | letters |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (Latijns), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (Cyrillisch) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Roemeens: de codetabel heeft alleen **ş ţ met cedille**, niet ș ț met een
   komma. De launcher (`6_launcher_*`) is een eigen Windows-programma en
   accepteert elke letter. Net als het webpaneel (`7_panel_*`), een pagina in de
   browser: beide zijn **UTF-8**, elke letter van elke taal.
4. **De chat van de bots** (rijen waarvan de notes "ASCII letters only"
   zeggen): de bots typen zoals spelers, in gewone letters a-z zonder accenten.
5. **Lengte.** Waar de notes "max N characters" zeggen, heeft het spel geen
   ruimte voor meer.
6. **Regeleinden** alleen waar het Engels ze heeft of de notes "new lines
   allowed" zeggen.
7. **Het webpaneel** (`7_panel_*`): de teksten komen in een webpagina, dus
   behoud de HTML-tags van het Engels precies zoals ze zijn (`<b>`, `</b>`,
   `<a href="...">`, `<br>` en de plaatshouders in de stijl `<number>` tussen
   punthaken) en voeg geen eigen `<`, `>` of `javascript:` toe. De variabelen zijn
   `%s`, `%d`, `%(name)s` en `{name}`; een benoemde `%(name)s` mag verschuiven.
   Een `%` gevolgd door een spatie (`25% a character`) is een procentteken. Een
   taal met minstens één vertaalde paneeltekst verschijnt in de taalkeuze van het
   paneel; wat niet vertaald is, verschijnt in het Engels.

## Een nieuwe taal

1. Kopieer de hele map `template/` naar een map met de tweeletterige ISO
   639-1-code van je taal (`hu`, `es`, `cs`, `pl`... - zie
   [de lijst](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Dat kan ook in een spreadsheet: download `template/`, vertaal en upload de
   bestanden in de nieuwe map (**Add file > Upload files**, typ `xx/` voor de
   naam om de map aan te maken).
2. Vertaal en open een pull request.

Een nieuwe taal vraagt wat werk in het spel voordat spelers hem kunnen kiezen
(talen buiten codetabel 1250 hebben ook een nieuwe client nodig), dus hij kan
een paar versies na de eerste vertaling komen.

## De controle

Elke pull request voert `tools/validate.py` uit (GitHub Actions). Die meldt,
bij de rij waar hij het vond:

- een `id` die niet in `template/` staat, of twee keer voorkomt;
- een gewijzigde kolom `english`;
- andere variabelen, plaatshouders, tags of kleurcodes dan in het Engels;
- in het blad van het webpaneel andere HTML-tags dan in het Engels, of een
  eigen `<`, `>` of `javascript:`;
- een letter buiten de codetabel van de taal, een tab, een stuurteken, een
  regeleinde waar dat niet mag, een te lange tekst.

Alleen de rijen die jouw pull request heeft gewijzigd worden beoordeeld;
problemen die al in de bestanden zaten worden geteld, maar niet jou
aangerekend. Zelf uitvoeren (Python 3, niets te installeren):
`python tools/validate.py nl`.

## Licentie

Door een pull request te openen ga je ermee akkoord dat je vertaling in Metin2
Singleplayer wordt gebruikt en onder dezelfde voorwaarden als het project
wordt gedeeld: [CC BY-NC-ND 4.0](LICENSE). Bijdragers worden in het project
vermeld. Metin2 zelf en de originele teksten zijn eigendom van Ymir
Interactive en Webzen.
