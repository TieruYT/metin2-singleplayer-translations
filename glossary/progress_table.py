#!/usr/bin/env python3
"""Print the progress table (language x sheet: translated/rows) for PROGRESS.md."""
import csv, glob, os
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
LANGS = ['de', 'tr', 'fr', 'es', 'it', 'ro', 'hu', 'nl', 'cs', 'el', 'ru', 'pt', 'da', 'ar', 'ko']
SHEETS = ['1_klient', '2_przedmioty_potwory', '3_gra_serwer', '4_questy', '5_boty_czat', '6_launcher']
print('| lang | ' + ' | '.join(SHEETS) + ' | total |')
print('|---|' + '---:|' * (len(SHEETS) + 1))
for lang in LANGS:
    if not os.path.isdir(os.path.join(ROOT, lang)):
        print('| %s | ' % lang + ' | '.join('-' for _ in SHEETS) + ' | (no folder) |')
        continue
    cells, T, D = [], 0, 0
    for s in SHEETS:
        t = d = 0
        for f in glob.glob(os.path.join(ROOT, lang, s + '_*.csv')):
            for r in csv.DictReader(open(f, encoding='utf-8')):
                t += 1
                d += bool(r['translation'].strip())
        cells.append('%d/%d' % (d, t))
        T += t
        D += d
    print('| %s | %s | %d/%d (%.1f%%) |' % (lang, ' | '.join(cells), D, T, 100.0 * D / max(T, 1)))
