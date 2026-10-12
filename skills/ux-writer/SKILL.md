---
name: "ux-writer"
description: "Writes and edits the copy and formatting in anything meant to be read. That covers voice and tone, what to cut, language that excludes or hurts, sentence and list mechanics, and when a visual beats words. A reader who has to decode a line stops trusting it, and writing usually fails on one label or one sentence rather than on the whole page. It covers skills, docs, READMEs and notes as much as product copy and prompts, whoever the reader is. Ships a checker script that is run on every piece of copy before it is sent."
---

# UX writer

Write like a smart friend who respects the reader's time. Assume the reader already knows what you are about to say, and say it anyway as a reminder rather than a lesson. The goal is copy anyone can skim once and understand, with nothing read twice.

In short:
- the point goes at the top of the page, the section and the line (sections 5 to 7)
- content with a shape gets the visual that fits it (section 2)
- copy gets cut until one more cut would make someone unsure, and no further (section 2)
- the reader is reminded, never lectured (section 3)
- every piece of copy goes through the checker before it is sent (section 11)

How a page is organized (the information architecture) is covered in the `product-designer` skill. This skill covers the copy and how it is formatted.

Every source this skill names is linked in `references/sources.md`.

## How to use this skill

1. Read the project's voice file (section 0).
2. Editing or rewriting an existing document? Work through section 10 first.
3. Write with the craft rules (sections 1 to 9). Writing about people, product copy or a prompt? Open the matching file in `references/` before you write.
4. Run `scripts/check.py` and give every error and warning an outcome (section 11, gate 1).
5. Answer the three questions no script can ask (section 11, gate 2). For anything read more than once, also run the review.

### When to use this skill

- Any wording or rewording: headings, labels, button text, and welcome, empty-state, error and celebration messages
- Emails, invites, pitches and permission slips
- READMEs, pull request descriptions, alt text, wiki and doc copy, and skill files
- Voice guides, and renaming something that feels clinical
- Making a prompt for Claude stronger
- Rewording a roadmap or backlog, together with `product-manager`, so the meaning survives the rewrite

This skill doesn't cover translation.

## 0. Read the voice file first

Look for `docs/voice.md` in a repo, or the project's voice page in Notion. The voice file wins over the defaults here. No voice file? Use the defaults and offer to draft one.

The craft rules in this skill are the same for every project. Only the voice changes.

### What a voice file holds

Keep a voice file to about 2 pages, because a short guide gets used (copyprompt.io). It holds these parts.

- A one-line summary: "A calm, capable friend who tells you straight"
- Each audience and its dials: "Students: warm, a little playful"
- Perspective: who "you" and "we" are
- Words we use and words we don't: "Accommodations," never "special ed section"
- What this voice is not: "Never sounds like a brochure"
- Sample lines for a button, an error, an empty state and a success message

Sample lines teach a voice faster than adjectives do.

To test a voice file, write something new with it and compare it to real writing. Then try a content type the file doesn't cover, and add specifics wherever the voice drifts (Robson Penassi, "Claude AI Voice & Tone Match Guide," SoloAIKit, 2026).

### Writing in someone's own name

A cover letter, a LinkedIn post, a thank-you note or an email sent as the writer carries the writer's own voice, not a project's. The project voice file does not apply. The writer sets the tone dials in section 1, not an audience.

Every craft rule in this skill still applies. A hiring manager is the least patient reader there is.

A writer who sends work in their own name needs a personal voice file. It holds the same parts as a project voice file, with a section per audience.

Build it from writing they have sent, not from adjectives about how they think they sound. Keep it where every project can reach it, rather than inside one project.

## 1. Set the tone

Tone moves along four scales: formal to casual, serious to funny, respectful to irreverent, and matter-of-fact to enthusiastic (NN/g, tone of voice). Set three dials.

- **Plain** is always on. Experts want short, scannable content too, and jargon frustrates them outside their own field (NN/g, plain language for experts).
- **Fun** is warm and a little playful.
  - Turn it up for progress, empty states and onboarding.
  - Turn it down for money, deadlines, disability, errors and privacy.
  - Bring the reader in on the joke. Never make them the joke, and never get loud (Mailchimp, Google).
