---
title: 'Plan de module - Atelier de Campagne'
status: 'ideation'
module_name: 'Atelier de Campagne'
module_code: 'adc'
module_description: 'Accompagne meneurs et joueurs dans la creation des personnages, des campagnes et des seances de jeu de role, puis dans le suivi de leur evolution, en s inspirant de Gamemastering et en s adaptant au systeme choisi.'
architecture: ''
standalone: true
expands_module: ''
skills_planned: []
config_variables: []
created: '2026-11-13'
updated: '2026-11-13'
---

# Module Plan

## Vision

<!-- What this module does, who it's for, and why it matters -->

## Architecture

Not ready — complete in Phase 3+

<!-- Architecture decision and rationale -->
<!-- Options: single agent with capabilities, multiple agents, hybrid, orchestrator pattern -->
<!-- Document WHY this architecture was chosen — future builders need the reasoning -->

### Memory Architecture

Not ready — complete in Phase 3+

<!-- Which pattern: personal memory only, personal + shared, or single shared memory? -->
<!-- If single shared memory: include the full folder structure -->
<!-- If shared memory: define the memory contract below -->

### Memory Contract

Not ready — complete in Phase 3+

<!-- For each curated file in the memory folder, document: -->
<!-- - Filename and purpose -->
<!-- - What agents read it -->
<!-- - What agents write to it -->
<!-- - Key content/structure -->

### Cross-Agent Patterns

Not ready — complete in Phase 3+

<!-- How do agents hand off work to each other? -->
<!-- Is the user the router? Is there an orchestrator? Service-layer relationships? -->
<!-- How does shared memory enable cross-domain awareness? -->

## Skills

Cinq skills couvrent le cycle complet de campagne. Chaque skill est un workflow guide, adaptable au systeme declare (GURPS en premier).

### 1. Creation de personnage (adc-creer-pj)

**Type:** workflow

**Persona:** accompagnateur attentif, pose des questions ouvertes, ne juge pas les choix du joueur.

**Core Outcome:** un PJ complet et jouable — concept, passe, valeurs, relations (amis/ennemis/problemes), traits, objectifs — dont les regles et capacites permettent de poursuivre ses objectifs.

**The Non-Negotiable:** le PJ doit etre lie au monde et aux autres PJ ; pas de fiche isolee sans accroche narrative.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Explorer le concept | concept de PJ clair | envies du joueur, cadre de campagne | concept formule |
| Creuser le passe et les relations | 2-4 relations ou problemes concrets | concept, systeme declare | liste de relations |
| Definir valeurs, traits, objectifs | 1 objectif principal + traits coherents | passe, relations | fiche de valeurs/objectifs |
| Verifier la mecanique | les regles permettent l'objectif | fiche, regles du systeme | validation ou ajustement |

**Memory:** lit le cadre de campagne en cours ; ecrit la fiche PJ dans la trace de campagne.

**Init Responsibility:** demande le systeme declare si pas encore connu ; recupere le cadre de campagne.

**Activation Modes:** interactive

**Tool Dependencies:** aucune externe ; s'appuie sur les regles du systeme declare.

**Design Notes:** GURPS premier systeme pris en charge, mais le deroule doit rester generique — seule la verification mecanique change selon le systeme.

### 2. Cadre de campagne (adc-cadre-campagne)

**Type:** workflow

**Persona:** architecte d'univers pragmatique — structure juste assez pour jouer, pas de lore inutile.

**Core Outcome:** un cadre de campagne credibel et jouable — genre, ton, epoque, echelle geographique et sociale, tensions locales — qui fera emerger des situations sans script predefini.

**The Non-Negotiable:** assez de structure pour que les lieux soient credibles, pas assez pour etouffer l'improvisation.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Definir genre, ton, epoque | cadre narratif pose | envies du meneur | fiche de cadre |
| Esquisser la geographie et la societe | carte mentale jouable | cadre narratif | lieux et factions clés |
| Identifier les tensions locales | 2-4 tensions generatrices de situations | lieux, factions | liste de tensions |

**Memory:** ecrit le cadre dans la trace de campagne ; tous les autres skills le lisent.

**Init Responsibility:** cree la structure de trace de campagne si premiere utilisation.

**Activation Modes:** interactive

**Tool Dependencies:** aucune.

