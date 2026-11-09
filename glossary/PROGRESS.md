# Fortschritt der Übersetzung

Regeln: siehe CLAUDE.md. Es werden nur leere `translation`-Zellen gefüllt.
Tabelle neu erzeugen: `python glossary/progress_table.py`.
Prüfen: `python tools/validate.py --base origin/main <lang>` (prüft auch `ko`; `glossary/check_ko.py` zeigt nur ko).

## Stand (übersetzt/Zeilen)

| lang | 1_klient | 2_przedmioty_potwory | 3_gra_serwer | 4_questy | 5_boty_czat | 6_launcher | 7_panel | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| de | 5750/5750 | 9926/10016 | 1016/1016 | 1483/8601 | 1582/3723 | 2307/2308 | 4414/4414 | 26478/35828 (73.9%) |
| tr | 5750/5750 | 10015/10015 | 1016/1016 | 8601/8601 | 3723/3723 | 2308/2308 | 4414/4414 | 35827/35827 (100.0%) |
| fr | 5750/5750 | 9869/10016 | 1016/1016 | 1483/8601 | 1588/3723 | 2307/2308 | 4414/4414 | 26427/35828 (73.8%) |
| es | 5750/5750 | 57/10016 | 1016/1016 | 1477/8601 | 17/3723 | 2308/2308 | 4414/4414 | 15039/35828 (42.0%) |
| it | 5750/5750 | 127/10016 | 1016/1016 | 1477/8601 | 322/3723 | 2307/2308 | 4414/4414 | 15413/35828 (43.0%) |
| ro | 5750/5750 | 9869/10016 | 1016/1016 | 1483/8601 | 1601/3723 | 2307/2308 | 4414/4414 | 26440/35828 (73.8%) |
| hu | 5750/5750 | 127/10016 | 1016/1016 | 1477/8601 | 322/3723 | 2307/2308 | 4414/4414 | 15413/35828 (43.0%) |
| nl | 5750/5750 | 127/10016 | 1016/1016 | 1477/8601 | 322/3723 | 2307/2308 | 4414/4414 | 15413/35828 (43.0%) |
| cs | 5750/5750 | 127/10016 | 1016/1016 | 1477/8601 | 322/3723 | 2307/2308 | 4414/4414 | 15413/35828 (43.0%) |
| el | 5750/5750 | 128/10016 | 1016/1016 | 1477/8601 | 72/3723 | 2307/2308 | 4414/4414 | 15164/35828 (42.3%) |
| ru | 5750/5750 | 128/10016 | 1016/1016 | 1477/8601 | 70/3723 | 2307/2308 | 4414/4414 | 15162/35828 (42.3%) |
| pt | 5750/5750 | 9869/10016 | 1014/1014 | 1483/8601 | 1588/3723 | 2307/2308 | 4414/4414 | 26425/35826 (73.8%) |
| da | 5750/5750 | 127/10016 | 1016/1016 | 1477/8601 | 322/3723 | 2307/2308 | 4414/4414 | 15413/35828 (43.0%) |
| ar | 5750/5750 | 128/10016 | 1016/1016 | 1477/8601 | 70/3723 | 2307/2308 | 4414/4414 | 15162/35828 (42.3%) |
| ko | 5750/5750 | 128/10016 | 1016/1016 | 1477/8601 | 70/3723 | 2307/2308 | 4414/4414 | 15162/35828 (42.3%) |

## Prüfung der fertigen Bereiche (Stand 2026-11-09)

- Keine leere `translation`-Zelle in 1_klient, 3_gra_serwer, 6_launcher_04 und
  7_panel, in keiner Sprache.
- de/7_panel_01–03 und tr/7_panel_01–06 waren schon im Original-Repo übersetzt
  (Commit „Panel: 7_panel section…“). Deshalb erscheinen sie nicht im PR.
- Zeilen mit Status `check` = Text ist eine Kopie des Englischen aus dem Original
  (de 643, tr 500, fr 751, ro 508, pt 762). Die meisten sind Namen/Kürzel, die
  so bleiben können (Bot, Status, Yang, /companion-Befehle). Einige sind aber
  noch englische Sätze, z. B. de 1_klient_09 (Klassen- und Reichstexte),
  de 7_panel_04 „Open the market preview“. Nach Regel nicht angefasst.
- es: 8810 Zeilen aus dem Community-PR haben Text, aber Status `new`; nicht
  angefasst.

## Erledigt

- 7_panel (Webpanel, UTF-8): 7_panel_01 bis 7_panel_07 in allen Sprachen fertig
  (4414/4414 Zeilen je Sprache, inkl. de und tr).
  HTML-Tags und Platzhalter wie im Englischen.
  Ungarisch: kein `%-a` ("98%-a") schreiben, der Validator liest `%-a` als
  Variable. Stattdessen den Satz so bauen, dass nach `%` ein Leerzeichen folgt,
  wie in den anderen Sprachen: "98% marad az esélyből", "(% az ölésekből)".
  Ebenso kein `%-uk`, `%-os`, `%-ig` usw. (`%-u`, `%-o`, `%-i` sind Variablen).
  Auch kein `100%-ra` (`%-r` ist eine Variable): "100 százalék" schreiben.
  Die Reihenfolge der Platzhalter muss wie im Englischen bleiben (z. B. in ko/tr
  "<b>%d %s</b> … <b>%s.%s</b>" nicht umstellen).
  Spielnamen im Panel: "Plague Pass"/"Plague Chest" bleiben englisch wie die
  Item-Namen; ro "Jack Calabaza" so übernommen wie im bestehenden NPC-Namen
  (spanisches Wort, Auffälligkeit – nicht korrigiert).