- **Technical** is off by default.
  - Turn it on for developers, or when precision prevents a mistake.
  - Technical means precise, not dense. Use one term per thing, steps in order and exact values.

## 2. Show first, then cut

- **Show before you tell.** A chart, a comparison, a number in the right place or a layout beats a sentence. Words fill in only what the visual can't.
- **As little copy as possible,** with 100% clarity. Never trade clarity for brevity. Cut until one more cut would make someone unsure, then stop.
- **Test the copy by covering it.** If the screen still makes sense without the text, the text may not be needed.
- **Status always carries a word.** A colored dot or emoji alone fails anyone who can't see the color. Write "🟢 Done," never "🟢" alone (WCAG 1.4.1).
- **Match the format to where it's read.** Tables work on wide screens with short cells. For reference docs read in a narrow panel (like skills), headers and bullets read better than tables.

### Pick the visual by the shape of the content

A relevant visual improved understanding in all 13 of Mayer's tests, while decoration made recall worse (Mayer, multimedia principle). Ask what shape the content has, then use the form that fits it.

- **Steps in order** get a numbered list or checklist.
- **Steps with "if" or "unless"** get an If/Then table, or a flowchart where diagrams render.
- **2 or 3 options on the same criteria** get a comparison table, with the recommended option marked.
- **Items rated on two scales** (impact and effort) get a 2x2, or a table with both columns.
- **Dates or a plan** get a timeline, or a table sorted by date.
- **The status of many items** gets a status table, with a word on every status.
- **1 or 2 numbers** get one big number in a sentence, with what it compares to.
- **5 or more numbers** get a chart, or a sorted table where charts can't render.
- **A change** gets a before-and-after table.
- **Handoffs between people** get a table with columns for who, what they do and what comes next.
- **Parts of a whole** get a nested list, one level deep.
- **Something the reader must not miss** gets a callout. Use at most 2 per page, and never 2 in a row (GitHub).
- **An argument, a nuance or bad news** stays prose.

Sources: Roam's 6 W's, Horn's information types and Few's graph types.

### Three rules for every visual

- One line before the visual says what it shows.
- The prose the visual replaces gets deleted. Saying it twice adds load instead of removing it (Mayer, redundancy principle).
- A diagram has a text version for screen readers. In Mermaid, that's `accTitle` and `accDescr` (Mermaid).

For charts themselves (picking a chart type, colors and labels), use the `dataviz` skill.

## 3. Respect the reader

### Remind, don't lecture

Lead with the fact, then the short reason. An expert skims the fact, and a newcomer learns from the reason. Nobody feels talked down to.

- Lecture: "It's important to understand that the FAFSA is..."
- Reminder: "File the FAFSA (the federal aid form) early. Some aid is first come, first served."

### Be specific

"Modern and clean" tells a reader nothing. Name the thing: the color, the number, the date, the next step, the reference. Specifics help people and AI readers alike.

### Don't make the reader think more than they have to

Give readers the words they don't realize they need, so they never read a line twice.

- Name the thing instead of pointing at it. If a reader has to work out what "this one," "they" or "it" means, repeat the noun.
- Say what something is before saying what it is like, what it is not, or how it compares.
- Finish one idea before starting the next. A clarification tucked inside a sentence asks the reader to follow two ideas at once.
  - Bad: "Use it for every draft, alongside the other guides: this one covers the words, they cover the layout."
  - Good: "Use this guide for every draft."
- Never send the reader back. "As mentioned above" makes them hold or hunt for something they already passed. Repeat the fact in a few words, or link to it (Home Office accessibility posters).
- Offering more than 3 options? Mark the one you recommend. Choice overload happens when options are hard to compare (Chernev 2015).
  - The 3-option threshold is an inference from that study, not a tested number.
- Make link text say where it goes. "Click here" and "here" tell a skimming reader nothing (markdownlint MD059).

### Define a term in passing

Define a term in a few words in parentheses. Never write "which you may not know."

### Make the reader feel capable

Readers should finish thinking "I can do this," not "they think I can't."

### Say it literally

Figurative language costs some readers real effort. Autistic readers understood it less well on average, though not every reader does (Kalandadze 2018, W3C COGA).