**Design Notes:** le cadre pulp annees 1920 d'Olivier est un exemple de campagne, pas un modele encode dans le module.

### 3. Preparation de seance (adc-preparer-seance)

**Type:** workflow

**Persona:** meneur prepare selon Gamemastering — concret, flexible, centre sur les PJ.

**Core Outcome:** une seance prete a jouer — amorce de conflit liee aux objectifs/relations des PJ, lieux utiles, PNJ pertinents, obstacles flexibles avec informations, defis, competences et approches possibles.

**The Non-Negotiable:** preparer une seance a la fois ; l'amorce doit venir des PJ, pas d'une intrigue imposee.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Formuler l'amorce et le conflit | point de depart lie aux PJ | fiches PJ, cadre, tensions, compte rendu precedent | amorce de seance |
| Preparer les lieux utiles | 2-3 lieux concrets et jouables | amorce, geographie du cadre | fiches de lieux |
| Preparer PNJ et adversaires | PNJ lies aux PJ, pas generiques | relations des PJ, amorce | fiches PNJ |
| Concevoir les obstacles | 2-4 obstacles flexibles avec consequences | amorce, competences des PJ | fiches obstacles |

**Memory:** lit fiches PJ, cadre, tensions, compte rendu precedent ; ecrit la preparation de seance.

**Init Responsibility:** verifie que PJ et cadre existent ; sinon oriente vers les skills 1 et 2.

**Activation Modes:** interactive

**Tool Dependencies:** aucune.

**Design Notes:** inspire des chapitres 6-11 et 22 de Gamemastering — obstacles simples, reussite non garantie, echec = consequence ou autre voie.

### 4. Compte rendu de seance (adc-compte-rendu)

**Type:** workflow

**Persona:** rapporteur factuel — consigne ce qui s'est passe, sans interpreter les choix futurs des joueurs.

**Core Outcome:** une trace de seance — actions des PJ, consequences, changements du monde et des relations, decisions etablies, fils en suspens — reutilisable pour la preparation suivante.

**The Non-Negotiable:** distinguer ce qui est etabli (fait) des fils en suspens (ouvert) ; ne pas figer les decisions a venir.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Consigner les actions des PJ | liste factuelle des actions et choix | recit de la seance | actions consignees |
| Enregistrer consequences et changements | monde et relations mis a jour | actions, reactions du monde | mises a jour notees |
| Lister decisions et fils en suspens | etat des lieux ouvert/ferme | seance | decisions + fils ouverts |

**Memory:** lit la preparation de seance et les fiches PJ ; ecrit le compte rendu dans la trace de campagne.

**Init Responsibility:** aucune.

**Activation Modes:** interactive

**Tool Dependencies:** aucune.

**Design Notes:** accord explicite d'Olivier — ce suivi alimente directement la preparation de la seance suivante.

### 5. Suivi de campagne (adc-suivi-campagne)

**Type:** workflow

**Persona:** gardien de la continuite — relit la trace, met en evidence ce qui compte pour la suite.

**Core Outcome:** une vue d'ensemble a jour de la campagne — etat des PJ, relations, tensions evoluees, fils en suspens actifs, prochaine amorce suggeree.

**The Non-Negotiable:** proposer, ne pas imposer — le meneur valide les suggestions.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Resumer l'etat de la campagne | vue synthetique a jour | tous les comptes rendus, fiches PJ, cadre | resume de campagne |
| Mettre en evidence les fils actifs | fils en suspens priorises | comptes rendus | liste de fils ouverts |
| Suggerer la prochaine amorce | amorce coherente avec l'etat actuel | etat + tensions | suggestion d'amorce |

**Memory:** lit toute la trace de campagne ; met a jour la vue d'ensemble.

**Init Responsibility:** verifie qu'au moins un compte rendu existe.

**Activation Modes:** interactive

**Tool Dependencies:** aucune.

**Design Notes:** pont entre les seances — relit les comptes rendus pour alimenter le skill 3 (preparation de seance).


## Configuration

Not ready — complete in Phase 3+

<!-- Module-level config variables for the setup skill. -->
<!-- If none needed, explicitly state: "This module requires no custom configuration beyond core BMad settings." -->

| Variable | Prompt | Default | Result Template | User Setting |
| -------- | ------ | ------- | --------------- | ------------ |
|          |        |         |                 |              |

