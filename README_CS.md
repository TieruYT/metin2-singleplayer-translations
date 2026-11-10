# Metin2 Singleplayer - komunitní překlady

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | **Čeština** | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Tento repozitář obsahuje texty hry **Metin2 Singleplayer** - herního klienta,
názvy předmětů a příšer, zprávy serveru, úkoly, chat botů, spouštěč pro Windows a klasický webový panel - aby si hráči mohli hru přeložit do svého jazyka. Obsahuje jen
překlady, žádný herní kód.

Každý pull request se automaticky kontroluje a přijaté překlady se dostanou do
hry v dalších verzích.

## Co tu najdeš

| složka | obsah |
|---|---|
| `template/` | všechny texty hry s prázdným sloupcem `translation`. Začátek nového jazyka. |
| `de/` `fr/` `pt/` `ro/` `tr/` | jazyky, které hra už má, s jejich současným překladem: oprav ho a doplň, co chybí (řádky se `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | nové jazyky, celé přeložené s pomocí AI: rodilí mluvčí, opravte prosím, co nezní dobře. |
| `en_US/` | americká angličtina: anglický zdrojový text (britský pravopis) v americkém pravopisu (color, armor, defense...). |
| `tools/validate.py` | kontrola, kterou projde každý pull request. |

Zdrojem je angličtina, polština je vedle jako vodítko; ani jedna nemá vlastní
složku.

Každá jazyková složka obsahuje stejné soubory CSV, rozdělené na části, aby je
GitHub mohl zobrazit a upravit (nejvýše 700 řádků v souboru):

| soubory | obsah |
|---|---|
| `1_klient_NN.csv` | klient: okna, tlačítka, nápovědy, dovednosti, pravidla |
| `2_przedmioty_potwory_NN.csv` | názvy předmětů a příšer, popisy předmětů |
| `3_gra_serwer_NN.csv` | vlastní zprávy serveru (chat, systémové řádky) |
| `4_questy_NN.csv` | dialogy úkolů |
| `5_boty_czat_NN.csv` | chat botů, povídání příšer, věty serveru |
| `6_launcher_NN.csv` | spouštěč pro Windows |
| `7_panel_NN.csv` | klasický webový panel (administrátorský panel na portu 7788, v prohlížeči) |

Každý soubor má sloupce:

| sloupec | |
|---|---|
| `id` | klíč řádku. **Nikdy ho neměň.** |
| `english` | text k překladu. **Nikdy ho neměň.** |
| `polski` | tentýž text polsky, jako vodítko (může být prázdný). |
| `translation` | **tvůj překlad - jediný sloupec, který upravuješ.** Prázdný = hra ukáže angličtinu. |
| `notes` | kde je text vidět, co se musí zachovat, omezení délky. |
| `status` | `new` (nepřeloženo), `done` (přeloženo), `check` (stejné jako angličtina - zkontroluj). Můžeš ho nastavit na `done`. |

## Jak překládat

### A. V prohlížeči (malé změny)

1. Otevři soubor, např. [`cs/1_klient_01.csv`](cs/1_klient_01.csv). GitHub ho
   ukáže jako tabulku; řádek najdeš vyhledávacím polem nad ní.
2. Klikni na tužku (**Edit this file**). Poprvé ti GitHub vytvoří kopii (fork).
3. Měň jen sloupec `translation` u řádků, které chceš. Text s čárkou,
   uvozovkami nebo novým řádkem je ve dvojitých uvozovkách (`"takhle, třeba"`);
   uvozovky uvnitř se píšou dvakrát (`""`).
4. Klikni na **Commit changes...**, pak **Propose changes**, pak **Create pull
   request**. Napiš jednou větou, co jsi přeložil.

### B. V tabulkovém procesoru (hodně řádků)

1. Stáhni soubory (otevři soubor, **Download raw file**; nebo zelené tlačítko
   **Code**, **Download ZIP**, pro všechno).
2. Otevři je v tabulkovém procesoru:
   - **Tabulky Google**: Soubor > Importovat > Nahrát. Funguje bez nastavení.
   - **LibreOffice Calc**: otevři soubor; zvol znakovou sadu **UTF-8**,
     oddělovač **čárka** a nastav sloupce jako **Text**.
   - **Excel**: na soubor neklikej dvakrát (Excel by špatně načetl písmena).
     Použij Data > Z textu/CSV, původ souboru **65001: Unicode (UTF-8)**,
     oddělovač **Čárka**. Ulož jako **CSV UTF-8 (s oddělovači - čárkami)**.
3. Vyplň sloupec `translation`. Soubory nepřejmenovávej, nepřidávej ani
   nemaž sloupce a neměň `id` a `english`. Řazení a filtrování nevadí.
4. Ulož jako CSV (UTF-8, oddělené čárkami) pod stejným názvem.
5. Na GitHubu otevři jazykovou složku, **Add file > Upload files**, přetáhni
   soubory, pak **Propose changes** a **Create pull request**.

Nemusíš přeložit všechno najednou - pošli, co máš.

## Pravidla

1. **Jen sloupec `translation`.** `id` a `english` zůstávají, jak jsou;
   kontrola odmítne soubor, ve kterém byly změněny.
2. **Zachovej každou proměnnou a každý kód přesně jako v angličtině, ve
   stejném pořadí** - doplňuje je hra:
   - proměnné printf: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... a `%%` (znak procenta);
   - zástupné symboly: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` je nový řádek v okně úkolu; `[WAIT]`, `[DELAY value;5]`,
     `[COLOR r;1|g;0|b;0]` jsou jeho příkazy;
   - barvy `|cffff0000` ... `|r`, odkazy `|H` ... `|h`, `|E` ... `|e`.

   Ve větě je můžeš přesunout, jak tvůj jazyk potřebuje, ale proměnné typu
   `%` musí zůstat ve stejném pořadí. Text v hranatých závorkách jako
   `[Guild]` nebo `[PT]` je běžný text: přelož ho.
3. **Písmena.** Hra vykresluje každý jazyk v jedné znakové sadě Windows, takže
   lze zobrazit jen její písmena - žádné emoji, žádné symboly jako `→` nebo
   `✓`:

   | znaková sada | jazyky | písmena |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (latinka), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (cyrilice) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Rumunština: znaková sada má jen **ş ţ se cedilou**, ne ș ț s čárkou.
   Spouštěč (`6_launcher_*`) je samostatný program pro Windows a přijme
   jakékoli písmeno. Stejně tak webový panel (`7_panel_*`), stránka v
   prohlížeči: oba jsou v **UTF-8**, jakékoli písmeno jakéhokoli jazyka.
4. **Chat botů** (řádky, jejichž notes říkají „ASCII letters only“): boti
   píšou jako hráči, obyčejnými písmeny a-z bez diakritiky.
5. **Délka.** Kde notes říkají „max N characters“, hra nemá místo na víc.
6. **Nové řádky** jen tam, kde je má angličtina nebo kde notes říkají „new
   lines allowed“.
7. **Webový panel** (`7_panel_*`): jeho texty končí na webové stránce, proto
   zachovej HTML značky angličtiny přesně tak, jak jsou (`<b>`, `</b>`,
   `<a href="...">`, `<br>` a zástupné symboly typu `<number>` ve špičatých
   závorkách) a nepřidávej žádné vlastní `<`, `>` ani `javascript:`. Jeho
   proměnné jsou `%s`, `%d`, `%(name)s` a `{name}`; pojmenované `%(name)s` se
   smí přesunout. `%` následované mezerou (`25% a character`) je znak procenta.
   Jazyk s aspoň jedním přeloženým textem panelu se objeví ve výběru jazyka
   panelu; co přeloženo není, se zobrazí anglicky.

## Nový jazyk

1. Zkopíruj celou složku `template/` do složky pojmenované dvoupísmenným
   kódem ISO 639-1 tvého jazyka (`hu`, `es`, `cs`, `pl`... - viz
   [seznam](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Jde to i v tabulkovém procesoru: stáhni `template/`, přelož a nahraj
   soubory do nové složky (**Add file > Upload files**, před název napiš
   `xx/`, tím se složka vytvoří).
2. Přelož a otevři pull request.

Nový jazyk potřebuje ve hře trochu práce, než si ho hráči budou moci vybrat
(jazyky mimo znakovou sadu 1250 potřebují i nového klienta), takže může přijít
až několik verzí po prvním překladu.

## Kontrola

Každý pull request spustí `tools/validate.py` (GitHub Actions). Ohlásí, u
řádku, kde to našla:

- `id`, které není v `template/`, nebo je tam dvakrát;
- změněný sloupec `english`;
- jiné proměnné, zástupné symboly, značky nebo barevné kódy než v angličtině;
- v listu webového panelu jiné HTML značky než v angličtině, nebo vlastní
  `<`, `>` či `javascript:`;
- písmeno mimo znakovou sadu jazyka, tabulátor, řídicí znak, nový řádek tam,
  kde není povolen, příliš dlouhý text.

Posuzují se jen řádky, které tvůj pull request změnil; problémy, které už v
souborech byly, se počítají, ale nepřičítají se tobě. Spuštění vlastními
silami (Python 3, nic se neinstaluje): `python tools/validate.py cs`.

## Licence

Otevřením pull requestu souhlasíš s tím, že tvůj překlad bude použit v Metin2
Singleplayer a sdílen za stejných podmínek jako projekt:
[CC BY-NC-ND 4.0](LICENSE). Přispěvatelé jsou v projektu uvedeni. Samotná hra
Metin2 a její původní texty patří společnostem Ymir Interactive a Webzen.
