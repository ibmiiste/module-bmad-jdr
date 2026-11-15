---
name: adc-creer-pj
description: Crée un personnage joueur complet et jouable, ancré dans le cadre de campagne et les autres PJ, et l'écrit dans la trace de campagne. Use when the user says "crée un PJ", "créer un personnage", "nouveau personnage joueur", or wants to turn player ideas into a playable character sheet.
---

# adc-creer-pj

## Overview

Act as the player's creation partner, in the spirit of the Gamemastering method: an attentive companion who asks open-ended questions and never judges the player's choices. The outcome is a complete, playable PJ sheet written into the campaign trace at `{project-root}/_bmad-output/campagne/personnages/<nom>.md`. Its consumers are the player and the meneur at the table, without this conversation in the room, so the bar is: a character gone through the nine creation steps — profession, outline, values, past, relationships, goals, traits, game-system mechanics, starting equipment — tied to the world and the other PJs, never an isolated sheet.

## Resolution rules

- Bare paths and `{skill-root}` (e.g. `assets/fiche-pj.md`) resolve from this skill's installed directory.
- `{project-root}` → the project working directory.
- `{skill-name}` → the skill directory's basename.

## On Activation

1. Load `{project-root}/_bmad/config.toml` (and `config.user.toml` if present): chat in `{communication_language}`, write the sheet in `{document_output_language}`.
2. Locate the campaign trace at `{project-root}/_bmad-output/campagne/`. If `cadre.md` is missing, stop and point the user to `adc-cadre-campagne` instead of inventing a setting. The game system is read from `cadre.md` if declared there, otherwise ask once and record it in the sheet. Read the existing `personnages/*.md` — the trace on disk is the state: re-read it, never rely on this conversation's memory of it.

## Créer le personnage

Open the floor first: invite the player to dump everything he has in mind — the character he wants to play, references, fragments of ideas — before any structured question. Then walk the nine creation steps with him, one section at a time, showing each as it firms up. Ask open-ended questions only — never "do you hate the King?", always "what do you hate most in the world?".

1. **Profession ou classe.** Who does he want to be? One rule with real consequences: the character must be likable — he cares about other people and the team can trust him; rough edges are fine, a lone sociopath is not.
2. **Esquisse.** One or two paragraphs that say who he is.
3. **Droits et méfaits.** A handful of values — what he stands for, what he refuses to do.
4. **Passé.** At least one meaningful event for each stretch of adult life; the past is where relationships take root.
5. **Amis, ennemis, problèmes.** 2-4 concrete relationships, each tied to the past and to the world: a friend or foe among the existing PJs or the cadre's NPCs, something owed, something feared. If this is the first PJ of the group, anchor him in the cadre alone.
6. **Objectifs.** One main goal the mechanics must make pursuable; shorter ones may emerge.
7. **Tics et traits.** One or two quirks to start.
8. **Mécanique.** Put the character into the declared game system (GURPS first) without randomization — match the player's desires, strong foundations with little experience — and check that the rules actually let him pursue his goal; adjust if they don't.
9. **Équipement de départ.** The bare minimum.

When all nine hold, write the sheet from `assets/fiche-pj.md` into `personnages/<nom>.md` (if a sheet with that name already exists, revise it in place). Show the finished sheet, ask "anything else, or is this character ready to play?", and only then call it done.
