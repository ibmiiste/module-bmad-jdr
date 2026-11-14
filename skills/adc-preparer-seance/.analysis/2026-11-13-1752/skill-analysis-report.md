# Analysis Report: skills/adc-preparer-seance

Generated: 2026-11-13T17:55:00+00:00 · Schema: 2

**Grade: Good**

> Good: structurally clean and lean (807 tokens, architecture lens passes clean), but the in-progress prep lives only in the conversation until the final write (1 high), and two deterministic file chores belong in a small pre-pass script.

The skill's strength is its single-file, destination-driven shape: SKILL.md sits well under its token tier, the frontmatter and resolution rules are canonical, and the Overview bar is enforced by the execution section and validated by a manual run on a realistic campaign trace. The main opportunity is working state: the prep sheet is written only once all four sections hold, so anything shaped mid-run dies on compaction; creating the sheet up front and filling it in place fixes that and makes the unplayed-prep revision rule cover mid-run resume too. Secondary opportunities are a pre-pass script for the trace inventory and seance numbering, and truncating the bar restated across Overview, bullets, and template.

| Severity | Count |
| --- | --- |
| Critical | 0 |
| High | 1 |
| Medium | 6 |
| Low | 4 |

## Themes

### 1. In-progress prep has no on-disk state until the final write

- Root cause: The skill shapes amorce/lieux/PNJ/obstacles in conversation and writes seance-<N>-preparation.md only when all four hold, so compaction or a revisit loses the shaped work; 'the trace on disk is the state' covers only prior inputs.
- Fix: Create seances/seance-<N>-preparation.md from assets/fiche-preparation.md at the start of shaping and fill each section in place as it firms up; the sheet becomes the structured working artifact and the existing revise-in-place rule covers mid-run resume.
- Findings:
  - `enhancement-1` Add working-state strategy: write the prep sheet incrementally as each section firms up — `SKILL.md ## Preparer la seance (final write only); assets/fiche-preparation.md`

### 2. Deterministic file inventory and seance numbering done in-prompt

- Root cause: The prompt globs the campaign trace, checks existence of cadre.md and character sheets, and computes <N> = max+1 from filenames — all unit-testable operations with one correct answer per directory state.
- Fix: Add a small native-Python pre-pass script (scripts/) that emits compact JSON {cadre_present, character_sheet_count, next_seance_number, unplayed_prep} for {project-root}/_bmad-output/campagne/; the prompt consumes the JSON and only judges stop/proceed and content.
- Findings:
  - `determinism-1` Prompt does trace structure/existence checks that gate activation — `skills/adc-preparer-seance/SKILL.md - 'On Activation' step 2`
  - `determinism-2` Prompt computes the next seance number and unplayed-prep detection from filenames — `skills/adc-preparer-seance/SKILL.md - 'Preparer la seance' final paragraph`

### 3. The bar is restated across Overview, prep bullets, and the template

- Root cause: The Overview already enumerates the four sections with counts and obstacle sub-fields; the four bullets and the fiche template repeat the same fields, so every invocation pays for the bar three times.
- Fix: Truncate the four bullets to one goal sentence keeping the two unique rules (one session at a time, detail restraint); strip the template to section headers or replace it with a five-line output spec in SKILL.md; cut the scripted closing question.
- Findings:
  - `leanness-1` Prep-section bullets restate the Overview bar almost field-for-field — `SKILL.md, section 'Preparer la seance' (the four bullets)`
  - `leanness-2` fiche-preparation.md template duplicates the bar in fill-in form — `assets/fiche-preparation.md (all 36 lines)`
  - `leanness-3` Scripted closing beat in the final paragraph — `SKILL.md, final paragraph of 'Preparer la seance'`

### 4. Customization surface opportunities exist but were declined by decision

- Root cause: The user explicitly declined customize.toml at build time (logged in .memlog.md), so the hardcoded template path, output destination, and missing on_complete hook are fork-if-needed points, not defects.
- Fix: No action now; if a real need for a swappable template or redirected output appears, opt into customize.toml then (preparation_template, preparation_output_path, on_complete) rather than forking preemptively.
- Findings:
  - `customization-1` Hardcoded template path should be a <purpose>_template scalar — `SKILL.md:31 (final write instruction)`
  - `customization-2` Hardcoded output destination should be a <purpose>_output_path candidate — `SKILL.md:10 (Overview) and SKILL.md:31 (write destination)`
  - `customization-3` Artifact-producing skill stops with no on_complete hook candidate — `SKILL.md:31 (terminal stage)`

### 5. Small missing soft patterns around the open floor

- Root cause: The open-floor dump has no parking spot for out-of-scope ideas, and the skill neither declares itself fundamentally interactive nor accepts a pre-supplied dump.
- Fix: Add one capture-don't-interrupt line (park out-of-scope material under Notes pour le meneur) and one line declaring the skill fundamentally interactive, optionally accepting an inline/path seed dump.
- Findings:
  - `enhancement-2` Add capture-don't-interrupt for out-of-scope material surfaced during the open floor — `SKILL.md ## Preparer la seance, open-floor paragraph`
  - `enhancement-3` Opportunity: declare the skill fundamentally interactive; optionally accept a pre-supplied dump as the open-floor seed — `SKILL.md ## Preparer la seance, first sentence`

