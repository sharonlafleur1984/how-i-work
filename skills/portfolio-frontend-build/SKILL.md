---
name: "portfolio-frontend-build"
description: "Use when moving a front end built in Claude artifacts or prompts into a real GitHub repo: bring the prototype in as-is, then rebuild it as clean, readable, tested code a designer can explore, store, and grow."
---

# From artifact to real repo: portfolio-grade front-end build

The starting point is usually a prototype built through prompts (a Claude artifact or a single HTML file). The goal is to move it into a real GitHub repo the owner can open, read, change, and store, then level it up into a codebase another front-end designer would study: every file easy to find, every decision written down, every screen accessible, tests that keep it healthy over time, and design and code that stay in sync. Combine a distinctive design with disciplined engineering. Spend boldness in one memorable place; keep everything around it quiet and consistent.

## Start from the artifact

1. Bring the prototype into the repo exactly as it works today, on its own branch, so there is a known-good version to compare against.
2. Swap any real personal data for sample data before the first commit. Turn off any live backend keys in the copy.
3. Write a short README that says what it is and that the rebuild is coming.
4. Treat the prototype as the spec: every screen, state, and behavior in it becomes a checklist item for the rebuild.
5. Rebuild piece by piece using the order of work below.

### Match the prototype before replacing it

- Before rebuilding, capture Playwright screenshots of every prototype screen and open state (modals, flipped cards, expanded sections) at phone and desktop sizes. Store them in `tests/visual/prototype/`.
- Keep a parity checklist in `docs/prototype-parity.md`: one row per screen, state, and behavior, with a status (not started, rebuilt, matches).
- A rebuilt screen is done only when it matches its screenshot (or the difference is an intentional, documented improvement) and its behaviors pass tests.
- Never delete the prototype until every row matches.

## 0. Before writing code

1. Read the repo's `CLAUDE.md`, `docs/ARCHITECTURE.md`, and `docs/design-system.md`. Follow recorded decisions; do not re-decide them.
2. If a decision is missing (framework, audience, hosting), stop and ask the owner one question at a time, with a recommendation.
3. Write a short plan: what changes, which files, which tests prove it. Show it before large changes.
4. Never commit real personal data. Use sample data only. Secrets live in `.env` (git-ignored) and CI secrets.

## 1. Order of work (each step depends on the one before)

1. Tooling and QA skeleton (so every later step is tested from day one), plus prototype screenshots
2. Design tokens, synced with Figma variables if the owner uses Figma
3. Base styles and layout primitives
4. Components, bottom level first (see section 6), each with tests, docs, and a Storybook page
5. Content moved into typed data files
6. Pages and flows composed from components and patterns
7. Accounts and data layer
8. Performance and polish pass

## 2. Repository structure

```
/
├─ src/
│  ├─ tokens/            # DTCG JSON: primitives, semantic, component
│  ├─ styles/            # layers: reset, tokens (generated), base, layout, utilities
│  ├─ components/        # single-purpose components, one folder each
│  │  └─ button/
│  │     ├─ button.tsx
│  │     ├─ button.css
│  │     ├─ button.test.tsx
│  │     ├─ button.stories.tsx
│  │     ├─ button.figma.tsx   # Code Connect template (optional)
│  │     └─ button.md          # purpose, variants, do/don't, a11y notes
│  ├─ composites/        # components with nested parts
│  │  └─ card/
│  │     ├─ card.tsx
│  │     ├─ card-header.tsx  # nested parts live in the parent's folder
│  │     ├─ card-footer.tsx
│  │     └─ ...
│  ├─ patterns/          # reusable combinations with usage rules
│  ├─ features/          # domain flows named by what the user does (explore, finance, dates)
│  ├─ content/           # JSON/YAML data + schemas (schools, tasks, scholarships, terms)
│  ├─ lib/               # pure helpers (dates, storage, formatting), fully unit-tested
│  └─ assets/            # optimized images (AVIF/WebP + fallback), fonts, icons (SVG sprite)
├─ tests/
│  ├─ e2e/               # Playwright user journeys
│  ├─ a11y/              # axe scans of every page and state
│  └─ visual/            # screenshot baselines (including prototype/)
├─ docs/
│  ├─ ARCHITECTURE.md
│  ├─ design-system.md   # tokens, rules, component and pattern index
│  ├─ prototype-parity.md
│  ├─ glossary.md        # plain-language terms for the owner
│  └─ decisions/         # ADRs: 0001-framework.md, 0002-tokens.md ...
├─ .storybook/
├─ .github/workflows/ci.yml
├─ CLAUDE.md
└─ README.md
```

Naming: kebab-case files, one component per folder, feature folders named by what the user does.

## 3. Semantic HTML rules

