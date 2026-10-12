# GitHub ruleset cheat sheet

**Last updated:** October 12, 2026

Every new repo gets one ruleset, "Protect main." Importing the ready-made file takes about a minute.

- Main can't be deleted or rewritten.
- Every change reaches main through a pull request.
- You can still merge your own pull requests.

## Fastest: import the file

1. In the repo, open **Settings**.
2. In the sidebar, under "Code and automation," click **Rules › Rulesets**.
3. Click **New ruleset**. It opens a menu.
4. Choose **Import a ruleset**, not "New branch ruleset."
5. Pick [`ruleset-protect-main.json`](ruleset-protect-main.json).
6. Check the screen against the table below.
7. Click **Create**.

## Filling it in by hand

| Field | Set it to | Why |
|---|---|---|
| Ruleset name | Protect main | Says what it does |
| Enforcement status | Active | "Disabled" saves it but does nothing |
| Bypass list | Leave empty | No one skips the rules, including you |
| Target branches | **Add target**, then **Include default branch** | Only main. Protecting every branch blocks Claude's working branches. |
| Restrict deletions | On | Main can't be deleted |
| Block force pushes | On | Main's history can't be rewritten |
| Require a pull request before merging | On, with **Required approvals** at 0 | Every change goes through a pull request. At 1, you couldn't merge your own. |
| Require status checks to pass | Off | Turn it on only once the repo has tests that run on pull requests |
| Automatically request Copilot code review | On | Optional second look on every pull request |
| Every other rule | Off | Not needed for a solo repo |

## When to change it

| If this happens | Change this |
|---|---|
| The repo gets tests that run on pull requests | Turn on **Require status checks** and add each test's name |
| Someone else starts working in the repo | Set **Required approvals** to 1 |
| The repo holds client work | Keep it private as well. A ruleset doesn't hide anything. |
