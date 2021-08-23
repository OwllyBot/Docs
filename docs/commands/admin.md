# Configuration générale

`?config` : Permet de configurer à la suite :

- Le prefix
- Les rôles ajoutés et supprimés automatiquement par la commande `?member`
- Le channel du [lexique](utilitaire.md#lexique)
- Les channels des fiches
- Les [personae](personae.md)
- Les [tags HRP](personae.md#tags-hrp)
- Les channels et catégories RP

# Prefix

- `?set_prefix <prefix>` : Permet de changer le préfixe
- `@Owlly prefix` et `$$prefix`: Permettent d’obtenir le préfixe du bot (en cas d’oublie ;))

# Member

## Administration

### Commande en ligne

- `?admin_member add <role>` : Permet d’enregistrer ou réenregistrer la liste des rôles donnés par la commande `?member` sans passer par le menu de configuration.
- `?admin_member rm <role>` : Permet de supprimer des rôles automatiquement par la commande `?member`.

Le paramètre `<role>` peut être une suite de rôle sous forme de nom, ID ou mention.

### Menus

- `menu_member add` : Ouvre le menu pour configurer les rôles ajoutés par la commande.
- `menu_member rm` : Ouvre le menu pour supprimer des rôles par la commande `member`.

## Ajouter un nouveau membre

`?member <user> <*role>`

- Cette commande permet de donner à un joueur divers rôles, qui peuvent exister ou non[^1].
- Elle permet aussi de supprimer des rôles automatiquement (configuré préalablement).
- Les `*role` peut être une suite de rôle sous forme d’ID, nom ou mention.
- `user` peut être un nom, une mention ou un ID.

`?set_role <user> <*role>*`  
Cette commande permet à un administrateur de rajouter des rôles rapidement à un membre.

- Les `*role` peut être une suite de rôle sous forme d’ID, nom ou mention.
- `user` peut être un nom, une mention ou un ID.

# Channel RP

`?chanRP`[^alias] : Ouvre le menu de configuration des channels et catégories RP.

# Pattern HRP

`?patternHRP` : Permet de configurer le pattern HRP, c'est-à-dire que :

- Les messages ayant ce pattern peuvent être supprimé automatiquement.
- Les messages ayant ce pattern ne sont pas transformé en persona.

Les différentes manières de configurer un pattern[^3] sont :

- `/text/`
- `/text`
- `text/`
- `stop` et `cancel` permettent d’annuler la configuration.
- `0` Permet de supprimer le pattern.

## Délais de suppression HRP

`?delay_HRP` : Cette commande ouvre un menu de configuration qui permet de configurer le délai de suppression.

[^1]: Les rôles n’existant pas sont créé par le bot.
[^alias]: `chanRP_menu` ; `config_chanRP`
[^3]: Vous pouvez mettre ce que vous désirez à la place de `/`