- One `<h1>` per page; headings never skip levels; headings describe content, not styling.
- Landmarks: `<header>`, `<nav>`, `<main>`, `<footer>`, `<section aria-labelledby>` for titled regions.
- Native elements first: `<button>` for actions, `<a href>` for navigation, `<dialog>` for modals, `<details>` for simple disclosure, `<fieldset>`/`<legend>` for grouped choices, `<input type="checkbox">` for checklists, `<table>` with `<th scope>` for comparisons, `<ol>`/`<ul>` for lists, `<time datetime>` for dates.
- Never make a `<div>` clickable. Never nest interactive elements.
- ARIA only when no native element exists; every ARIA pattern follows the APG (radio group, tabs, disclosure).
- Every image has meaningful `alt`, or `alt=""`/`aria-hidden` when decorative. Information is never in an image alone.
- Forms: visible labels, helpful errors tied with `aria-describedby`.

## 4. CSS architecture

- Cascade layers in this order: `@layer reset, tokens, base, layout, components, utilities, overrides;`
- No `!important` outside `overrides` (goal: zero). No ID selectors. Low, flat specificity.
- Components only use semantic or component tokens, never raw values or primitives.
- Logical properties (`margin-block`, `padding-inline`), `clamp()` type scale, container queries for components, media queries only for page layout.
- Every animation is disabled or reduced under `prefers-reduced-motion`.
- Focus is always visible (`:focus-visible`), 3:1 minimum contrast.

## 5. Design tokens (three tiers, W3C DTCG format)

1. **Primitives:** raw values named by what they are (`color.red.600`, `space.8`). Never used by components.
2. **Semantic:** named by purpose (`color.text.primary`, `color.status.alert`, `space.section`). Components use these.
3. **Component:** only when 3+ components share a decision that may change independently (`button.primary.bg`).

Rules: names read category, property, variant, state (`color.bg.surface.hover`). Never encode a value in a name. Build tokens to CSS custom properties (and Figma variables when the owner uses Figma) with Style Dictionary or an equivalent. Tokens are the single source of truth; a lint rule fails any raw hex, px spacing, or font size in component CSS.

## 6. Components, nesting, and patterns

Five levels. Each level may use only the levels below it, never above or sideways into a feature.

| Level | What it is | Examples | Lives in |
|---|---|---|---|
| 1. Tokens | Design decisions as data | color, space, type, radius, motion | `src/tokens/` |
| 2. Components | One job, no nested parts | Button, Chip, Icon, Link, Badge | `src/components/` |
| 3. Composites | Components with nested parts that only make sense together | Card (header, body, footer), Modal (header, body, footer), Tabs (list, tab, panel) | `src/composites/` |
| 4. Patterns | Reusable combinations with rules for when and how to use them | modal footer with navigation + rank picker, flip-card deck, filter bar, empty state | `src/patterns/` |
| 5. Features and pages | Real screens and user flows | explore schools, financial planning, important dates | `src/features/` |

Nesting rules:
- Nested parts live in their parent's folder and are exported with it (`Card`, `CardHeader`, `CardFooter`). They are never imported alone from outside the parent.
- Prefer composition (children and named slots) over long prop lists. If a component needs more than about 8 props, split it or turn it into a composite.
- A component promotes up a level only when it is reused in 3 or more places. Do not build a pattern for a one-off.
- Features own data and state; components, composites, and patterns receive data through props and stay pure.

Every item at levels 2 to 4 ships with: markup, styles, behavior, tests, an a11y note, a Storybook page, and a docs page listing variants, states (default, hover, focus, active, disabled, loading, empty, error), and do/don't examples. Pattern pages also say when to use it, when not to, and which components it is built from. Storybook is grouped by level (Tokens, Components, Composites, Patterns, Pages) so the hierarchy is visible. Button hierarchy: one primary per screen, secondary for alternatives, tertiary text for side trips.

## 7. Content and state

- All content lives in `src/content/` with a schema (Zod or JSON Schema). Build fails on invalid content.
- UI state and saved user data go through one storage module in `src/lib/`; nothing else touches `localStorage` or the network directly.
- Dates are real dates (`2027-10-01`), formatted at render time.

## 8. Design and code loop

When the owner designs in Figma, connect the two sides with three links. None of them rewrites code automatically; they keep both sides visible and matched.

1. **Token sync (the only link that moves changes).** Tokens in `src/tokens/` and Figma variables stay matched through Style Dictionary or a token-sync plugin. Decide and record in an ADR which side is the source of truth. A CI check fails if they drift.
2. **Code Connect.** Map each Figma component to its code component so Figma Dev Mode shows the real code. Use Figma's template files (`*.figma.tsx`), not the retired Storybook-specific parser.
3. **Storybook and Figma side by side.** Add the Storybook design add-on so each story shows its Figma frame, and publish Storybook so the Storybook Connect plugin can show live stories inside Figma.

When a design changes: update tokens first, then components, then the Storybook story, then the Code Connect template. The visual tests catch anything missed.

## 9. Quality pipeline (runs locally on commit and in CI on every pull request)

