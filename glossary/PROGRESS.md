# Fortschritt der Übersetzung

Regeln: siehe CLAUDE.md. Es werden nur leere `translation`-Zellen gefüllt.
Tabelle neu erzeugen: `python glossary/progress_table.py`.
Prüfen: `python tools/validate.py --base origin/main <lang>` (prüft auch `ko`; `glossary/check_ko.py` zeigt nur ko).

## Stand (übersetzt/Zeilen)

| lang | 1_klient | 2_przedmioty_potwory | 3_gra_serwer | 4_questy | 5_boty_czat | 6_launcher | 7_panel | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| de | 5750/5750 | 9999/10016 | 1016/1016 | 5568/8601 | 2970/3723 | 2307/2308 | 4414/4414 | 32024/35828 (89.4%) |
| tr | 5750/5750 | 10015/10015 | 1016/1016 | 8601/8601 | 3723/3723 | 2308/2308 | 4414/4414 | 35827/35827 (100.0%) |
| fr | 5750/5750 | 10008/10016 | 1016/1016 | 5568/8601 | 2970/3723 | 2307/2308 | 4414/4414 | 32033/35828 (89.4%) |
| es | 5750/5750 | 9320/10016 | 1016/1016 | 5568/8601 | 2480/3723 | 2308/2308 | 4414/4414 | 30856/35828 (86.1%) |
| it | 5750/5750 | 9318/10016 | 1016/1016 | 5568/8601 | 2480/3723 | 2307/2308 | 4414/4414 | 30853/35828 (86.1%) |
| ro | 5750/5750 | 10008/10016 | 1016/1016 | 5568/8601 | 2970/3723 | 2307/2308 | 4414/4414 | 32033/35828 (89.4%) |
| hu | 5750/5750 | 9330/10016 | 1016/1016 | 5567/8601 | 2479/3723 | 2307/2308 | 4414/4414 | 30863/35828 (86.1%) |
| nl | 5750/5750 | 9334/10016 | 1016/1016 | 5568/8601 | 2480/3723 | 2307/2308 | 4414/4414 | 30869/35828 (86.2%) |
| cs | 5750/5750 | 9333/10016 | 1016/1016 | 5568/8601 | 2480/3723 | 2307/2308 | 4414/4414 | 30868/35828 (86.2%) |
| el | 5750/5750 | 9334/10016 | 1016/1016 | 5568/8601 | 2230/3723 | 2307/2308 | 4414/4414 | 30619/35828 (85.5%) |
| ru | 5750/5750 | 9334/10016 | 1016/1016 | 5568/8601 | 2228/3723 | 2307/2308 | 4414/4414 | 30617/35828 (85.5%) |
| pt | 5750/5750 | 10008/10016 | 1014/1014 | 5568/8601 | 2970/3723 | 2307/2308 | 4414/4414 | 32031/35826 (89.4%) |
| da | 5750/5750 | 9286/10016 | 1016/1016 | 5568/8601 | 2479/3723 | 2307/2308 | 4414/4414 | 30820/35828 (86.0%) |
| ar | 5750/5750 | 9334/10016 | 1016/1016 | 5568/8601 | 2227/3723 | 2307/2308 | 4414/4414 | 30616/35828 (85.5%) |
| ko | 5750/5750 | 9334/10016 | 1016/1016 | 5568/8601 | 2225/3723 | 2307/2308 | 4414/4414 | 30614/35828 (85.4%) |
| en_US | 5750/5750 | 10016/10016 | 1016/1016 | 8601/8601 | 3709/3723 | 2308/2308 | 4414/4414 | 35814/35828 (100.0%) |

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
  und der Alten Dame stehen in `glossary/glossary.csv` (Notiz „quest texts“).
  Auffälligkeit (nicht korrigiert): Bei zusammengesetzten Sätzen wie
  „Up until now you have delivered “ + Zahl + „branches.“ fehlt im Englischen
  das Leerzeichen vor dem zweiten Teil; die Leerzeichen wurden wie im
  Englischen übernommen (Polnisch hat dort eins).
- 4_questy_03: alle leeren Zellen in allen 14 Sprachen gefüllt (inkl. es).
  Neue Namen (Altar der Macht, Landagent, Burgen Listhmos/Milaard/Dendera,
  Verräter Balso, Schwarzwind-Bande, Buch der Vorsehung, Reiskuchen-Kästen,
  Waffenschmied/Rüstungsschmied/Schmuckdesigner usw.) wurden einheitlich
  übersetzt. ko: Yang = 냥, wie in den bestehenden ko-Zeilen.
  Auffälligkeiten (nicht korrigiert):
  - Feste des Roten Drachen: der englische Text ist an mehreren Stellen
    fehlerhafte Maschinenübersetzung; der Sinn wurde aus dem Polnischen
    übernommen.
  - de: bestehende Itemnamen „Hellgrüner Holzkasten“ (Lightgreen Ebony Box)
    und „Gildenkriegsmeister“ (Battle Bailiff) wurden so übernommen.
  - Ranglisten-Tabellen (guild_ranking): ein Spaltenname direkt nach `|` darf
    nicht mit E/e/H/h/r beginnen, sonst hält der Validator ihn für einen
    Farbcode (`|E`); daher pt „Jogos empatados“, ro „Meciuri egale“,
    es „Tablas“ statt „Empates/Egaluri“.
