# Analysis Report: skills/adc-compte-rendu

Generated: 2026-11-15T16:10:32Z · Schema: 2

**Grade: Good**

> Good: a structurally sound simple-workflow skill whose fait/suspens contract is enforced end-to-end and consumed downstream; one high (session-number derivation computed in-prompt instead of by script) and two medium entry-path gaps remain, all clearable in one fix pass.

The skill's strength is its topology and contract discipline: a 761-token inline SKILL.md with correct frontmatter triggers, the template correctly placed in assets/, and the established-vs-open distinction enforced identically in SKILL.md, the fiche, and the consumer skill adc-preparer-seance's input glob. Its main opportunity is moving the deterministic plumbing — which seance-<N> file to write, whether a compte rendu already exists — out of the prompt and into a pre-pass script, and hardening the two entry paths (in-place revision, fresh project with no trace yet) that currently rely on conversation memory or an undefined <N>.

| Severity | Count |
| --- | --- |
| Critical | 0 |
| High | 1 |
| Medium | 2 |
| Low | 4 |

## Themes

### 1. Session-number and existence plumbing still lives in the prompt

- Root cause: SKILL.md derives <N> ('highest existing seance number without a compte rendu yet') and checks file existence by scanning seances/ on every invocation; this is pure glob/parse/max work with one correct answer that gates the output path and misleads adc-preparer-seance downstream if wrong.
- Fix: Add stdlib script scripts/next-seance.py (PEP 723) that globs _bmad-output/campagne/seances/seance-*-*.md and emits pre-pass JSON (next_N, compte_rendu_exists, preparation_path); SKILL.md calls it and consumes the JSON, keeping only the judgment in-prompt. The script also supplies the <N>=1 fallback when seances/ is empty.
- Findings:
  - `determinism-1` Prompt computes <N> and compte-rendu existence by scanning the seances/ directory instead of consuming pre-pass JSON — `SKILL.md:32 (Rédiger le compte rendu, final paragraph); same file-inventory work implied at SKILL.md:21 (On Activation step 2)`

### 2. Entry paths under-specified: in-place revision and fresh-project trace

- Root cause: On Activation reads the preparation and PJ sheets but never an existing seance-<N>-compte-rendu.md, so a revision can start from conversation memory and silently drop established decisions; and with no campagne/ trace or seances/ directory, <N> is undefined and the write target has no home, with no stop-and-redirect like the sibling skill's.
- Fix: Extend the On Activation read list with the existing compte rendu (trace-on-disk is the state), and add one guard line: if the campagne trace or seances/ is missing, stop and point to adc-cadre-campagne / adc-creer-pj instead of inventing a trace — mirroring adc-preparer-seance.
- Findings:
  - `enhancement-1` Add: revise-in-place path never reads the existing compte rendu first — `SKILL.md On Activation step 2 (L21-22) vs. 'Rédiger le compte rendu' final paragraph (L30-31)`
  - `enhancement-2` Add: graceful-degradation guard when the campaign trace or seances/ is missing — `SKILL.md On Activation step 2 (L21-22)`

### 3. Residual ceremony: three low lines that restate or decorate

- Root cause: Resolution rules defines {skill-root}/{skill-name} tokens the body never uses, 'Open is not settled.' restates the Overview bar, and the On Activation 1./2. numbering marks independent obligations as a sequence. All three fail the core test with predicted_delta null, so the cut is free.
- Fix: Apply the three proposed_smallest truncations from the leanness lens (drop unused token rules, drop the restated sentence, un-number the two activation steps into bullets or one goal sentence).
- Findings:
  - `leanness-1` Resolution rules block defines tokens the skill never uses — `SKILL.md:14-16 (Resolution rules)`
  - `leanness-2` "Open is not settled." restates the Overview bar and beats its own absence — `SKILL.md:31 (Fils en suspens bullet, Rédiger le compte rendu)`
  - `leanness-3` On Activation numbered sequence is decoration, not a true sequence — `SKILL.md:20-21 (On Activation, steps 1-2)`

## Strengths

- Architecture pass: frontmatter uses the two-part quoted-trigger format, topology matches the simple-workflow shape (single 761-token SKILL.md, template in assets/, nothing carved that should not be), every routed bare path resolves.
- The fait/suspens non-negotiable is enforced end-to-end: stated in the Overview bar, sectioned in the body, mirrored in the fiche (Décisions établies vs Fils en suspens), and consumed downstream by adc-preparer-seance's seance-*-compte-rendu.md glob.
- Customization pass: customize.toml correctly absent per the logged 'Non, fixe' decision, no other config mechanism leaked in, and the would-be knobs (fiche template, seances/ path) are cross-skill contracts, not org-divergent points.
- Producing patterns correctly applied, nothing over-applied: open-floor opening, consumer-named bar, soft closing gate, trace-on-disk as state.

## Recommendations

1. Add scripts/next-seance.py emitting pre-pass JSON (next_N, compte_rendu_exists, preparation_path, empty-seances fallback N=1) and consume it in SKILL.md instead of in-prompt scanning. (resolves: determinism-1)
2. Harden On Activation: re-read an existing seance-<N>-compte-rendu.md on revision, and stop-and-redirect to adc-cadre-campagne / adc-creer-pj when the campagne trace or seances/ is missing. (resolves: enhancement-1, enhancement-2)
3. Apply the three leanness truncations (unused resolution tokens, restated 'Open is not settled.', un-numbered activation steps) — all have predicted_delta null, so cut without an eval. (resolves: leanness-1, leanness-2, leanness-3)

## Experience

