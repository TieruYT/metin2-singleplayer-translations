#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check the translations in this repository.

    python tools/validate.py                 # every language folder
    python tools/validate.py tr de           # only these folders
    python tools/validate.py --base origin/main
        # errors only for rows a pull request changed; problems that were
        # already there are counted, not reported as errors

Every CSV file of a language folder (de/, tr/, hu/...) is compared with the
file of the same name in template/:

  - the header is: id, english, polski, translation, notes, status;
  - every id is an id of the template's sheet, and only once;
  - the id and the english column are the template's (never edit them);
  - a translation keeps the English text's printf variables (%s %d %.1f...),
    in the same order, its {placeholders}, its [TAGS] and its |c..|r, |H..|h,
    |E..|e codes;
  - no tab or control character, and a new line only where the English has
    one or the notes say "new lines allowed";
  - every letter is in the Windows code page the game draws the language in
    (the launcher's sheet and the web panel's take any letter: UTF-8; a text
    the notes mark "ASCII letters only" uses plain letters alone), and
    the text is no longer than the notes allow;
  - the web panel's sheet (7_panel) keeps the English's HTML tags exactly,
    its count of '<' and '>', and brings no javascript: of its own - its
    texts go into a web page; its variables are Python's (%s, %(name)s, which
    may move), and a [WORD] there is ordinary text.

