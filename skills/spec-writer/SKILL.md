---
name: "spec-writer"
description: "Writes and reviews area specs so every spec reads the same way and every line can be checked. Covers who brings what, the rules every spec follows, and the standard section list."
---

# Spec writer

Status: draft. The section list uses the recommended defaults. If Sharon overturns one, update this skill.

## TL;DR

- Start with the area owner. They say what the area is for, what keeps breaking and what is out of scope.
- Then the product manager, designer and engineer write it together, all three across every section. Each argues for a different risk, and the answers come out of that tension.
- Make every line checkable. A requirement names how it gets checked, a metric names the problem it watches, and a skipped section says N/A and why.

## Before drafting

The area's specialist loads this skill and plays the area owner. Then load the rest of the team:

- `product-manager`, `product-designer` and `product-engineer` for the content
- `working-with-sharon` and `ux-writer` for the wording

Then answer three questions.

1. Who reads the spec, and what do they decide after reading it?
2. What must it do, kept separate from what would be nice?
3. Low fidelity or high? Agreeing on a direction, or building from it?

## Who brings what

Two stakeholders and three specialists.

**Sharon** brings what matters, what is allowed and what is not worth doing.
- Breaks a tie on approving the spec, answering Open decisions, and what goes on the bench.

**The area owner** brings the goals of the area and what keeps breaking.
- Breaks a tie on Problems to solve, Goals, Out of scope and Rabbit holes.
- Approves the spec, and has to read the finished spec to do it.

**The product manager** owns value and viability. Will people use it, and is it worth doing at all? **[CAGAN]**
- Says why this, why now, and what success looks like.
- Breaks a tie on TL;DR, Requirements, How we'll judge the options, Success metrics, Risks and what we'd do, and Build order.

**The product designer** owns usability and delight. Can people use it, and do they love using it? **[CAGAN]**
- Reduces uncertainty rather than making screens. Asks whether to build it at all, frames the real problem, and thinks in systems rather than one-off pages. **[DSC]**
- Makes using it feel good, not only possible.
- Breaks a tie on Page design.

**The product engineer** owns feasibility. Can it be built, is it robust, and will it scale when it needs to? **[CAGAN]**
- Keeps data consistent, handles edge cases, draws clear boundaries between parts, and keeps the system simple to change. **[AWM]**
- Designs so growth later does not mean a rebuild, without building for scale before it is needed.
- Breaks a tie on Sources of truth, Fields and editors, and Dependencies.

### Ties, not territory

Breaking a tie is not owning a section. The three specialists work every section together, and a designer with a better idea about Sources of truth should say it. If the three cannot agree, the tie-breaker decides and says why.

One hard edge applies to the stakeholders. A stakeholder who writes their own requirements and then approves them has approved nothing. So the area owner and Sharon bring goals and problems and sign off. When either writes part of a spec, they do it in a specialist's role, and somebody else approves it.

## Rules for every spec

1. **The spec describes the best answer, not the current one.** How the area works today is there to be challenged. If the best answer replaces a source of truth, a field or a tool, the spec says so.
2. **TL;DR stands alone at the top.** At most three bullets, readable without the rest. **[ADK]**
3. **Goals and Out of scope never overlap.** If something sits in both, one of them is wrong. **[ADK]**
4. **Every requirement says how it gets checked, on the same line.** A requirement nobody can verify is a wish. **[ADK]**
5. **Everything that needs Sharon goes in Open decisions**, each item with a recommendation. Nothing that needs her is left in the prose. **[ADK]**
6. **A section that does not apply says N/A, with one line saying why.** A silently missing section makes a gap look like a decision. **[ADK]**
7. **References are concrete.** A real link, a database ID or a file path, never "see the Notion page." **[ADK]**
8. **No preamble.** Say the thing, not what the section will describe. **[ADK]**
9. **Decide fidelity first.** Low fidelity agrees a direction, high fidelity is built from. Mixing them produces neither. **[LENNY]**
10. **The test is whether the product engineer opens it.** A complete spec nobody reads has failed. **[LENNY]**
11. **A spec can add a section the list does not have** if it names the problem that section solves. The list is the floor, not the ceiling.

## How to write a success metric

Four steps, in order. If one has no answer, the metric comes out.

1. **The problem it watches.** Named and specific, taken from Problems to solve.
2. **The one observable thing that changes if the problem is fixed.** One, not a dashboard of five.
3. **Where that number comes from.** A named source of truth.
4. **What you would do if it moved the wrong way.** If the honest answer is nothing, the metric is trivia.

Example from Home Management:

1. Nothing tells Sharon a chore was skipped, so she finds out when it matters.
2. Skipped chores she learns about from the Life Hub rather than from the consequence.
3. The chores database, Skipped and Acknowledged fields.
4. If it stays at zero, change Page design so skipped chores show on the Life Hub.

Step 4 is the one that gets skipped, and the one that makes the metric real.

## What goes wrong in a spec

- **A requirement and a design choice in one bullet.** In "show the meal plan as a carousel," the meal plan is required and the carousel is a design choice. **[ADK]**
- **"Best practice" standing in for a requirement**, with no measurable outcome. **[ADK]**
- **Fields and screens named before the direction is agreed.** **[LENNY]**
- **Writing for the author** instead of the product engineer. **[LENNY]**

## The section list

Every spec uses these sections in this order. A section marked "when it applies" appears only when it has something to say. Every other section appears in every spec, saying N/A when it does not apply.

### At the top

- **TL;DR**, at most 3 bullets. The first bullet says what the area is for.
- **Status and last updated**
- **What the words mean**, one line per term

### Why the area needs work

This group is where the area owner has something to say that the specialists do not.