| Layer | Tool | Gate |
|---|---|---|
| Types | TypeScript `strict` | no errors |
| Lint and format | ESLint or Oxlint, Stylelint, Prettier or Oxfmt | no errors |
| Tokens | Stylelint rule or custom check | no raw values in components; tokens match Figma |
| Layers | lint rule on imports | no level imports from a higher level |
| Unit | Vitest | pure logic 90%+ covered |
| Component | Vitest browser mode or Storybook tests | every variant and state |
| End to end | Playwright | every user journey, desktop and phone sizes |
| Accessibility | axe-core in Playwright and Storybook | zero violations, every page and open state |
| Visual | Playwright screenshots | no unreviewed diffs; prototype parity tracked |
| Performance | Lighthouse CI + size budget | scores and bundle under budget |
| Hygiene | Knip, Gitleaks, dependency audit | no unused code, secrets, or known vulnerabilities |
| Content | schema validation | all data valid |

Git hooks (Lefthook or Husky) run lint, types, and unit tests before commit. GitHub Actions runs everything. Netlify builds a preview link for every pull request, and Storybook is published so every component has a shareable link.

## 10. Documentation

- `README.md`: what it is, a screenshot, how to run, how to test, links to docs and Storybook.
- `docs/ARCHITECTURE.md`: folder map, the five levels, data flow, state, how to add a component or a piece of content.
- `docs/design-system.md`: token tables, rules, component and pattern index.
- `docs/prototype-parity.md`: what has been rebuilt from the prototype and what is left.
- `docs/glossary.md`: plain-language definitions of every technical term used in the repo.
- `docs/decisions/`: one short ADR per significant choice (context, decision, consequences).
- If the repo has a GitHub wiki, keep a plain-language dashboard there with progressive disclosure that links to all of the above, Storybook, and the skills used, so the owner can find everything without reading code.

## 11. Learning mode

The owner is a designer learning to work in code. The repo should teach as it grows.

- Every pull request description has a short "What changed and how it works" section in plain language: what the user will notice, which files changed, and one sentence on the concept behind it.
- The first time a new term, tool, or file type appears, explain it in plain language and add it to `docs/glossary.md`.
- Leave short comments in code only where the why is not obvious. Explain decisions, not syntax.
- When there are two reasonable ways to do something, name both briefly and say which was chosen and why.

## 12. Definition of done (every change)

- [ ] Uses tokens and existing components; no one-off values
- [ ] Sits at the right level and imports only from levels below
- [ ] Semantic HTML; keyboard works; screen reader labels make sense
- [ ] Works at phone, tablet, and desktop widths; no horizontal scroll
- [ ] Reduced motion respected
- [ ] Storybook page added or updated; Figma link and Code Connect updated if used
- [ ] Tests added or updated; the whole pipeline passes
- [ ] Prototype parity row updated if this rebuilds part of the prototype
- [ ] Docs and glossary updated if behavior, a rule, or a new term changed
- [ ] Small, focused commit with a clear message; pull request with before and after screenshots and a plain-language "how it works" note

## 13. Working with the owner

- Answer first, a few bullets, then a caveat. Show at most 3 options and mark the recommendation.
- Ask one question at a time. Recommendation is not approval: confirm before changing or deleting anything.
- Say plainly when something better exists than what was asked for.
- Assume the owner is a designer learning to work in code: explain terms in plain language the first time they come up.

## 14. Growth mindset: how this skill keeps getting better

Based on Carol Dweck's *Mindset* ([Farnam Street summary](https://fs.blog/carol-dweck-mindset/)): ability grows through effort, feedback, and learning from mistakes. This skill is never finished. It is "not yet."

**While working**
- Treat every correction from the owner, every failing test, and every review comment as information, not failure. Ask: which rule here allowed the problem, or which rule is missing?
- Engage with mistakes instead of hiding them. Say plainly when this skill's guidance led to a wrong result.
- Challenge the rules. Tools and best practices change fast: before leaning on a rule, ask whether a tool is deprecated, a version has moved on, or a better practice now exists.
- Notice what worked too, so good patterns get written down, not only failures.

**Self-review at the end of a task**
1. Did the owner correct, redo, or push back on anything this skill told me to do?
2. Did the pipeline, a reviewer, or a real user catch something this skill should have prevented?
3. Did a situation come up that this skill doesn't cover?
4. Is any tool, version, or practice in this skill out of date?

If any answer is yes, bring one short suggestion.

**Self-healing, always with the owner's approval**
- A skill can't change itself, and nothing changes without the owner's yes. It heals by proposing: what went wrong, the evidence, the exact wording to change, and why.
- At most one suggestion per task, at the very end, in one line: "Skill update idea: ... Want me to propose it?" Never interrupt the work for it.
- Self-editing: prefer rewriting or removing a rule over adding a new one, so the skill stays usable.
- When a change is approved, propose the whole updated skill, update any public copy (such as `docs/skills/` in a repo) in the same pass, and add a line to the change log.

## Change log

- 2026-09-25: Created from front-end best practice research.
- 2026-09-25: Reframed around moving from a Claude artifact to a real repo; added nesting and patterns, prototype matching, the design and code loop, and learning mode.
- 2026-09-26: Added growth mindset, self-review, and self-healing.