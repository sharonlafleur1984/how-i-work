#!/usr/bin/env python3
"""Mechanical checks for the ux-writer skill. Run on every piece of copy.

    python3 scripts/check.py <file> [<file> ...]

Exit code 1 if anything is flagged. Every finding needs an outcome: fixed, or a
reviewed exception with the reason said out loud.
"""
import collections, io, re, sys

CUT = {
    'simply': 'cut', 'just': 'cut', 'easy': 'cut', 'easily': 'cut',
    'obviously': 'cut', 'of course': 'cut', 'basically': 'cut',
    'essentially': 'cut', 'very': 'cut', 'really': 'cut',
    'actually': 'only if it carries meaning', 'currently': 'usually cut',
    'note that': 'cut', 'it is important': 'cut', 'please': 'cut in instructions',
    'great question': 'cut', 'amazing': 'cut', 'absolutely': 'cut',
    'utilize': 'use', 'configure': 'set', 'additional': 'more', 'advise': 'tell',
    'leverage': 'use', 'facilitate': 'help', 'approximately': 'about',
    'commence': 'start', 'demonstrate': 'show', 'prior to': 'before',
    'in order to': 'to',
}
HURT = {
    'crazy': 'confusing', 'insane': 'extreme', 'dumb': 'unclear', 'lame': 'weak',
    'sanity check': 'quick check', 'blacklist': 'blocklist', 'whitelist': 'allowlist',
    'master/slave': 'primary/replica', 'special needs': 'name the need or accommodation',
    'suffers from': 'has', 'wheelchair-bound': 'uses a wheelchair',
    'handicapped': 'disabled', 'blind to': 'unaware of', 'fell on deaf ears': 'ignored',
    'non-white': 'name the group', 'caucasian': 'white', 'spirit animal': 'favorite',
    'totem pole': 'ranking', 'the elderly': 'older adults', 'guys': 'everyone',
    'mankind': 'people', 'manpower': 'staff', 'sexual preference': 'sexual orientation',
    'illegal alien': 'undocumented', 'the disabled': 'disabled people',
}
HEDGE = re.compile(r'\b(might|may|could)\s+(possibly|perhaps|maybe)\b'
                   r'|\b(possibly|perhaps)\s+(might|may)\b', re.I)
POINTER = re.compile(r'^(not|this|these|that|those|it|its|they|them|their|other)\b', re.I)
COUNT_HEAD = re.compile(r'^#+\s+(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\s+\S+\s*$', re.I)
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')
LINK_ONLY = re.compile(r'^\[[^\]]+\]\([^)]+\)\.?$')
TAG = re.compile(r'\s*\[[A-Z]{2,8}\]\s*$')   # a trailing provenance tag is not a sentence


