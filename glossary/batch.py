#!/usr/bin/env python3
"""Batch workflow for filling empty translation cells in many languages at once.

    python glossary/batch.py prep 1_klient_01 [--max 40] [--langs de,fr]
        1. fills empty cells whose english text already has a translation in
           the same language (consistency) or has nothing to translate
           (numbers, codes, fonts...);
        2. prints the next unique english texts still empty in some language
           and saves them as the current batch.
    python glossary/batch.py apply answers.txt
        answers.txt:   @<n>            (item number of the current batch)
                       <lang>=<text>   (one line per language; * = every language)
        "<NL>" stands for a new line. Leading/trailing blanks are copied from the
        English. Each text is checked like tools/validate.py; rows that fail are
        reported and left empty.
    python glossary/batch.py commit
        one commit per language and file that has no empty cell left.

Only empty translation cells are ever written; status becomes "done".
"""
import argparse
import collections
import csv
import glob
import io
import json
import os
import re
import subprocess
import sys
import unicodedata

sys.dont_write_bytecode = True
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import validate  # noqa: E402

LANGS = ['de', 'fr', 'pt', 'ro', 'es', 'it', 'hu', 'cs', 'nl', 'da', 'el', 'ru', 'ar', 'ko', 'tr']
CP = dict(validate.CODEPAGES, ko='cp949')
STATE = os.path.join(os.environ.get('BATCH_STATE', os.path.join(ROOT, '.git')), 'batch_state.json')
TRAILER = ('\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
           'Claude-Session: https://claude.ai/code/session_013JsyiEv1Zjk6MphvvBJgnt')


def load(path):
    raw = io.open(path, encoding='utf-8', newline='').read()
    lt = '\r\n' if raw.split('\n', 1)[0].endswith('\r') else '\n'
    return list(csv.reader(io.StringIO(raw, newline=''))), lt


def save(path, rows, lt):
    s = io.StringIO()
    csv.writer(s, lineterminator=lt).writerows(rows)
    io.open(path, 'w', encoding='utf-8', newline='').write(s.getvalue())


def codepage(lang, fname):
    return 'utf-8' if fname.startswith(validate.UTF8_SHEETS) else CP[lang]


def source(row):
    return row[1] if row[1].strip() else row[2]


STRIP = re.compile(r"%[-+ #0']*\d*(?:\.\d*)?(?:hh|ll|I64|h|l|L)?[diouxXeEfFgGcsp%]|\{[^{}]*\}|\[[A-Z_/][^\]]*\]"
                   r"|\|c[0-9a-fA-F]{8}|\|[rhHEe]|\|H[^|]*\|h")


NONLATIN = ('el', 'ru', 'ar', 'ko')


def nothing_to_translate(text, lang):
    rest = STRIP.sub('', text)
    names = '' if lang in NONLATIN else 'Yang|Shinsoo|Chunjo|Jinno|Ninja|Sura|'
    rest = re.sub(r'\b(?:Arial|Tahoma|Gulim|GM|HP|SP|EXP|IP|M1|M2|OK|PvP|PvM|' + names +
                  r'[A-Z]\d*|\d+x|x\d+|v\d+)\b', '', rest)
    return not re.search(r'[^\W\d_]', rest)


def fold_ascii(text):
    text = text.replace('ß', 'ss').replace('æ', 'ae').replace('Æ', 'Ae').replace('ø', 'o').replace('Ø', 'O') \
        .replace('ł', 'l').replace('Ł', 'L').replace('œ', 'oe').replace('ı', 'i').replace('İ', 'I')
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')


def fix_blanks(english, text):
    lead = re.match(r'\s*', english).group()
    trail = re.search(r'\s*$', english).group()
    return lead + text.strip() + trail if text.strip() else text


def check(lang, fname, english, notes, text):
    return validate.problem(english, notes, text, codepage(lang, fname),
                            panel=fname.startswith(validate.PANEL_SHEET))


def lang_files(lang, pattern='*'):
    return sorted(glob.glob(os.path.join(ROOT, lang, pattern + '.csv')))


