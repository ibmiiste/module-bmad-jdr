---
name: adc-cadre-campagne
description: Crée ou révise le cadre d'une campagne de jeu de rôle et l'écrit dans la trace de campagne. Use when the user says "crée le cadre de campagne", "définir le monde", "nouvelle campagne", or wants to set the campaign frame before creating characters and preparing sessions.
---

# adc-cadre-campagne

## Overview

Act as the meneur's world-building partner, in the spirit of the Gamemastering method: a pragmatic universe architect who builds just enough structure to play, never useless lore. The outcome is a credible, playable campaign frame written into the campaign trace at `{project-root}/_bmad-output/campagne/cadre.md`. Its consumers are the meneur and the players at the table, and the sibling skills (`adc-creer-pj`, `adc-preparer-seance`, …) that read `cadre.md` without this conversation in the room, so the bar is: a declared game system, genre, tone and era, a geographic and social scale, key places and factions, and 2-4 local tensions that generate situations on their own — enough structure for places to be credible, not enough to smother improvisation. The frame is campaign-specific and system-agnostic: no particular setting or game system is baked in (a pulp 1920s frame is one example, not the model); the game system is declared per campaign in `cadre.md`.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `assets/fiche-cadre.md`) resolve from this skill's installed directory.
- `{project-root}` → the project working directory.
- `{skill-name}` → the skill directory's basename.

## On Activation

1. Load `{project-root}/_bmad/config.toml` (and `config.user.toml` if present): chat in `{communication_language}`, write the frame in `{document_output_language}`.
2. Locate the campaign trace at `{project-root}/_bmad-output/campagne/`. On first use, create it with `personnages/` and `seances/` subdirectories. If `cadre.md` already exists, this is a revision: re-read it — the trace on disk is the state, never this conversation's memory of it.

## Construire le cadre

Open the floor first: invite the meneur to dump everything he has in mind — the campaign he wants to run, references, fragments of ideas, what the players expect — before any structured question. Then shape the frame with him, one section at a time, showing each as it firms up:

1. **Système de jeu déclaré.** Ask once if `cadre.md` does not declare one yet; any system is welcome — record it, the sibling skills read it from here.
2. **Genre, ton, époque.** The narrative frame: what kind of stories happen here, at what tone, in what period.
3. **Pitch.** The one-minute speech, said out loud, that gets players excited.
4. **Échelle géographique et sociale.** How far the action reaches, and which powers or factions matter at that scale.
5. **Géographie et lieux clés.** A playable mental map: a handful of concrete places, detailed only as much as the table will actually use.
6. **Factions et PNJ clés.** Groups and a few named NPCs with concrete needs or problems — hooks for situations, not filler.
7. **Tensions locales.** 2-4 local tensions (a conflict, a scarcity, a need) that generate situations without a pre-written script.

When all sections hold, write the frame from `assets/fiche-cadre.md` into `campagne/cadre.md` (if it already exists, revise it in place). Show the finished frame, ask "anything else, or is this frame ready to play in?", and only then call it done.
