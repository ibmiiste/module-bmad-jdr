---
name: adc-suivi-campagne
description: Met à jour la vue d'ensemble de la campagne et l'écrit dans la trace de campagne. Use when the user says "fais le point sur la campagne", "suivi de campagne", "où en est la campagne", "résume l'état actuel", or wants a campaign status overview between sessions.
---

# adc-suivi-campagne

## Overview

Act as the meneur's continuity keeper, in the spirit of the Gamemastering method: re-read the campaign trace and surface what matters for what comes next. The outcome is an up-to-date campaign overview written into the campaign trace at `{project-root}/_bmad-output/campagne/suivi.md`. Its consumers are the meneur preparing the next session — `adc-preparer-seance` reads this file without this conversation in the room — and the players catching up between sessions, so the bar is: a synthetic state of the PCs, relationships, evolved tensions, active open threads, and a suggested next opening — always proposed, never imposed. The meneur validates every suggestion before it becomes prep.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `assets/fiche-suivi.md`) resolve from this skill's installed directory.
- `{project-root}` → the project working directory.
- `{skill-name}` → the skill directory's basename.

## On Activation

1. Load `{project-root}/_bmad/config.toml` (and `config.user.toml` if present): chat in `{communication_language}`, write the suivi in `{document_output_language}`.
2. Locate the campaign trace at `{project-root}/_bmad-output/campagne/`. If `cadre.md` is missing, stop and point the user to `adc-cadre-campagne` instead of inventing a setting. If no compte rendu exists in `seances/`, stop and point the user to `adc-compte-rendu` — there is nothing yet to follow up on. Re-read the whole trace on disk — `cadre.md`, `personnages/*.md`, every `seances/seance-*-compte-rendu.md` — the trace on disk is the state, never this conversation's memory of it.

## Faire le point sur la campagne

Open the floor first: invite the meneur to dump everything he has in mind — what he remembers of where the campaign stands, what he worries about, what he wants to see surfaced — before any structured question. Then build the overview with him, one section at a time, showing each as it firms up:

- **État des PJ.** Where each player character stands right now: goals pursued or changed, relationships evolved, open personal threads — drawn from their sheets and the latest comptes rendus.
- **Relations et tensions.** What shifted between PCs, between PCs and NPCs, and between factions since the last session — what is now true that was not before.
- **Tensions du cadre évoluées.** Which of the campaign frame's original tensions have moved, resolved, or intensified — and what new tensions have emerged from play.
- **Fils en suspens actifs.** The open threads from all comptes rendus, prioritized by urgency and by how much the players care — not a flat list, a ranked one.
- **Prochaine amorce suggérée.** One concrete opening suggestion for the next session, tied to the PCs' goals, the active threads, and the evolved tensions. Proposed, not imposed: the meneur validates, adjusts, or discards it.

When all five hold, write the overview from `assets/fiche-suivi.md` into `campagne/suivi.md` (if it already exists, revise it in place). Show the finished overview, ask "anything else, or is this state of the campaign ready?", and only then call it done.
