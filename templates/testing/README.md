# Starter test kit

**Copy it into a new repo** once the repo has code worth protecting. Each file says where it goes.

| File | Goes in | What it does |
|---|---|---|
| [vitest.config.ts](vitest.config.ts) | repo root | Runs every `*.test.ts(x)` file in `tests/` |
| [tests/setup.ts](tests/setup.ts) | `tests/` | Starts each test clean, with stand-ins for what the test browser lacks |
| [tests/global-setup.ts](tests/global-setup.ts) | `tests/` | Builds generated files once, before any test runs |
| [tests/css.ts](tests/css.ts) | `tests/` | One shared way for tests to read CSS |
| [tests/css-rules.test.ts](tests/css-rules.test.ts) | `tests/` | No `!important` (except to honor reduce motion, forced colors or more contrast), no ID selectors, logical spacing |
| [tests/axe.test.tsx](tests/axe.test.tsx) | `tests/` | Fails on any axe accessibility issue on the main page |
| [test.yml](test.yml) | `.github/workflows/` | Runs the tests on every pull request |

## Set up

1. Copy the files.
2. Install the tools: `npm install -D vitest jsdom @testing-library/react @vitejs/plugin-react axe-core`
3. Add `"test": "vitest run"` to the scripts in `package.json`.
4. In `tests/axe.test.tsx`, point the import at the repo's main page.
5. Run `npm test`. Fix what fails before relying on it.
6. Once `test.yml` has run on a pull request, turn on **Require status checks** and add **test** ([ruleset guide](../github-ruleset.md)).

## Rules the kit follows

- **Tests only read shared files.** Anything generated is built once in `global-setup.ts`. Test files run in parallel, so a test that rebuilds a file can catch another one mid-write.
- **Every dependency installs from npm or GitHub.** A `file:../other-repo` dependency exists only on your Mac, so the pull request check can't install it.
- **Each check guards something.** Leave out a test that has nothing to protect yet.