Only Python 3's standard library is used. Exit code 1 when an error is found.
"""
from __future__ import print_function

import argparse
import collections
import csv
import io
import os
import re
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
TEMPLATE = 'template'
COLUMNS = ['id', 'english', 'polski', 'translation', 'notes', 'status']
STATUSES = ('', 'new', 'done', 'check')

# The Windows code page the game client draws each language in.
CODEPAGES = {
    'pl': 'cp1250', 'cs': 'cp1250', 'sk': 'cp1250', 'hu': 'cp1250', 'ro': 'cp1250', 'hr': 'cp1250',
    'sl': 'cp1250', 'bs': 'cp1250', 'sr': 'cp1250', 'sq': 'cp1250',
    'ru': 'cp1251', 'uk': 'cp1251', 'bg': 'cp1251', 'be': 'cp1251', 'mk': 'cp1251',
    'de': 'cp1252', 'fr': 'cp1252', 'es': 'cp1252', 'it': 'cp1252', 'pt': 'cp1252', 'nl': 'cp1252',
    'da': 'cp1252', 'sv': 'cp1252', 'no': 'cp1252', 'nb': 'cp1252', 'fi': 'cp1252', 'ca': 'cp1252',
    'gl': 'cp1252', 'eu': 'cp1252', 'is': 'cp1252', 'ga': 'cp1252', 'id': 'cp1252', 'ms': 'cp1252',
    'tl': 'cp1252', 'sw': 'cp1252', 'af': 'cp1252',
    'el': 'cp1253', 'tr': 'cp1254', 'az': 'cp1254', 'he': 'cp1255', 'ar': 'cp1256', 'fa': 'cp1256',
    'lt': 'cp1257', 'lv': 'cp1257', 'et': 'cp1257', 'vi': 'cp1258', 'ko': 'cp949',
    'en': 'cp1252',
}
# A regional variant has a folder of its own (en_US/ next to the British
# source): it is drawn in the code page of its language.

# printf conversions: %s, %d, %5.1f, %lld, %%...
CONVERSION = re.compile(r"%(?:\(\w+\))?([-+ #0']*)(\*|\d+)?(?:\.(\*|\d*))?(hh|ll|I64|h|l|L|q|j|z|t)?"
                        r"([diouxXeEfFgGcrsap%])")
# Conversions that take the same kind of argument may replace each other.
KIND = {'d': 'd', 'i': 'd', 'o': 'u', 'u': 'u', 'x': 'u', 'X': 'u', 'e': 'f', 'E': 'f', 'f': 'f', 'F': 'f',
        'g': 'f', 'G': 'f', 'a': 'f', 'c': 'c', 's': 's', 'r': 's', 'p': 'p'}
PLACEHOLDER = re.compile(r'\{[^{}\s]*\}')
# The quest window's markup ([WAIT], [DELAY value;5], [COLOR r;1|g;0|b;0]):
# a capitalised word of four letters or more, alone or with its arguments.
# A text in brackets ([Guild], [PT], [ESC]) is translated like any other.
TAG = re.compile(r'\[(?!ENTER\])/?[A-Z][A-Z_]{3,}(?:[ ;=][^\]\[]*)?\]')
CODE = re.compile(r'\|c[0-9a-fA-F]{8}|\|[rhHEe]')
MAX_LENGTH = re.compile(r'max (\d+) characters')
PART = re.compile(r'^(?P<sheet>[1-7]_[a-z_]+?)(?:_(?P<part>\d+))?\.csv$')
HTML_TAG = re.compile(r'</?[A-Za-z][^<>]*>')
# The sheets shown by a program of their own, which draws any letter (UTF-8),
# not by the game client and its one code page.
UTF8_SHEETS = ('6_launcher', '7_panel')
# The classic web panel's sheet: HTML and Python's %-formatting.
PANEL_SHEET = '7_panel'


def variables(text, panel=False):
    """The printf arguments a text takes, by kind and in order. A '%' that is
    a percent sign in prose ("20% during", "% Erfolg") is not one. The web
    panel's texts are Python's %-formatting, which has no ' flag and whose
    space flag nobody writes ("25% a character", Turkish "%'si" are prose),
    and whose named %(name)s may move (compared as a set)."""
    out = []
    for m in CONVERSION.finditer(text):
        if m.group(5) == '%':
            continue
        after = text[m.end():m.end() + 1]
        if ' ' in m.group(1) and (panel or after.isalpha()):
            continue
        if panel and "'" in m.group(1):
            continue
        name = re.match(r'%\((\w+)\)', m.group(0))
        kind = KIND[m.group(5)]
        # A float's precision is what the reader sees: '%0f' for '%.0f' draws
        # six decimals, '%.1f' for '%.0f' one. None is printf's default, six.
        precision = '.' + (m.group(3) or '0') if kind == 'f' and m.group(3) is not None else ''
        out.append((name.group(1) + ':' if name else '') + kind + precision + (m.group(4) or ''))
    if panel and any(':' in c for c in out):
        out.sort()
    return out


def html_problem(english, text):
    """The web panel's rule: a translation keeps the English's markup."""
    a, b = sorted(HTML_TAG.findall(english)), sorted(HTML_TAG.findall(text))
    if a != b:
        return 'HTML tags %s, the English has %s (keep them exactly)' % (' '.join(b) or 'none', ' '.join(a) or 'none')
    if (english.count('<'), english.count('>')) != (text.count('<'), text.count('>')):
        return "a '<' or '>' that the English does not have"
    if 'javascript:' in text.lower() and 'javascript:' not in english.lower():
        return 'a javascript: address'
    return None


def codes(text):
    return sorted(c[:2].lower() if c.startswith('|c') else c for c in CODE.findall(text))


def problem(english, notes, text, codepage, panel=False):
    """Why `text` cannot be the translation of `english`, or None."""
    multiline = '\n' in english or 'new lines allowed' in notes
    if not multiline and ('\n' in text or '\r' in text):
        return 'a new line in a one-line text (use [ENTER] only if the English has it)'
    if '\t' in text and '\t' not in english:
        return 'a tab character'
    for c in text:
        if (ord(c) < 0x20 and c not in '\r\n\t') or ord(c) == 0x7f:
            return 'a control character %r' % c
    if 'ASCII letters only' in notes:
        for c in text:
            if ord(c) > 0x7e:
                return 'the letter %r: this text is typed by the bots in the chat, use plain letters (a-z) only' % c
    try:
        raw = text.replace('\r\n', '\n').encode(codepage)
    except UnicodeEncodeError as e:
        return ("the character %r is not in %s, the code page the game draws this language in "
                "(no emoji; see the README for the letters)" % (text[e.start:e.end], codepage))
    m = MAX_LENGTH.search(notes)
    if m and len(raw) > int(m.group(1)):
        return 'too long: %d characters, at most %s' % (len(raw), m.group(1))
    if 'percent sign here' not in notes:
        a, b = variables(english, panel), variables(text, panel)
        if a != b:
            return 'variables %s, the English has %s (same ones, same order)' % (
                ' '.join(b) or 'none', ' '.join(a) or 'none')
    for name, find in (('placeholders', PLACEHOLDER.findall), ('tags', TAG.findall), ('colour/link codes', codes)):
        if panel and name == 'tags':
            continue   # the quest window's markup; the web panel shows a [WORD] as it is
        a, b = sorted(find(english)), sorted(find(text))
        if a != b:
            return '%s %s, the English has %s' % (name, ' '.join(b) or 'none', ' '.join(a) or 'none')
    if panel:
        return html_problem(english, text)
    return None


def read_csv(data, label):
    """(header, [(line, row)]) of a CSV file's text."""
    if data.startswith('﻿'):
        data = data[1:]
    first = data.split('\n', 1)[0]
    delimiter = ';' if first.count(';') > first.count(',') else ','
    reader = csv.reader(io.StringIO(data, newline=''), delimiter=delimiter)
    rows = []
    header = None
    start = 1
    for row in reader:
        if header is None:
            header = [c.strip().lower() for c in row]
        elif any(cell.strip() for cell in row):
            rows.append((start, row))
        start = reader.line_num + 1
    return header or [], rows, delimiter


