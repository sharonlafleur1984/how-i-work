#!/usr/bin/env python3
"""Mechanical checks for the ux-writer skill. Run on every piece of copy.

    python3 scripts/check.py <file> [<file> ...]

Exit code 1 if any error is flagged. Findings marked (warning) or (suggestion) do
not fail the run. Warnings still need an outcome: fixed, or a reviewed exception with
the reason said out loud. Suggestions are worth a look; they misfire more often.
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
# Words a writer must judge in context: they fail a check only as warnings.
JUDGMENT = {'only if it carries meaning', 'usually cut'}
# "easy" is cut when it claims a task is easy for the reader, not when it describes a thing.
EASY_CLAIM = re.compile(r"\b(is|are|it's|its|that's|was|be|so|very|pretty|really|super|quite)\s+easy\b"
                        r"|\beasy\s+(to|as|enough)\b", re.I)
HEDGE = re.compile(r'\b(might|may|could)\s+(possibly|perhaps|maybe)\b'
                   r'|\b(possibly|perhaps)\s+(might|may)\b', re.I)
POINTER = re.compile(r'^(not|this|these|that|those|it|its|they|them|their|other)\b', re.I)
COUNT_HEAD = re.compile(r'^#+\s+(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\s+\S+\s*$', re.I)
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')
LINK_ONLY = re.compile(r'^\[[^\]]+\]\([^)]+\)\.?$')
PARA_SENTENCES, PARA_WORDS = 5, 60   # section 5: error past these
PARA_WARN_WORDS = 50                 # section 5: warning past this (W3C COGA)
SENT_WARN, SENT_MAX = 25, 34         # section 5: warning past 25 words (GOV.UK), error past 34
SUMMARY_FROM_WORDS = 300             # section 7: pages this long open with a summary
BACKREF = re.compile(r'\b(as (mentioned|noted|discussed|stated|described|shown) '
                     r'(above|earlier|before|previously)|see (above|below)|'
                     r'see the (previous|last|earlier) section|the above|aforementioned|'
                     r'previously mentioned)\b', re.I)
OPENER = re.compile(r'^(this (document|page|section|doc|guide)|in this (document|page|section|doc|guide))\b', re.I)
STEP_CHAIN = re.compile(r'\b(and then|after that|afterwards|once that is done)\b|,\s*then\b', re.I)
ACRONYMS = {'API', 'APIS', 'AWS', 'FAQ', 'HTML', 'CSS', 'JSON', 'PDF', 'URL', 'UI', 'UX',
            'ID', 'IDS', 'OK', 'PR', 'S3', 'WCAG', 'COGA', 'BDA', 'NN', 'GOV', 'UK', 'US',
            'USA', 'EU', 'CEO', 'AI', 'LUFS', 'WAV', 'MP3', 'MDT', 'PST', 'PDT', 'AM', 'PM',
            'TODO', 'README', 'SKILL', 'MD', 'IEP', 'ADHD', 'TL', 'DR', 'BLUF', 'ISO', 'FAFSA',
            'W3C', 'NHS', 'WAI', 'ARIA', 'SVG', 'PNG', 'CSV', 'SQL', 'HTTP', 'HTTPS', 'DNS'}
CAPS_RUN = re.compile(r'\b([A-Z][A-Z0-9]{1,})\b(?:[\s/&-]+\b([A-Z][A-Z0-9]{1,})\b)+')
ITALIC = re.compile(r'(?<![*\w])\*(?![*\s])[^*\n]+?(?<![\s*])\*(?![*\w])'
                    r'|(?<![\w_])_(?![_\s])[^_\n]+?(?<![\s_])_(?![\w_])')
HEADING_EVERY = 300                  # section 6: words of body text between headings
MAX_STEPS = 7                        # section 5: numbered steps per list (Microsoft style guide)
MAX_OPTIONS = 3                      # section 5: more options than this need a marked pick
MAX_CALLOUTS = 2                     # section 7: callouts per page (GitHub docs)
BOLD_MAX_WORDS = 8                   # section 5: a bold lead-in this long stops being an anchor
SEQ_WORDS = re.compile(r'\b(first|then|next|after that|finally|afterwards|once)\b', re.I)
COND_START = re.compile(r'(?:^|[.;]\s+)(if|when|unless)\b', re.I)
HEAD_OPENER = re.compile(r'^(this (section|page|part|chapter)|in this (section|page|part)|'
                         r'below (is|are)|the following)\b', re.I)
IDIOMS = ['piece of cake', 'ballpark', 'low-hanging fruit', 'move the needle', 'circle back',
          'touch base', 'on the same page', 'boil the ocean', 'deep dive', 'game changer',
          'game-changer', 'hit the ground running', 'at the end of the day', 'in a nutshell',
          'back to square one', 'ball is in your court', 'bite the bullet', 'cut corners',
          'outside the box', 'drop the ball', 'on the fly', 'under the hood', 'no-brainer',
          'bells and whistles', 'tip of the iceberg', 'up in the air', 'on the back burner',
          'heavy lifting', 'take it for a spin', 'out of left field', 'level up']
DOUBLE_NEG = re.compile(r"\b(not|n't)\s+(un\w{4,}|non-?\w{4,}|(in|im|ir|il)\w*(able|ible|ent|ant|ive|ate|ful|ar)"
                        r"|dis\w{4,})\b|\bnot\s+\w+\s+(nothing|never|no one|none)\b", re.I)
VAGUE_TIME = re.compile(r'\b(soon|asap|shortly|in a bit|at some point|down the road|'
                        r'in the near future|sometime)\b', re.I)
VAGUE_LINK = re.compile(r'\[(click here|here|this|link|read more|more)\]\(', re.I)
DATE = re.compile(r'\b(\d{4}-\d{2}-\d{2}|(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)'
                  r'[a-z]*\.?\s+\d{1,2})\b', re.I)
STATUS_WORDS = re.compile(r'\b(done|blocked|in progress|at risk|on track|complete|pending|'
                          r'not started|overdue)\b', re.I)
FRAGMENT_END = {'to', 'for', 'of', 'the', 'a', 'an', 'and', 'or', 'with', 'are', 'is',
                'include', 'includes', 'like', 'as', 'by', 'from', 'in', 'on', 'at', 'be',
                'into', 'about', 'than', 'such', 'covers', 'means', 'needs', 'gets'}
STATUS_EMOJI = re.compile('[\U0001F534\U0001F7E0\U0001F7E1\U0001F7E2\U0001F535\U0001F7E3'
                          '\U0001F7E4\u26AA\u26AB\u2705\u274C\u2B55\U0001F6A6\u26A0]\uFE0F?')
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
        if '!' in uq.replace('[!', '[') and not is_row:
            f['exclamation mark'].append((n, s[:72]))
        if HEDGE.search(uq):
            f['hedge stack'].append((n, s[:72]))
        for w, fix in CUT.items():
            if re.search(r'\b%s\b' % re.escape(w), low):
                if w == 'easy' and not EASY_CLAIM.search(low):
                    continue             # "easy dinners" describes a thing; "it's easy" judges the reader's task
                if fix in JUDGMENT:
                    f['cut unless it carries meaning (warning)'].append((n, '"%s" -> %s' % (w, fix)))
                else:
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
                if wc > SENT_MAX:
                    f['sentence over 34 words'].append((n, '%dw: %s' % (wc, sent[:58])))
                elif wc > SENT_WARN:
                    f['sentence over 25 words (warning)'].append((n, '%dw: %s' % (wc, sent[:58])))
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
            stem = re.sub(r'^([-*]|\d+[.)]|#+)\s+', '', plain(ln.strip())).rstrip(':').split()
            complete = len(stem) >= 4 and stem[-1].lower() not in FRAGMENT_END
            if complete and len(caps) == len(kids):
                continue                     # a full lead-in sentence, then full-sentence bullets
            if kids and caps and len(caps) != len(kids):
                f['colon stem its bullets do not finish'].append(
                    (i + 1, '%d of %d bullets start as new sentences' % (len(caps), len(kids))))

    # paragraphs: a block of plain lines (not headings, bullets, tables, quotes or code)
    # holds one idea, in at most PARA_SENTENCES sentences and PARA_WORDS words.
    in_code, ref_zone, block, start = False, False, [], 0
    body_from = 0
    if lines and lines[0].strip() == '---':          # skip YAML frontmatter
        body_from = next((i + 1 for i in range(1, len(lines)) if lines[i].strip() == '---'), 0)

    def close(block, start):
        if not block or ref_zone:
            return
        para = ' '.join(block)
        sc, wc = len(sentences(para)), len(plain(para).split())
        if sc > PARA_SENTENCES or wc > PARA_WORDS:
            f['paragraph too long'].append(
                (start, '%d sentences, %dw: %s' % (sc, wc, plain(para)[:50])))
        elif wc > PARA_WARN_WORDS:
            f['paragraph over 50 words (warning)'].append(
                (start, '%dw: %s' % (wc, plain(para)[:50])))

    for n, ln in enumerate(lines, 1):
        if n <= body_from:
            continue
        s = ln.strip()
        if s.startswith('```'):
            in_code = not in_code
            close(block, start); block = []
            continue
        plain_line = (s and not in_code and not s.startswith(('#', '|', '- ', '* ', '>', '<'))
                      and not re.match(r'^\d+\.\s', s) and s != '---')
        if plain_line:
            if not block:
                start = n
            block.append(s)
        else:
            close(block, start); block = []
            if s.startswith('#'):
                ref_zone = bool(re.search(r'\b(sources?|provenance|references?)\b', s.lower()))
    close(block, start)

    # ---- structure checks (section 3, 5, 6, 7 and 2). Code blocks are skipped. ----
    in_code, heads, prev_level, h1s = False, {}, 0, 0
    body_words, first_h1 = 0, None
    for n, ln in enumerate(lines, 1):
        if n <= body_from:
            continue
        s = ln.strip()
        if s.startswith('```'):
            in_code = not in_code
            continue
        if in_code or not s:
            continue
        uq = unquoted(plain(ln)) if not s.startswith('#') else ''
        raw_uq = unquoted(re.sub(r'\*\*[^*]+\*\*', ' ', ln))       # bold removed, quotes removed

        # headings: one H1, no skipped levels, no duplicates (markdownlint MD001, MD024, MD025)
        m = re.match(r'^(#{1,6})\s+(.*)$', s)
        if m:
            level, text = len(m.group(1)), plain(m.group(2)).strip().lower()
            if level == 1:
                h1s += 1
                if h1s == 2:
                    f['more than one H1'].append((n, text[:60]))
                if first_h1 is None:
                    first_h1 = n
            if prev_level and level > prev_level + 1:
                f['heading skips a level'].append((n, 'H%d after H%d: %s' % (level, prev_level, text[:50])))
            if text in heads:
                f['duplicate heading'].append((n, 'same as line %d: %s' % (heads[text], text[:50])))
            heads.setdefault(text, n)
            prev_level = level
            continue

        body_words += len(plain(s).split())

        # back-references make the reader hold or hunt for earlier content (section 3)
        if BACKREF.search(uq):
            f['points back instead of repeating'].append((n, s[:72]))

        # emphasis is bold only (section 5)
        if ITALIC.search(raw_uq) or re.search(r'<(u|i|em)>', raw_uq.lower()):
            f['italics or underline for emphasis'].append((n, s[:72]))
        for cm in CAPS_RUN.finditer(uq.replace('ALL CAPS', 'all caps')):
            words = re.findall(r'[A-Z][A-Z0-9]+', cm.group(0))
            if any(w not in ACRONYMS for w in words):
                f['ALL CAPS run'].append((n, cm.group(0)[:60]))

        # numbered steps hold one action each (section 5)
        if re.match(r'^\d+[.)]\s', s):
            step = s.split(None, 1)[1] if len(s.split(None, 1)) > 1 else ''
            if STEP_CHAIN.search(unquoted(plain(step))):
                f['numbered step holds more than one action (warning)'].append((n, plain(step)[:60]))

        # status needs a word, never color alone (section 2, WCAG 1.4.1)
        cells = [c.strip() for c in s.strip('|').split('|')] if s.startswith('|') else [re.sub(r'^([-*]|\d+[.)])\s+', '', s)]
        for c in cells:
            if STATUS_EMOJI.search(c) and not re.search(r'[A-Za-z]{2,}', STATUS_EMOJI.sub('', c)):
                f['status shown by color alone'].append((n, c[:40]))

    # in a SKILL.md, an unescaped dollar sign before a digit is swapped out on load (section 7)
    if path.endswith('SKILL.md'):
        for n, ln in enumerate(lines, 1):
            for m in re.finditer(r'(?<!\\)\$\d', ln):
                f['unescaped dollar sign in a SKILL.md'].append((n, ln.strip()[:60]))

    # ---- page shape: headings, lists, bold, options, callouts, literal words, visuals ----
    # Wiki sidebars and footers (_Sidebar.md) are navigation, not reading, so they skip this part.
    nav_file = path.rsplit('/', 1)[-1].startswith('_')
    in_code, since_head, after_head, callouts, prev_callout = False, 0, False, 0, False
    list_items, list_start, list_numbered, prev2 = [], 0, False, ['', '']
    acr_seen = set()

    def close_list():
        if not list_items:
            return
        tops = [x for x in list_items if x[1] < 2]
        if len(list_items) == 1 and not list_numbered:
            f['list with one item (warning)'].append((list_start, tops[0][2][:50]))
        if list_numbered and len(tops) > MAX_STEPS:
            f['more than 7 numbered steps (warning)'].append((list_start, '%d steps' % len(tops)))
        if any(x[1] >= 4 for x in list_items):
            f['list nested more than one level (warning)'].append((list_start, ''))
        lead = ' '.join(prev2_at_start).lower()
        body = ' '.join(x[2] for x in list_items).lower()
        if 'option' in lead and len(tops) > MAX_OPTIONS and 'recommend' not in body + lead:
            f['more than 3 options with no recommendation (warning)'].append(
                (list_start, '%d options' % len(tops)))

    prev2_at_start = ['', '']
    for n, ln in enumerate(lines, 1):
        if n <= body_from or nav_file:
            continue
        s = ln.strip()
        if s.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'^(\s*)([-*]|\d+[.)])\s+(.*)$', ln)
        if m and s:
            numbered = m.group(2)[0].isdigit()
            if list_items and not m.group(1) and numbered != list_numbered:
                close_list(); list_items = []
            if not list_items:
                list_start, list_numbered, prev2_at_start = n, m.group(2)[0].isdigit(), prev2[:]
            list_items.append((n, len(m.group(1).expandtabs(4)), m.group(3)))
        elif s:
            close_list(); list_items = []
        if s:
            prev2 = [prev2[1], s]
        if not s:
            continue

        if s.startswith('#'):
            since_head, after_head = 0, True
            continue
        words = len(plain(s).split()) if not s.startswith('|') else 0
        since_head += words
        if since_head > HEADING_EVERY:
            f['over 300 words without a heading (warning)'].append((n, plain(s)[:50]))
            since_head = 0
        if after_head and not s.startswith(('|', '-', '*', '>', '<', '**Last updated')):
            if HEAD_OPENER.match(plain(s)):
                f['section opens by describing itself (warning)'].append((n, plain(s)[:60]))
            after_head = False

        # callouts: at most 2 per page, never 2 in a row
        is_callout = s.startswith('> [!')
        if is_callout:
            callouts += 1
            if prev_callout:
                f['two callouts in a row (warning)'].append((n, s[:40]))
        if not s.startswith('>'):
            prev_callout = False
        elif is_callout:
            prev_callout = True

        # bold: anchors, not decoration
        spans = re.findall(r'\*\*([^*]+)\*\*', unquoted(re.sub(r'`[^`]*`', ' ', ln)))
        bare = re.sub(r'^([-*]|\d+[.)])\s+', '', s)
        if re.match(r'^\*\*[^*]+\*\*[.:]?$', bare) and not s.startswith('|'):
            f['bold line used as a heading (warning)'].append((n, bare[:50]))
        elif len(spans) > 2 and not s.startswith('|'):
            f['more than 2 bold spans on a line (warning)'].append((n, plain(s)[:50]))
        for sp in spans:
            if len(sp.split()) > BOLD_MAX_WORDS:
                f['bold span over 8 words (warning)'].append((n, sp[:50]))

        if s.startswith(('|', '>')) or re.match(r'^([-*]|\d+[.)])\s', s):
            text = unquoted(plain(s))
        else:
            text = unquoted(plain(s))
            # prose that should be a list, a table or a visual
            if len(SEQ_WORDS.findall(text)) >= 2 and len(sentences(s)) >= 2:
                f['steps written as a paragraph (warning)'].append((n, plain(s)[:60]))
            if len(COND_START.findall(text)) >= 2:
                f['conditions written as a paragraph (warning)'].append((n, plain(s)[:60]))
            if re.search(r'\b(vs\.?|versus|compared (to|with))\b', text, re.I):
                f['comparison in prose: try a table (suggestion)'].append((n, plain(s)[:60]))
            if len(DATE.findall(text)) >= 3:
                f['3 or more dates in prose: try a timeline (suggestion)'].append((n, plain(s)[:60]))
            if len(set(w.lower() for w in STATUS_WORDS.findall(text))) >= 3:
                f['statuses in prose: try a status table (suggestion)'].append((n, plain(s)[:60]))

        # literal words (section 3)
        low = text.lower()
        for idiom in IDIOMS:
            if re.search(r'\b%s\b' % re.escape(idiom), low):
                f['idiom: say it literally (suggestion)'].append((n, '"%s"' % idiom))
        if DOUBLE_NEG.search(text):
            f['double negative (suggestion)'].append((n, DOUBLE_NEG.search(text).group(0)))
        if VAGUE_TIME.search(text):
            f['vague time: give a date (suggestion)'].append((n, VAGUE_TIME.search(text).group(0)))
        if VAGUE_LINK.search(ln):
            f['link text says nothing (warning)'].append((n, VAGUE_LINK.search(ln).group(0)[:30]))
        for acr in ([] if '[!' in s else re.findall(r'\b[A-Z]{2,6}s?\b', text.replace('ALL CAPS', 'all caps'))):
            base = acr.rstrip('s') if acr.endswith('s') and acr[:-1].isupper() else acr
            if base in ACRONYMS or base in acr_seen or base == 'CODE':
                continue
            acr_seen.add(base)
            if not re.search(r'\(%s\)|%s\s*\(' % (re.escape(base), re.escape(base)), ln):
                f['acronym not spelled out on first use (suggestion)'].append((n, base))
    if not nav_file:
        close_list()
    if callouts > MAX_CALLOUTS:
        f['more than 2 callouts on the page (warning)'].append((0, '%d callouts' % callouts))

    # pages over SUMMARY_FROM_WORDS open with a short summary under the title (section 7)
    if first_h1 is not None and body_words >= SUMMARY_FROM_WORDS:
        j = first_h1
        while j < len(lines) and (not lines[j].strip() or lines[j].strip().startswith('**Last updated')):
            j += 1
        blk, blk_start = [], j + 1
        while j < len(lines) and lines[j].strip() and not lines[j].strip().startswith('#'):
            blk.append(lines[j].strip()); j += 1
        items = [b for b in blk if re.match(r'^([-*]|\d+[.)])\s', b)]
        text = ' '.join(blk)
        if not blk:
            f['no summary under the title'].append((first_h1, 'a heading follows the title directly'))
        elif OPENER.match(plain(text)):
            f['summary describes the page instead of saying the point'].append((blk_start, plain(text)[:60]))
        elif (items and len(items) > 5) or (not items and len(sentences(text)) > 3):
            f['summary under the title is too long'].append((blk_start, plain(text)[:60]))

    # Bullet parallelism is NOT checked here on purpose. Telling a gerund acting as a
    # noun ("Over-apologizing") from a gerund acting as an instruction ("Putting a
    # requirement and a design choice in one bullet") needs a part-of-speech judgment this
    # script cannot make, and a check that cries wolf teaches people to ignore the script.
    # It lives in the review checklist in section 11 instead.

    print('=== %s ===' % path)
    if not f:
        print('  clean')
    for k in sorted(f, key=lambda k: ('(warning)' in k, '(suggestion)' in k, k)):
        print('  [%s] %d' % (k, len(f[k])))
        for n, d in f[k][:10]:
            print('      line %d: %s' % (n, d))
    return sum(len(v) for k, v in f.items() if '(warning)' not in k and '(suggestion)' not in k)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(1 if sum(check(p) for p in sys.argv[1:]) else 0)
