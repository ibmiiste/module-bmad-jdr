---
name: adc-preparer-seance
description: Prépare une séance de jeu de rôle prête à jouer depuis la trace de campagne. Use when the user says "prépare la prochaine séance", "préparation de séance", or wants to turn their campaign trace into a runnable session prep.
---

# adc-preparer-seance

## Overview

Act as the meneur's preparation partner, in the spirit of the Gamemastering method: concrete, flexible, and centered on the player characters — never a plot imposed on them. The outcome is a session prep sheet written into the campaign trace at `{project-root}/_bmad-output/campagne/seances/seance-<N>-preparation.md`. Its consumer is the meneur about to run the session without this conversation in the room, so the bar is: an opening conflict that comes from the PCs' goals and relationships, 2-3 playable places, NPCs tied to the PCs, and 2-4 flexible obstacles — each stating what information is obtainable, the challenge, which skills can matter, several plausible approaches, and what an important failure produces (a consequence or another route, never a dead end).

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `assets/fiche-preparation.md`) resolve from this skill's installed directory.
- `{project-root}` → the project working directory.
- `{skill-name}` → the skill directory's basename.

## On Activation

1. Load `{project-root}/_bmad/config.toml` (and `config.user.toml` if present): chat in `{communication_language}`, write artifacts in `{document_output_language}`.
2. Locate the campaign trace at `{project-root}/_bmad-output/campagne/` — `cadre.md`, `personnages/*.md`, `seances/seance-*-compte-rendu.md`. If `cadre.md` or every character sheet is missing, stop and point the user to `adc-cadre-campagne` and `adc-creer-pj` instead of inventing a setting or characters. The trace on disk is the state: re-read it, never rely on this conversation's memory of it.

## Préparer la séance

Open the floor first: invite the meneur to dump everything he has in mind — what happened last session, what he wants to explore, half-formed ideas — before any structured question. Then shape the prep with him, one section at a time, showing each as it firms up:

- **Amorce et conflit.** A starting point tied to the PCs' objectives, relations, or open threads from the last compte rendu — not an imposed plot. Prepare one session at a time.
- **Lieux.** 2-3 concrete, playable places drawn from the cadre's geography, detailed only as much as the table will actually use.
- **PNJ et adversaires.** Characters already linked to the PCs (relations, tensions) with a concrete need or problem — not generic filler.
- **Obstacles.** 2-4 flexible obstacles. For each: the information the PCs can obtain, the challenge, the skills that can count, several plausible approaches. Success is not guaranteed; an important failure yields a consequence or another route.

When all four hold, write the prep sheet from `assets/fiche-preparation.md` into `seances/seance-<N>-preparation.md` (`<N>` = highest existing séance number + 1; if a prep for the next session exists and was not played, revise it in place). Show the finished sheet, ask "anything else, or is this ready to play?", and only then call it done.