- 4_questy_04: alle leeren Zellen in allen 14 Sprachen gefüllt (inkl. es).
  Neue Namen (Stallbursche, Waffen-/Militär-Pferdebuch, Pferdebild,
  Dämonenbogenschützen, Ariyoung, Aranyo, Soon, Milgyo-Buch, Deokbae,
  Yu-Rang, Huahn-So, Baek-Go, Alter Pirat, Thorr Sarch usw.) wurden einheitlich
  übersetzt; Fertigkeiten und Orte nach dem Glossar.
  Auffälligkeiten (nicht korrigiert):
  - `horse_summon._290_say`: in der Spalte `polski` steht deutscher Text
    („s Feuerphönix“).
  - Das Glossar hat zwei Zeilen „Horse Medal“ mit unterschiedlichen Werten
    für es/el/ru.
  - de-Itemtabelle: „Handu-Up“ = „Aufgewertete Gegenstände“ und
    „Wild Boar“ = „Eis-Golem“; in den Quests wurden Handu-Up und Wildschwein
    verwendet.
  - Englisch schreibt denselben Arzt einmal „Baek-So“ und einmal „Beak-Go“;
    übersetzt wurde einheitlich Baek-Go.
  - de: „battle bailiff“ im Regeltext des Reichskampfs als „Kampfvogt“
    übersetzt; der bestehende Itemname dafür ist „Gildenkriegsmeister“.
- Nacharbeit zu 4_questy_04 (auf Wunsch):
  - „Monkey Dungeon“ in meinen Zeilen auf die Spielnamen vereinheitlicht
    (de Affendungeon, fr Donjon des Singes, pt Masmorra dos Macacos,
    ro Temnita Maimutelor, es Mazmorra de Monos, hu majomkazamata,
    nl Apenkerker, el Μπουντρούμι των Πιθήκων, it Dungeon delle scimmie).
  - „battle bailiff“ im Regeltext des Reichskampfs in allen 14 Sprachen an den
    NPC-Namen angeglichen (de Gildenkriegsmeister, ro Administratorul luptelor …).
  - de Itemtabelle korrigiert: m:name:8502 „Eis-Golem“ → „Wildschwein“,
    m:name:20086 „Aufgewertete Gegenstände“ → „Handu-Up“; ebenso ro 20086
    „Obiecte uppgrade“ → „Handu-Up“ (wie fr/pt/tr).
  - Glossar: doppelte Zeile „Horse Medal“ zusammengeführt (Werte, die in den
    Übersetzungen benutzt werden; pl aus der alten Zeile übernommen).
  - Nur upstream (in template/) lösbar, da `english`/`polski` nicht geändert
    werden dürfen: `horse_summon._290_say` hat in `polski` deutschen Text
    („s Feuerphönix“); das Englische schreibt den Arzt teils „Baek-So“
    (`locale.huanso.find_text_1`) und „Beak-Go“ (`locale.huanso.find_text_2`,
    `npc_talk._120_say`). Alle Übersetzungen verwenden einheitlich Baek-Go.
  - Bestehende (nicht eigene) Zeilen in el/ar 7_panel_03–05 schreiben Baek-Go
    lateinisch statt Μπεκ-Γκο / بيك-غو; nicht geändert.
- en_US: neuer Ordner mit amerikanischem Englisch (35.792 Zeilen, davon 1.551
  mit US-Schreibweise wie color/armor/defense/jewelry/soccer), erzeugt mit
  `python3 glossary/build_en_us.py`; `tools/validate.py` erlaubt dafür
  Regionalordner wie `en_US` (Codepage von `en`). Offen bleiben nur 36 Zeilen
  ohne englischen Text (nur `polski`).
- Stand 2026-11-09 abends (Branch `claude/translations-5`, auf upstream/main inkl. pt-PR von iahgod neu aufgesetzt):
  offen sind 4_questy_05-13 (Rest), 5_boty_czat (Rest), Beschreibungen in 2_przedmioty_potwory und die
  "check"-Zeilen in de/fr/pt/ro/tr (laut Projektinhaber pruefen, ggf. uebersetzen, auf done setzen).
- 14 Zeilen in 5_boty_czat_05/06 (`b:phrase:`, nur Polnisch, mit %s/%d/%u/%ld) lassen sich in keiner Sprache
  eintragen: tools/validate.py vergleicht die Variablen mit der leeren english-Spalte. Abhilfe upstream:
  English nachtragen oder im Validator bei leerer english-Spalte die polski-Spalte nehmen. Auch tr ist betroffen.
- Zeilen, in denen ein Prozentzeichen vor einem Wort steht ("10% de"), liest der Validator als Variable; solche
  Uebersetzungen werden mit "Prozent"/"por ciento" o. ae. ausgeschrieben.
- Auffaelligkeit (nicht geaendert): de "Wild Dog" ist in bestehenden Zeilen "Flammenkrieger"; in neuen Texten
  "Wilder Hund". de "Reitkarte (PM)" und "Kupferverziert. Bogen" in Fliesstexten als "Reitkarte" bzw.
  "Kupferverzierter Bogen".
- Namen: in lateinischen Sprachen bleiben NPC-/Monsternamen unveraendert (Geuk-Hon-Gab, Jae-Seon Kim);
  el/ru/ar/ko verwenden die bestehende Transliteration (z. B. Гык-Хон-Габ, 극혼갑).
- Qualitaet: Die Texte der neuen Sprachen sind KI-uebersetzt. Korrekturen von Muttersprachlern aus der
  Community sind ausdruecklich willkommen.
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