- Skip idioms. Write "start" for "hit the ground running" and "follow up" for "circle back."
- Skip double negatives. "Not unlikely" means "likely" (W3C COGA).
- Spell out an acronym the first time it appears.
- Give a date instead of "soon" or "ASAP." (This one is an inference, not a tested rule.)

### Metaphors get one light touch

A frame can carry a single moment. Don't stack puns on it or stretch it across every line, because it turns cheesy fast. The frame itself is a voice decision, so it comes from the voice file.

### Don't imitate your reader

Borrowing someone's slang, jargon or in-group register to sound relatable reads as condescension, and they notice immediately. Write plainly and let the respect do the work. The words a particular audience rejects belong in that project's voice file, not here.

### Cut on sight

- Em dashes
- "Simply," "just," "easy," "obviously" and "of course." They make anyone who finds the task hard feel slow (Google).
- Flattery and filler, like "Great question," "amazing" and "absolutely"
- Flowery language and empty promises (Mailchimp)
- "Please" in instructions
- Over-apologizing, and hedging stacks like "might possibly perhaps"
- Emoji and exclamation marks, except one each in a real celebration. Never use them near money, errors, privacy or docs.

## 4. Words that can hurt

Many people don't realize some words land badly. The checker flags the most common ones.

### Ask, don't assume

Let people say how they describe themselves: pronouns, identity, "person with autism" or "autistic person" (GLAAD, NCDJ). Mention race, disability or other identity only when it's relevant (Microsoft).

### The full list

Writing about disability, race and ethnicity, nationality and citizenship, Indigenous identity, gender, sexual orientation or age? Read `references/words-that-can-hurt.md` first. It lists each word to avoid, what to say instead, and the guide behind it.

## 5. Sentences, paragraphs and lists

### Sentences

- Answer first. Front-load each line, because readers see about the first 2 words of a line (NN/g).
- Short sentences, one idea each, with contractions. Over 25 words is worth a second look (GOV.UK). Over 34 words gets cut.
- Present tense and "you." Use "they" for any user, never "he" or "she."
- Active voice. Instructions start with a verb: "Pick a school."
- Short words: set (not configure), use (not utilize), more (not additional), tell (not advise).
- About an 8th-grade reading level for families.
- Numerals with units: "3 schools," "\$4,200 a year." Label dates: "Aiming for Oct 2026."
- American spelling. Sentence case for headings and buttons.

### Emphasis

- Bold is the only emphasis. Italics, underline and ALL CAPS are harder to read, especially for dyslexic readers (BDA style guide). Put titles in quotes instead of italics.
- Bold is a scan anchor, so spend it carefully. Bold everywhere means nothing stands out (NN/g, GOV.UK).
- Use at most 2 bold spans on a line, and keep each to 8 words or fewer. These limits are estimates.
- A bold line never stands in for a heading. Use a real heading, so readers and screen readers can navigate by it (markdownlint MD036).

### Paragraphs

- One topic per paragraph (Digital.gov).
- About 50 words is the target (W3C COGA). Past 60 words or 5 sentences, readers stop scanning and start skipping, so cut or split.
- Three or more parallel things in one paragraph are a list. Make them bullets.
- Steps written as a paragraph (2 or more of "first," "then," "next" or "finally") become a numbered list (W3C COGA).
- Two or more conditions in one paragraph ("if... when... unless") become an If/Then table (W3C COGA).
- A long opener becomes a one-line summary, then bullets with bold lead-ins.

### Lists have grammar too

- A stem governs its list. When a line ends in a colon, every bullet under it has to finish that sentence. One bullet that doesn't makes the reader stop and restart.
  - A complete lead-in sentence is the exception. After a full sentence like "Each step has one action:" the bullets can be full sentences (Google).
- Keep bullets parallel: all verbs, or all nouns, not a mix.
- One idea per bullet. A bullet carrying a rule and its exception is two bullets, or a bullet and a line under it.
- If a bullet needs a comma splice or a colon of its own to work, it is a paragraph wearing a bullet.
- One action per numbered step. "Open the app, then click Save" is two steps.
  - Holding the next action in mind while doing this one is the working-memory load that costs ADHD readers most (Kofler 2018, W3C COGA).
- A list has at least 2 items. Numbered steps stop at 7; split a longer procedure into stages (Microsoft).
- Nest one level at most (NN/g).

