# Metin2 Singleplayer - fællesskabets oversættelser

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | **Dansk** | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Dette repository indeholder teksterne fra **Metin2 Singleplayer** -
spilklienten, navnene på genstande og monstre, serverens beskeder, quests,
botternes chat og Windows-launcheren - så spillerne kan oversætte spillet til
deres eget sprog. Det indeholder kun oversættelser: ingen spilkode.

Hver pull request bliver kontrolleret automatisk, og godkendte oversættelser
kommer med i spillet i de følgende versioner.

## Hvad findes her

| mappe | indhold |
|---|---|
| `template/` | alle spillets tekster med kolonnen `translation` tom. Starten på et nyt sprog. |
| `de/` `fr/` `pt/` `ro/` `tr/` | de sprog, spillet allerede har, med deres nuværende oversættelse: ret den, og udfyld det, der mangler (rækker med `status` `new`). |
| `hu/` `es/` `it/` `cs/` | nye sprog, endnu ikke påbegyndt (kopier af `template/`). |
| `tools/validate.py` | kontrollen, som hver pull request gennemgår. |

Engelsk er kilden, og polsk vises ved siden af som reference; ingen af dem har
sin egen mappe.

Hver sprogmappe indeholder de samme CSV-filer, delt op i dele, så GitHub kan
vise og redigere dem (højst 700 rækker pr. fil):

| filer | indhold |
|---|---|
| `1_klient_NN.csv` | klienten: vinduer, knapper, værktøjstip, færdigheder, regler |
| `2_przedmioty_potwory_NN.csv` | navne på genstande og monstre, beskrivelser af genstande |
| `3_gra_serwer_NN.csv` | serverens egne beskeder (chat, systemlinjer) |
| `4_questy_NN.csv` | dialogerne i quests |
| `5_boty_czat_NN.csv` | botternes chat, monstrenes snak, serverens sætninger |
| `6_launcher_NN.csv` | Windows-launcheren |

Hver fil har kolonnerne:

| kolonne | |
|---|---|
| `id` | rækkens nøgle. **Ændr den aldrig.** |
| `english` | teksten, der skal oversættes. **Ændr den aldrig.** |
| `polski` | den samme tekst på polsk, som reference (kan være tom). |
| `translation` | **din oversættelse - den eneste kolonne, du redigerer.** Tom = spillet viser det engelske. |
| `notes` | hvor teksten ses, hvad der skal bevares, en længdegrænse. |
| `status` | `new` (ikke oversat), `done` (oversat), `check` (det samme som det engelske - tjek det). Du må sætte den til `done`. |

## Sådan oversætter du

### A. I browseren (små ændringer)

1. Åbn filen, f.eks. [`da/1_klient_01.csv`](da/1_klient_01.csv). GitHub viser
   den som en tabel; brug søgefeltet over den til at finde en række.
2. Klik på blyanten (**Edit this file**). Første gang laver GitHub en kopi (en
   fork) til dig.
3. Ændr kun kolonnen `translation` i de rækker, du vil. En tekst med et komma,
   et anførselstegn eller et linjeskift står i dobbelte anførselstegn
   (`"sådan, her"`); et anførselstegn inde i den skrives to gange (`""`).
4. Klik på **Commit changes...**, så **Propose changes**, så **Create pull
   request**. Skriv i én sætning, hvad du har oversat.

### B. I et regneark (mange rækker)

1. Download filerne (åbn en fil, **Download raw file**; eller den grønne knap
   **Code**, **Download ZIP**, for det hele).
2. Åbn dem i et regneark:
   - **Google Sheets**: Filer > Importér > Upload. Virker uden indstillinger.
   - **LibreOffice Calc**: åbn filen; vælg tegnsæt **UTF-8**, separator
     **komma**, og sæt kolonnerne til **Tekst**.
   - **Excel**: dobbeltklik ikke på filen (Excel ville læse bogstaverne
     forkert). Brug Data > Fra tekst/CSV, filoprindelse **65001: Unicode
     (UTF-8)**, afgrænser **Komma**. Gem som **CSV UTF-8 (kommasepareret)**.
