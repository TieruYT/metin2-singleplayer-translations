# Metin2 Singleplayer - traduzioni della community

[English](README.md) | [Polski](README_PL.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | **Italiano** | [Português](README_PT.md) | [Română](README_RO.md) | [Magyar](README_HU.md) | [Nederlands](README_NL.md) | [Čeština](README_CS.md) | [Dansk](README_DA.md) | [Ελληνικά](README_EL.md) | [Русский](README_RU.md) | [العربية](README_AR.md) | [한국어](README_KO.md)

Questo repository contiene i testi di **Metin2 Singleplayer** - il client di
gioco, i nomi di oggetti e mostri, i messaggi del server, le missioni, la chat dei bot, il launcher per Windows e il pannello web classico - così che i giocatori possano tradurre il
gioco nella propria lingua. Contiene solo traduzioni: nessun codice di gioco.

Ogni pull request viene controllata automaticamente e le traduzioni accettate
entrano nel gioco nelle versioni successive.

## Cosa c'è qui

| cartella | contenuto |
|---|---|
| `template/` | tutti i testi del gioco, con la colonna `translation` vuota. Il punto di partenza di una nuova lingua. |
| `de/` `fr/` `pt/` `ro/` `tr/` | le lingue che il gioco ha già, con la loro traduzione attuale: correggila e completa ciò che manca (righe con `status` `new`). |
| `hu/` `es/` `it/` `cs/` `nl/` `da/` `el/` `ru/` `ar/` `ko/` | lingue nuove, tradotte interamente con l'aiuto dell'IA: madrelingua, correggete ciò che suona male. |
| `en_US/` | inglese americano: il testo sorgente inglese (ortografia britannica) in ortografia statunitense (color, armor, defense...). |
| `tools/validate.py` | il controllo che ogni pull request deve superare. |

L'inglese è la fonte e il polacco è mostrato accanto come riferimento;
nessuno dei due ha una cartella propria.

Ogni cartella di lingua contiene gli stessi file CSV, divisi in parti perché
GitHub possa mostrarli e modificarli (al massimo 700 righe per file):

| file | contenuto |
|---|---|
| `1_klient_NN.csv` | il client: finestre, pulsanti, suggerimenti, abilità, regole |
| `2_przedmioty_potwory_NN.csv` | nomi di oggetti e mostri, descrizioni degli oggetti |
| `3_gra_serwer_NN.csv` | i messaggi propri del server (chat, righe di sistema) |
| `4_questy_NN.csv` | i dialoghi delle missioni |
| `5_boty_czat_NN.csv` | la chat dei bot, le chiacchiere dei mostri, le frasi del server |
| `6_launcher_NN.csv` | il launcher per Windows |
| `7_panel_NN.csv` | il pannello web classico (il pannello di amministrazione sulla porta 7788, nel browser) |

Ogni file ha le colonne:

| colonna | |
|---|---|
| `id` | la chiave della riga. **Non modificarla mai.** |
| `english` | il testo da tradurre. **Non modificarlo mai.** |
| `polski` | lo stesso testo in polacco, come riferimento (può essere vuoto). |
| `translation` | **la tua traduzione - l'unica colonna che modifichi.** Vuota = il gioco mostra l'inglese. |
| `notes` | dove si vede il testo, cosa va mantenuto, un limite di lunghezza. |
| `status` | `new` (non tradotto), `done` (tradotto), `check` (uguale all'inglese - controllalo). Puoi impostarlo su `done`. |

## Come tradurre

### A. Nel browser (piccole modifiche)

1. Apri il file, ad es. [`it/1_klient_01.csv`](it/1_klient_01.csv). GitHub lo
   mostra come tabella; usa la casella di ricerca sopra per trovare una riga.
2. Clicca sulla matita (**Edit this file**). La prima volta GitHub crea una
   copia (un fork) per te.
3. Modifica solo la colonna `translation` delle righe che vuoi. Un testo con
   una virgola, delle virgolette o un a capo sta tra virgolette doppie
   (`"così, ad esempio"`); le virgolette al suo interno si scrivono due volte
   (`""`).
4. Clicca su **Commit changes...**, poi **Propose changes**, poi **Create
   pull request**. Scrivi in una frase cosa hai tradotto.

### B. In un foglio di calcolo (molte righe)

1. Scarica i file (apri un file, **Download raw file**; oppure il pulsante
   verde **Code**, **Download ZIP**, per tutto).
2. Aprili in un foglio di calcolo:
   - **Google Sheets**: File > Importa > Carica. Funziona senza impostazioni.
   - **LibreOffice Calc**: apri il file; scegli il set di caratteri
     **UTF-8**, il separatore **virgola** e imposta le colonne su **Testo**.
   - **Excel**: non fare doppio clic sul file (Excel leggerebbe male le
     lettere). Usa Dati > Da testo/CSV, origine file **65001: Unicode
     (UTF-8)**, delimitatore **Virgola**. Salva come **CSV UTF-8 (delimitato
     da virgole)**.
3. Compila la colonna `translation`. Non rinominare i file, non aggiungere né
   togliere colonne e non modificare `id` e `english`. Ordinare e filtrare va
   bene.
4. Salva come CSV (UTF-8, separato da virgole) con lo stesso nome.
5. Su GitHub apri la cartella della lingua, **Add file > Upload files**,
   trascina i tuoi file, poi **Propose changes** e **Create pull request**.

Non devi tradurre tutto in una volta - invia quello che hai.

## Regole

1. **Solo la colonna `translation`.** `id` e `english` restano come sono; il
   controllo rifiuta un file in cui sono stati modificati.
2. **Mantieni ogni variabile e ogni codice esattamente come nell'inglese,
   nello stesso ordine** - li compila il gioco:
   - variabili printf: `%s` `%d` `%u` `%ld` `%.1f` `%5d` ... e `%%` (un segno di percentuale);
   - segnaposto: `{0}` `{#0}` `{name}` `{skrot}` ...;
   - `[ENTER]` è un a capo in una finestra di missione; `[WAIT]`,
     `[DELAY value;5]`, `[COLOR r;1|g;0|b;0]` sono i suoi comandi;
   - colori `|cffff0000` ... `|r`, collegamenti `|H` ... `|h`, `|E` ... `|e`.

   Puoi spostarli all'interno della frase come richiede la tua lingua, ma le
   variabili di tipo `%` devono restare nello stesso ordine. Un testo tra
   parentesi quadre come `[Guild]` o `[PT]` è testo normale: traducilo.
3. **Lettere.** Il gioco disegna ogni lingua in una tabella codici di
   Windows, quindi si possono mostrare solo le sue lettere - niente emoji,
   niente simboli come `→` o `✓`:

   | tabella codici | lingue | lettere |
   |---|---|---|
   | 1250 | pl, cs, sk, hu, ro, hr, sl, sr (latino), bs, sq | ą ć ę ł ń ó ś ź ż, á č ď é ě í ň ř š ť ú ů ý ž, ő ű, ă â î ş ţ |
   | 1251 | ru, uk, bg, be, mk, sr (cirillico) | а б в г д ... я, є і ї ґ, ў, ђ ј љ њ ћ џ |
   | 1252 | de, fr, es, it, pt, nl, da, sv, no, fi, ca, id ... | à á â ã ä å æ ç è é ê ë ì í î ï ñ ò ó ô õ ö ø ù ú û ü ß œ |
   | 1253 | el | α β γ δ ... ω, ά έ ή ί ό ύ ώ |
   | 1254 | tr, az | ç ğ ı İ ö ş ü, â î û |
   | 1257 | lt, lv, et | ā č ē ģ ī ķ ļ ņ š ū ž, ą ę ė į ų |

   Rumeno: la tabella codici ha solo **ş ţ con la cediglia**, non ș ț con la
   virgola. Il launcher (`6_launcher_*`) è un programma Windows a sé e accetta
   qualsiasi lettera. Lo stesso vale per il pannello web (`7_panel_*`), una pagina
   nel browser: entrambi sono in **UTF-8**, qualsiasi lettera di qualsiasi lingua.
4. **La chat dei bot** (righe le cui note dicono "ASCII letters only"): i bot
   scrivono come i giocatori, con lettere semplici a-z senza accenti.
5. **Lunghezza.** Dove le note dicono "max N characters", il gioco non ha
   spazio per altro.
6. **A capo** solo dove li ha l'inglese o dove le note dicono "new lines
   allowed".
7. **Il pannello web** (`7_panel_*`): i suoi testi finiscono in una pagina web,
   quindi mantieni i tag HTML dell'inglese esattamente come sono (`<b>`, `</b>`,
   `<a href="...">`, `<br>` e i segnaposto del tipo `<number>` tra parentesi
   angolari) e non aggiungere `<`, `>` o `javascript:` tuoi. Le sue variabili
   sono `%s`, `%d`, `%(name)s` e `{name}`; un `%(name)s` con nome può spostarsi.
   Un `%` seguito da uno spazio (`25% a character`) è un segno di percentuale.
   Una lingua con almeno un testo del pannello tradotto compare nella scelta
   della lingua del pannello; ciò che non è tradotto appare in inglese.

## Una nuova lingua

1. Copia l'intera cartella `template/` in una cartella con il codice ISO
   639-1 di due lettere della tua lingua (`hu`, `es`, `cs`, `pl`... - vedi
   [l'elenco](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)).
   Puoi farlo in un foglio di calcolo: scarica `template/`, traduci e carica i
   file nella nuova cartella (**Add file > Upload files**, scrivi `xx/`
   davanti al nome per creare la cartella).
2. Traduci e apri una pull request.

Una nuova lingua richiede un po' di lavoro nel gioco prima che i giocatori
possano sceglierla (le lingue fuori dalla tabella codici 1250 richiedono anche
un nuovo client), quindi può arrivare qualche versione dopo la prima
traduzione.

## Il controllo

Ogni pull request esegue `tools/validate.py` (GitHub Actions). Segnala, alla
riga in cui l'ha trovato:

- un `id` che non è in `template/`, o che compare due volte;
- una colonna `english` modificata;
- variabili, segnaposto, tag o codici colore diversi dall'inglese;
- nel foglio del pannello web, tag HTML diversi dall'inglese, o un `<`, `>`
  o `javascript:` propri;
- una lettera fuori dalla tabella codici della lingua, una tabulazione, un
  carattere di controllo, un a capo dove non è consentito, un testo troppo
  lungo.

Vengono giudicate solo le righe modificate dalla tua pull request; i problemi
già presenti nei file vengono contati, non attribuiti a te. Per eseguirlo da
solo (Python 3, niente da installare): `python tools/validate.py it`.

## Licenza

Aprendo una pull request accetti che la tua traduzione venga usata in Metin2
Singleplayer e condivisa alle stesse condizioni del progetto:
[CC BY-NC-ND 4.0](LICENSE). I collaboratori vengono citati nel progetto.
Metin2 e i suoi testi originali appartengono a Ymir Interactive e Webzen.
