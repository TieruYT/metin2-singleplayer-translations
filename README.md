# Metin2 Singleplayer - community translations

**English** | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

This repository holds the texts of **Metin2 Singleplayer** - the game client,
the item and monster names, the server's messages, the quests, the bots' chat,
the Windows launcher and the classic web panel - so that players can translate
the game into their own language. It contains translations only: no game code.

Every pull request is checked automatically, and accepted translations go into
the game in the following versions.

## What is here

| folder | what |
|---|---|
| `template/` | every text of the game, the `translation` column empty. The start of a new language. |
| `de/` `fr/` `pt/` `ro/` `tr/` | the languages the game already has, with their current translation filled in: correct it and fill in what is missing (rows with `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | new languages, fully translated with AI help: native speakers, please correct what sounds wrong. |
| `en_US/` | American English: the English source (British spelling) in US spelling (color, armor, defense...). |
| `tools/validate.py` | the check every pull request goes through. |

English is the source and Polish is shown beside it for reference; neither
has a folder of its own.

Each language folder holds the same CSV files, cut into parts so that GitHub
can show and edit them (at most 700 rows a file):

| files | what |
|---|---|
| `1_klient_NN.csv` | the client: windows, buttons, tooltips, skills, rules |
| `2_przedmioty_potwory_NN.csv` | item and monster names, item descriptions |
| `3_gra_serwer_NN.csv` | the server's own messages (chat, system lines) |
| `4_questy_NN.csv` | the quests' dialogs |
| `5_boty_czat_NN.csv` | the bots' chat, the monsters' chatter, the server's phrases |
| `6_launcher_NN.csv` | the Windows launcher |
| `7_panel_NN.csv` | the classic web panel (the admin panel on port 7788, in the browser) |

Every file has the columns:

| column | |
|---|---|
| `id` | the row's key. **Never change it.** |
| `english` | the text to translate. **Never change it.** |
| `polski` | the same text in Polish, for reference (may be empty). |
| `translation` | **your translation - the only column you edit.** Empty = the game shows the English. |
| `notes` | where the text is seen, what must be kept, a length limit. |
| `status` | `new` (not translated), `done` (translated), `check` (the same as the English - check it). You may set it to `done`. |

## How to translate

### A. In the browser (small changes)

1. Open the file, e.g. [`de/1_klient_01.csv`](de/1_klient_01.csv). GitHub shows
   it as a table; use the search box above it to find a row.
2. Click the pencil (**Edit this file**). GitHub makes a copy (a fork) for
   you the first time.
3. Change only the `translation` column of the rows you want. A text with a
   comma, a quote or a new line is in double quotes (`"like, this"`); a
   quote inside it is written twice (`""`).
4. Click **Commit changes...**, then **Propose changes**, then **Create pull
   request**. Say in a sentence what you translated.

### B. In a spreadsheet (a lot of rows)

1. Download the files (open a file, **Download raw file**; or the green
   **Code** button, **Download ZIP**, for everything).
2. Open them in a spreadsheet:
   - **Google Sheets**: File > Import > Upload. Works with no settings.
   - **LibreOffice Calc**: open the file; choose character set **UTF-8**,
     separator **comma**, and set the columns to **Text**.
   - **Excel**: do not double-click the file (Excel would read the letters
     wrongly). Use Data > From Text/CSV, File origin **65001: Unicode
     (UTF-8)**, delimiter **Comma**. Save as **CSV UTF-8 (comma delimited)**.
3. Fill in the `translation` column. Do not rename the files, add or remove
   columns, or change `id` and `english`. Sorting and filtering are fine.
4. Save as CSV (UTF-8, comma separated) under the same name.
5. On GitHub open the language folder, **Add file > Upload files**, drop your
   files in, then **Propose changes** and **Create pull request**.

You need not translate everything at once - send what you have.

## Rules

1. **Only the `translation` column.** `id` and `english` stay as they are;
   the check refuses a file where they were changed.
2. **Keep every variable and code exactly as in the English, in the same
   order** - they are filled in by the game:
   - printf variables: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... and `%%` (a percent sign);
   - placeholders: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` is a new line in a quest window; `[WAIT]`, `[DELAY value;5]`,
     `[COLOR r;1|g;0|b;0]` are its commands;
   - colours `|cffff0000` ... `|r`, links `|H` ... `|h`, `|E` ... `|e`.

   You may move them within the sentence, as your language needs, but
   variables of the `%` kind must stay in the same order. A text in brackets
   such as `[Guild]` or `[PT]` is ordinary text: translate it.
3. **Letters.** The game draws each language in one Windows code page, so
   only its letters can be shown - no emoji, no symbols such as `→` or `✓`:

   | code page | languages | letters |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (Latin), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (Cyrillic) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Romanian: the code page has **ş ţ with a cedilla** only, not ș ț with a
   comma. The launcher (`6_launcher_*`) is a Windows program of its own and
   takes any letter, and so does the web panel (`7_panel_*`), a page in a
   browser: both are **UTF-8**, any letter of any language.
4. **The bots' chat** (rows whose notes say "ASCII letters only"): the bots
   type like players, in plain letters a-z with no accents.
5. **Length.** Where the notes say "max N characters", the game has no room
   for more.
6. **New lines** only where the English has them or the notes say "new lines
   allowed".
7. **The web panel** (`7_panel_*`): its texts go into a web page, so keep the
   English's HTML tags exactly as they are (`<b>`, `</b>`, `<a href="...">`,
   `<br>`, and the `<number>`-style placeholders in angle brackets) and add no
   `<`, `>` or `javascript:` of your own. Its variables are `%s`, `%d`,
   `%(name)s` and `{name}`; a named `%(name)s` may move. A `%` followed by a
   space (`25% a character`) is a percent sign. A language with at least one
   translated panel text appears in the panel's language switch; what is not
   translated shows in English.

## A new language

1. Copy the whole `template/` folder to a folder named with your language's
   two-letter ISO 639-1 code (`hu`, `es`, `cs`, `pl`... - see
   [the list](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   You can do it in a spreadsheet: download `template/`, translate, and
   upload the files into the new folder (**Add file > Upload files**, type
   `xx/` in front of the name to make the folder).
2. Translate and open a pull request.

A new language needs some work in the game before players can choose it
(languages outside code page 1250 also need a new client), so it may come a
few versions after the first translation.

## The check

Every pull request runs `tools/validate.py` (GitHub Actions). It reports, at
the row it found it:

- an `id` that is not in `template/`, or twice;
- a changed `english` column;
- other variables, placeholders, tags or colour codes than the English;
- in the web panel's sheet, other HTML tags than the English, or a `<`, `>`
  or `javascript:` of its own;
- a letter outside the language's code page, a tab, a control character, a
  new line where none is allowed, a text too long.

Only the rows your pull request changed are judged; problems that were
already in the files are counted, not held against you. To run it yourself
(Python 3, nothing to install): `python tools/validate.py de`.

## Licence

By opening a pull request you agree that your translation is used in Metin2
Singleplayer and shared under the same terms as the project:
[CC BY-NC-ND 4.0](LICENSE). Contributors are credited in the project.
Metin2 itself and its original texts belong to Ymir Interactive and Webzen.
