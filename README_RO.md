# Metin2 Singleplayer - traduceri ale comunității

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | **Română** | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Acest depozit conține textele din **Metin2 Singleplayer** - clientul jocului,
numele obiectelor și ale monștrilor, mesajele serverului, misiunile, chatul boților, launcherul pentru Windows și panoul web clasic - pentru ca jucătorii să poată traduce
jocul în propria limbă. Conține doar traduceri: niciun cod al jocului.

Fiecare pull request este verificat automat, iar traducerile acceptate intră
în joc în versiunile următoare.

## Ce găsești aici

| dosar | conținut |
|---|---|
| `template/` | toate textele jocului, cu coloana `translation` goală. Punctul de plecare al unei limbi noi. |
| `de/` `fr/` `pt/` `ro/` `tr/` | limbile pe care jocul le are deja, cu traducerea lor actuală: corectează-o și completează ce lipsește (rândurile cu `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | limbi noi, traduse complet cu ajutorul AI: vorbitori nativi, corectați ce sună greșit. |
| `en_US/` | engleză americană: textul sursă englezesc (ortografie britanică) în ortografie americană (color, armor, defense...). |
| `tools/validate.py` | verificarea prin care trece fiecare pull request. |

Engleza este sursa, iar poloneza este afișată alături ca referință; niciuna
nu are un dosar propriu.

Fiecare dosar de limbă conține aceleași fișiere CSV, împărțite în bucăți ca
GitHub să le poată afișa și edita (cel mult 700 de rânduri pe fișier):

| fișiere | conținut |
|---|---|
| `1_klient_NN.csv` | clientul: ferestre, butoane, indicii, abilități, reguli |
| `2_przedmioty_potwory_NN.csv` | numele obiectelor și ale monștrilor, descrierile obiectelor |
| `3_gra_serwer_NN.csv` | mesajele proprii ale serverului (chat, linii de sistem) |
| `4_questy_NN.csv` | dialogurile misiunilor |
| `5_boty_czat_NN.csv` | chatul boților, vorbăria monștrilor, frazele serverului |
| `6_launcher_NN.csv` | launcherul pentru Windows |
| `7_panel_NN.csv` | panoul web clasic (panoul de administrare pe portul 7788, în browser) |

Fiecare fișier are coloanele:

| coloană | |
|---|---|
| `id` | cheia rândului. **Nu o modifica niciodată.** |
| `english` | textul de tradus. **Nu îl modifica niciodată.** |
| `polski` | același text în poloneză, ca referință (poate fi gol). |
| `translation` | **traducerea ta - singura coloană pe care o editezi.** Gol = jocul afișează engleza. |
| `notes` | unde apare textul, ce trebuie păstrat, o limită de lungime. |
| `status` | `new` (netradus), `done` (tradus), `check` (la fel ca în engleză - verifică-l). Îl poți seta la `done`. |

## Cum traduci

### A. În browser (modificări mici)

1. Deschide fișierul, de ex. [`ro/1_klient_01.csv`](ro/1_klient_01.csv).
   GitHub îl afișează ca tabel; folosește caseta de căutare de deasupra ca să
   găsești un rând.
2. Apasă pe creion (**Edit this file**). Prima dată, GitHub face o copie (un
   fork) pentru tine.
3. Modifică doar coloana `translation` a rândurilor dorite. Un text cu o
   virgulă, ghilimele sau un rând nou stă între ghilimele duble
   (`"așa, de exemplu"`); ghilimelele din interior se scriu de două ori
   (`""`).
4. Apasă **Commit changes...**, apoi **Propose changes**, apoi **Create pull
   request**. Spune într-o propoziție ce ai tradus.

### B. Într-o foaie de calcul (multe rânduri)

1. Descarcă fișierele (deschide un fișier, **Download raw file**; sau butonul
   verde **Code**, **Download ZIP**, pentru tot).
2. Deschide-le într-o foaie de calcul:
   - **Google Sheets**: Fișier > Importă > Încarcă. Funcționează fără setări.
   - **LibreOffice Calc**: deschide fișierul; alege setul de caractere
     **UTF-8**, separatorul **virgulă** și setează coloanele ca **Text**.
   - **Excel**: nu face dublu clic pe fișier (Excel ar citi greșit literele).
     Folosește Date > Din text/CSV, origine fișier **65001: Unicode (UTF-8)**,
     delimitator **Virgulă**. Salvează ca **CSV UTF-8 (delimitat prin
     virgulă)**.
3. Completează coloana `translation`. Nu redenumi fișierele, nu adăuga și nu
   șterge coloane și nu modifica `id` și `english`. Sortarea și filtrarea sunt
   în regulă.
4. Salvează ca CSV (UTF-8, separat prin virgulă) cu același nume.
5. Pe GitHub deschide dosarul limbii, **Add file > Upload files**, trage
   fișierele, apoi **Propose changes** și **Create pull request**.

Nu trebuie să traduci totul deodată - trimite ce ai.

## Reguli

1. **Doar coloana `translation`.** `id` și `english` rămân cum sunt;
   verificarea respinge un fișier în care au fost modificate.
2. **Păstrează fiecare variabilă și fiecare cod exact ca în engleză, în
   aceeași ordine** - jocul le completează:
   - variabile printf: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... și `%%` (un semn procent);
   - substituenți: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` este un rând nou într-o fereastră de misiune; `[WAIT]`,
     `[DELAY value;5]`, `[COLOR r;1|g;0|b;0]` sunt comenzile ei;
   - culori `|cffff0000` ... `|r`, legături `|H` ... `|h`, `|E` ... `|e`.

   Le poți muta în propoziție cum are nevoie limba ta, dar variabilele de tip
   `%` trebuie să rămână în aceeași ordine. Un text între paranteze drepte,
   ca `[Guild]` sau `[PT]`, este text obișnuit: tradu-l.
3. **Litere.** Jocul desenează fiecare limbă într-o pagină de cod Windows,
   așa că se pot afișa doar literele ei - fără emoji, fără simboluri ca `→`
   sau `✓`:

   | pagină de cod | limbi | litere |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (latină), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (chirilică) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Română: pagina de cod are doar **ş ţ cu sedilă**, nu ș ț cu virgulă (în
   fișierele jocului). Launcherul (`6_launcher_*`) este un program Windows
   separat și acceptă orice literă. La fel și panoul web (`7_panel_*`), o pagină în
   browser: ambele sunt **UTF-8**, orice literă a oricărei limbi.
4. **Chatul boților** (rândurile ale căror note spun „ASCII letters only”):
   boții scriu ca jucătorii, cu litere simple a-z, fără diacritice.
5. **Lungime.** Unde notele spun „max N characters”, jocul nu are loc pentru
   mai mult.
6. **Rânduri noi** doar unde le are engleza sau unde notele spun „new lines
   allowed”.
7. **Panoul web** (`7_panel_*`): textele lui ajung într-o pagină web, așa că
   păstrează etichetele HTML din engleză exact cum sunt (`<b>`, `</b>`,
   `<a href="...">`, `<br>` și substituenții de tipul `<number>` între paranteze
   unghiulare) și nu adăuga niciun `<`, `>` sau `javascript:` propriu.
   Variabilele lui sunt `%s`, `%d`, `%(name)s` și `{name}`; un `%(name)s` cu nume
   se poate muta. Un `%` urmat de spațiu (`25% a character`) este semnul
   procentului. O limbă cu cel puțin un text tradus din panou apare în selectorul
   de limbă al panoului; ce nu este tradus apare în engleză.

## O limbă nouă

1. Copiază tot dosarul `template/` într-un dosar numit cu codul ISO 639-1 de
   două litere al limbii tale (`hu`, `es`, `cs`, `pl`... - vezi
   [lista](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Poți face asta într-o foaie de calcul: descarcă `template/`, tradu și
   încarcă fișierele în dosarul nou (**Add file > Upload files**, scrie `xx/`
   înaintea numelui ca să creezi dosarul).
2. Tradu și deschide un pull request.

O limbă nouă are nevoie de puțină muncă în joc înainte ca jucătorii să o
poată alege (limbile din afara paginii de cod 1250 au nevoie și de un client
nou), așa că poate apărea la câteva versiuni după prima traducere.

## Verificarea

Fiecare pull request rulează `tools/validate.py` (GitHub Actions). Semnalează,
la rândul unde l-a găsit:

- un `id` care nu este în `template/`, sau apare de două ori;
- o coloană `english` modificată;
- alte variabile, substituenți, etichete sau coduri de culoare decât în
  engleză;
- în foaia panoului web, alte etichete HTML decât în engleză, sau un `<`, `>`
  sau `javascript:` propriu;
- o literă din afara paginii de cod a limbii, un tab, un caracter de control,
  un rând nou unde nu este permis, un text prea lung.

Sunt judecate doar rândurile modificate de pull request-ul tău; problemele
care existau deja în fișiere sunt numărate, nu ți se impută. Ca s-o rulezi
singur (Python 3, nimic de instalat): `python tools/validate.py ro`.

## Licență

Deschizând un pull request, ești de acord ca traducerea ta să fie folosită în
Metin2 Singleplayer și distribuită în aceleași condiții ca proiectul:
[CC BY-NC-ND 4.0](LICENSE). Contribuitorii sunt menționați în proiect. Metin2
și textele sale originale aparțin Ymir Interactive și Webzen.