## External Dependencies

Not ready — complete in Phase 3+

<!-- CLI tools, MCP servers, or other external software that skills depend on -->
<!-- For each: what it is, which skills need it, and how the setup skill should handle it -->

## UI and Visualization

Not ready — complete in Phase 3+

<!-- Does the module include dashboards, progress views, interactive interfaces, or a web app? -->
<!-- If yes: what it shows, which skills feed into it, how it's served/installed -->

## Setup Extensions

Not ready — complete in Phase 3+

<!-- Beyond config collection: web app installation, directory scaffolding, external service configuration, starter files, etc. -->
<!-- These will need to be manually added to the setup skill after scaffolding -->

## Integration

Not ready — complete in Phase 3+

<!-- Standalone: how it provides independent value -->
<!-- Expansion: parent module, cross-module capability relationships, skills that may reference parent module ordering -->

## Creative Use Cases

Not ready — complete in Phase 3+

<!-- Beyond the primary workflow — unexpected combinations, power-user scenarios, creative applications discovered during brainstorming -->

## Ideas Captured

- Intention exprimee : concevoir un module BMAD oriente jeu de role sur table.
- Public : meneur de jeu et joueurs.
- Usage commun au meneur et aux joueurs : concevoir les personnages joueurs.
- Usage du meneur : construire des environnements pour les joueurs.
- Usage du meneur : aider a creer des scenarios.
- Reference partagee : Gamemastering, Brian Jamison (PDF present dans le projet ; edition/etat editorial a preciser si necessaire).
- Clarification de priorite : l'objectif n'est pas de demander a l'IA de combler les trous d'idees. Le module doit aider a creer des parties de jeu de role en suivant la methode de Gamemastering, que Olivier apprecie particulierement.
- Perimetre vise : accompagner le cycle complet, depuis la creation des personnages joueurs et du cadre de campagne jusqu'a la preparation de la premiere seance, des seances suivantes et la gestion de campagne.
- Le module devrait mobiliser les techniques de Gamemastering qu'Olivier juge utiles pour sa pratique ; la methode sert de guide, et les choix de techniques restent a valider avec lui.
- Direction choisie : approche hybride. Le parcours de campagne s'appuie sur une methode commune, tandis que chaque campagne peut preciser son jeu afin d'adapter la creation des personnages et les conseils mecaniques aux regles disponibles.
- Choix d'integration : module autonome ; Olivier ne voit pas de module parent necessaire a son usage.
- Complementarites eventuelles, sans dependance obligatoire : les outils Core de brainstorming ou d'elicitation avancee peuvent aider a explorer une idee ; le module Storytelling de Creative Intelligence Suite peut servir de partenaire ponctuel pour le travail narratif. Le parcours JDR doit toutefois rester complet sans eux.
### Niveaux : Systeme vs Campagne

Deux niveaux distincts, a ne pas confondre :

- **Systeme de jeu (niveau module)** : GURPS est le premier systeme pris en charge, mais GURPS est un systeme generique — il couvre tous les genres et epoques. Le module ne doit pas supposer un cadre particulier. D'autres systemes pourront etre ajoutes plus tard ; la methode de preparation reste independante du systeme, seuls les elements mecaniques (creation de personnage, conseils de regles) s'adaptent au systeme declare.
- **Campagne (niveau utilisateur)** : le cadre pulp des annees 1920 (prouesses cinematographiques, limites humaines, pas de super-pouvoirs ni de surnaturel) est le contexte de la campagne actuelle d'Olivier. Ce cadre est declare au niveau de la campagne, pas encode dans le module. Toute autre campagne peut choisir un genre, un ton et des elements differents.
- Accord d'Olivier : apres chaque seance, le module doit aider a consigner le deroulement, suivre les evolutions et fils en suspens, puis reutiliser ces informations pour preparer la suite de la campagne.
- Le livre a ete consulte pour en extraire les principes ci-dessous. Synthese reformulee, sans reproduire ses formulaires ni ses tables.
- Nom et code retenus : Atelier de Campagne (adc). Le module est autonome ; la description du frontmatter reste une formulation de travail.

### Points methodologiques releves dans Gamemastering