- 6_launcher (6_launcher_01 bis _04): alle leeren Zellen in allen Sprachen
  gefüllt, bis auf eine Zeile (siehe unten, BLESSING-Zeile).
- 4_questy_01: alle leeren Zellen in allen 14 Sprachen gefüllt (inkl. es).
  Gleiche englische Texte in anderen Dateien wurden mit gefüllt (z. B. NPC- und
  Itemnamen in 2_przedmioty_potwory).
- 4_questy_02: alle leeren Zellen in allen 14 Sprachen gefüllt (inkl. es).
  Die Namen aus den Biologen-Quests (Chaegirab) und den Quests von Seon-Pyeong
  und der Alten Dame stehen in  (Notiz „quest texts“).
  Auffälligkeit (nicht korrigiert): Bei zusammengesetzten Sätzen wie
  „Up until now you have delivered “ + Zahl + „branches.“ fehlt im Englischen
  das Leerzeichen vor dem zweiten Teil; die Leerzeichen wurden wie im
  Englischen übernommen (Polnisch hat dort eins).
- Reich-Begriff angeglichen (nur eigene Zeilen in 6_launcher, 7_panel und
  4_questy_01): ko 제국, nl rijk, da rige, cs říše, wie im Glossar und im Client.
- tr: alle 532 leeren Zellen gefüllt (14 Dateien), 0 neue Validator-Fehler.
- Glossar `glossary/glossary.csv`: 133 Begriffe, Spalten für alle Zielsprachen
  (pl = Referenz aus der Spalte `polski`).

## Konventionen aus bestehenden Zeilen

- Quests: Namen von Monstern, NPCs und Orten wie in 2_przedmioty_potwory der
  jeweiligen Sprache; wo es dort keine gibt, eigene Namen, gesammelt in
  `glossary/glossary.csv` (Notiz „quest texts“).
- Seuchenverlies (Plague Dungeon): die Item- und Monsternamen (Small/Great
  Plague Key, Plagued Warrior, Seal Stone, Plague Metin …) bleiben in allen
  Sprachen englisch, weil de/fr/pt/ro sie in der Itemtabelle englisch haben.
  Übersetzt werden nur Plague Dungeon, Plague Cure und Ancient Seal.
- Begleiter-Flüsterbefehle (come, go play, wait, shopping, status) bleiben
  englisch, wie in den bestehenden de/fr/pt/ro-Zeilen.
- Validator-Falle in Quests: nach `% ` darf kein kurzes Wort stehen, das wie
  eine printf-Umwandlung aussieht („% a “, „% d'“, „% le “, „% zu “, „% to “).
  Stattdessen „Prozent/százalék/pour cent“ schreiben oder das Wort umstellen.

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
- `es/6_launcher_03.csv` (Zeilenenden gemischt: CRLF am Zeilenende, LF in
  mehrzeiligen Zellen): unser Commit 7b66632 hatte daraus überall CRLF gemacht;
  mit a76e21c wieder byte-gleich mit main bis auf die eine neue Zeile.
- Der Validator meldet auf `main` bereits 121 Fehler in bestehenden Zeilen
  (vor allem tr `5_boty_czat_*`: Variablen, die im Englischen fehlen).

- `6_launcher_03.csv`, Zeile `l:e7d018eb4b06` („Blessing Scrolls from Metin
  stones: chance changed from 5% to 1% …“) bleibt in de, fr, pt, ro, it, hu,
  cs, nl, da, el, ru, ar und ko leer. Der Validator liest im Englischen
  „5% to“ als Variable `% t` + `o` (printf-Leerzeichen-Flag) und findet
  `ut`; jede Übersetzung ohne genau diese Zeichenfolge wird abgelehnt.
  tr hat in dieser Zeile denselben Altfehler, es hat den englischen Text.
  Vorschlag ans Projekt: Englisch auf „5 % to 1 %“ oder „5 percent“ ändern
  oder die Regel im Validator anpassen.
- ro: 6_launcher_02 „Sprijină proiectul“ (von uns, aus 1_klient_06 übernommen)
  auf „Sprijina proiectul“ geändert. Die bestehenden ro-Zeilen mit Diakritika
  in 1_klient_05/06 und 2_przedmioty_potwory_09–11 sind nicht von uns und
  wurden nicht geändert.

### Inhalt tr (falsche bestehende Übersetzungen)
- `Elder Rider` → „Ticaret yöneticisi“ (= Handelsverwalter); neue Zeilen: „Yaşlı Süvari“.
- `Assault Cavalry Totem` → „Kırmızı ginseng (Prem.)“; neue Zeilen: „Hücum Süvarisi Totemi“.
- `Gold Horse Medal` → „Altın at kitabı“ (= Buch); neue Zeilen: „Altın At Madalyonu“.
- `Gold Carrot` → „At yemi“ (= Pferdefutter); neue Zeilen: „Altın Havuç“.
- `Haneul` → „Orman Bekçileri Lideri“, `Ji Jin` → „Kawuco“, `Meijin` → „Andastra“,
  `Vampiric Merchant` → „Enigma Tapın. (Bonus B)“: passen nicht zum Englischen;
  neue Zeilen behalten die Namen bzw. „Vampir Tüccar“.
- `SP` → „INT“ in einer Zeile.
- de: `Elder Rider` steht in einer bestehenden Zeile als „Trade Administrator“
  (englisch, falsch); `Haneul`, `Ji Jin`, `Meijin` haben in de wie in tr falsche
  Namen. Neue Zeilen: „Alter Reiter“ bzw. die Namen selbst.

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
