# Personae

## Administration
!!! Note
	Ces commandes sont réservés aux administrateurs du serveur.

→ [Liens vers le tutoriel](../tuto/personae.md#Administration)
### Activation
- `?active_persona 0` : Désactive globalement les Personae sur le serveur.
- `?active_persona 1` : Active globalement les Personae sur le serveur.

!!! Warning
	Cette commande écrase le nombre maximum de Personae autorisé. 

!!! Note
	Il est possible de passer par `?max_config -1` et `?max_config 0` pour désactiver les Personae sur le serveur.

`?admin_rp` : Affiche le panneau de configuration des Personae, permettant de modifier les différents paramètres à partir de choix.

### Sticky Mode
!!! Note
	Le `sticky` permet de garder son persona en permanence, sauf lors de l’utilisation d’un autre “token” ou du [Pattern HRP|pattern HRP](admin.md#Pattern%20HRP)

`?sticky_mode`[^1] : Active ou désactive le mode sticky.

### Limitation
La commande `?max_config <nombre>`[^2] permet de limiter le nombre de Persona des joueurs, avec le `<nombre>` indiqué.

### Tag
Les tags des Personae sont des patterns préconfigurés par les admins se trouvant sur l’ensemble des Personae. Ils peuvent être **avant** ou **après** le nom du personnage, et être :
- Le pseudo du joueur : `@user`;
- Le nom du serveur : `@server` ;
- L’ID du Persona : `@persona` ; 

Il est aussi possible de configurer la mise en forme, avec, par exemple :
- `@user - Personae Nom`
- `Personae - [@User]`
- `[@Server] - Personae`

## Personae
→ [Liens vers le tutoriel](../tuto/personae.md#Création)] 

- `?personae` : Ouvre le menu de configuration des Personae.
- `?personae_edit` : Ouvre le menu d’édition des Personae.

### Edition
!!! Note
	Il est aussi possible d’utiliser les token des personnages en plus de leurs noms. 

- `?personae nom <nom_personae> <nouveau_nom>` : Permet d’éditer le nom d’une Persona `<nom_personae>` par `<nouveau_nom>`.
-  `?personae token <nom_Personae>` : Permet d’éditer le token d’une Persona .
- `?personae image <nom_personae>` : Permet d’éditer l’image d’une Persona.
- `?personae delete <nom>` : Permet de supprimer une Persona.

### Message

→ [Lien vers le tutoriel](../tuto/personae.md#Message)

- Les Personæ se déclenchent à l’envoie d’un message avec un token (ou nom, en fonction du mode sticky et de la persona utilisé précédemment.)
- L’édition se fait par l’utilisation de la fonction “réponse” de discord : Il suffit de répondre à son message avec le nouveau message.
- La suppression se fait par l’ajout de la réaction `❌`.


[^1]: `?sticky_config` ; `?config_sticky`
[^2]: `?maxDC <nb>` ; `?maxdc_config <nb>` ; `config_max <nb>`