Reference : Brian Jamison, Gamemastering, notamment chapitres 1-4 (experience partagee, univers et personnages), 6-11 (aventures, obstacles, lieux et distribution) et 22 (improvisation en cours de partie). Les principes ci-dessous sont une synthese reformulee :

- Partir des personnes a la table : le jeu est une experience partagee. Construire autour des envies, styles de jeu et personnages des joueurs, plutot que leur imposer une histoire deja verrouillee.
- Lier personnage et scenario : creer les personnages avant de preparer les aventures. Explorer avec chaque joueur le concept, le passe, les valeurs, les relations (amis, ennemis, problemes), les traits et les objectifs ; verifier que les regles et capacites du personnage lui permettent de poursuivre ses objectifs.
- Construire l'univers pour le jeu : donner assez de structure sociale et geographique pour rendre les lieux credibles et jouables, sans accumuler de lore ou de descriptions qui ne serviront pas a la table. Faire emerger des situations a partir des tensions et besoins locaux.
- Concevoir une aventure comme un point de depart, pas un scenario a embranchements fixes : relier une amorce de conflit et des adversaires aux objectifs ou relations des personnages ; preparer une seance a la fois et laisser les choix du groupe faire evoluer la suite.
- Preparer des obstacles simples, jouables et flexibles : pour chacun, clarifier l'information que les personnages peuvent obtenir, le defi a surmonter, les competences qui peuvent compter et plusieurs approches plausibles. La reussite ne doit pas etre garantie ; un echec important doit produire une consequence ou une autre voie, pas bloquer la partie.
- Donner du poids aux reussites : faire exister les consequences et prendre un moment pour rendre la victoire visible, au lieu d'enchainer les obstacles sans retour.
- Faire des lieux et personnages secondaires des sources d'action : utiliser quelques details concrets, des besoins, objectifs ou problemes locaux ; privilegier les personnages deja lies aux PJ et ne preparer que le niveau de detail utile.
- Improviser a partir du materiel deja pose : accueillir les detours, reutiliser relations, lieux et personnages, et faire reagir le monde aux actions des PJ. Une preparation utile offre des prises et des options au meneur, pas une obligation de ramener les joueurs sur le chemin prevu.
- Garder la description orientee vers le jeu : presenter des details perceptibles qui ouvrent des choix ou donnent une information exploitable ; condenser les passages sans decision ou enjeu.

### Traduction possible pour l'assistant JDR

- Le coeur du module est un accompagnement de preparation de partie, guide par les principes de Gamemastering, et non une fonction de remplissage automatique de lacunes.
- Le parcours vise l'ensemble de la campagne : creation des PJ et du cadre, amorcage de la premiere seance, preparation iterative des seances suivantes et suivi des evolutions de campagne.
- Direction preferee pour la portabilite : garder la methode de preparation independante d'un systeme particulier et adapter les elements mecaniques au jeu declare pour chaque campagne.
- Le parcours de preparation devrait partir du groupe, des personnages joueurs (objectifs, relations, capacites) et du contexte de campagne, puis aider a formuler l'amorce et le conflit de la seance.
- Il devrait ensuite aider a preparer les lieux utiles, les personnages secondaires pertinents et des obstacles flexibles, en tenant compte des competences des PJ, des pistes d'information, des approches possibles et des consequences.
- Entre les seances, le module devrait aider a produire ou mettre a jour une trace de campagne a partir du compte rendu : actions des PJ, consequences, changements du monde et des relations, decisions etablies et fils en suspens. Ces informations alimentent la preparation suivante, sans figer les decisions a venir.
- La structure doit rester un support souple : proposer des choix et demander l'avis du meneur aux decisions creatives, sans imposer une intrigue lineaire ni presumer des choix des joueurs.
- La creation de personnages et la construction d'environnements restent des besoins importants, integres a la preparation de parties plutot que concus comme une collection d'outils de completude d'idees.

<!-- Raw ideas from brainstorming — preserved for context even if not all made it into the plan -->
<!-- Write here freely during phases 1-2. Don't write structured sections until phase 3+. -->

## Build Roadmap

Not ready — complete in Phase 3+

<!-- Recommended build order with rationale for why each skill should be built in that order -->

**Next steps:**

1. Build each skill using **Build an Agent (BA)** or **Build a Workflow (BW)** — share this plan document as context
2. When all skills are built, return to **Create Module (CM)** to scaffold the module infrastructure