- **Meneur after a played session (organic trigger)** — open-floor dump of what happened → four sections shaped one at a time (actions, consequences, decisions, open threads) → written to seances/seance-<N>-compte-rendu.md → read by adc-preparer-seance for the next prep
- **Revision of an existing compte rendu** — On Activation re-reads the on-disk compte rendu (after fix) → contradictions surface before in-place overwrite → same four sections
- **User arriving in a fresh project with no trace** — guard stops and redirects to adc-cadre-campagne / adc-creer-pj (after fix) instead of dead-ending on an undefined <N>
- Headless: Fundamentally interactive — the input is the meneur's in-memory retelling of the session, so no parameter can replace the open-floor conversation (enhancement-3, low, no change required).

## Findings

### High (1)

#### determinism-1 — Prompt computes <N> and compte-rendu existence by scanning the seances/ directory instead of consuming pre-pass JSON

- Lens: determinism
- Location: `SKILL.md:32 (Rédiger le compte rendu, final paragraph); same file-inventory work implied at SKILL.md:21 (On Activation step 2)`
- Evidence: L32 derives <N> as 'the highest existing séance number without a compte rendu yet' and conditions on existing files; given the same seances/ directory the answer is always identical, unit-testable with fixture files, and involves no interpreted meaning — it passes the determinism test and fires the signal-verb scan ('highest existing', 'without ... yet', 'if ... exists'). A wrong N writes or revises the wrong file and misleads adc-preparer-seance downstream.
- Recommendation: Push the derivation into a script: add scripts/next-seance.py (stdlib, PEP 723) that globs {project-root}/_bmad-output/campagne/seances/seance-*-*.md, computes the highest séance number lacking a compte rendu plus exists-flags, and emits compact JSON; SKILL.md calls the script, consumes the JSON, and keeps only the judgment in-prompt.

### Medium (2)

#### enhancement-1 — Add: revise-in-place path never reads the existing compte rendu first

- Lens: enhancement
- Location: `SKILL.md On Activation step 2 (L21-22) vs. 'Rédiger le compte rendu' final paragraph (L30-31)`
- Evidence: The skill supports in-place revision and declares 'the trace on disk is the state', but On Activation reads only the preparation and PJ sheets — seance-<N>-compte-rendu.md is never in the read list, so a revision can start from conversation memory and silently drop previously established decisions.
- Recommendation: Add 'and seances/seance-<N>-compte-rendu.md if it exists' to the On Activation read list, so an in-place revision starts from the on-disk version and contradictions surface before overwriting.

#### enhancement-2 — Add: graceful-degradation guard when the campaign trace or seances/ is missing

- Lens: enhancement
- Location: `SKILL.md On Activation step 2 (L21-22)`
- Evidence: The sibling adc-preparer-seance stops and redirects when its dependencies are missing; adc-compte-rendu hedges only on the preparation and PJ sheets ('if they exist'). If _bmad-output/campagne/seances/ does not exist, <N> is undefined and the write target has no home — a user arriving by organic trigger in a fresh project dead-ends.
- Recommendation: Add one line to On Activation: if the campagne trace or seances/ is missing, stop and point the user to adc-cadre-campagne (and adc-creer-pj) instead of inventing a trace; define the <N> fallback as 1 when no séance exists yet.

### Low (4)

#### leanness-1 — Resolution rules block defines tokens the skill never uses

- Lens: leanness
- Location: `SKILL.md:14-16 (Resolution rules)`
- Evidence: The block defines {skill-root} and {skill-name}, but both tokens appear only inside the rules themselves; the body uses only {project-root} (3x) and the bare path assets/fiche-compte-rendu.md.
- Recommendation: Truncate the block to the two load-bearing rules: bare paths resolve from the skill's installed directory, and {project-root} → the project working directory.
- Proposed smallest: ## Resolution rules
- Bare paths (e.g. `assets/fiche-compte-rendu.md`) resolve from this skill's installed directory.
- `{project-root}` → the project working directory.

#### leanness-2 — "Open is not settled." restates the Overview bar and beats its own absence

- Lens: leanness
- Location: `SKILL.md:31 (Fils en suspens bullet, Rédiger le compte rendu)`
- Evidence: The Overview (L10) already states the bar 'established (fait) kept strictly apart from open (suspens)'; the bullet's closing sentence adds no new constraint — a restated fact across sections.
- Recommendation: Delete the sentence; the heading, the enumeration above it, and the Overview bar already carry the rule.
- Proposed smallest: - **Fils en suspens.** What stays open: unanswered questions, promises not yet kept, threats still looming, threads dropped or to pick back up.

#### leanness-3 — On Activation numbered sequence is decoration, not a true sequence

- Lens: leanness
- Location: `SKILL.md:20-21 (On Activation, steps 1-2)`
- Evidence: Step 1 (load config for languages) and step 2 (locate and re-read the campaign trace) are independent obligations with no data or guard dependency between them, yet the 1./2. numbering tells the reader to march them in order.
- Recommendation: Replace the numbered pair with bullets, or one goal sentence covering config languages and trace re-read; the 'trace on disk is the state' why stays.

#### enhancement-3 — Opportunity: headless readiness is fundamentally interactive — acceptable, with one optional adaptation

- Lens: enhancement
- Location: `SKILL.md 'Rédiger le compte rendu' opening (L25-26)`
- Evidence: The skill's input is the meneur's in-memory retelling of the session; the value is the conversation and no parameter can replace the open-floor question — fundamentally interactive is the right classification.
- Recommendation: No change required. If headless use emerges, accept an optional path to a notes/transcript file that replaces the open-floor dump; until then the interactive-only contract is correct.
