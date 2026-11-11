# Metin2 Singleplayer - tłumaczenia społeczności

[English](README.md) | **Polski** | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Italiano](README_IT.md) | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

To repozytorium zawiera teksty gry **Metin2 Singleplayer** - klienta, nazwy
przedmiotów i potworów, komunikaty serwera, questy, czat botów, launcher
Windows i klasyczny panel WWW - żeby gracze mogli przetłumaczyć grę na swój język. Są tu tylko
tłumaczenia, bez kodu gry.

Każdy pull request jest sprawdzany automatycznie, a przyjęte tłumaczenia
trafiają do gry w kolejnych wersjach.

## Co tu jest

| folder | co |
|---|---|
| `template/` | wszystkie teksty gry z pustą kolumną `translation`. Początek nowego języka. |
| `de/` `fr/` `pt/` `ro/` `tr/` | języki, które gra już ma, z obecnym tłumaczeniem: popraw je i uzupełnij braki (wiersze ze `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | nowe języki, w całości przetłumaczone z pomocą AI: rodzimi użytkownicy, poprawcie to, co brzmi źle. |
| `en_US/` | angielski amerykański: angielski tekst źródłowy (pisownia brytyjska) w pisowni amerykańskiej (color, armor, defense...). |
| `tools/validate.py` | sprawdzenie, przez które przechodzi każdy pull request. |

Angielski jest źródłem, a polski stoi obok pomocniczo; żaden z nich nie ma
własnego folderu.

Każdy folder języka ma te same pliki CSV, podzielone na części, żeby GitHub
mógł je pokazać i edytować (najwyżej 700 wierszy w pliku):

| pliki | co |
|---|---|
| `1_klient_NN.csv` | klient: okna, przyciski, opisy, umiejętności, regulamin |
| `2_przedmioty_potwory_NN.csv` | nazwy przedmiotów i potworów, opisy przedmiotów |
| `3_gra_serwer_NN.csv` | komunikaty serwera (czat, linie systemowe) |
| `4_questy_NN.csv` | dialogi questów |
| `5_boty_czat_NN.csv` | czat botów, okrzyki potworów, frazy serwera |
| `6_launcher_NN.csv` | launcher Windows |
| `7_panel_NN.csv` | klasyczny panel WWW (panel administratora na porcie 7788, w przeglądarce) |

Kolumny każdego pliku:

| kolumna | |
|---|---|
| `id` | klucz wiersza. **Nigdy go nie zmieniaj.** |
| `english` | tekst do przetłumaczenia. **Nigdy go nie zmieniaj.** |
| `polski` | ten sam tekst po polsku, pomocniczo (może być pusty). |
| `translation` | **Twoje tłumaczenie - jedyna kolumna, którą edytujesz.** Pusta = gra pokaże angielski. |
| `notes` | gdzie tekst widać, czego nie ruszać, limit długości. |
| `status` | `new` (brak tłumaczenia), `done` (jest), `check` (to samo co po angielsku - sprawdź). Możesz ustawić `done`. |

## Jak tłumaczyć

### A. W przeglądarce (drobne zmiany)

1. Otwórz plik, np. [`de/1_klient_01.csv`](de/1_klient_01.csv). GitHub pokazuje
   go jako tabelę; pole wyszukiwania nad nią znajdzie wiersz.
2. Kliknij ołówek (**Edit this file**). Za pierwszym razem GitHub zrobi Ci
   kopię (fork).
3. Zmieniaj tylko kolumnę `translation` wybranych wierszy. Tekst z przecinkiem,
   cudzysłowem albo nową linią jest w cudzysłowie (`"o, tak"`); cudzysłów
   wewnątrz pisze się podwójnie (`""`).
4. Kliknij **Commit changes...**, potem **Propose changes** i **Create pull
   request**. Napisz jednym zdaniem, co przetłumaczyłeś.

### B. W arkuszu (dużo wierszy)

1. Pobierz pliki (otwórz plik, **Download raw file**; albo zielony przycisk
   **Code**, **Download ZIP**, żeby mieć wszystko).
2. Otwórz je w arkuszu:
   - **Google Sheets**: Plik > Importuj > Prześlij. Działa bez ustawień.
   - **LibreOffice Calc**: otwórz plik; wybierz zestaw znaków **UTF-8**,
     separator **przecinek** i ustaw kolumny na **Tekst**.
   - **Excel**: nie otwieraj pliku dwuklikiem (Excel źle odczyta litery).
     Dane > Z tekstu/CSV, pochodzenie pliku **65001: Unicode (UTF-8)**,
     ogranicznik **Przecinek**. Zapisz jako **CSV UTF-8 (rozdzielany
     przecinkami)**.
3. Wypełnij kolumnę `translation`. Nie zmieniaj nazw plików, nie dodawaj ani
   nie usuwaj kolumn, nie zmieniaj `id` i `english`. Sortowanie i filtry są
   w porządku.
4. Zapisz jako CSV (UTF-8, przecinki) pod tą samą nazwą.
5. Na GitHubie otwórz folder języka, **Add file > Upload files**, wrzuć pliki,
   potem **Propose changes** i **Create pull request**.

Nie trzeba tłumaczyć wszystkiego naraz - wyślij, co masz.

## Zasady

1. **Tylko kolumna `translation`.** `id` i `english` zostają bez zmian;
   sprawdzenie odrzuci plik, w którym je zmieniono.
2. **Zachowaj każdą zmienną i każdy kod dokładnie tak jak w angielskim,
   w tej samej kolejności** - wstawia je gra:
   - zmienne printf: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... oraz `%%` (znak procentu);
   - pola: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` to nowa linia w oknie questu; `[WAIT]`, `[DELAY value;5]`,
     `[COLOR r;1|g;0|b;0]` to jego polecenia;
   - kolory `|cffff0000` ... `|r`, linki `|H` ... `|h`, `|E` ... `|e`.

   Możesz przenieść je w inne miejsce zdania, jeśli wymaga tego Twój język,
   ale zmienne zaczynające się od `%` muszą zostać w tej samej kolejności.
   Tekst w nawiasach, np. `[Guild]` albo `[PT]`, to zwykły tekst: przetłumacz go.
3. **Litery.** Gra rysuje każdy język w jednej stronie kodowej Windows, więc
   pokaże tylko jej litery - bez emoji i symboli w rodzaju `→` czy `✓`:

   | strona kodowa | języki | litery |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (łacinka), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (cyrylica) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Rumuński: strona kodowa ma tylko **ş ţ z cedyllą**, nie ș ț z przecinkiem.
   Launcher (`6_launcher_*`) to osobny program Windows i przyjmie każdą literę,
   tak samo panel WWW (`7_panel_*`), strona w przeglądarce: oba są w **UTF-8**,
   każda litera każdego języka.
4. **Czat botów** (wiersze, w których notes mówi „ASCII letters only”): boty
   piszą jak gracze, zwykłymi literami a-z, bez znaków diakrytycznych.
5. **Długość.** Gdzie notes mówi „max N characters”, gra nie ma miejsca na
   więcej.
6. **Nowe linie** tylko tam, gdzie ma je angielski albo notes mówi „new lines
   allowed”.
7. **Panel WWW** (`7_panel_*`): jego teksty trafiają na stronę internetową,
   więc zachowaj znaczniki HTML z angielskiego dokładnie tak, jak są (`<b>`,
   `</b>`, `<a href="...">`, `<br>` i pola w nawiasach ostrych w rodzaju
   `<number>`) i nie dodawaj własnych `<`, `>` ani `javascript:`. Zmienne to
   `%s`, `%d`, `%(nazwa)s` i `{nazwa}`; nazwane `%(nazwa)s` można przestawiać.
   `%` ze spacją po nim (`25% a character`) to znak procentu. Język z choćby
   jednym przetłumaczonym tekstem panelu pojawia się w przełączniku języków
   panelu; to, czego nie przetłumaczono, panel pokazuje po angielsku.

## Nowy język

1. Skopiuj cały folder `template/` do folderu nazwanego dwuliterowym kodem
   ISO 639-1 Twojego języka (`hu`, `es`, `cs`... - zobacz
   [listę](https://pl.wikipedia.org/wiki/Kody_j%C4%99zyk%C3%B3w_ISO_639)).
   Można to zrobić arkuszem: pobierz `template/`, przetłumacz i wgraj pliki do
   nowego folderu (**Add file > Upload files**, wpisz `xx/` przed nazwą, żeby
   powstał folder).
2. Przetłumacz i otwórz pull request.

Nowy język wymaga trochę pracy w grze, zanim gracze będą mogli go wybrać
(języki spoza strony kodowej 1250 potrzebują też nowego klienta), więc może
pojawić się kilka wersji po pierwszym tłumaczeniu.

## Sprawdzenie

Każdy pull request uruchamia `tools/validate.py` (GitHub Actions). Zgłasza,
przy wierszu, w którym to znalazł:

- `id`, którego nie ma w `template/`, albo które jest dwa razy;
- zmienioną kolumnę `english`;
- inne zmienne, pola, polecenia albo kody kolorów niż w angielskim;
- literę spoza strony kodowej języka, tabulator, znak sterujący, nową linię
  tam, gdzie jej nie wolno, za długi tekst.

Oceniane są tylko wiersze, które zmienia Twój pull request; problemy, które
już były w plikach, są liczone, ale nie przeszkadzają. Żeby uruchomić
sprawdzenie samemu (Python 3, nic do instalowania): `python tools/validate.py de`.

## Licencja

Otwierając pull request, zgadzasz się, że Twoje tłumaczenie zostanie użyte
w Metin2 Singleplayer i udostępnione na tych samych warunkach co projekt:
[CC BY-NC-ND 4.0](LICENSE). Autorzy tłumaczeń są wymieniani w projekcie.
Sam Metin2 i jego oryginalne teksty należą do Ymir Interactive i Webzen.
