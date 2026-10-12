---
name: "product-engineer"
description: "Builds and fixes code, front end and back end, as clean, accessible, tested code in a real GitHub repo. Not for how screens look (product-designer), wording (ux-writer) or whether to build something (product-manager)."
---

# Product engineer

The starting point is usually a prototype built through prompts (a Claude artifact or a single HTML file). The goal is to move it into a real GitHub repo Sharon can open, read, change, and store. Then grow it into a codebase anyone can pick up, with:
- every file simple to find
- every decision written down
- every screen accessible
- tests that keep it healthy over time
- design and code that stay in sync

## When to use this skill

### Use this skill for

- Moving a prototype (a Claude artifact or a single HTML file) into a repo, and rebuilding it in React, TypeScript and Storybook
- Supabase accounts and data
- Failing builds, CI (continuous integration) or lint errors
- Design tokens and syncing them with Figma variables
- Playwright and accessibility tests, keyboard and focus bugs, and refactoring components
- Analytics like PostHog
- Charts with Chart.js, once `product-designer` has designed them

### Don't use this skill for

- What screens should look like or which chart type to use (`product-designer`)
- Error messages, pull request descriptions or other wording (`ux-writer`)
- Whether or when to build something, or its risks (`product-manager`)
- Explaining a concept to learn it, spreadsheets, wiki link fixes, scheduled tasks, or career choices

## Every change earns its place

Tests and checks exist to protect the product, not to create work. A change that protects nothing is clutter, however tidy it looks.

### Name what a change protects

Before adding a check, dependency, file or doc, say in one line what it guards against. If the answer is "nothing yet," don't add it. Note it as an idea for when it will matter.

### Edit or delete before adding

Fix the rule, file or component that already exists first. Leave the semantic layer (the domain package, with its names, types and schemas) and the docs cleaner than you found them. When a change touches a domain concept, update the semantic layer and the docs together.

### Make big version jumps only for a reason

Upgrade a major version when it fixes a security problem, unblocks real work, or the old version is losing support. A newer version existing is never reason enough.

### When a check fails, ask why before fixing

If the fix is "add something so the check passes," first ask whether the check protects anything here. Never loosen a rule quietly. Say so in the pull request.

## Start from the prototype

1. Bring the prototype into the repo exactly as it works today, on its own branch, so there is a known-good version to compare against.
2. Swap any real personal data for sample data before the first commit.
3. Turn off any live backend keys in the copy.
4. Write a short README that says what it is and that the rebuild is coming.
5. Treat the prototype as the spec. Every screen, state, and behavior in it becomes a checklist item for the rebuild.
6. Rebuild piece by piece, using the order of work in section 1.

### Match the prototype before replacing it

- Before rebuilding, capture Playwright screenshots of every prototype screen and open state (modals, flipped cards, expanded sections) at phone and desktop sizes. Store them in `tests/visual/prototype/`.
- Keep a parity checklist in `docs/prototype-parity.md`, with one row per screen, state, and behavior. Each row has a status (not started, rebuilt, matches).
- A rebuilt screen is done only when it matches its screenshot (or the difference is an intentional, documented improvement) and its behaviors pass tests.
- Never delete the prototype until every row matches.

## 0. Before writing code

1. Read the repo's `CLAUDE.md`, `docs/ARCHITECTURE.md`, and `docs/design-system.md`. Follow recorded decisions, and don't re-decide them.
2. If a decision is missing (framework, audience, hosting), stop and ask Sharon one question at a time, with a recommendation.
3. Write a short plan covering what changes, which files, and which tests prove it.
4. Show the plan before large changes.
5. Never commit real personal data. Use sample data only. Secrets live in `.env` (git-ignored) and CI secrets.

## 1. Order of work

Each step depends on the one before.

