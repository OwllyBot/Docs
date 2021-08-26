# Utilitaire

Les utilitaires sont une série de commandes permettant de débug et d’obtenir des informations sur Owlly.

## Lexique

→ Permet de chercher un texte parmi un channel préconfiguré.

- `?note_config <channel>`
    - Le channel peut être sous forme d’ID, de nom ou de mention.
    - `0` désactive la commande.
- `?search <mot>` [^alias] : Permet de rechercher un mot parmi le channel configuré. En cas de plusieurs match, tous les résultats sont envoyés. Les mots orthographiés sans leurs accents fonctionnent aussi.

## Ping
`?ping` : Permet d’avoir la latence du bot.

## Préfixe
`@Owlly prefix` et `$$prefix`: Permettent d’obtenir le préfixe du bot (en cas d’oublie ;))

## Informations
`?info` affiche des informations sur le bot, tel que :

- Son préfixe
- Sa latence
- Son language (python)
- Le github
- Le kofi


### Signaler un bug
`?info bug` affiche les infos permettant de signaler un bug 

### Roadmap
`?info roadmap` : Donne les liens vers les avancées en cours sur le bot.

### Kofi
`?info kofi` : Donne le lien vers le kofi

## Purge
`?purge`[^purge]: Permet de nettoyer un channel 

[^alias]: `?lexique <mot>`
[^purge]: `?clean`

