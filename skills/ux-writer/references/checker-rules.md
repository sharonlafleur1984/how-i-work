# Checker rules

Part of the `ux-writer` skill, section 11. Everything `scripts/check.py` flags, by level. The script is the source of truth; update this list when the script changes.

## Errors fail the run (exit code 1)

- Em dashes, en dashes, stray exclamation marks and emoji
- The cut-on-sight words, and the language in section 4
- Headings and table column headers that point instead of naming a subject
- Headings that are a count rather than a subject
- Bullets carrying a colon of their own, or holding more than one idea
- Fragment colon stems whose bullets do not finish the sentence
- Sentences over 34 words, and a sentence that appears in two places
- Paragraphs over about 60 words or 5 sentences
- Pages over 300 words with no short summary under the title
- Back-references like "as mentioned above"
- Italics, underline and runs of ALL CAPS
- Headings out of order, a second H1, or duplicate headings
- Status shown by color alone
- In a SKILL.md, a dollar sign that is not escaped

## Warnings need an outcome but don't fail the run

- Sentences over 25 words, and paragraphs over 50 words
- Numbered steps that chain actions with "then"
- 300 words without a heading, and a section that opens by describing itself
- Steps or conditions written as a paragraph
- Lists with one item, more than 7 steps, or two levels of nesting
- Bold used as a heading, more than 2 bold spans on a line, or a bold span over 8 words
- More than 3 options with no recommendation
- More than 2 callouts on a page, or 2 in a row
- Link text like "click here"

## Suggestions are worth a look and misfire more often

- Idioms, double negatives, and "soon" instead of a date
- Acronyms not spelled out on first use
- A comparison, 3 or more dates, or 3 or more statuses written in prose, where a table or timeline may work better