def plain(t):
    t = re.sub(r'`[^`]*`', 'CODE', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    return TAG.sub('', t.replace('**', '').rstrip())


def unquoted(t):
    """Blank out quoted and code spans. A skill or voice file quotes the words it bans."""
    t = re.sub(r'`[^`]*`', ' ', t)
    t = re.sub(r'\((?:not|never|instead of)\s[^)]*\)', ' ', t)   # "use (not utilize)"
    return re.sub(r'"[^"]*"|\u201c[^\u201d]*\u201d|\u2018[^\u2019]*\u2019', ' ', t)


def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', plain(t)) if s.strip()]


def check(path):
    text = io.open(path, encoding='utf-8').read()
    lines = text.split('\n')
    f = collections.defaultdict(list)
    seen = {}
    ref_zone = False

    for n, ln in enumerate(lines, 1):
        s = ln.strip()
        low = unquoted(plain(ln)).lower()
        is_head, is_row = s.startswith('#'), s.startswith('|')
        is_bullet = s.startswith(('- ', '* '))
        body = bool(s) and not is_head and not is_row
        if is_head:
            ref_zone = bool(re.search(r'\b(sources?|provenance|references?)\b', low))

        if '—' in ln or '–' in ln:
            f['em dash or en dash'].append((n, s[:72]))
        uq = unquoted(plain(ln))
        if EMOJI.search(uq):
            f['emoji'].append((n, s[:72]))
        if '!' in uq and not is_row:
            f['exclamation mark'].append((n, s[:72]))
        if HEDGE.search(uq):
            f['hedge stack'].append((n, s[:72]))
        for w, fix in CUT.items():
            if re.search(r'\b%s\b' % re.escape(w), low):
                f['cut on sight'].append((n, '"%s" -> %s' % (w, fix)))
        for w, fix in HURT.items():
            if re.search(r'\b%s\b' % re.escape(w.replace('/', r'\/')), low):
                f['language that can hurt'].append((n, '"%s" -> %s' % (w, fix)))

        if is_head:
            h = re.sub(r'^#+\s*', '', plain(s))
            if POINTER.match(h):
                f['heading points instead of naming'].append((n, h[:72]))
            if COUNT_HEAD.match(s):
                f['heading is a count, not a subject'].append((n, h[:72]))
        if is_row and not re.match(r'^\|[\s:|-]+\|$', s):
            prev = lines[n].strip() if n < len(lines) else ''
            if re.match(r'^\|[\s:|-]+\|$', prev):           # this row is the header row
                for cell in [c.strip() for c in s.strip('|').split('|')]:
                    if cell and POINTER.match(plain(cell)):
                        f['column header points instead of naming'].append((n, cell))

        if is_bullet:
            b = s[2:]
            pb = plain(b)
            halves = unquoted(pb).split(':', 1)
            if (not LINK_ONLY.match(b) and len(halves) == 2
                    and len(halves[0].split()) >= 5 and len(halves[1].split()) >= 5):
                f['bullet carries a colon of its own'].append((n, pb[:72]))
            if len(sentences(b)) > 3:
                f['bullet holds more than one idea'].append((n, '%d sentences: %s'
                                                             % (len(sentences(b)), pb[:55])))
        if body and not ref_zone:
            for sent in sentences(ln):
                wc = len(sent.split())
                if wc > 34:
                    f['sentence over 34 words'].append((n, '%dw: %s' % (wc, sent[:58])))
                key = re.sub(r'[^a-z ]', '', sent.lower()).strip()
                if len(key) > 40:
                    if key in seen:
                        f['sentence repeated'].append((n, 'repeats line %d' % seen[key]))
                    else:
                        seen[key] = n

    # colon stems: every bullet under a line ending in ":" must finish that sentence
    for i, ln in enumerate(lines):
        if ln.rstrip().endswith(':') and not ln.strip().startswith('|'):
            kids, j = [], i + 1
            while j < len(lines) and (lines[j].strip().startswith('- ') or not lines[j].strip()):
                if lines[j].strip().startswith('- '):
                    kids.append(lines[j].strip()[2:])
                j += 1
            kids = [k for k in kids if not LINK_ONLY.match(k)]
            caps = [k for k in kids if re.match(r'^[A-Z][a-z]', plain(k))]
            if kids and caps and len(caps) != len(kids):
                f['colon stem its bullets do not finish'].append(
                    (i + 1, '%d of %d bullets start as new sentences' % (len(caps), len(kids))))

    # Bullet parallelism is NOT checked here on purpose. Telling a gerund acting as a
    # noun ("Over-apologizing") from a gerund acting as an instruction ("Putting a
    # requirement and a design choice in one bullet") needs a part-of-speech judgment this
    # script cannot make, and a check that cries wolf teaches people to ignore the script.
    # It lives in the review checklist in section 11 instead.

    print('=== %s ===' % path)
    if not f:
        print('  clean')
    for k in sorted(f):
        print('  [%s] %d' % (k, len(f[k])))
        for n, d in f[k][:10]:
            print('      line %d: %s' % (n, d))
    return sum(len(v) for v in f.values())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(1 if sum(check(p) for p in sys.argv[1:]) else 0)