3. Udfyld kolonnen `translation`. Omdøb ikke filerne, tilføj eller fjern ikke
   kolonner, og ændr ikke `id` og `english`. Sortering og filtrering er fint.
4. Gem som CSV (UTF-8, kommasepareret) under samme navn.
5. Åbn sprogmappen på GitHub, **Add file > Upload files**, træk dine filer
   ind, og vælg så **Propose changes** og **Create pull request**.

Du behøver ikke at oversætte det hele på én gang - send det, du har.

## Regler

1. **Kun kolonnen `translation`.** `id` og `english` forbliver, som de er;
   kontrollen afviser en fil, hvor de er ændret.
2. **Bevar hver variabel og hver kode nøjagtigt som i det engelske, i samme
   rækkefølge** - spillet udfylder dem:
   - printf-variabler: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... og `%%` (et procenttegn);
   - pladsholdere: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` er et linjeskift i et questvindue; `[WAIT]`,
     `[DELAY value;5]`, `[COLOR r;1|g;0|b;0]` er dets kommandoer;
   - farver `|cffff0000` ... `|r`, links `|H` ... `|h`, `|E` ... `|e`.

   Du må flytte dem rundt i sætningen, som dit sprog kræver, men variabler af
   typen `%` skal blive i samme rækkefølge. En tekst i kantede parenteser som
   `[Guild]` eller `[PT]` er almindelig tekst: oversæt den.
3. **Bogstaver.** Spillet tegner hvert sprog i én Windows-tegntabel, så kun
   dens bogstaver kan vises - ingen emoji, ingen symboler som `→` eller `✓`:

   | tegntabel | sprog | bogstaver |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (latinsk), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (kyrillisk) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Rumænsk: tegntabellen har kun **ş ţ med cedille**, ikke ș ț med komma.
   Launcheren (`6_launcher_*`) er et selvstændigt Windows-program og tager
   ethvert bogstav.
4. **Botternes chat** (rækker, hvis notes siger "ASCII letters only"):
   botterne skriver som spillere, med almindelige bogstaver a-z uden accenter.
5. **Længde.** Hvor notes siger "max N characters", har spillet ikke plads til
   mere.
6. **Linjeskift** kun hvor det engelske har dem, eller notes siger "new lines
   allowed".

## Et nyt sprog

1. Kopiér hele mappen `template/` til en mappe, der hedder dit sprogs
   tobogstavs ISO 639-1-kode (`hu`, `es`, `cs`, `pl`... - se
   [listen](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Det kan også gøres i et regneark: download `template/`, oversæt, og upload
   filerne til den nye mappe (**Add file > Upload files**, skriv `xx/` foran
   navnet for at oprette mappen).
2. Oversæt, og åbn en pull request.

Et nyt sprog kræver lidt arbejde i spillet, før spillerne kan vælge det (sprog
uden for tegntabel 1250 kræver også en ny klient), så det kan komme nogle
versioner efter den første oversættelse.

## Kontrollen

Hver pull request kører `tools/validate.py` (GitHub Actions). Den melder, ved
den række, hvor den fandt det:

- et `id`, der ikke står i `template/`, eller som står der to gange;
- en ændret kolonne `english`;
- andre variabler, pladsholdere, tags eller farvekoder end i det engelske;
- et bogstav uden for sprogets tegntabel, en tabulator, et kontroltegn, et
  linjeskift, hvor det ikke er tilladt, en for lang tekst.

Kun de rækker, din pull request har ændret, bliver bedømt; problemer, der
allerede var i filerne, bliver talt med, men ikke lagt dig til last. Kør den
selv (Python 3, intet at installere): `python tools/validate.py da`.

## Licens

Ved at åbne en pull request accepterer du, at din oversættelse bruges i Metin2
Singleplayer og deles på samme vilkår som projektet:
[CC BY-NC-ND 4.0](LICENSE). Bidragydere krediteres i projektet. Metin2 selv og
dets originale tekster tilhører Ymir Interactive og Webzen.
