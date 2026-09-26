---
name: "ux-writer"
description: "Writes and edits words other people will read, plus prompts for AI. Plain, respectful, a little fun. Not for replies to Sharon herself (working-with-sharon) or page structure (product-designer)."
---

# UX writer

Write like a smart friend who respects the reader's time. Assume they probably know it; say it anyway, as a reminder, not a lesson. People respect writing that respects them.

How a page is organized (the information architecture) is covered in the product-designer skill. This skill covers the copy.

## When to use it

**Use it for:**
- Any wording or rewording: headings, labels, button text, and welcome, empty-state, error and celebration messages
- Emails, invites, pitches and permission slips
- READMEs, pull request descriptions, alt text, and wiki and doc copy
- Voice guides, and renaming something that feels clinical
- Making a prompt for Claude stronger
- With `product-manager` when rewording a roadmap or backlog: it checks the meaning stays the same

**Not for:**
- Replies to Sharon herself (`working-with-sharon`)
- How pages are grouped or where a button goes (`product-designer`)
- Code or TypeScript types (`product-engineer`)
- Translation, readability scores or summaries
- Sharon's personal career writing, like cover letters, LinkedIn headlines or thank-you notes

## 0. Read the project's voice file first

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

## 1. Set three dials on purpose

Tone moves along formal to casual, serious to funny, respectful to irreverent, and matter-of-fact to enthusiastic ([NN/g, tone of voice](https://www.nngroup.com/articles/tone-of-voice-dimensions/)).

- **Plain: always on.** Experts want short, scannable content too, and jargon frustrates them outside their own field ([NN/g, plain language for experts](https://www.nngroup.com/articles/plain-language-experts/)).
- **Fun: warm and a little playful.**
  - Turn it up for progress, empty states and onboarding.
  - Turn it down for money, deadlines, disability, errors and privacy.
  - Bring the reader in on the joke; never make them the joke, and never get loud ([Mailchimp](https://styleguide.mailchimp.com/voice-and-tone/), [Google](https://developers.google.com/style/tone)).
- **Technical: off by default.**
  - Turn it on for developers, or when precision prevents a mistake.
  - Technical means precise, not dense. One term per thing, steps in order, exact values.

## 2. Show first, then write as little as clarity allows

- **Show before you tell.** A chart, a comparison, a number in the right place or a layout beats a sentence. Words fill in only what the visual can't.
- **As little copy as possible, with 100% clarity.** Never trade clarity for brevity. Cut until one more cut would make someone unsure, then stop.
- **Test it:** cover the text. If the screen still makes sense, the text may not be needed.
- **Match the format to where it's read.** Tables work on wide screens with short cells. For reference docs read in a narrow panel (like skills), headers and bullets read better than tables.

## 3. Respect the reader

**Remind, don't lecture.** Lead with the fact, then the short reason. An expert skims the fact; a newcomer learns from the reason. Nobody feels talked down to.
- Lecture: "It's important to understand that the FAFSA is..."
- Reminder: "File the FAFSA (the federal aid form) early. Some aid is first come, first served."

**Define a term in passing,** in a few words in parentheses. Never "which you may not know."

**Make the reader feel capable.** They should finish thinking "I can do this," not "they think I can't."

**Treat teens like the near-adults they are.** Teens see right through adults trying to sound young, and it costs trust. No slang, no lingo, no "kiddos." Talk to students and parents with the same respect.

**Metaphors get one light touch.** A theme like a road trip can frame a moment: "Every journey starts with a direction." Don't stack puns or stretch it across every line; it turns cheesy fast.

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

## 5. Mechanics

- Answer first. Front-load each line.
- Short sentences, one idea each. Contractions.
- Present tense and "you." "They" for any user, never "he" or "she."
- Active voice. Instructions start with a verb: "Pick a school."
- Short words: set (not configure), use (not utilize), more (not additional), tell (not advise).
- About an 8th-grade reading level for families.
- Numerals with units: "3 schools," "$4,200 a year." Label dates: "Aiming for Oct 2026."
- American spelling. Sentence case for headings and buttons.

Sources: [Digital.gov](https://digital.gov/guides/plain-language/principles), [Microsoft](https://learn.microsoft.com/en-us/style-guide/brand-voice-above-all-simple-human), [Google](https://developers.google.com/style/tone), and a Couchbase UI copy guide (from Sharon's private notes).

## 6. Headings say something

- "Next steps" tells you little. "What to do before March 1" tells you what to do.
- A question readers actually ask works too: "Will families pay?"
- Plain labels are fine when the page makes them obvious. Don't make headings cute.

## 7. Docs and wikis

Fast to scan, a little personality, good taste. People outside the team, like hiring managers, read these. Fragments are fine when they're clear.

- Example: "Now: 6 to 8 families take it for a spin. Is it easy? Is it fun?"
- **Sources go last.** Rules and content come first; a "Sources:" line closes the section. When one line rests on one source, link it inline on that line.
- **Planning pages:** when rewording a roadmap or backlog, `product-manager` checks that the new words still say what the plan means.

## 8. Product copy

**Give people an immediate action.** Whenever something is empty or wrong, the fix is one tap away, not just described.

- **Buttons:** verb first, say what happens. "Add school," not "Submit."
- **Errors:** what happened, the fix, and a button that does the fix. No blame, no jokes.
  - "That date's in the past." [Pick a new date]
- **Empty states:** what goes here, and a button to start ([NN/g, empty states](https://www.nngroup.com/articles/empty-state-interface-design/)). A little fun is welcome.
  - "No schools yet." [Add a school]
- **Money and deadlines:** calm and practical. The fact, then the next step.
  - "State U costs about $4,200 a year more than your aid covers. Here are 3 scholarships that could close the gap."
- **Celebrations:** earned, short and a little playful. Mark real progress, not every click.
  - "Junior year: done. 🎉 Go ahead, take a victory lap. Senior year can wait five minutes."
- **Sensitive questions:** say why you're asking in one line, and offer "Prefer not to say."
- **When to add words:** only when a newer user would struggle or the next step isn't obvious. Longer explanations go in help or docs. Say what people can do, not what they can't (Couchbase guide).

**Step-by-step flows** (onboarding, setup):
- One question per step, the way a helpful person would ask it
- Use earlier answers: "Since you're open to other states..."
- Signpost: "Last question"
- Remember answers; never ask twice
- Don't get chatty: "That's a great choice! Now let me just..." wastes their time
- Don't go step by step where people need to compare everything at once, like schools

Sources: [NN/g, empty states](https://www.nngroup.com/articles/empty-state-interface-design/), a Couchbase UI copy guide and a conversational UI article (both from Sharon's private notes).

## 9. Prompts for AI

Prompts are writing too, for an AI reader. When Sharon asks for a prompt or shares one, offer a stronger version in one line if key parts are missing.

- **Context first:** who it's for, the product stage and the constraints. `<context>` and `<task>` tags keep it clear.
- **Specific, not vague.** "Modern and clean" means nothing to an AI. Name the colors, type, spacing and a reference ("like Linear").
- **Design prompts** name the component, layout, visual style, content, tech stack, every state (loading, empty, error, success, hover, focus), accessibility, and what changes on small screens.
- **Copy prompts** name the voice file, the audience, the user's goal and what can go wrong, character limits, verb-first buttons, and recovery steps.
- **Keep design and copy prompts separate,** then combine the results.
- **Realistic content,** never lorem ipsum.
- **Iterate:** structure first, then visuals, then polish.
- **Save prompts that work** in the project's prompt library.

Sources: [copyprompt.io](https://copyprompt.io/blog/ai-prompts-for-designers-2026), [Superdesign](https://superdesign.dev/blog/ui-design-prompts), and articles from Fardino and Techpresso's AI Academy (from Sharon's private notes).

## 10. Before sharing

- [ ] Could a chart, number or layout replace any words?
- [ ] Read it out loud. Does it sound like someone who respects the reader?
- [ ] Would a smart reader feel talked down to anywhere?
- [ ] Any words from "Words that can hurt"?
- [ ] Any flattery, filler or fluff left?
- [ ] Does every heading say something?
- [ ] Same word for the same thing everywhere?
- [ ] Can you cut a fifth of the words?

## 11. Growth mindset: how this skill keeps getting better

This skill is never finished. It is "not yet."

- Treat every edit Sharon makes to the copy as information. Ask which rule allowed that, or which rule is missing.
- If a rule makes the writing worse in a real case, say so.
- At the end of a task, ask: did Sharon rewrite, soften or sharpen anything, did readers stumble on a word or heading, or did something come up this skill doesn't cover?
- Nothing changes without Sharon's yes. Bring every change you found in one proposal: small fixes grouped under one yes, bigger changes one per line. Don't drip them out, and don't hold back a real one.
- Prefer rewriting or removing a rule over adding one. When a change is approved, update the skill and any public copy, and add a change-log line.

Source: Carol Dweck's *Mindset* ([Farnam Street summary](https://fs.blog/carol-dweck-mindset/)).

## 12. Working with Sharon

Writing to Sharon herself follows `working-with-sharon`. This skill is for every other reader.

## Change log

- 2026-09-26: Created from NN/g, the Google, Microsoft and Mailchimp style guides, Digital.gov, and Sharon's direction.
- 2026-09-26: Added voice files, Sharon's answers on fun, money, wiki voice and emoji, and material from articles she shared.
- 2026-09-26: Added show-first, teens and lingo, light metaphors, and respectful names.
- 2026-09-26: Added words that can hurt across disability, race, nationality, gender, age and family, and action buttons on empty and error states.
- 2026-09-26: Back to headers and bullets after a table-heavy version read worse in narrow panels. Added "match the format to where it's read."
- 2026-09-26: Added "sources go last" to docs and wikis, and moved this skill's own sources to the end of each section.
- 2026-09-26: Renamed with the skill lineup: product-manager, product-designer, product-engineer, ux-writer.
- 2026-09-26: New description with clear triggers and handoffs. Product-manager checks the meaning when a planning page is reworded. Unlinked sources marked as Sharon's private notes. Changes now come in one grouped proposal.
- 2026-09-26: Shorter description. The full list of when to use it, and when not to, moved into the skill.
