# Fortschritt der Übersetzung

Regeln: siehe CLAUDE.md. Es werden nur leere `translation`-Zellen gefüllt.
Tabelle neu erzeugen: `python glossary/progress_table.py`.
Prüfen: `python tools/validate.py --base origin/main <lang>` (für `ko`: `python glossary/check_ko.py`).

## Stand (übersetzt/Zeilen)

| lang | 1_klient | 2_przedmioty_potwory | 3_gra_serwer | 4_questy | 5_boty_czat | 6_launcher | total |
|---|---:|---:|---:|---:|---:|---:|---:|
| de | 5243/5750 | 9922/10016 | 1016/1016 | 171/8601 | 1575/3723 | 2/2308 | 17929/31414 (57.1%) |
| tr | 5750/5750 | 10015/10015 | 1016/1016 | 8601/8601 | 3723/3723 | 2308/2308 | 31413/31413 (100.0%) |
| fr | 5258/5750 | 9864/10016 | 1016/1016 | 171/8601 | 1571/3723 | 2/2308 | 17882/31414 (56.9%) |
| es | 5750/5750 | 0/10016 | 1016/1016 | 0/8601 | 0/3723 | 2307/2308 | 9073/31414 (28.9%) |
| it | 4306/5750 | 60/10016 | 24/1016 | 60/8601 | 103/3723 | 15/2308 | 4568/31414 (14.5%) |
| ro | 5243/5750 | 9864/10016 | 1016/1016 | 171/8601 | 1571/3723 | 2/2308 | 17867/31414 (56.9%) |
| hu | 4306/5750 | 60/10016 | 24/1016 | 60/8601 | 103/3723 | 15/2308 | 4568/31414 (14.5%) |
| nl | 4306/5750 | 60/10016 | 24/1016 | 60/8601 | 103/3723 | 15/2308 | 4568/31414 (14.5%) |
| cs | 4306/5750 | 60/10016 | 24/1016 | 60/8601 | 103/3723 | 15/2308 | 4568/31414 (14.5%) |
| el | 4307/5750 | 61/10016 | 24/1016 | 61/8601 | 4/3723 | 15/2308 | 4472/31414 (14.2%) |
| ru | 4307/5750 | 61/10016 | 24/1016 | 61/8601 | 4/3723 | 15/2308 | 4472/31414 (14.2%) |
| pt | 5258/5750 | 9864/10016 | 1014/1014 | 171/8601 | 1571/3723 | 2/2308 | 17880/31412 (56.9%) |
| da | 4306/5750 | 60/10016 | 24/1016 | 60/8601 | 103/3723 | 15/2308 | 4568/31414 (14.5%) |
| ar | 4307/5750 | 61/10016 | 24/1016 | 61/8601 | 4/3723 | 15/2308 | 4472/31414 (14.2%) |
| ko | 4307/5750 | 61/10016 | 24/1016 | 61/8601 | 4/3723 | 15/2308 | 4472/31414 (14.2%) |

## Erledigt

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
