---
name: "motion"
description: "Plans, specs and reviews UI motion (transitions, micro-interactions, animated states and data or audio-driven visuals), teaches Figma Motion, and turns Figma animations into code. Sharon never has to learn a code library."
---

# Motion

Every animation helps someone understand what happened, or it gets cut. AI agents write animation code that feels generic without a written spec of timing, easing and triggers ([Emil Kowalski](https://emilkowal.ski/ui/agents-with-taste)). This skill is that spec.

In short:
- a job for every animation (section 1)
- timing and easing from section 2, stored as tokens
- reduced motion built in, never added later (section 3)
- a short spec per animation (section 4)
- one tool for Sharon, Figma Motion; every library for Claude Code (section 5)
- how-to guides for Figma Motion (section 6), Figma Motion into code (section 7) and Claude Motion (section 8)

## When to use this skill

Use it for:
- transitions, micro-interactions, hover and press states, loading and progress
- moving between views (compact to expanded, panel open and close)
- charts, meters, waveforms and anything driven by live data or audio
- teaching Sharon a Figma Motion step, or doing it with her
- turning a Figma Motion animation into code
- short explainer animations and animated charts for decks (Claude Motion)
- reviewing motion in a design, prototype or build
- choosing an animation tool or library

Don't use it for:
- what a screen looks like or how it's organized (`product-designer`)
- wording on screen (`ux-writer`)
- wiring code beyond the motion itself (`product-engineer`)

## 1. Every animation needs a job

An animation earns its place only if it does one of these:
- **Feedback:** confirms an action worked (a press, a save).
- **State change:** shows something changed (playing, listening, loading).
- **Spatial origin:** shows where something came from or went (a panel sliding from its button).
- **Attention:** points to the one thing that matters now. Use rarely.

Don't animate:
- actions people repeat many times a day, or trigger from the keyboard ([Emil Kowalski](https://emilkowal.ski/ui/you-dont-need-animations))
- anything only because it's possible
- intros that make people wait for content

If the job isn't clear in one sentence, cut the animation.

## 2. The numbers

### Duration

| Change | Duration |
|---|---|
| Small feedback (press, toggle, hover) | 100 to 150ms |
| Medium (dropdown, tooltip, small panel) | 150 to 250ms |
| Large (modal, page or view change) | 250 to 400ms |
| Fades of text or overlays | up to about 500ms when it must feel gentle |

By 500ms, UI motion starts to feel like a drag ([NN/g](https://www.nngroup.com/articles/animation-duration/)). Exits are shorter than entrances.

### Easing

- **Entering:** ease-out (fast start, gentle stop).
- **Leaving:** ease-in.
- **Moving on screen:** ease-in-out.
- **Dragged or interruptible things:** a spring, so it can change direction mid-move.
- Never linear, except for progress bars, spinners and anything tied to real time, like a playhead.
- "Back" easings (overshoot) and bouncy springs are for rare, playful moments only.

### Performance

- Animate only transform and opacity when possible. They stay smooth.
- Animations can be interrupted. A second click never waits for the first animation to finish.
- Heavy visuals (waveforms, meters, glows) stay smooth during audio or video playback, or they get simplified.

### Loading

- Content loading: a skeleton screen shaped like the content that's coming.
- Known duration or known steps: a progress bar.
- Progress shows real progress, per section 3.

### Tokens

Durations and easings are design tokens (for example `motion.duration.fast`, `motion.easing.enter`), never one-off values ([Design Tokens Community Group format](https://www.designtokens.org/tr/drafts/format/)). A product uses a small set, about 3 durations and 3 easings. In Figma, these live as easing variables and custom animation styles (section 6).

## 3. Reduced motion and truthfulness

- Respect the reduced-motion setting everywhere ([WCAG 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html), [W3C C39](https://www.w3.org/WAI/WCAG22/Techniques/css/C39)).
- With reduced motion, replace movement with an instant change or a short fade. Never remove information.
- Nothing flashes more than 3 times a second.
- Motion never carries meaning alone. Pair it with a label, icon or state text.
- **Data-driven visuals show real data.** A chart, meter or waveform that looks live must be live, with no fake readings. Never present a static image as live data.
- Every chart also shows its key numbers as text.

## 4. The motion spec

Fill this in with Sharon, one animation at a time. Claude Code builds from it.

| Field | Answer |
|---|---|
| Element | What moves |
| Job | Feedback, state change, spatial origin or attention (section 1) |
| Trigger | What starts it (click, load, data change, voice state) |
| From and to | Start and end state |
| Duration and easing | Token names from section 2 |
| Exit | How it leaves, if it leaves |
| Interrupted | What happens if triggered again mid-animation |
| Repeats | Plays once or loops, and whether it changes after repeated use |
| Reduced motion | The replacement |
| Figma link | The frame with the animation, if one exists |

The fields follow Dan Saffer's microinteraction model of trigger, rules, feedback and loops ([Microinteractions](https://microinteractions.com/)). Keep specs short. If a field doesn't apply, write "none." Figma Motion doesn't record the trigger, exit states or reduced-motion behavior, so the spec always carries those.

## 5. Tools: Sharon learns one, Claude Code handles the rest

Sharon's time goes to judgment, not libraries. Never ask her to learn a code library.

**Sharon designs in Figma Motion** (section 6). **Claude Code builds** from the spec and the Figma link (section 7), picking the simplest tool that does the job:

| Need | Tool |
|---|---|
| Simple hover, press, fade, slide | Plain CSS transitions |
| Moving between views or pages | CSS View Transitions, with a fallback |
| React UI motion, springs, layout changes | Motion library ([motion.dev](https://motion.dev)) |
| Audio waveforms, regions, A/B compare | wavesurfer.js |
| Live meters, spectrum, custom data visuals | Canvas, fed by real data (Web Audio API for live audio) ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Visualizations_with_Web_Audio_API)) |
| Interactive illustrations that react to input | Rive, only when the art itself must respond |
| Linear decorative playback | Lottie, exported from Figma Motion |
| Short explainer video or animated chart for a deck | Claude Motion (section 8), if the plan has it |

Follow these rules when picking a tool.
- Fewer tools is better. Don't add a library a simpler tool already covers.
- Check the license before using a library in client work. Avoid AGPL libraries in commercial products.
- AI video generators (Runway, Kling, Veo and similar) make flat video for marketing, not working UI. Don't use them for interface motion.
- Tools change monthly. Re-check a pick before recommending it for a new project.

## 6. Figma Motion: how to use it

Figma Motion is in open beta, so steps change. If a step doesn't match what Sharon sees, check [Figma's help center](https://help.figma.com/hc/en-us/articles/41405906446999). When Sharon asks how to do something, give the one next step, not the whole section.

A missing or grayed-out control may need a paid plan. The Figma agent, Dev Mode handoff, and exports over 1920x1080 or 30 frames per second all do ([Figma blog](https://www.figma.com/blog/introducing-figma-motion/), [export](https://help.figma.com/hc/nl/articles/41307983648407), [handoff](https://help.figma.com/hc/en-us/articles/41296356954263)).

### Open the timeline

1. Switch the toolbar toggle to **Motion**. The timeline appears across the bottom of the screen.
2. Animated layers must be inside a frame. The top-level frame (placed directly on the canvas) owns the timeline.

Timeline controls, left to right ([source](https://help.figma.com/hc/en-us/articles/41405906446999)):
- **Play/pause:** button or Spacebar.
- **Auto-keyframe:** records every change as a keyframe while on.
- **Current time:** type a value to jump the playhead.
- **Duration:** defaults to 2000ms. Type a value or drag the handle on the right.
- **Time unit:** toggles seconds and milliseconds. Use milliseconds for UI work.
- **Playback mode:** Loop, Once or Ping-pong.
- **Collapse layers:** folds all layer tracks.

Zoom the timeline with a trackpad pinch or Command plus the mouse wheel. Each animated object has a layer track. Drag the track to move it in time, or drag its ends to change the duration of everything on it.

### Fastest path: preset animations

For most UI work, start here, not with keyframes ([presets](https://help.figma.com/hc/nl/articles/41307886266135)).

1. Select the layers.
2. Click **+** in the **Animations** section of the right sidebar.
3. Pick a type (fade, move, scale and others) and set its options.
4. Or click **Animations** to add a composite style, which applies several presets at once.

The new animation lands at the playhead. Drag it to change when it starts, and drag its ends to change its duration. Click it to change type, settings, duration or easing.

### Keyframes, for anything presets can't do

A keyframe sets a property's value at a moment. Two keyframes make a move, and Figma fills in between ([keyframes](https://help.figma.com/hc/en-us/articles/41307938657559)). Properties that can animate show a diamond next to their field in the right sidebar.

Manual method:
1. Move the playhead to the start.
2. Click the diamond next to the property.
3. Type the start value.
4. Move the playhead to the end and type the end value. A second keyframe appears.
5. Press Spacebar to preview.

Auto-keyframe method: turn on auto-keyframe (a red bar appears on the timeline), move the playhead, then change values. Every change while it's on becomes a keyframe, including accidents, so turn it off when done.

Working with keyframes:
- Hollow diamond is unselected, filled is selected. Shift-click or drag a box to select several.
- Double-click a keyframe to jump the playhead to it, then edit its value in the sidebar.
- Closer keyframes mean faster motion.
- Hold Shift while dragging keyframes to snap them to the playhead or to other keyframes.
- Delete removes a selected keyframe. Select a property's row and press Delete to clear all its keyframes.

### Set easing in Figma

Click an animation, or the line between two keyframes, then use the **Easing** menu ([easing](https://help.figma.com/hc/en-us/articles/41414048690839)).

| Menu option | Matches section 2 |
|---|---|
| Ease out | Entering (the default) |
| Ease in | Leaving |
| Ease in and out | Moving on screen |
| Spring presets (Gentle, Quick, Bouncy, Slow) | Interruptible motion; start with Quick |
| Linear | Progress bars, spinners |
| Hold | A jump with no transition, for snapping between states or a rhythm |
| Ease out back | Overshooting entrance, for rare playful moments |
| Ease in back, ease in and out back | Wind-up before an exit or move, also rare |
| Custom bezier | Exact curve from the spec; type the cubic-bezier value or drag the handles |
| Custom spring | Set the Bounce value |

Save custom curves and springs as **easing variables** so every file shares them. Variables can have modes, switched at the page level, which update every animation that uses them ([Figma blog](https://www.figma.com/blog/introducing-figma-motion/)).

### Reusable motion: styles and components

- **Custom animation styles** save easing, duration and other settings for reuse. Combine them into bigger patterns and publish them to a library ([update](https://forum.figma.com/product-updates-3/motion-adds-custom-styles-audio-text-animations-and-lottie-export-58554)).
- Styles are how motion tokens live in Figma.
- **Animated components** carry their motion into every file that uses them.
- The Figma agent and coding agents can apply published styles automatically.

### Text, audio and shaders

- **Text animations:** animate characters, words or lines. The text stays editable.
- **Audio:** drag an audio file onto the timeline, then trim, split and line it up with keyframes. Audio exports with MP4 and WebM.
- **Shaders:** every property a shader exposes can be keyframed.

### The Figma agent

On paid plans, the agent builds motion on the timeline from a prompt ([Figma blog](https://www.figma.com/blog/introducing-figma-motion/)).
- It can also critique an animation, adjust easing and timing, or rebuild it.
- Prompt it with the motion spec fields from section 4.
- Check its result against the numbers in section 2.

### Export

1. Select the top-level frame (it shows a Motion icon).
2. In the **Export** section, open the **Animated** tab.
3. Pick a format and settings.
4. Click **Export**, then **Download**.

| Format | Use it for | Settings |
|---|---|---|
| MP4, WebM | Portfolio reels, reviews, sharing | Size, frame rate, quality |
| GIF | Docs, Slack, quick shares | Size, frame rate, loop or once |
| SVG | Simple vector animation | Size, frame rate |
| Lottie (JSON) | One animation for an app or site | |
| dotLottie | Compressed, multiple animations, bundled assets | |

Lottie limits ([Figma](https://help.figma.com/hc/nl/articles/41307983648407), [LottieFiles](https://docs.lottiefiles.com/en/integrations/figma/04_figma-to-lottie/figma-motion-export)):
- Exports cleanly: position, opacity, size, corner radius, solid colors, stroke weight, trim paths, drop shadow, layer blur, masks, text movement and opacity, linear, custom and hold easing.
- Check in preview first: springs, rotation and scale with custom pivots, some gradients, complex layouts.
- Doesn't export: shaders, video, angular gradients, animated gradients, animated text content, background blur, inner shadow, glass and noise effects. Shadows, glass and noise freeze on the first frame.
- Always test in the Lottie player the product will use.

### Handoff to developers

Developers copy code from Dev Mode ([handoff](https://help.figma.com/hc/en-us/articles/41296356954263)).
1. Select the animated frame.
2. Open the Motion tab in the Inspect panel. Show in timeline view gives a read-only timeline.
3. Under Code, pick CSS, React or JSON.
4. Click Copy.

React code uses the Motion library, so the project needs `motion` installed ([motion.dev](https://motion.dev/docs/figma)). Coding agents get the frame link instead (section 7).

### Practice

Before a real project, suggest the Figma Motion playground file in the Figma Community ([presets](https://help.figma.com/hc/nl/articles/41307886266135)).

## 7. Reading Figma Motion into code (for Claude)

When Sharon shares a Figma link to an animated frame, Claude reads the motion through the Figma MCP server instead of guessing.

Read the motion:
1. Parse `fileKey` and `node-id` from the URL, changing `-` to `:` in the node id. Start a Figma session first, per the Figma MCP instructions.
2. Call `get_design_context` for the static layout.
3. Call `get_motion_context` with `recursive=true`. It returns the animated layers, keyframes with easing, ready-made CSS and motion.dev snippets, and `timelineCohorts` for animations that play together.

Build it:
1. Use the snippet values exactly: timing, easing, keyframes and `transformOrigin`. Don't regenerate them, and don't invent motion for layers with no data.
2. Match each animated layer to its element by exact node id before trying a fallback id. A fallback id is shared by every copy of a component, so using it animates all of them.
3. Use the project's existing motion library before adding Motion.
4. Build one animation end to end and check it before doing the rest.
5. Add the trigger and reduced-motion version from the spec, since Figma doesn't store them.

Pitfalls ([figma-implement-motion skill](https://mcpservers.org/zh-CN/agent-skills/figma/mcp-server-guide/figma-implement-motion)):
- If an element already has a static rotation, animate the offset, not the absolute value.
- Tailwind centering (`-translate-x-1/2`) shares `transform` with Motion. Use a static wrapper or Motion's `x: "-50%"`.
- In text animations, `startMs` already includes the delay. Don't add it twice.
- For coordinated motion, drive every member from the cohort's duration and loop mode.
- If a layer can't animate in code, leave a TODO naming its node id and tell Sharon. Never drop it silently.

To make a video for review, `export_video` renders a timeline to MP4. Pass the top-level frame, not a nested layer.

## 8. Claude Motion

Claude Motion turns content into short animations, like an explainer, an animated chart for a deck, or a product walkthrough ([Claude Help Center](https://support.claude.com/en/articles/17454997-get-started-with-claude-motion)).

### What it is and isn't

- Each animation is code that animates text, charts, shapes and images, and it plays like a short video. Change one word, number or timing and the rest stays the same.
- It doesn't make realistic footage or people. It's not a tool for product UI, live avatars or interactive motion.
- Good uses for Sharon: portfolio case-study reels, animated charts for a pitch, explaining a flow to a client.

### Who has it

Claude Motion is only on Team and Enterprise plans, and Sharon's account doesn't have it as of October 2026 ([SmartScope](https://smartscope.blog/en/blog/claude-motion-free-pro-max-availability-use-motion-2026/)). Until it does, use Figma Motion's MP4 export for reels.

### How to use it

1. In a chat, select **Output** and choose **Motion**, or type `/motion`, or pick a Motion template from the Artifacts tab ([Layer3 guide](https://www.layer3labs.io/guides/claude-motion)).
2. Describe it: who will watch, where it plays, roughly how long, and the content to show. Attach the data, report or images to use.
3. Revise one detail at a time, in chat ("slow down the second scene") or directly in the editor.
4. Click **Export** and choose MP4.

Longer or complex animations use more of the plan's usage, and there's no published length or resolution limit, so export a short test first.

## 9. Check before shipping

- [ ] Every animation has a job in one sentence
- [ ] Durations and easings use tokens or published Figma styles
- [ ] Interruptible, and no waiting on a finished animation
- [ ] Reduced-motion version works
- [ ] Smooth during playback and on a slower device
- [ ] Data visuals show real data, with text numbers
- [ ] Nothing animates that people repeat constantly
- [ ] Code matches the Figma Motion values exactly, if a Figma link exists
- [ ] A new animation pattern has Sharon's approval (per `product-designer`)

## 10. Working with Sharon

Writing to Sharon follows `working-with-sharon`. For motion work, three habits matter most.
- Bring motion decisions one at a time.
- Show it moving instead of describing it, when possible.
- When teaching Figma Motion, give the next step only, then wait.

## 11. Getting better

Treat every correction from Sharon as a sign that a rule is missing or wrong. Figma Motion and Claude Motion change monthly, so re-check sections 6 to 8 against their help pages when something doesn't match. Bring changes to this skill in one grouped proposal. Nothing changes without Sharon's yes.

## Change log

| Date | Change |
|---|---|
| 2026-10-22 | Created from Sharon's October 2026 research on UI animation tools, NN/g timing guidance, WCAG, Emil Kowalski's motion rules, the DTCG token format, and the Figma, LottieFiles, motion.dev and Claude help pages. |
| 2026-10-22 | Added loading guidance (section 2) and the Repeats field to the motion spec (section 4), from Dan Saffer's microinteraction model. |