- **How the area works today**
- **Problems to solve**
- **Goals**, as outcomes rather than features
- **Out of scope.** Anything here can still be promoted into Problems to solve later.

### How the area works

- **Sources of truth**
- **Fields and editors**
- **Page design**
- **Requirements**, each tagged Must, Should or Could
- **Dependencies**, when it applies

Page design covers the area's own page, what the Life Hub shows from it, what sits behind progressive disclosure (hidden until you ask for it), and what never appears anywhere. It stays one section, because splitting UX from UI adds a section without adding a decision.

### Choices, and what is still open

- **How we'll judge the options**, when there are options
- **Options and the pick**, when there are options. One table of the options, the chosen row marked, one line on what choosing it costs.
- **Open decisions**, the calls only Sharon can make, each with a recommendation
- **On the bench**, links only

### What could go wrong, and how we'd know

- **Success metrics**, each paired with a problem
- **Risks and what we'd do**, when it applies
- **Rabbit holes**, when it applies
- **Known defects**, when it applies

### What happens next

- **Build order**, in dependency order, when something is being built

### Sections left out on purpose

- **Purpose** is the first bullet of the TL;DR.
- **Validation** is rule 4.
- **Open questions** are folded into Open decisions.
- **Rollout and adoption** is parked on the bench.
- **Decision record** links to `claude/decisions.md` instead. Two copies of a decision drift.

## Sections that need a definition

Examples come from Home Management.

### Sources of truth

One place you believe per question. When two places disagree, the answer is already decided, so nobody argues it again at 7am.

- **Do we have eggs?** Pantry Persona, not your memory or the last receipt.
- **Is the Zillow tour Wednesday?** Google Calendar, not the email that proposed it.
- **What are we eating Thursday?** The Pantry Persona meal plan, not the text thread about dinner.
- **Did the water bill get paid?** The budgeting app, not the bank app's pending list.

The section is a list like that: each question, and the one place that answers it.

### Fields and editors

The blanks that exist, and who fills each one.

- **Quantity on hand** is filled by the receipt scan.
- **Do not buy again** is filled by Sharon.
- **Reorder by** is calculated from usage. Nobody types it.

Almost every field is machine filled, person filled or computed. One combination needs naming in full: "a machine fills it and a person may overwrite." Listing two editors loses the overwrite, which is how a synced assignments list once broke.

### How the area works today

What happens right now, including the parts that happen in someone's head. Not a list of software.

Home Management today: meals live in Pantry Persona, chores live in Sharon's memory, tours live on the calendar, and nothing says when a chore got skipped. That skipped chore becomes an entry in Problems to solve.

This section is never N/A. "Nothing happens today, it falls through" is an answer. It is also the one section the spec is allowed to overturn: writing down today's setup is how the spec argues against it.

## Where ideas go

The bench holds ideas. The spec holds what has been agreed. An area owner pitching inside a spec turns a description into an argument, and only Sharon can accept an idea.

So the spec carries On the bench as links only, with no detail and no pitching. The area owner still sees what is there and does not re-propose something already declined. When an idea graduates off the bench, it becomes an entry in Problems to solve.

## Where a spec lives

Every spec is two linked pages, because the product repo is public and the household is private.

- **The public spec** goes in the project's repo wiki, in `docs/wiki/`. It holds the sections, rules and requirements, with no household details and no specialist names. Roles stand in for names: "the home specialist," not a nickname.
- **The private details** go in a Notion page in [Project Documents](https://app.notion.com/p/a3bcb29062cf4ad288dc1c8b067b93ed). That page holds the real examples, the actual fields, and anything only this household would know.
- **Each page links to the other.** The public spec says which sections have private detail, without saying what it is.
- **Index both in the same pass.** Add a row to `docs/wiki/Documents.md` in the pull request, and a row in Project Documents.

The test for any line: would it make sense to a stranger who never sees the house? If not, it goes in the private page.

## How specs are worded

Sharon reads every spec, so `working-with-sharon` and `ux-writer` both apply. Run the ux-writer checker on every finished spec.

Familiar names were swapped for plainer ones:

- **Data model** is Fields and editors.
- **Background and current state** is How the area works today.
- **Evaluation criteria** is How we'll judge the options.
- **Terminology** is What the words mean.
- **Non-goals** is Out of scope.

## Sources

Unmarked rules and sections came out of this project's own work: Sources of truth, Fields and editors, Page design, Problems to solve, On the bench and Known defects.

- **[ADK]** [adk-plan-spec, sujeet-pro](https://sharedcontext.ai/skills/external/sujeet-pro/adk-plan-spec), the source of TL;DR, Goals, Out of scope, Requirements, Dependencies, Success metrics, Risks, Build order, and most of the rules
- **[LENNY]** [writing-specs-designs, refound/lenny](https://awesomeskill.ai/skill/refoundai-lenny-skills-writing-specs-designs), the source of the fidelity rule and the read-it test
- **[RFC]** [rfc-specification, jpoutrin/product-forge](https://skills.cat/skills/jpoutrin/product-forge/rfc-specification), the source of Status, What the words mean, How the area works today, and the options sections
- **[SU]** Shape Up, the source of Rabbit holes
- **[CAGAN]** [The Four Big Risks, SVPG](https://svpg.com/four-big-risks/), the source of which role owns which risk
- **[DSC]** [Senior designers don't design more screens, Design Systems Collective](https://www.designsystemscollective.com/senior-designers-dont-design-more-screens-they-solve-bigger-problems-e26c5f4c7c07)
- **[AWM]** [Developer practices for long-term maintainability, Advanced Web Machinery](https://advancedweb.hu/developer-practices-for-long-term-product-maintainability/)
- [Writing better RFCs and design docs](https://dev.to/pixari/writing-better-rfcs-and-design-docs-20pj)