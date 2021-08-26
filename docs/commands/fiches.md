# Title test ????

## Administration
!!! Note  
	Les commandes suivantes sont réservés aux administrateurs du serveur.

### Configuration
- `?admin_fiche` : Cette commande permet de choisir les champs ainsi que les parties d’une fiche, d’en supprimer mais aussi d’en rajouter.
- `?admin_fiche add` : Permet d’ajouter des champs sur les fiches
- `?admin_fiche chan`[^chan] : Permet de régler les channels des présentations.
- `?admin_fiche create`[^new] : Permet de lancer la complète des champs et parties d’une fiche. 
- `?admin_fiche delete`[^del] : Permet de supprimer des champs et des parties à une fiche.
- `?admin_fiche add` : Permet d’ajouter des champs à une fiche
- `?admin_fiche see`[^see] : Permet de voir la fiche et ses champs.
- `?admin_fiche part`[^part] : Permet de rajouter des parties

### Création
!!! Note
	Les commandes peuvent être lancées par tous ceux ayant la permission de gérer les surnoms (`Manage Nicknames`)

- `?pj`[^pj] : Lance la création d’une fiche pour un personnage joueur (PJ)
- `?pnj`[^pnj] : Lance la création d’une fiche pour un personnage non-joueur (PNJ)

### Édition
!!! Note
	Les commandes peuvent être lancées par tous ceux ayant la permission de gérer les surnoms (`Manage Nicknames`)


`?admin_edit` : Permet de prendre la main sur une présentation en cours et l’éditer. 

## Joueurs
!!! Note
	Ces commandes peuvent être lancées par n’importe qui.


- `?fiche` : Permet d’afficher le menu d’édition d’une fiche en cours. 
- `?fiche edit` : Permet d’éditer un champ déjà écrit.
- `?fiche delete` : Permet de supprimer une fiche en cours.
- `?fiche reprise` : Permet de reprendre l’écriture d’une fiche
- `?fiche see`[^check] : Permet de voir une fiche. 

[^chan]: `?admin_fiche channel`
[^new]: `?admin_fiche new`
[^del]: `?admin_fiche del` ; `?admin_fiche rm`
[^see]: `?admin_fiche check`
[^part]: `?admin_fiche add_part`
[^pj]: `?add_pj` ; `?validation` ; `?add_pres` ; `?add_presentation`
[^pnj]: `?add_pnj` ; `?validation_pnj`
[^check]: `?fiche check`