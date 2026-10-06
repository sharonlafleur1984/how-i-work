---
name: "ux-writer"
description: "Writes and edits the copy in anything meant to be read: voice and tone, what to cut, language that excludes or hurts, and sentence and list mechanics. A reader who has to decode a line stops trusting it, and writing usually fails on one label or one sentence rather than on the whole page. It covers skills, docs, READMEs and notes as much as product copy and prompts, whoever the reader is. Ships a checker script that is run on every piece of copy before it is sent."
---

# UX writer

Write like a smart friend who respects the reader's time. Assume the reader already knows what you are about to say, and say it anyway as a reminder rather than a lesson.

How a page is organized (the information architecture) is covered in the product-designer skill. This skill covers the copy.

## When to use this skill

**Use it for:**
- Any wording or rewording: headings, labels, button text, and welcome, empty-state, error and celebration messages
- Emails, invites, pitches and permission slips
- READMEs, pull request descriptions, alt text, wiki and doc copy, and skill files
- Voice guides, and renaming something that feels clinical
- Making a prompt for Claude stronger
- With `product-manager` when rewording a roadmap or backlog, so the meaning survives the rewrite

**Not for** translation.

## 0. Read the voice file first

Look for `docs/voice.md` in a repo, or the project's voice page in Notion. It wins over the defaults here. No voice file? Use the defaults and offer to draft one.

The craft rules in this skill are the same for every project. Only the voice changes.