def memory(lang):
    tm = collections.defaultdict(collections.Counter)
    for path in lang_files(lang):
        rows, _ = load(path)
        for r in rows[1:]:
            if len(r) == 6 and r[3].strip():
                tm[source(r)][r[3]] += 1
    return {k: v.most_common(1)[0][0] for k, v in tm.items()}


def fill(lang, mapping, only_file=None):
    """mapping: english -> text. Writes every empty cell of the language whose
    english is in mapping and passes the checks. Returns (filled, problems)."""
    filled, problems = collections.Counter(), []
    for path in lang_files(lang, only_file or '*'):
        fname = os.path.basename(path)
        rows, lt = load(path)
        n = 0
        for r in rows[1:]:
            if len(r) != 6 or r[3].strip():
                continue
            src = source(r)
            if src not in mapping:
                continue
            text = fix_blanks(src, mapping[src])
            if 'ASCII letters only' in r[4]:
                if lang not in NONLATIN:
                    text = fold_ascii(text)
                elif not text.isascii():
                    continue  # bots type plain a-z: filled later with a romanised text
            # rows with no English are checked against the Polish text, as in tools/validate.py
            why = check(lang, fname, r[1] if r[1].strip() else r[2], r[4], text)
            if why:
                problems.append((lang, fname, r[0], why, text))
                continue
            r[3], r[5] = text, 'done'
            n += 1
        if n:
            save(path, rows, lt)
            filled[fname] += n
    return filled, problems


def cmd_prep(args):
    langs = args.langs.split(',') if args.langs else [l for l in LANGS if os.path.isdir(os.path.join(ROOT, l))]
    need = collections.OrderedDict()
    auto = collections.Counter()
    for lang in langs:
        tm = memory(lang)
        path = os.path.join(ROOT, lang, args.file + '.csv')
        rows, _ = load(path)
        empty = [r for r in rows[1:] if len(r) == 6 and not r[3].strip() and source(r).strip()]
        mapping = {}
        for r in empty:
            src = source(r)
            if src in tm:
                mapping[src] = tm[src]
            elif nothing_to_translate(src, lang):
                mapping[src] = src
        if mapping:
            f, _p = fill(lang, mapping, args.file)
            auto[lang] += sum(f.values())
        rows, _ = load(path)
        for r in rows[1:]:
            if len(r) == 6 and not r[3].strip() and source(r).strip():
                need.setdefault(source(r), {'notes': set(), 'langs': [], 'en': bool(r[1].strip())})
                e = need[source(r)]
                e['notes'].add(r[4])
                if lang not in e['langs']:
                    e['langs'].append(lang)
    if auto:
        print('auto-filled:', dict(auto))
    items = list(need.items())
    print('remaining unique texts in %s: %d' % (args.file, len(items)))
    batch, chars = [], 0
    for src, e in items:
        if len(batch) >= args.max or (batch and chars + len(src) > args.chars):
            break
        batch.append({'src': src, 'langs': e['langs'], 'notes': sorted(e['notes'])})
        chars += len(src)
    json.dump({'file': args.file, 'items': batch}, io.open(STATE, 'w', encoding='utf-8'), ensure_ascii=False)
    all_langs = last_flags = None
    for i, b in enumerate(batch, 1):
        flags = []
        for n in b['notes']:
            for part in n.split(' | ')[1:]:
                if part.startswith(('keep:', 'new lines', '{#0}')) or 'filled in' in part:
                    continue
                flags.append(part)
        if not b['notes'][0].startswith(('quest', 'launcher')):
            flags.insert(0, b['notes'][0].split(' | ')[0])
        ls = ','.join(b['langs'])
        if ls != all_langs:
            print('== langs: %s' % ls)
            all_langs = ls
        fl = ('[' + '; '.join(sorted(set(flags))) + ']') if flags else ''
        print('@%d %s' % (i, fl if fl != last_flags else ''))
        last_flags = fl
        print(b['src'].replace('\n', '<NL>'))


