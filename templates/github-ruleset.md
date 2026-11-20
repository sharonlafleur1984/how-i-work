# GitHub ruleset cheat sheet

**Last updated:** November 19, 2026

Every new repo gets one ruleset, "Protect main." Importing the ready-made file takes about a minute.

- Main can't be deleted or rewritten.
- Branches merge straight into main daily, with no pull request.
- Only main is protected, so working branches can be deleted once merged.

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
| Require a pull request before merging | Off | Branches merge straight into main daily |
| Require status checks to pass | Off | The checks run on the Mac before every push |
| Every other rule | Off | Not needed for a solo repo |

## When to change it

| If this happens | Change this |
|---|---|
| Someone else starts working in the repo | Turn on **Require a pull request**, with **Required approvals** at 1 |
| The repo holds client work | Keep it private as well. A ruleset doesn't hide anything. |