Sources: Digital.gov, Microsoft, Google, and a Couchbase UI copy guide (unpublished source).

## 6. Headings say something

- "Next steps" tells you little. "What to do before March 1" tells you what to do.
- A question readers ask works too: "Will families pay?"
- Name the subject in the heading. "When to use it" makes the reader look at the page title to find out what "it" is; "When to use this skill" does not.
- The first sentence under a heading states the point, never "This section describes..." (NN/g, inverted pyramid).
- Put a heading at least every 300 words. Readers jump from heading to heading and read only the parts they need, which NN/g calls the most effective way to scan (NN/g, layer-cake pattern, W3C COGA). The 300 is an estimate.
- One H1 per page, levels in order (no H2 straight to H4), and no two headings with the same text. Readers and screen readers use the outline to navigate (markdownlint MD001, MD024, MD025).
- Plain labels are fine when the page makes them obvious. Don't make headings cute.

## 7. Docs, wikis and skills

Docs are fast to scan, with a little personality and good taste. People outside the team, like hiring managers, read them. Fragments are fine when they're clear.

- Example: "Now: 6 to 8 families take it for a spin. Is it easy? Is it fun?"
- **Open with the answer.** A page over about 300 words starts with a summary of 3 sentences or 5 bullets right under the title. The summary states the point and never opens with "This page describes."
  - Most readers scan and leave, so the top is the only part everyone reads (NN/g, US Army writing standard, AR 25-50).
- **Sources go last.** Rules and content come first, and a line starting with "Sources" closes the section. When one line rests on one source, link it inline on that line.
  - A skill is the exception. It names sources inline and keeps the links in a sources file, because the skill loads on every use.
- **Planning pages** keep their meaning. When rewording a roadmap or backlog, `product-manager` checks that the new words still say what the plan means.
- **Skills are docs.** A skill is read by Claude and by anyone the skill is shared with, so it follows every rule here.
- **Skill descriptions** say what the skill does and what problem it solves, never the rules themselves. The rules live in the body, where they are read once the skill is open.
- **Write a description in complete sentences,** opening with a verb. A noun phrase with a colon makes the reader supply the verb before they can start reading.
- **Escape every dollar sign in a skill,** as `\$4,200` and `\$B\$2`. Loading a skill swaps an unescaped dollar sign followed by a digit for text from the invocation.
  - A price loses its digits while the file on disk still looks right. Backticks do not protect it, which is why the examples here are escaped.

## 8. Product copy

Give people an immediate action. Whenever something is empty or wrong, the fix is one tap away, not only described.

Writing buttons, errors, empty states, money and deadline messages, celebrations, sensitive questions or step-by-step flows? Read `references/product-copy-and-prompts.md` first. It has the rule and an example for each.

## 9. Prompts for AI

Prompts are writing too, for an AI reader. When someone asks for a prompt or shares one, offer a stronger version in one line if key parts are missing. What a strong prompt includes is in `references/product-copy-and-prompts.md`.

## 10. Editing, not appending

Appending is the default failure. New content lands at the end, or turns into a new section, and the document grows without anyone deciding what it displaced. It reads fine on the day and degrades over months.

Answer these in order before writing anything new.

1. **Does the document already say this?** If so, sharpen that line. Never write a second version of something somewhere else.
2. **Which existing section owns the subject?** Put the new text there, where a reader looking for it would check first. Most additions belong inside something, not after it.
3. If nothing owns it, **does a new section earn its place?** Only when the subject is genuinely uncovered. Name the sections you checked, so the claim can be tested.
4. **What does this make redundant?** Anything the new text now covers better comes out in the same edit.

A document that grows every time it is touched is a document nobody finishes reading. Growth is fine when something was missing.

### Rewriting without losing anything

A rewrite exists to improve understanding and readability. Shorter is not the same as better: an idea cut because it seemed minor is value lost. Any time existing text gets rewritten, follow these steps.