def read_file(path):
    with io.open(path, encoding='utf-8', newline='') as f:
        return f.read()


def git_show(base, rel):
    try:
        out = subprocess.check_output(['git', '-C', ROOT, 'show', '%s:%s' % (base, rel)], stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, OSError):
        return None
    return out.decode('utf-8', 'replace')


class Report(object):
    def __init__(self):
        self.errors = 0
        self.warnings = 0
        self.old = 0

    def error(self, path, line, msg):
        self.errors += 1
        print('::error file=%s,line=%d::%s' % (path, line, msg) if os.environ.get('GITHUB_ACTIONS')
              else '%s:%d: error: %s' % (path, line, msg))

    def warning(self, path, line, msg):
        self.warnings += 1
        print('::warning file=%s,line=%d::%s' % (path, line, msg) if os.environ.get('GITHUB_ACTIONS')
              else '%s:%d: warning: %s' % (path, line, msg))


def load_template(report):
    """sheet -> {id: (english, polski, notes)}"""
    folder = os.path.join(ROOT, TEMPLATE)
    sheets = collections.OrderedDict()
    for name in sorted(os.listdir(folder)):
        m = PART.match(name)
        if not m:
            continue
        header, rows, _d = read_csv(read_file(os.path.join(folder, name)), name)
        if header != COLUMNS:
            report.error('%s/%s' % (TEMPLATE, name), 1, 'template header is %s' % header)
            continue
        table = sheets.setdefault(m.group('sheet'), {})
        for _line, row in rows:
            row = (row + [''] * 6)[:6]
            table[row[0]] = (row[1], row[2], row[4])
    return sheets