## Strengths

- Architecture lens passes clean: frontmatter holds only name+description with quoted triggers, canonical Resolution rules block, all workflow content inline in one 807-token SKILL.md (well under the 2000 desired tier), template correctly in assets/, every routed bare path exists.
- Destination-driven Overview names the consumer (meneur at the table without the conversation) and the bar, and the execution section enforces it verbatim; validated by a manual run on a realistic pulp-1920 trace producing a conforming seance-2-preparation.md.
- Graceful degradation is wired: missing cadre or character sheets routes to adc-cadre-campagne / adc-creer-pj instead of inventing content.
- Open-floor opening and soft-gate closing are present and not over-applied; no ALL-CAPS directives, no numbered-step marching.

## Recommendations

1. Write the prep sheet incrementally: create seance-<N>-preparation.md from the template at the start of shaping and fill each section in place as it firms up. (resolves: enhancement-1)
2. Add scripts/trace_inventory.py pre-pass emitting {cadre_present, character_sheet_count, next_seance_number, unplayed_prep} as JSON; SKILL.md consumes it for the prereq check and the write target. (resolves: determinism-1, determinism-2)
3. Truncate the four prep bullets to one goal sentence, strip assets/fiche-preparation.md to section headers (or inline a five-line output spec), cut the scripted closing question. (resolves: leanness-1, leanness-2, leanness-3)
4. Add one capture-don't-interrupt line for out-of-scope ideas (park under Notes pour le meneur) and declare the skill fundamentally interactive with an optional seed dump. (resolves: enhancement-2, enhancement-3)
5. Leave customization as shipped-fixed (user decision); revisit only if a concrete override need appears. (resolves: customization-1, customization-2, customization-3)

## Experience