**What a voice file holds.** Keep it to about 2 pages; a short guide gets used ([copyprompt.io](https://copyprompt.io/blog/ai-prompts-for-designers-2026)).
- A one-line summary: "A calm, capable friend who tells you straight"
- Each audience and its dials: "Students: warm, a little playful"
- Perspective: who "you" and "we" are
- Words we use and words we don't: "Accommodations," never "special ed section"
- What this voice is not: "Never sounds like a brochure"
- Sample lines for a button, an error, an empty state and a success message

Sample lines teach a voice faster than adjectives do. To test a voice file, write something new with it and compare it to real writing, then try a content type it doesn't cover. Add specifics wherever it drifts (Robson Penassi, "Claude AI Voice & Tone Match Guide," SoloAIKit, 2026).

**Writing in someone's own name uses their own voice, not a project's.** A cover letter, a LinkedIn post, a thank-you note or an email sent as themselves carries the writer's voice. The project voice file does not apply, and the writer sets the dials in section 1, not an audience. Every craft rule in this skill still applies, and a hiring manager is the least patient reader there is.

A writer who sends work in their own name needs a voice file of their own, holding the same things listed above with a section per audience. Build it from writing they have sent, not from adjectives about how they think they sound. Keep it where every project can reach it, rather than inside one of them.

## 1. Set the tone

Tone moves along formal to casual, serious to funny, respectful to irreverent, and matter-of-fact to enthusiastic ([NN/g, tone of voice](https://www.nngroup.com/articles/tone-of-voice-dimensions/)).

- **Plain: always on.** Experts want short, scannable content too, and jargon frustrates them outside their own field ([NN/g, plain language for experts](https://www.nngroup.com/articles/plain-language-experts/)).
- **Fun: warm and a little playful.**
  - Turn it up for progress, empty states and onboarding.
  - Turn it down for money, deadlines, disability, errors and privacy.
  - Bring the reader in on the joke; never make them the joke, and never get loud ([Mailchimp](https://styleguide.mailchimp.com/voice-and-tone/), [Google](https://developers.google.com/style/tone)).
- **Technical: off by default.**
  - Turn it on for developers, or when precision prevents a mistake.
  - Technical means precise, not dense. One term per thing, steps in order, exact values.

## 2. Show first, then cut

- **Show before you tell.** A chart, a comparison, a number in the right place or a layout beats a sentence. Words fill in only what the visual can't.
- **As little copy as possible, with 100% clarity.** Never trade clarity for brevity. Cut until one more cut would make someone unsure, then stop.
- **Test the copy:** cover the text. If the screen still makes sense, the text may not be needed.
- **Match the format to where it's read.** Tables work on wide screens with short cells. For reference docs read in a narrow panel (like skills), headers and bullets read better than tables.

## 3. Respect the reader

**Remind, don't lecture.** Lead with the fact, then the short reason. An expert skims the fact; a newcomer learns from the reason. Nobody feels talked down to.
- Lecture: "It's important to understand that the FAFSA is..."
- Reminder: "File the FAFSA (the federal aid form) early. Some aid is first come, first served."

**Be specific.** "Modern and clean" tells a reader nothing. Name the thing: the color, the number, the date, the next step, the reference. This holds for people and for AI readers alike.

**Don't make the reader think more than they have to.** Give them the words they don't realize they need, so they never read a line twice.
- Name the thing instead of pointing at it. If a reader has to work out what "this one," "they" or "it" means, repeat the noun.
- Say what something is before saying what it is like, what it is not, or how it compares.
- Finish one idea before starting the next. A clarification tucked inside a sentence asks the reader to follow two at once.
- Bad: "Use it for every draft, alongside the other guides: this one covers the words, they cover the layout."
- Good: "Use this guide for every draft."

**Define a term in passing,** in a few words in parentheses. Never "which you may not know."

**Make the reader feel capable.** They should finish thinking "I can do this," not "they think I can't."

**Don't imitate your reader.** Borrowing someone's slang, jargon or in-group register to sound relatable reads as condescension, and they clock it immediately. Write plainly and let the respect do the work. Which words a particular audience rejects belongs in that project's voice file, not here.

**Metaphors get one light touch.** A frame can carry a single moment. Don't stack puns on it or stretch it across every line, because it turns cheesy fast. The frame itself is a voice decision, so it comes from the voice file.

**Cut on sight:**
- Em dashes
- "Simply," "just," "easy," "obviously," "of course": they make anyone who finds it hard feel slow ([Google](https://developers.google.com/style/tone))
- Flattery and filler: "Great question," "amazing," "absolutely"
- Flowery language and empty promises ([Mailchimp](https://styleguide.mailchimp.com/voice-and-tone/))
- "Please" in instructions
- Over-apologizing and hedging stacks ("might possibly perhaps")
- Emoji and exclamation marks, except one each in a real celebration. Never near money, errors, privacy or docs.

## 4. Words that can hurt

Many people don't realize these land badly. The name in parentheses is the guide each line comes from; links are at the end of this section.

**Ask, don't assume.** Let people say how they describe themselves: pronouns, identity, "person with autism" or "autistic person" (GLAAD, NCDJ). Mention race, disability or other identity only when it's relevant (Microsoft).

**Disability**
- Not "crazy," "insane," "dumb," "lame" or "sanity check." Say confusing, unclear, quick check (Google).
- Not "special needs." Name the need or the accommodation (NCDJ).
- Not "suffers from," "wheelchair-bound" or "handicapped." Say has, uses a wheelchair, disabled (NCDJ).
- Not "blind to" or "fell on deaf ears." Say unaware of, ignored (Google, UW).
- Name sensitive things the way people would name them: "Accommodations," not "special ed section" or "disability mode."

**Race and ethnicity**
- Not "non-white." Name the specific group (UW).
- Not "Caucasian." Say white (UW).
- Not "blacklist/whitelist" or "master/slave." Say blocklist/allowlist, primary/replica (Google).
- "Diverse" describes groups, never one person (UW).

**Nationality and citizenship**
- Not "illegal" or "alien" for people. Say undocumented, and only when it's relevant (UW).
- Not "citizens" when you mean everyone. Say residents (UW).

**Indigenous identity**
- Not "tribe," "spirit animal" or "totem pole" as metaphors. Say team, favorite, ranking (UW, Microsoft).

**Gender and sexual orientation**
- Not "guys" for a group, "he" as the default, "mankind" or "manpower." Say everyone, they, people, staff (UW, Microsoft).
- Not "husband or wife" or "mother or father" when you don't know. Say spouse or partner, parent or guardian (UW).
- Not "sexual preference." Say sexual orientation (UW).

**Age**
- Not "the elderly." Say older adults (Google).

Sources: [Google](https://developers.google.com/style/inclusive-documentation), [Microsoft](https://learn.microsoft.com/en-us/style-guide/bias-free-communication), [NCDJ](https://cronkite.asu.edu/ncdj/disability-language-style-guide), [University of Washington (UW)](https://www.washington.edu/brand/guides/equitable-language-guide/), [GLAAD](https://glaad.org/reference/).

## 5. Sentences and lists

- Answer first. Front-load each line.
- Short sentences, one idea each. Contractions.
- Present tense and "you." "They" for any user, never "he" or "she."
- Active voice. Instructions start with a verb: "Pick a school."
- Short words: set (not configure), use (not utilize), more (not additional), tell (not advise).
- About an 8th-grade reading level for families.
- Numerals with units: "3 schools," "\$4,200 a year." Label dates: "Aiming for Oct 2026."
- American spelling. Sentence case for headings and buttons.

**Lists have grammar too.**
- A stem governs its list. When a line ends in a colon, every bullet under it has to finish that sentence. One bullet that doesn't makes the reader stop and restart.
- Keep bullets parallel: all verbs, or all nouns, not a mix.
- One idea per bullet. A bullet carrying a rule and its exception is two bullets, or a bullet and a line under it.
- If a bullet needs a comma splice or a colon of its own to work, it is a paragraph wearing a bullet.

Sources: [Digital.gov](https://digital.gov/guides/plain-language/principles), [Microsoft](https://learn.microsoft.com/en-us/style-guide/brand-voice-above-all-simple-human), [Google](https://developers.google.com/style/tone), and a Couchbase UI copy guide (unpublished source).

## 6. Headings say something

- "Next steps" tells you little. "What to do before March 1" tells you what to do.
- A question readers ask works too: "Will families pay?"
- Name the subject in the heading. "When to use it" makes the reader look at the page title to find out what "it" is; "When to use this skill" does not.
- Plain labels are fine when the page makes them obvious. Don't make headings cute.

## 7. Docs, wikis and skills

Fast to scan, a little personality, good taste. People outside the team, like hiring managers, read these. Fragments are fine when they're clear.

- Example: "Now: 6 to 8 families take it for a spin. Is it easy? Is it fun?"
- **Sources go last.** Rules and content come first; a "Sources:" line closes the section. When one line rests on one source, link it inline on that line.
- **Planning pages:** when rewording a roadmap or backlog, `product-manager` checks that the new words still say what the plan means.
- **Skills are docs.** A skill is read by Claude and by anyone the skill is shared with, so it follows every rule here.
- **A skill description says what the skill does and what problem it solves,** never the rules themselves. The rules live in the body, where they are read once the skill is open.
- **Write a description in complete sentences,** opening with a verb. A noun phrase with a colon makes the reader supply the verb before they can start reading.
- **Escape every dollar sign in a skill,** as `\$4,200` and `\$B\$2`. Loading a skill swaps an unescaped dollar sign followed by a digit for text from the invocation, so a price loses its digits while the file on disk still looks right. Backticks do not protect it, which is why the examples here are escaped.

## 8. Product copy

**Give people an immediate action.** Whenever something is empty or wrong, the fix is one tap away, not only described.

- **Buttons:** verb first, say what happens. "Add school," not "Submit."
- **Errors:** what happened, the fix, and a button that does the fix. No blame, no jokes.
  - "That date's in the past." [Pick a new date]
- **Empty states:** what goes here, and a button to start ([NN/g, empty states](https://www.nngroup.com/articles/empty-state-interface-design/)). A little fun is welcome.
  - "No schools yet." [Add a school]
- **Money and deadlines:** calm and practical. The fact, then the next step.
  - "State U costs about \$4,200 a year more than your aid covers. Here are 3 scholarships that could close the gap."
- **Celebrations:** earned, short and a little playful. Mark real progress, not every click.
  - "Junior year: done. 🎉 Go ahead, take a victory lap. Senior year can wait five minutes."
- **Sensitive questions:** say why you're asking in one line, and offer "Prefer not to say."
- **When to add words:** only when a newer user would struggle or the next step isn't obvious. Longer explanations go in help or docs. Say what people can do, not what they can't.

**Step-by-step flows** (onboarding, setup):
- One question per step, the way a helpful person would ask it
- Use earlier answers: "Since you're open to other states..."
- Signpost: "Last question"
- Remember answers; never ask twice
- Don't get chatty: "That's a great choice! Now let me just..." wastes their time
- Don't go step by step where people need to compare everything at once, like schools

Sources: [NN/g, empty states](https://www.nngroup.com/articles/empty-state-interface-design/), a Couchbase UI copy guide and a conversational UI article (both unpublished sources).

## 9. Prompts for AI

Prompts are writing too, for an AI reader. When someone asks for a prompt or shares one, offer a stronger version in one line if key parts are missing.

- **Context first:** who it's for, the product stage and the constraints. `<context>` and `<task>` tags keep it clear.
- **Design prompts** name the component, layout, visual style, content, tech stack, every state (loading, empty, error, success, hover, focus), accessibility, what changes on small screens, and a reference ("like Linear").
- **Copy prompts** name the voice file, the audience, the user's goal and what can go wrong, character limits, verb-first buttons, and recovery steps.
- **Keep design and copy prompts separate,** then combine the results.
- **Realistic content,** never lorem ipsum.
- **Iterate:** structure first, then visuals, then polish.
- **Save prompts that work** in the project's prompt library.

Sources: [copyprompt.io](https://copyprompt.io/blog/ai-prompts-for-designers-2026), [Superdesign](https://superdesign.dev/blog/ui-design-prompts), and articles from Fardino and Techpresso's AI Academy (unpublished sources).

## 10. Editing, not appending

Appending is the default failure. New content lands at the end, or turns into a new section, and the document grows without anyone deciding what it displaced. It reads fine on the day and degrades over months.

Work through these in order before writing anything new.

1. **Does the document already say this?** If so, sharpen that line. Never write a second version of something somewhere else.
2. **Which existing section owns the subject?** Put it there, where a reader looking for it would check first. Most additions belong inside something, not after it.
3. **If nothing owns it, does a new section earn its place?** Only when the subject is genuinely uncovered. Name the sections you checked, so the claim can be tested.
4. **What does this make redundant?** Anything the new text now covers better comes out in the same edit.

A document that grows every time it is touched is a document nobody finishes reading. Growth is fine when something was missing.

## 11. Before sending

Two gates. The script catches what a script can catch, which leaves judgment for what it cannot.

### Gate 1: run the checker

`scripts/check.py` holds every rule in this skill a machine can test.

- Em dashes, en dashes, stray exclamation marks and emoji
- The cut-on-sight words, and the language in section 4
- Headings and table column headers that point instead of naming a subject
- Headings that are a count rather than a subject
- Bullets carrying a colon of their own, or holding more than one idea
- Colon stems whose bullets do not finish the sentence
- Sentences over 34 words, and a sentence that appears in two places
- In a SKILL.md, a dollar sign that is not escaped

Run it on every piece of copy, every time, before sending.

```
python3 scripts/check.py <file> [<file> ...]
```

Exit code 1 means something is flagged. Copy that is not in a file yet gets written to one first: a message, a button label, a commit description, a doc and a reply all go through the same check.

Reading the file and judging it by eye is not a substitute. The misses are never the lines that got looked at.

Every finding needs one of two outcomes before anything is sent.

- **Fixed.** The rule was right.
- **A reviewed exception, with the reason said out loud.** A colon introducing a short list of names, "is fixed" where naming an agent adds nothing, and a quoted fragment counted as a sentence are all real exceptions. An exception nobody can justify out loud is a miss wearing a justification.

### Gate 2: three questions no script can ask

1. **Where does the reader have to work?** Find the pronoun they must resolve, the verb the sentence left out, the line they would read twice.
2. **Did you write an absolute?** Name a real case that breaks it. Most "never," "always" and "not for" lines are false and nobody checks.
3. **Does your most confident line rule anything out?** If nobody would argue the opposite, it says nothing.

### Lines you did not write this time

Carried-over text is where the misses live, because editing a line to match a renamed heading feels like having reviewed it. Both gates cover every line in the file, not the lines changed in this pass. Keeping a line is choosing it.

### The review

Run it on anything read more than once: a skill, a doc, a page, a message that matters. These are the checks a script cannot make.

- [ ] Could a chart, number or layout replace any words?
- [ ] Read it out loud. Does it sound like someone who respects the reader?
- [ ] Would a smart reader feel talked down to anywhere?
- [ ] Does every heading and every column header name its subject?
- [ ] Are the bullets in each list parallel? The script cannot judge this, because a gerund acting as a noun is parallel with a noun phrase and a gerund acting as an instruction is not.
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
- Bring every change you found in one proposal and wait for a yes. Group small fixes under one yes, give bigger changes one line each. Don't drip them out, and don't hold back a real one.
- Rewrite or remove a rule before adding one. Keep history in the document history table, not in the skill.

Source: Carol Dweck's *Mindset* ([Farnam Street summary](https://fs.blog/carol-dweck-mindset/)).

## 13. working-with-sharon builds on this

That skill covers what a reply needs beyond good copy: the answer-first shape, how many bullets, how many options, one question at a time, and pacing. The craft rules here hold underneath it.

There is no handoff and nothing to route. A reply follows both. So does a skill, a doc, a wiki page and a note someone writes to themselves.