def parse_answers(path):
    ans = collections.defaultdict(dict)
    cur = None
    for line in io.open(path, encoding='utf-8').read().split('\n'):
        if not line.strip():
            continue
        m = re.match(r'^@(\d+)\s*$', line)
        if m:
            cur = int(m.group(1))
            continue
        m = re.match(r'^([a-z]{2}|\*)=(.*)$', line)
        if m and cur is not None:
            ans[cur][m.group(1)] = m.group(2).replace('<NL>', '\n')
        elif cur is not None and ans[cur]:
            last = list(ans[cur])[-1]
            ans[cur][last] += '\n' + line  # continuation (should not happen)
    return ans


def cmd_apply(args):
    state = json.load(io.open(STATE, encoding='utf-8'))
    items = state['items']
    ans = parse_answers(args.answers)
    per_lang = collections.defaultdict(dict)
    missing = []
    for i, b in enumerate(items, 1):
        a = ans.get(i, {})
        for lang in b['langs']:
            text = a.get(lang, a.get('*'))
            if text is None:
                missing.append('@%d %s' % (i, lang))
                continue
            per_lang[lang][b['src']] = text
    total, problems = collections.Counter(), []
    for lang, mapping in per_lang.items():
        f, p = fill(lang, mapping)
        total[lang] = sum(f.values())
        problems += p
    print('filled:', dict(total))
    if missing:
        print('MISSING:', ' '.join(missing))
    for lang, fname, rid, why, text in problems:
        print('PROBLEM %s %s %s: %s | %r' % (lang, fname, rid, why, text[:120]))


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True).stdout


def stage(rel):
    """git add, but a file stored with CRLF on main keeps CRLF in the commit
    (.gitattributes would normalise it to LF and every line would show as changed)."""
    head = subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:' + rel], capture_output=True).stdout
    if b'\r\n' in head:
        path = os.path.join(ROOT, rel)
        data = open(path, 'rb').read().replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
        sha = subprocess.run(['git', '-C', ROOT, 'hash-object', '-w', '--no-filters', '--stdin'],
                             input=data, capture_output=True).stdout.decode().strip()
        git('update-index', '--cacheinfo', '100644,%s,%s' % (sha, rel))
    else:
        git('add', rel)


def cmd_commit(args):
    changed = [l for l in git('diff', '--name-only').split('\n') if l.endswith('.csv')]
    # files hidden with "git update-index --assume-unchanged" (CRLF on main) may hold real edits
    changed += [l[2:] for l in git('ls-files', '-v').split('\n') if l[:2] == 'h ' and l.endswith('.csv')]
    changed = sorted(set(changed))
    done = 0
    for rel in sorted(changed):
        lang, fname = rel.split('/')
        rows, _ = load(os.path.join(ROOT, rel))
        if any(len(r) == 6 and not r[3].strip() and source(r).strip() for r in rows[1:]) and not args.all:
            continue
        old = {}
        for r in list(csv.reader(io.StringIO(git('show', 'HEAD:' + rel), newline='')))[1:]:
            if len(r) == 6:
                old[r[0]] = r[3]
        n = sum(1 for r in rows[1:] if len(r) == 6 and r[3] != old.get(r[0], r[3]))
        if not n:
            continue  # only line endings differ: leave the file as it is on main
        stage(rel)
        git('commit', '-q', '-m', '%s: %s übersetzt (%d Zeilen)%s' % (lang, fname[:-4], n, TRAILER))
        done += 1
    print('commits:', done)


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd')
    a = sub.add_parser('prep')
    a.add_argument('file')
    a.add_argument('--max', type=int, default=40)
    a.add_argument('--chars', type=int, default=2500)
    a.add_argument('--langs')
    b = sub.add_parser('apply')
    b.add_argument('answers')
    c = sub.add_parser('commit')
    c.add_argument('--all', action='store_true', help='also commit files that still have empty cells')
    args = p.parse_args()
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    {'prep': cmd_prep, 'apply': cmd_apply, 'commit': cmd_commit}[args.cmd](args)


if __name__ == '__main__':
    main()
