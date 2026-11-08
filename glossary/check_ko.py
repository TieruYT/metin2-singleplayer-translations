#!/usr/bin/env python3
"""Check the Korean translation (ko/), which tools/validate.py does not know.

    python glossary/check_ko.py

Uses the checks of tools/validate.py (variables in the same order,
placeholders, tags, colour codes, new lines, length) with code page cp949
for the game's sheets and UTF-8 for the launcher. tools/validate.py itself
is not changed.
"""
import collections
import csv
import io
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.dont_write_bytecode = True  # keep tools/ free of __pycache__
import validate  # noqa: E402


def main():
    folder = os.path.join(ROOT, 'ko')
    if not os.path.isdir(folder):
        print('no ko/ folder')
        return 1
    report = validate.Report()
    template = validate.load_template(report)
    rows = done = 0
    for name in sorted(os.listdir(folder)):
        m = validate.PART.match(name)
        if not m or m.group('sheet') not in template:
            continue
        table = template[m.group('sheet')]
        codepage = 'utf-8' if m.group('sheet') == '6_launcher' else 'cp949'
        rel = 'ko/' + name
        header, data, _d = validate.read_csv(validate.read_file(os.path.join(folder, name)), rel)
        if header != validate.COLUMNS:
            report.error(rel, 1, 'bad header')
            continue
        for line, row in data:
            if len(row) != 6:
                report.error(rel, line, 'row has %d columns' % len(row))
                continue
            rows += 1
            rid, english, _pl, text, _notes, _status = row
            if rid not in table:
                report.error(rel, line, 'unknown id %r' % rid)
                continue
            if english.replace('\r\n', '\n') != table[rid][0].replace('\r\n', '\n'):
                report.error(rel, line, 'english column changed')
                continue
            if not text.strip():
                continue
            done += 1
            why = validate.problem(table[rid][0], table[rid][2], text, codepage)
            if why:
                report.error(rel, line, '%s: %s' % (rid, why))
    print('ko: %d rows, %d translated, %d errors' % (rows, done, report.errors))
    return 1 if report.errors else 0


if __name__ == '__main__':
    sys.exit(main())
