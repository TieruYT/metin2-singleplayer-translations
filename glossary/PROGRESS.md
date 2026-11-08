# Fortschritt der Übersetzung

Regeln: siehe CLAUDE.md. Es werden nur leere `translation`-Zellen gefüllt.
Tabelle neu erzeugen: `python glossary/progress_table.py`.
Prüfen: `python tools/validate.py --base origin/main <lang>` (für `ko`: `python glossary/check_ko.py`).

## Stand (übersetzt/Zeilen)

| lang | 1_klient | 2_przedmioty_potwory | 3_gra_serwer | 4_questy | 5_boty_czat | 6_launcher | total |
|---|---:|---:|---:|---:|---:|---:|---:|
| de | 4918/5750 | 9922/10016 | 1016/1016 | 171/8601 | 1571/3723 | 0/2308 | 17598/31414 (56.0%) |
| tr | 5750/5750 | 10015/10015 | 1016/1016 | 8601/8601 | 3723/3723 | 2308/2308 | 31413/31413 (100.0%) |
| fr | 4956/5750 | 9864/10016 | 1016/1016 | 171/8601 | 1571/3723 | 0/2308 | 17578/31414 (56.0%) |
| es | 5748/5750 | 0/10016 | 1016/1016 | 0/8601 | 0/3723 | 2307/2308 | 9071/31414 (28.9%) |
| it | 0/5750 | 0/10016 | 0/1016 | 0/8601 | 0/3723 | 0/2308 | 0/31414 (0.0%) |
| ro | 4953/5750 | 9864/10016 | 1016/1016 | 171/8601 | 1571/3723 | 0/2308 | 17575/31414 (55.9%) |
| hu | 0/5750 | 0/10016 | 0/1016 | 0/8601 | 0/3723 | 0/2308 | 0/31414 (0.0%) |
| nl | - | - | - | - | - | - | (no folder) |
| cs | 0/5750 | 0/10016 | 0/1016 | 0/8601 | 0/3723 | 0/2308 | 0/31414 (0.0%) |
| el | - | - | - | - | - | - | (no folder) |
| ru | - | - | - | - | - | - | (no folder) |
| pt | 4971/5750 | 9864/10016 | 1014/1014 | 171/8601 | 1571/3723 | 0/2308 | 17591/31412 (56.0%) |
| da | - | - | - | - | - | - | (no folder) |
| ar | - | - | - | - | - | - | (no folder) |
| ko | - | - | - | - | - | - | (no folder) |

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
