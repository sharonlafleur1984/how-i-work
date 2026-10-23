---
name: meeting-project-update
description: Update a project’s wiki, live task tracker and shared workspace after a meeting, using confirmed decisions and open questions from its notes.
---

# Update a project after a meeting

Keep the project’s current work, decisions, questions and forecast consistent across its repository, live project tracker and shared workspace. Use Sharon’s ux-writer, working-with-sharon and product-manager skills, plus the project’s voice guidance.

## Read the project context

Resolve the repository, task tracker and shared workspace from the current request or established project context. Read their instructions and current content before editing. Use the repository’s established wiki publishing workflow.

Read the meeting transcript or participant recap. Archive available transcripts and recordings in the project’s authorized local storage, preserving source and coverage. Keep private source material out of public repositories. A meeting time or unreadable link establishes no decisions.

Compare the source with current records and open update pull requests. Preserve IDs, prior decisions and unrelated content. Repeated runs must not create duplicate questions, tasks, decisions or pull requests.

## Reconcile the meeting

- Current focus owns immediate priorities, review preparation and reference links.
- Decisions owns confirmed choices, their date, decision maker, reason, scope and source. Link superseding decisions without erasing history.
- Questions owns unresolved inputs whose answers change the work, with an answer owner and what each answer changes.
- Meeting notes owns the dated recap and action items; update the index when adding a record.

Keep proposals distinct from approvals and work-planning choices distinct from client decisions. Log durations only when supplied; do not infer working time from activity timestamps.

## Update all affected destinations

1. Update repository wiki sources and relevant issue bodies.
2. Update the live project tracker’s item order, applicable statuses, prerequisites, estimates and roadmap date fields.
3. Update the shared workspace’s current focus, decisions, meeting record and forecast where relevant.

A wiki merge does not reorder a project. Inspect the live view’s filters, grouping, sorting and date fields. Move existing items instead of duplicating them. Check that newly added tasks appear in the intended roadmap group.

When priorities change the forecast, use the established capacity, holidays and remaining-work assumptions. Label provisional estimates. Shift dependent work and roll up parent dates without counting parent hours again. Preserve completed work and historical starts.

Use the same finish date and scope across the planning issue, project overview, wiki and shared workspace. Name unscoped work excluded from the estimate. Keep stretch goals distinct from commitments.

## Publish and verify

Use a branch and the project’s pull-request workflow. An independent reviewer checks preserved meaning when rewriting existing content. Run Sharon’s writing checker and review links and IDs.

Verify each affected destination after saving: repository commit or pull request, live tracker order and dates, and shared workspace content. After an authorized merge, check the wiki publishing result. A failed publish is unfinished work.

Keep a partial update incomplete and record what remains. Reconcile saved state before retrying; never replay successful writes blindly. Report the saved result and any unresolved gap without claiming the whole update is done.

## Automatic meeting updates

A skill does not schedule itself. Use it under an explicitly authorized automation or meeting follow-up request. Keep the source and processed-content fingerprint in the automation’s authorized local state only after all affected destinations are verified.

Stay quiet when no substantive evidence changed. Report new access blockers once, leave unreadable content unprocessed and retry on later runs. Do not merge pull requests, message others or change sharing permissions unless separately authorized.
