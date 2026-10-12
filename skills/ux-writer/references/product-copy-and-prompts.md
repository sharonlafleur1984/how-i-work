# Product copy and prompts

Part of the `ux-writer` skill, sections 8 and 9. Read this before writing interface copy (buttons, errors, empty states, money and deadline messages, celebrations, sensitive questions, step-by-step flows) or a prompt for an AI.

## 8. Product copy

Give people an immediate action. Whenever something is empty or wrong, the fix is one tap away, not only described.

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

### When to add words

Add words only when a newer user would struggle or the next step isn't obvious. Longer explanations go in help or docs. Say what people can do, not what they can't.

### Step-by-step flows

Onboarding and setup go one question at a time.

- Ask one question per step, the way a helpful person would ask it.
- Use earlier answers: "Since you're open to other states..."
- Signpost the end: "Last question."
- Remember answers, and never ask twice.
- Don't get chatty. "That's a great choice! Now let me just..." wastes their time.
- Don't go step by step where people need to compare everything at once, like schools.

Sources: [NN/g, empty states](https://www.nngroup.com/articles/empty-state-interface-design/), a Couchbase UI copy guide and a conversational UI article (both unpublished sources).

## 9. Prompts for AI

Prompts are writing too, for an AI reader. When someone asks for a prompt or shares one, offer a stronger version in one line if key parts are missing.

- **Context comes first:** who it's for, the product stage and the constraints. `<context>` and `<task>` tags keep it clear.
- **Design prompts** name the component, layout, visual style, content, tech stack, every state (loading, empty, error, success, hover, focus), accessibility, what changes on small screens, and a reference ("like Linear").
- **Copy prompts** name the voice file, the audience, the user's goal and what can go wrong, character limits, verb-first buttons, and recovery steps.
- **Keep design and copy prompts separate,** then combine the results.
- **Use realistic content,** never lorem ipsum.
- **Iterate in order:** structure first, then visuals, then polish.
- **Save prompts that work** in the project's prompt library.

Sources: [copyprompt.io](https://copyprompt.io/blog/ai-prompts-for-designers-2026), [Superdesign](https://superdesign.dev/blog/ui-design-prompts), and articles from Fardino and Techpresso's AI Academy (unpublished sources).