def validate_language(code, template, report, base=None):
    folder = os.path.join(ROOT, code)
    codepage = CODEPAGES.get(code)
    if codepage is None and re.match(r'^[a-z]{2,3}_[A-Z]{2}$', code):
        codepage = CODEPAGES.get(code.split('_')[0])   # en_US: the code page of en
    stats = [0, 0]   # rows, translated
    if codepage is None:
        report.error('%s/' % code, 1, "'%s' is no language code this repository knows: use the ISO 639-1 code "
                     "of the language (hu, es, cs...) or ask in the pull request" % code)
        return stats
    seen = {}
    for name in sorted(os.listdir(folder)):
        rel = '%s/%s' % (code, name)
        path = os.path.join(folder, name)
        if os.path.isdir(path) or not name.lower().endswith('.csv'):
            continue
        m = PART.match(name)
        if not m or m.group('sheet') not in template:
            report.error(rel, 1, 'not a file of template/ (keep the template\'s file names)')
            continue
        table = template[m.group('sheet')]
        # The launcher is a Windows program of its own and the web panel a
        # page in a browser: both show any letter.
        sheet_codepage = 'utf-8' if m.group('sheet') in UTF8_SHEETS else codepage
        panel = m.group('sheet') == PANEL_SHEET
        data = read_file(path)
        header, rows, delimiter = read_csv(data, rel)
        if header != COLUMNS:
            report.error(rel, 1, 'the header must be: %s' % ','.join(COLUMNS))
            continue
        if delimiter != ',' or data.startswith('﻿'):
            report.warning(rel, 1, 'saved with %s; please save as CSV UTF-8 with commas, as in template/'
                           % ('semicolons' if delimiter != ',' else 'a byte order mark'))
        before = {}
        if base:
            old = git_show(base, rel)
            if old is not None:
                for _l, r in read_csv(old, rel)[1]:
                    r = (r + [''] * 6)[:6]
                    before[r[0]] = r[3]
        for line, row in rows:
            if len(row) != len(COLUMNS):
                report.error(rel, line, 'the row has %d columns, not %d (a comma or quote out of place?)'
                             % (len(row), len(COLUMNS)))
                continue
            rid, english, polski, text, notes, status = row
            stats[0] += 1
            if rid not in table:
                report.error(rel, line, "unknown id %r: the id column must never be edited" % rid)
                continue
            if rid in seen:
                report.error(rel, line, 'the id %r is already in %s' % (rid, seen[rid]))
                continue
            seen[rid] = '%s:%d' % (rel, line)
            t_english, t_polski, t_notes = table[rid]
            if english.replace('\r\n', '\n') != t_english.replace('\r\n', '\n'):
                report.error(rel, line, 'the english column was changed: translate in the "translation" column only')
                continue
            if polski != t_polski or notes != t_notes:
                report.warning(rel, line, 'the polski or notes column differs from template/ (only "translation" '
                               'is read)')
            if status.strip().lower() not in STATUSES:
                report.warning(rel, line, 'status %r: use new, done or check' % status)
            if not text.strip():
                continue
            stats[1] += 1
            # A row whose English column is empty (a few bot chat lines exist
            # only in Polish) is checked against the Polish text instead.
            why = problem(t_english if t_english.strip() else t_polski, t_notes, text, sheet_codepage, panel)
            if why:
                if base and before.get(rid) == text:
                    report.old += 1
                else:
                    report.error(rel, line, '%s: %s' % (rid, why))
    return stats


def main(argv=None):
    parser = argparse.ArgumentParser(description='Check the translations of this repository.')
    parser.add_argument('languages', nargs='*', help='language folders (default: all)')
    parser.add_argument('--base', help='a git ref: report errors only for rows changed since it')
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    report = Report()
    template = load_template(report)
    if not template:
        print('validate: template/ holds no sheet')
        return 1
    codes = args.languages or sorted(
        d for d in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, d)) and re.match(r'^[a-z]{2,3}(_[A-Z]{2})?$', d))
    lines = ['| language | rows | translated |', '|---|---:|---:|']
    for code in codes:
        if not os.path.isdir(os.path.join(ROOT, code)):
            report.error(code, 1, 'no such folder')
            continue
        rows, done = validate_language(code, template, report, args.base)
        lines.append('| %s | %d | %d (%.1f%%) |' % (code, rows, done, 100.0 * done / max(1, rows)))
    total = sum(len(t) for t in template.values())
    summary = ['Template: %d rows in %d sheets.' % (total, len(template)), ''] + lines + ['',
               '%d errors, %d warnings%s.' % (report.errors, report.warnings,
                                              ', %d older problems not caused by this change' % report.old
                                              if args.base else '')]
    print('\n'.join(summary))
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with io.open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as f:
            f.write('## Translation check\n\n' + '\n'.join(summary) + '\n')
    return 1 if report.errors else 0


if __name__ == '__main__':
    sys.exit(main())