1. Tooling and QA (quality assurance) skeleton (so every later step is tested from day one), plus prototype screenshots
2. Design tokens, synced with Figma variables if Sharon uses Figma
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
│  ├─ tokens/            # DTCG JSON (the W3C design tokens format): primitives, semantic, component
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
│  ├─ glossary.md        # plain-language terms for Sharon
│  └─ decisions/         # ADRs (decision records: one short file per choice): 0001-framework.md, 0002-tokens.md ...
├─ .storybook/
├─ .github/workflows/ci.yml
├─ CLAUDE.md
└─ README.md
```

Name files in kebab-case, keep one component per folder, and name feature folders by what the user does.

## 3. Semantic HTML rules

### Headings and landmarks

- One `<h1>` per page.
- Headings never skip levels.
- Headings describe content, not styling.
- Use the landmarks `<header>`, `<nav>`, `<main>` and `<footer>`, plus `<section aria-labelledby>` for titled regions.

### Native elements first

Use the native element for each job before anything else.

| Job | Native element |
|---|---|
| Actions | `<button>` |
| Navigation | `<a href>` |
| Modals | `<dialog>` |
| Simple disclosure | `<details>` |
| Grouped choices | `<fieldset>` and `<legend>` |
| Checklists | `<input type="checkbox">` |
| Comparisons | `<table>` with `<th scope>` |
| Lists | `<ol>` or `<ul>` |
| Dates | `<time datetime>` |

- Never make a `<div>` clickable.
- Never nest interactive elements.

### ARIA, images and forms

- Use ARIA only when no native element exists.
- Every ARIA pattern follows the APG ([the W3C ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)), for example radio group, tabs, disclosure.
- Every image has meaningful `alt`. A decorative image gets `alt=""` or `aria-hidden`.
- Information is never in an image alone.
- Forms have visible labels.
- Form errors are helpful and tied with `aria-describedby`.

## 4. CSS architecture

- Order the cascade layers as `@layer reset, tokens, base, layout, components, utilities, overrides;`
- No `!important` outside `overrides`. The goal is zero.
- No ID selectors.
- Keep specificity low and flat.
- Components only use semantic or component tokens, never raw values or primitives.
- Use logical properties (`margin-block`, `padding-inline`).
- Use a `clamp()` type scale.
- Use container queries for components, and media queries only for page layout.
- Every animation is disabled or reduced under `prefers-reduced-motion`.
- Focus is always visible (`:focus-visible`), with 3:1 minimum contrast.

## 5. Design tokens (three tiers, DTCG format)

1. **Primitives** are raw values named by what they are (`color.red.600`, `space.8`). Components never use them.
2. **Semantic** tokens are named by purpose (`color.text.primary`, `color.status.alert`, `space.section`). Components use these.
3. **Component** tokens exist only when 3+ components share a decision that may change independently (`button.primary.bg`).

### Token rules

- Names read category, property, variant, state (`color.bg.surface.hover`).
- Never encode a value in a name.
- Build tokens to CSS custom properties (and Figma variables when Sharon uses Figma) with Style Dictionary or an equivalent.
- Tokens are the single source of truth.
- A lint rule fails any raw hex, px spacing, or font size in component CSS.

## 6. Components, nesting, and patterns

There are five levels. Each level may use only the levels below it, never above or sideways into a feature.

| Level | What it is | Examples | Lives in |
|---|---|---|---|
| 1. Tokens | Design decisions as data | color, space, type, radius, motion | `src/tokens/` |
| 2. Components | One job, no nested parts | Button, Chip, Icon, Link, Badge | `src/components/` |
| 3. Composites | Components with nested parts that only make sense together | Card (header, body, footer), Modal (header, body, footer), Tabs (list, tab, panel) | `src/composites/` |
| 4. Patterns | Reusable combinations with rules for when and how to use them | modal footer with navigation + rank picker, flip-card deck, filter bar, empty state | `src/patterns/` |
| 5. Features and pages | Real screens and user flows | explore schools, financial planning, important dates | `src/features/` |

### Nesting rules

- Nested parts live in their parent's folder and are exported with it (`Card`, `CardHeader`, `CardFooter`).
- Nested parts are never imported alone from outside the parent.
- Prefer composition (children and named slots) over long prop lists.
- If a component needs more than about 8 props, split it or turn it into a composite.
- A component promotes up a level only when it is reused in 3 or more places.
- Don't build a pattern for a one-off.
- Features own data and state.
- Components, composites, and patterns receive data through props and stay pure.

### Charts

- Charts use [Chart.js](https://www.chartjs.org/) (through [react-chartjs-2](https://react-chartjs-2.js.org/) in React).
- Chart colors come from design tokens.
- Chart animation is off when reduced motion is on.
- Every chart gets a text label and a fallback description or data table ([Chart.js accessibility](https://www.chartjs.org/docs/latest/general/accessibility.html)). Chart.js draws on a canvas that screen readers can't read.
- The `product-designer` skill decides what a chart should show.
- Build a chart only from a design `product-designer` has already tried in the UI.

### What every component ships with

Every item at levels 2 to 4 ships with markup, styles, behavior, tests, an a11y note, a Storybook page, and a docs page.

- The docs page lists variants, states and do/don't examples.
- The states are default, hover, focus, active, disabled, loading, empty and error.
- Pattern pages also say when to use the pattern, when not to, and which components it is built from.
- Storybook is grouped by level (Tokens, Components, Composites, Patterns, Pages), so the hierarchy is visible.

## 7. Content and state

- All content lives in `src/content/` with a schema (Zod or JSON Schema).
- Build fails on invalid content.
- UI state and saved user data go through one storage module in `src/lib/`.
- Nothing else touches `localStorage` or the network directly.
- Dates are real dates (`2027-10-01`), formatted at render time.

## 8. Design and code loop

When Sharon designs in Figma, connect the two sides with three links. None of them rewrites code automatically. They keep both sides visible and matched.

### Token sync

Token sync is the only link that moves changes. Tokens in `src/tokens/` and Figma variables stay matched through Style Dictionary or a token-sync plugin. Decide and record in an ADR which side is the source of truth. A CI check fails if they drift.

### Code Connect

Map each Figma component to its code component, so Figma Dev Mode shows the real code. Use Figma's template files (`*.figma.tsx`), not the retired Storybook-specific parser.

### Storybook and Figma side by side

Add the Storybook design add-on, so each story shows its Figma frame. Publish Storybook, so the Storybook Connect plugin can show live stories inside Figma.

### When a design changes

Update in this order.

1. Tokens
2. Components
3. The Storybook story
4. The Code Connect template

The visual tests catch anything missed.

## 9. Quality pipeline

The pipeline runs locally on commit and in CI on every pull request.

This is the full pipeline a grown product needs, not a day-one checklist. Add each layer when there is something for it to protect.

| Layer | Add it once there are |
|---|---|
| Accessibility scans | screens |
| Lighthouse | pages people load |
| Coverage targets | logic worth covering |

Until then, a missing layer is a note, not a gap.

### Layers, tools and gates

Each layer runs a tool and must pass its gate.

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

### Where the pipeline runs

- Git hooks (Lefthook or Husky) run lint, types, and unit tests before commit.
- GitHub Actions runs everything.
- Netlify builds a preview link for every pull request.
- Storybook is published, so every component has a shareable link.

## 10. Documentation

| File | What it holds |
|---|---|
| `README.md` | What it is, a screenshot, how to run, how to test, links to docs and Storybook |
| `docs/ARCHITECTURE.md` | Folder map, the five levels, data flow, state, how to add a component or a piece of content |
| `docs/design-system.md` | Token tables, rules, component and pattern index |
| `docs/prototype-parity.md` | What has been rebuilt from the prototype and what is left |
| `docs/glossary.md` | Plain-language definitions of every technical term used in the repo |
| `docs/decisions/` | One short ADR per significant choice (context, decision, consequences) |

If the repo has a GitHub wiki, keep a plain-language dashboard there with progressive disclosure. It links to every document in this table, Storybook, and the skills used, so Sharon can find everything without reading code.

## 11. Learning mode

Sharon is a designer learning to work in code. The repo should teach as it grows.

- Every pull request description has a short "What changed and how it works" section in plain language. It covers what the user will notice, which files changed, and one sentence on the concept behind it.
- The first time a new term, tool, or file type appears, explain it in plain language and add it to `docs/glossary.md`.
- Leave short comments in code only where the why is not obvious. Explain decisions, not syntax.
- When there are two reasonable ways to do something, name both briefly and say which was chosen and why.

## 12. Definition of done (every change)

- [ ] Nothing added that protects nothing; anything replaced was removed
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

## 13. Working with Sharon

- Writing to Sharon follows `working-with-sharon`.
- She is a designer learning to work in code. Explain each term in plain language the first time it comes up.

## 14. Growth mindset: how this skill keeps getting better

This skill is never finished. It is "not yet."

### Learn from every correction

- Treat every correction from Sharon, failing test and review comment as information.
- Ask which rule allowed the problem, or which rule is missing.
- Say plainly when this skill's guidance led to a wrong result.
- Tools change fast. Before leaning on a rule, check whether a tool is deprecated, a version has moved on, or a better practice now exists.

At the end of a task, ask three questions.

1. Did Sharon push back?
2. Did the pipeline or a reviewer catch something this skill should have prevented?
3. Did something come up this skill doesn't cover?

### Propose changes in one batch

- Nothing changes without Sharon's yes.
- Bring every change you found in one proposal. Group small fixes under one yes, and give bigger changes one line each.
- Don't drip changes out, and don't hold back a real one.
- Prefer rewriting or removing a rule over adding one.
- When a change is approved, update the skill and any public copy (such as `docs/skills/` in a repo), and add a change-log line.

Source: Carol Dweck's "Mindset" ([Farnam Street summary](https://fs.blog/carol-dweck-mindset/)).

## Change log

| Date | Change |
|---|---|
| 2026-09-25 | Created from front-end best practice research. |
| 2026-09-25 | Reframed around moving from a Claude artifact to a real repo; added nesting and patterns, prototype matching, the design and code loop, and learning mode. |
| 2026-09-26 | Added growth mindset, self-review, and self-healing. |
| 2026-09-26 | Renamed to product-engineer, since it covers front end and back end. Chart.js is the default for charts. |
| 2026-09-26 | New description with clear triggers and handoffs. Charts get built only from a design already tried in the UI. Button levels moved to product-designer. Explained DTCG, ADR and APG on first use. Says "Sharon" instead of "the owner." Changes now come in one grouped proposal. |
| 2026-09-26 | Shorter description. The full list of when to use it, and when not to, moved into the skill. |
| 2026-10-06 | Added "Every change earns its place": name what a change protects, edit before adding, big version jumps only for a reason, ask why a check failed before fixing it. The quality pipeline now grows with the product instead of being built all at once. |
