# Fortschritt der Übersetzung

Regeln: siehe CLAUDE.md. Es werden nur leere `translation`-Zellen gefüllt.
Tabelle neu erzeugen: `python glossary/progress_table.py`.
Prüfen: `python tools/validate.py --base origin/main <lang>` (für `ko`: `python glossary/check_ko.py`).

## Stand (übersetzt/Zeilen)

| lang | 1_klient | 2_przedmioty_potwory | 3_gra_serwer | 4_questy | 5_boty_czat | 6_launcher | 7_panel | total |
|---|---|---|---|---|---|---|---|---|
| de | 5750/5750 | 9922/10016 | 1016/1016 | 176/8601 | 1580/3723 | 6/2308 | 2913/4414 | 21363/35828 (59.6%) |
| tr | 5750/5750 | 10015/10015 | 1016/1016 | 8601/8601 | 3723/3723 | 2308/2308 | 4246/4414 | 35659/35827 (99.5%) |
| fr | 5750/5750 | 9864/10016 | 1016/1016 | 180/8601 | 1586/3723 | 15/2308 | 2913/4414 | 21324/35828 (59.5%) |
| es | 5750/5750 | 13/10016 | 1016/1016 | 9/8601 | 12/3723 | 2307/2308 | 2894/4414 | 12001/35828 (33.5%) |
| it | 5750/5750 | 83/10016 | 1016/1016 | 85/8601 | 316/3723 | 29/2308 | 2889/4414 | 10168/35828 (28.4%) |
| ro | 5750/5750 | 9864/10016 | 1016/1016 | 180/8601 | 1599/3723 | 15/2308 | 2913/4414 | 21337/35828 (59.6%) |
| hu | 5750/5750 | 83/10016 | 1016/1016 | 85/8601 | 316/3723 | 29/2308 | 2889/4414 | 10168/35828 (28.4%) |
| nl | 5750/5750 | 83/10016 | 1016/1016 | 85/8601 | 316/3723 | 29/2308 | 2889/4414 | 10168/35828 (28.4%) |
| cs | 5750/5750 | 83/10016 | 1016/1016 | 85/8601 | 316/3723 | 29/2308 | 2889/4414 | 10168/35828 (28.4%) |
| el | 5750/5750 | 84/10016 | 1016/1016 | 86/8601 | 69/3723 | 29/2308 | 2889/4414 | 9923/35828 (27.7%) |
| ru | 5750/5750 | 84/10016 | 1016/1016 | 86/8601 | 68/3723 | 29/2308 | 2889/4414 | 9922/35828 (27.7%) |
| pt | 5750/5750 | 9864/10016 | 1014/1014 | 180/8601 | 1586/3723 | 15/2308 | 2913/4414 | 21322/35826 (59.5%) |
| da | 5750/5750 | 83/10016 | 1016/1016 | 85/8601 | 316/3723 | 29/2308 | 2889/4414 | 10168/35828 (28.4%) |
| ar | 5750/5750 | 84/10016 | 1016/1016 | 86/8601 | 68/3723 | 29/2308 | 2889/4414 | 9922/35828 (27.7%) |
| ko | 5750/5750 | 84/10016 | 1016/1016 | 86/8601 | 68/3723 | 29/2308 | 2889/4414 | 9922/35828 (27.7%) |

## Erledigt

- 7_panel (Webpanel, UTF-8): 7_panel_01 bis 7_panel_04 in allen 13 neuen Sprachen
  fertig (fr, pt, ro, es, it, hu, cs, nl, da, el, ru, ar, ko; dazu de in 04); 05-07 folgen.
  HTML-Tags und Platzhalter wie im Englischen.
  Ungarisch: kein `%-a` ("98%-a") schreiben, der Validator liest `%-a` als
  Variable. Stattdessen den Satz so bauen, dass nach `%` ein Leerzeichen folgt,
  wie in den anderen Sprachen: "98% marad az esélyből", "(% az ölésekből)".
  Ebenso kein `%-uk`, `%-os`, `%-ig` usw. (`%-u`, `%-o`, `%-i` sind Variablen).
- tr: alle 532 leeren Zellen gefüllt (14 Dateien), 0 neue Validator-Fehler.
- Glossar `glossary/glossary.csv`: 133 Begriffe, Spalten für alle Zielsprachen
  (pl = Referenz aus der Spalte `polski`).

## Konventionen aus bestehenden Zeilen

- ro: bestehende Zeilen sind fast durchgehend ohne diakritische Zeichen
  (35 von 17.575 Zeilen haben ă/â/î/ş/ţ). Neue ro-Zeilen folgen dem, damit
  der Text einheitlich bleibt. (Offene Frage an das Projektteam.)