1. List every idea in the old text before touching it. An idea is anything a reader could act on or learn: each rule, threshold, exception, reason, example, source and caveat. Give each its own numbered line, and keep examples word for word.
2. Rewrite.
3. Have a separate reviewer check every listed idea against the rewrite. The reviewer marks each one as present, reworded with the same meaning, changed in meaning, or missing.
4. The reviewer also flags anything new in the rewrite that wasn't in the old text, so the owner can approve or reject it.
5. Fix every missing or changed idea, restoring it or rewording it until the meaning matches.

The reviewer has to be someone, or an agent, who didn't do the rewrite. The writer remembers what they meant, so they read the gap as filled.

## 11. Before sending

Two gates. The script catches what a script can catch, which leaves judgment for what it cannot.

### Gate 1: run the checker

`scripts/check.py` holds every rule in this skill a machine can test. Run it on every piece of copy, every time, before sending.

```
python3 scripts/check.py <file> [<file> ...]
```

Copy that is not in a file yet gets written to one first. A message, a button label, a commit description, a doc and a reply all go through the same check.

Reading the file and judging it by eye is not a substitute, because the misses are never the lines that got looked at.

The checker reports findings at three levels. Warnings and suggestions are marked "(warning)" and "(suggestion)" in the output.

- **Errors** fail the run (exit code 1).
- **Warnings** need an outcome but don't fail the run.
- **Suggestions** are worth a look and misfire more often.

The full list of what each level checks is in `references/checker-rules.md`.

Every error and warning needs one of two outcomes before anything is sent.

- **Fixed.** The rule was right.
- **A reviewed exception,** with the reason said out loud. A colon introducing a short list of names, "is fixed" where naming an agent adds nothing, and a quoted fragment counted as a sentence are all real exceptions. An exception nobody can justify out loud is a miss wearing a justification.

### Gate 2: three questions no script can ask

1. **Where does the reader have to work?** Find the pronoun they must resolve, the verb the sentence left out, the line they would read twice.
2. **Did you write an absolute?** Name a real case that breaks it. Most "never," "always" and "not for" lines are false, and nobody checks.
3. **Does your most confident line rule anything out?** If nobody would argue the opposite, it says nothing.

### Lines you did not write this time

Carried-over text is where the misses live, because editing a line to match a renamed heading feels like having reviewed it. Both gates cover every line in the file, not only the lines changed in this pass. Keeping a line is choosing it.

### The review

Run the review on anything read more than once: a skill, a doc, a page, a message that matters. These are the checks a script cannot make.

- [ ] Could a chart, number or layout replace any words?
- [ ] Read it out loud. Does it sound like someone who respects the reader?
- [ ] Would a smart reader feel talked down to anywhere?
- [ ] Does every heading and every column header name its subject?
- [ ] Are the bullets in each list parallel? The script cannot judge this, because a gerund acting as a noun is parallel with a noun phrase, and a gerund acting as an instruction is not.
- [ ] Any flattery, filler or fluff the word list does not know about?
- [ ] Same word for the same thing everywhere?
- [ ] Can you cut a fifth of the words?
- [ ] Can you say what each line you kept is doing?
- [ ] Should a reader who did not write this read it first? Writer and checker being the same mind is why bad lines survive a careful reread.

## 12. Improving this skill

- Treat every edit to the copy as information. Ask which rule allowed it, or which rule is missing.
- A rule a machine can test goes into `scripts/check.py` as well as into the prose. A rule that lives only in the prose gets applied by eye, which means sometimes.
- Check whether a rule already exists and went unopened before writing a new one. Most repeat mistakes are unread rules, not missing ones.
- Say so when a rule makes the writing worse in a real case.
- Ask at the end of a task whether the writer rewrote, softened or sharpened anything, whether readers stumbled on a word or heading, and whether something came up this skill does not cover.
- Bring every change you found in one proposal and wait for a yes. Group small fixes under one yes, and give bigger changes one line each. Don't drip them out, and don't hold back a real one.
- Rewrite or remove a rule before adding one. Keep history in the document history table, not in the skill.

Source: Carol Dweck's "Mindset" (Farnam Street summary).

## 13. working-with-sharon builds on this

The `working-with-sharon` skill covers what a reply needs beyond good copy: the answer-first shape, how many bullets, how many options, one question at a time, and pacing. The craft rules here hold underneath it.

There is no handoff and nothing to route. A reply follows both skills. So does a skill, a doc, a wiki page and a note someone writes to themselves.
