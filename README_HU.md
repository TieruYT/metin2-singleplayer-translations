# Metin2 Singleplayer - közösségi fordítások

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | **Magyar** | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Ez a tároló a **Metin2 Singleplayer** szövegeit tartalmazza - a játékklienst,
a tárgyak és szörnyek neveit, a szerver üzeneteit, a küldetéseket, a botok csevegését, a Windowsos indítót és a klasszikus webpanelt -, hogy a játékosok lefordíthassák a játékot
a saját nyelvükre. Csak fordításokat tartalmaz, játékkódot nem.

Minden pull requestet automatikusan ellenőrzünk, az elfogadott fordítások a
következő verziókban kerülnek a játékba.

## Mi található itt

| mappa | tartalom |
|---|---|
| `template/` | a játék összes szövege, üres `translation` oszloppal. Egy új nyelv kiindulópontja. |
| `de/` `fr/` `pt/` `ro/` `tr/` | a játékban már meglévő nyelvek a jelenlegi fordításukkal: javítsd, és egészítsd ki, ami hiányzik (a `status` `new` sorok). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | új nyelvek, teljesen lefordítva MI segítségével: anyanyelvi beszélők, javítsátok, ami rosszul hangzik. |
| `en_US/` | amerikai angol: az angol forrásszöveg (brit helyesírás) amerikai helyesírással (color, armor, defense...). |
| `tools/validate.py` | az ellenőrzés, amelyen minden pull request átmegy. |

Az angol a forrás, a lengyel referenciaként mellette látható; egyiknek sincs
saját mappája.

Minden nyelvi mappában ugyanazok a CSV-fájlok vannak, részekre vágva, hogy a
GitHub meg tudja jeleníteni és szerkeszteni őket (fájlonként legfeljebb 700
sor):

| fájlok | tartalom |
|---|---|
| `1_klient_NN.csv` | a kliens: ablakok, gombok, súgószövegek, képességek, szabályok |
| `2_przedmioty_potwory_NN.csv` | tárgyak és szörnyek nevei, tárgyleírások |
| `3_gra_serwer_NN.csv` | a szerver saját üzenetei (csevegés, rendszersorok) |
| `4_questy_NN.csv` | a küldetések párbeszédei |
| `5_boty_czat_NN.csv` | a botok csevegése, a szörnyek fecsegése, a szerver mondatai |
| `6_launcher_NN.csv` | a Windowsos indító |
| `7_panel_NN.csv` | a klasszikus webpanel (az adminpanel a 7788-as porton, böngészőben) |

Minden fájl oszlopai:

| oszlop | |
|---|---|
| `id` | a sor kulcsa. **Soha ne módosítsd.** |
| `english` | a fordítandó szöveg. **Soha ne módosítsd.** |
| `polski` | ugyanaz a szöveg lengyelül, referenciaként (lehet üres). |
| `translation` | **a fordításod - az egyetlen oszlop, amelyet szerkesztesz.** Üres = a játék az angolt mutatja. |
| `notes` | hol látható a szöveg, mit kell megtartani, hosszkorlát. |
| `status` | `new` (nincs lefordítva), `done` (lefordítva), `check` (ugyanaz, mint az angol - ellenőrizd). Átállíthatod `done`-ra. |

## Hogyan fordíts

### A. A böngészőben (kisebb módosítások)

1. Nyisd meg a fájlt, pl. [`hu/1_klient_01.csv`](hu/1_klient_01.csv). A GitHub
   táblázatként mutatja; a fölötte lévő keresőmezővel találsz meg egy sort.
2. Kattints a ceruzára (**Edit this file**). Első alkalommal a GitHub másolatot
   (forkot) készít neked.
3. Csak a kívánt sorok `translation` oszlopát módosítsd. A vesszőt,
   idézőjelet vagy sortörést tartalmazó szöveg dupla idézőjelek között áll
   (`"így, például"`); a benne lévő idézőjelet kétszer kell írni (`""`).
4. Kattints a **Commit changes...**, majd a **Propose changes**, végül a
   **Create pull request** gombra. Egy mondatban írd le, mit fordítottál.

### B. Táblázatkezelőben (sok sor)

1. Töltsd le a fájlokat (nyiss meg egy fájlt, **Download raw file**; vagy a
   zöld **Code** gomb, **Download ZIP**, mindenhez).
2. Nyisd meg őket egy táblázatkezelőben:
   - **Google Táblázatok**: Fájl > Importálás > Feltöltés. Beállítás nélkül
     működik.
   - **LibreOffice Calc**: nyisd meg a fájlt; válaszd az **UTF-8**
     karakterkészletet, a **vessző** elválasztót, és állítsd az oszlopokat
     **Szöveg** típusúra.
   - **Excel**: ne kattints duplán a fájlra (az Excel rosszul olvasná a
     betűket). Használd az Adatok > Szövegből/CSV-ből menüt, fájl eredete
     **65001: Unicode (UTF-8)**, elválasztó **Vessző**. Mentsd **CSV UTF-8
     (vesszővel tagolt)** formátumban.
3. Töltsd ki a `translation` oszlopot. Ne nevezd át a fájlokat, ne adj hozzá
   és ne törölj oszlopot, ne módosítsd az `id`-t és az `english`-t. A
   rendezés és szűrés rendben van.