- pt: europäisches Portugiesisch, informelles „tu“ (tua/teu/podes), „Definições“,
  „Palavra-passe“, „bónus“.
- de: HP = TP, SP = MP; fr/pt/ro: HP = PV, SP = PM.
- tr: „Lucky Ticket“ bleibt englisch, Item Shop = „Nesne Market“, Dragon Coins
  = „Ejderha Parası“ (Kurzform EP), Companion = „Yoldaş“, Auto Hunt = „Otomatik Av“.

## Auffälligkeiten (nicht geändert, nur gemeldet)

### Struktur
- `tr/2_przedmioty_potwory_11.csv`: Zeile `m:name:20220` fehlt (Template hat sie).
- `pt/3_gra_serwer_01.csv`: Zeilen `e:69410cd4d4d3` und `e:c930307efc9c` fehlen.
- `es/`: 15 Dateien sind im Repo mit CRLF-Zeilenenden eingecheckt, obwohl
  `.gitattributes` LF verlangt (Git zeigt sie dauerhaft als geändert).
- `es/`: ~9.000 übersetzte Zeilen haben noch `status` `new`.
- Der Validator meldet auf `main` bereits 121 Fehler in bestehenden Zeilen
  (vor allem tr `5_boty_czat_*`: Variablen, die im Englischen fehlen).

### Inhalt tr (falsche bestehende Übersetzungen)
- `Elder Rider` → „Ticaret yöneticisi“ (= Handelsverwalter); neue Zeilen: „Yaşlı Süvari“.
- `Assault Cavalry Totem` → „Kırmızı ginseng (Prem.)“; neue Zeilen: „Hücum Süvarisi Totemi“.
- `Gold Horse Medal` → „Altın at kitabı“ (= Buch); neue Zeilen: „Altın At Madalyonu“.
- `Gold Carrot` → „At yemi“ (= Pferdefutter); neue Zeilen: „Altın Havuç“.
- `Haneul` → „Orman Bekçileri Lideri“, `Ji Jin` → „Kawuco“, `Meijin` → „Andastra“,
  `Vampiric Merchant` → „Enigma Tapın. (Bonus B)“: passen nicht zum Englischen;
  neue Zeilen behalten die Namen bzw. „Vampir Tüccar“.
- `SP` → „INT“ in einer Zeile.

## Rückmeldung der Projektbetreuer (zum ersten Pull Request)

- Validator auf `main`: keine Fehler, keine neuen Warnungen; nichts überschrieben.
- Zeilenenden: Dateien, die auf `main` mit CRLF liegen (`es/`), behalten CRLF.
  Nie nur wegen Zeilenenden ändern. `glossary/batch.py commit` schreibt solche
  Dateien deshalb mit CRLF in den Commit. `git config core.autocrlf false` setzen.
- nl, da: gleiche Codepage wie de/fr, kommen mit dem nächsten Client-Update.
- ru, el: brauchen eine Änderung in der Client-EXE (cp1251/1253), kommen später.
- ar (rechts-nach-links), ko (Doppelbyte): erst nach einer Analyse; die Daten
  sind im Repository trotzdem willkommen.
- READMEs: die englische README bleibt die Referenz; Übersetzungen können
  hinterherhinken, wenn sie sich ändert.
- `tools/validate.py` (ko = cp949) wurde auf Wunsch des Nutzers geändert; bei
  Pull Requests von Nicht-Mitgliedern lehnt die CI Änderungen an `tools/` ab.
- Der erste Pull Request wurde gemergt (Squash-Commit 49dc74f auf `main`). Vor und
  nach dem Merge liegen nur die 15 `es/`-Dateien mit CRLF auf `main`; `tr/` und
  `cs/` waren dort immer LF, ihre Änderungen sind echte Inhalte.
- Weitere Arbeit liegt auf dem neuen Zweig `claude/translations-2` (basiert auf
  dem gemergten `main`).
- `1_klient_*` ist für alle Sprachen vollständig.
- `es/` und `tr/` werden laut Betreuer gerade auch von anderen übersetzt. Darum
  nur einzelne leere Zeilen füllen und die CRLF-Zeilenenden von `es/` nie
  umschreiben (sonst zeigt der Diff jede Zeile als geändert und es gibt Konflikte).
- Validator-Falle: ein `|` direkt vor `E`, `e`, `H`, `h` oder `r` gilt als
  Farb-/Link-Code; Übersetzungen dürfen nach `|` nicht so beginnen.
