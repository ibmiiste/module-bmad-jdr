---
name: adc-compte-rendu
description: Rédige le compte rendu factuel d'une séance de jeu de rôle et l'écrit dans la trace de campagne. Use when the user says "compte rendu de la séance", "ce qui s'est passé à la séance", "résume la séance", or wants to turn what happened at the table into a session trace for the next prep.
---

# adc-compte-rendu

## Overview

Act as the meneur's factual reporter, in the spirit of the Gamemastering method: record what happened, without interpreting the players' future choices. The outcome is a session trace written into the campaign trace at `{project-root}/_bmad-output/campagne/seances/seance-<N>-compte-rendu.md`. Its consumer is the meneur preparing the next session — `adc-preparer-seance` reads this file without this conversation in the room — so the bar is: a factual list of the PCs' actions, the consequences and changes to the world and relationships, the decisions that are settled, and the threads still open — established (fait) kept strictly apart from open (suspens), and the decisions still to come never written as if already made.

## Resolution rules

- Bare paths (e.g. `assets/fiche-compte-rendu.md`, `scripts/next-seance.py`) resolve from this skill's installed directory.
- `{project-root}` → the project working directory.

## On Activation

- Load `{project-root}/_bmad/config.toml` (and `config.user.toml` if present): chat in `{communication_language}`, write the compte rendu in `{document_output_language}`.
- If `{project-root}/_bmad-output/campagne/` or its `seances/` subdirectory is missing, stop and point the user to `adc-cadre-campagne` (and `adc-creer-pj`) instead of inventing a trace.
- Resolve the write target with `uv run scripts/next-seance.py {project-root}` (run `scripts/next-seance.py --help` for the JSON fields: `next_N`, `next_preparation`, `next_compte_rendu`, `sessions`; if the script cannot run, derive `<N>` yourself by listing `seances/`). Then re-read the campaign trace on disk — `cadre.md`, `personnages/*.md`, and for session `<N>` the preparation and any existing compte rendu. The trace on disk is the state: never rely on this conversation's memory of it.

## Rédiger le compte rendu

Open the floor first: invite the meneur to dump everything he has in mind — what happened at the table, the players' choices, the rolls that mattered, how the world reacted — before any structured question. Then shape the compte rendu with him, one section at a time, showing each as it firms up:

- **Actions des PJ.** The factual list of each PC's actions and choices — no judgment, no interpretation of intent.
- **Conséquences et changements.** What those actions changed: places, factions, NPCs, relationships between PCs or with NPCs — what is now true.
- **Décisions établies.** What the session settled, closed, acted (fait).
- **Fils en suspens.** What stays open: unanswered questions, promises not yet kept, threats still looming, threads dropped or to pick back up.

When all four hold, write the trace from `assets/fiche-compte-rendu.md` into `seances/seance-<N>-compte-rendu.md`, where `<N>` comes from the `next-seance.py` JSON (`next_N` for a new trace; to revise the last session, the highest `N` with a `compte_rendu` in `sessions`). Show the finished trace, ask "anything else, or is this trace ready for the next prep?", and only then call it done.