4. Mentsd CSV-ként (UTF-8, vesszővel tagolt) ugyanazon a néven.
5. A GitHubon nyisd meg a nyelvi mappát, **Add file > Upload files**, húzd be
   a fájlokat, majd **Propose changes** és **Create pull request**.

Nem kell mindent egyszerre lefordítanod - küldd el, ami megvan.

## Szabályok

1. **Csak a `translation` oszlop.** Az `id` és az `english` marad, ahogy van;
   az ellenőrzés elutasítja azt a fájlt, amelyben módosultak.
2. **Minden változót és kódot pontosan úgy tarts meg, mint az angolban,
   ugyanabban a sorrendben** - ezeket a játék tölti ki:
   - printf-változók: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... és `%%` (egy százalékjel);
   - helyőrzők: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - az `[ENTER]` sortörés a küldetésablakban; a `[WAIT]`, a
     `[DELAY value;5]` és a `[COLOR r;1|g;0|b;0]` a parancsai;
   - színek `|cffff0000` ... `|r`, hivatkozások `|H` ... `|h`, `|E` ... `|e`.

   A mondaton belül áthelyezheted őket, ahogy a nyelved kívánja, de a `%`
   típusú változóknak ugyanabban a sorrendben kell maradniuk. A szögletes
   zárójelben álló szöveg, mint a `[Guild]` vagy a `[PT]`, közönséges szöveg:
   fordítsd le.
3. **Betűk.** A játék minden nyelvet egy Windows-kódlapon rajzol ki, így csak
   annak betűi jeleníthetők meg - se emoji, se olyan jelek, mint a `→` vagy a
   `✓`:

   | kódlap | nyelvek | betűk |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (latin), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (cirill) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Román: a kódlapon csak **cedillás ş ţ** van, vesszős ș ț nincs. Az indító
   (`6_launcher_*`) önálló Windows-program, és bármilyen betűt elfogad. Ugyanígy a webpanel (`7_panel_*`), egy oldal a
   böngészőben: mindkettő **UTF-8**, bármely nyelv bármely betűje.
4. **A botok csevegése** (azok a sorok, amelyek notes mezője szerint „ASCII
   letters only”): a botok úgy gépelnek, mint a játékosok, egyszerű a-z
   betűkkel, ékezetek nélkül.
5. **Hossz.** Ahol a notes „max N characters”-t ír, ott a játékban nincs hely
   többnek.
6. **Sortörés** csak ott, ahol az angolban is van, vagy ahol a notes „new
   lines allowed”-ot ír.
7. **A webpanel** (`7_panel_*`): a szövegei egy weboldalra kerülnek, ezért
   tartsd meg az angol HTML-címkéit pontosan úgy, ahogy vannak (`<b>`, `</b>`,
   `<a href="...">`, `<br>` és a `<number>`-szerű helyőrzők csúcsos zárójelben),
   és ne tegyél hozzá saját `<`, `>` vagy `javascript:` elemet. A változói `%s`,
   `%d`, `%(name)s` és `{name}`; egy nevesített `%(name)s` áthelyezhető. A
   szóközzel követett `%` (`25% a character`) százalékjel. Az a nyelv, amelynek
   legalább egy panelszövege le van fordítva, megjelenik a panel nyelvválasztójában;
   ami nincs lefordítva, angolul jelenik meg.

## Új nyelv

1. Másold a teljes `template/` mappát egy olyan mappába, amelynek neve a
   nyelved kétbetűs ISO 639-1 kódja (`hu`, `es`, `cs`, `pl`... - lásd
   [a listát](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Táblázatkezelőben is megoldható: töltsd le a `template/` mappát, fordíts,
   és töltsd fel a fájlokat az új mappába (**Add file > Upload files**, írd a
   név elé, hogy `xx/`, így jön létre a mappa).
2. Fordíts, és nyiss egy pull requestet.

Egy új nyelvhez némi munka kell a játékban, mielőtt a játékosok választhatják
(az 1250-es kódlapon kívüli nyelvekhez új kliens is kell), így az első
fordítás után néhány verzióval később érkezhet.

## Az ellenőrzés

Minden pull request lefuttatja a `tools/validate.py`-t (GitHub Actions). Annál
a sornál jelzi, ahol megtalálta:

- olyan `id`-t, amely nincs a `template/` mappában, vagy kétszer szerepel;
- módosított `english` oszlopot;
- az angoltól eltérő változókat, helyőrzőket, címkéket vagy színkódokat;
- a webpanel lapján az angoltól eltérő HTML-címkéket, vagy saját `<`, `>`
  vagy `javascript:` elemet;
- a nyelv kódlapján kívüli betűt, tabulátort, vezérlőkaraktert, nem
  engedélyezett sortörést, túl hosszú szöveget.

Csak a pull requested által módosított sorokat bírálja el; a fájlokban már
meglévő hibákat megszámolja, de nem rád terheli. Saját futtatás (Python 3,
semmit sem kell telepíteni): `python tools/validate.py hu`.

## Licenc

Pull request nyitásával elfogadod, hogy a fordításodat a Metin2 Singleplayer
felhasználja, és a projekttel azonos feltételekkel teszi közzé:
[CC BY-NC-ND 4.0](LICENSE). A közreműködőket a projekt feltünteti. Maga a
Metin2 és eredeti szövegei a Ymir Interactive és a Webzen tulajdonai.