- **Preparation interactive** — Activation (config + prereq check on the trace) -> open floor dump by the meneur -> shape amorce, lieux, PNJ, obstacles one at a time -> write/revise seances/seance-<N>-preparation.md -> show sheet, soft-gate, done.
- **Degraded first use** — No cadre.md or no personnages/*.md -> stop and point to adc-cadre-campagne / adc-creer-pj; nothing is invented.
- Headless: Fundamentally interactive (co-shaping is the value); no headless mode claimed, which the enhancement lens rates a fine answer; an optional pre-supplied dump seed would make it partially adaptable (enhancement-3).

## Findings

### High (1)

#### enhancement-1 — Add working-state strategy: write the prep sheet incrementally as each section firms up

- Lens: enhancement
- Location: `SKILL.md ## Preparer la seance (final write only); assets/fiche-preparation.md`
- Evidence: Multi-turn skill that builds something, but the sheet is written to seances/seance-<N>-preparation.md only once, 'when all four hold'. Until that write, everything shaped lives only in the conversation and dies on compaction or revisit. The .memlog.md at the skill root is the builder's build-time log, not a runtime working-state strategy.
- Recommendation: Create seance-<N>-preparation.md from assets/fiche-preparation.md at the start of shaping and fill each section in place as it firms up: the sheet itself becomes the structured working artifact, re-readable after compaction; the unplayed-prep revise-in-place rule then covers mid-run resume and next-week revision. No memlog needed; the fiche's schema is the contract.

### Medium (6)

#### determinism-1 — Prompt does trace structure/existence checks that gate activation

- Lens: determinism
- Location: `skills/adc-preparer-seance/SKILL.md - 'On Activation' step 2`
- Evidence: The prompt globs and checks the campaign trace itself (cadre.md, personnages/*.md, seances/seance-*-compte-rendu.md) with a pass/fail stop condition downstream behavior depends on.
- Recommendation: Determinism leak (structure checks / file existence are unit-testable): apply the determinism test and signal-verb scan, then use the pre-pass JSON pattern - a trace-inventory script emits compact JSON (cadre_present, character_sheet_count, seance files) so the prompt consumes the inventory and only judges the stop/proceed message.

#### determinism-2 — Prompt computes the next seance number and unplayed-prep detection from filenames

- Lens: determinism
- Location: `skills/adc-preparer-seance/SKILL.md - 'Preparer la seance' final paragraph`
- Evidence: Deriving <N> means listing seances/, parsing the integer out of every seance-<N>-* filename, taking max+1, and checking whether seance-<N>-preparation.md exists without a matching compte rendu - count/parse/compare work re-done on every invocation to pick the write target.
- Recommendation: Determinism leak by the determinism test (identical directory state always yields identical <N>) and signal-verb scan ('count', 'extract', 'compare', 'list all'): extend the pre-pass script to emit {next_seance_number, existing_preps, unplayed_prep} as compact JSON; the prompt then only decides prep content, not numbering.

#### leanness-1 — Prep-section bullets restate the Overview bar almost field-for-field

- Lens: leanness
- Location: `SKILL.md, section 'Preparer la seance' (the four bullets)`
- Evidence: The Overview bar already states the four sections with counts and obstacle sub-fields; the four bullets repeat the same items with the same counts and sub-fields. Only unique content: 'Prepare one session at a time' and 'detailed only as much as the table will actually use'.
- Recommendation: Truncate the four bullets to one goal sentence that keeps the unique rules; the Overview bar defines what each must contain.
- Proposed smallest: Open the floor first: invite the meneur to dump everything he has in mind before any structured question. Then shape the prep with him section by section - amorce, lieux, PNJ, obstacles - one session at a time, each detailed only as much as the table will actually use, showing each as it firms up. The bar in the Overview defines what each section must contain.
- Predicted delta: Expected loss near zero on real input: every section and field is already required by the Overview bar and the smallest version preserves the two unique rules. Residual risk: interactive shaping drifting off-checklist mid-conversation; route to variant eval to confirm.

#### customization-1 — Hardcoded template path should be a <purpose>_template scalar

- Lens: customization
- Location: `SKILL.md:31 (final write instruction)`
- Evidence: SKILL.md writes the prep sheet from assets/fiche-preparation.md - the template path is baked in with no customize.toml to swap it; anyone needing a different layout must fork the whole skill. One template only, so below the two-or-more high-opportunity threshold.
- Recommendation: If the skill opts into customization, expose preparation_template = "assets/fiche-preparation.md" under [workflow] and reference it as {workflow.preparation_template}. Declined by user decision at build time.

#### customization-3 — Artifact-producing skill stops with no on_complete hook candidate

- Lens: customization
- Location: `SKILL.md:31 (terminal stage)`
- Evidence: The skill produces a concrete artifact (the session prep sheet) and ends right after showing it, with no customize.toml to carry the universal on_complete default.
- Recommendation: If opted in, bake on_complete = "" under [workflow] so a user can attach a terminal instruction (log the run, hand off to adc-compte-rendu) without forking. Declined by user decision at build time.

#### enhancement-2 — Add capture-don't-interrupt for out-of-scope material surfaced during the open floor

- Lens: enhancement
- Location: `SKILL.md ## Preparer la seance, open-floor paragraph`
- Evidence: The open floor invites a full dump, but the skill gives no path for material belonging to future sessions or the cadre; unprompted ideas are either redirected (breaking flow) or dropped.
- Recommendation: Add one line: park out-of-scope material silently under 'Notes pour le meneur' in the fiche (e.g. idees pour les seances suivantes) and keep shaping the current session.

### Low (4)

#### leanness-2 — fiche-preparation.md template duplicates the bar in fill-in form

- Lens: leanness
- Location: `assets/fiche-preparation.md (all 36 lines)`
- Evidence: Every template field maps to a line already stated in the Overview bar or the prep bullets; the template is a format-the-output skeleton whose content the model is already told in the entry file on every invocation.
- Recommendation: Replace the template file with a five-line output spec in SKILL.md naming the artifact's sections, or keep the file but strip it to section headers only.
- Proposed smallest: When all four hold, write seances/seance-<N>-preparation.md as a markdown sheet with sections: 'Amorce et conflit', 'Lieux' (one subsection per place), 'PNJ et adversaires' (one per NPC), 'Obstacles' (one per obstacle, covering information, defi, competences, approches, consequence en cas d'echec), and 'Notes pour le meneur'.
- Predicted delta: Likely no material loss - section names preserve cross-session structural consistency of the artifact. Possible minor loss: per-field fill-in nudges that push flavor text into places. Route to variant eval to confirm.

#### customization-2 — Hardcoded output destination should be a <purpose>_output_path candidate

- Lens: customization
- Location: `SKILL.md:10 (Overview) and SKILL.md:31 (write destination)`
- Evidence: The artifact destination {project-root}/_bmad-output/campagne/seances/seance-<N>-preparation.md is hardcoded and interlocked with the trace root read at activation, so not clearly org-dependent - the weak output-path lift the spec rates low.
- Recommendation: If opted in, expose preparation_output_path paired with run_folder_pattern and read them as {workflow.*}. Declined by user decision at build time.

#### enhancement-3 — Opportunity: declare the skill fundamentally interactive; optionally accept a pre-supplied dump as the open-floor seed

- Lens: enhancement
- Location: `SKILL.md ## Preparer la seance, first sentence`
- Evidence: The only input path is the conversational open-floor question; no parameter, file path, or inline text can seed the run, so a headless caller cannot get a usable return without a live conversation.
- Recommendation: Fundamentally interactive is a fine answer - state it explicitly. Optionally let the open floor also accept a supplied dump (inline text or a path under the campaign trace) so a headless caller gets a first-draft sheet to iterate on.

#### leanness-3 — Scripted closing beat in the final paragraph

- Lens: leanness
- Location: `SKILL.md, final paragraph of 'Preparer la seance'`
- Evidence: 'Show the finished sheet, ask "anything else, or is this ready to play?", and only then call it done' is an imagined transcript, not a rule with a failure consequence; the <N> computation and revise-in-place rule in the same paragraph are real wiring and stay.
- Recommendation: Cut the scripted question; keep the write-target wiring, show the finished sheet, and call it done.
