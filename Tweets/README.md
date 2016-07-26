# Données (tweets) sur l'Euro 2016
----------------------------------

## Scripts de récupération de Tweets

### Préalable

Il vous faut des clés pour utiliser l'API de Twitter
- loguez-vous sur https://apps.twitter.com/
- sélectionnez *Create New App*
- les clés à utiliser sont dans *Keys and Access Tokens*
- configurez le scirpt `confg.py`

### Scripts disponibles

Trois scripts sont disponibles
- `retrieveeuro.py` : récupération de tweets sur le hashtag #Euro2016
- `retrieveids.py` : récupération de tweets à partir d'une liste d'IDs
- `retrievemedias.py` : récupération de tweets selon la source

## Tweets de train et de dev

### Téléchargement des matchs

Les tweets ont été sélectionnés par SYSTRAN en utilisant de l'API (streaming). Nous les avons stockés sur un [serveur web](http://helium.lab.parisdescartes.fr:2232/tweets/).

Ils peuvent être téléchargés automatiquement grâce au script `downloadmatchs.sh` (qui vous créera l'arborescence dans votre git, téléchargera les IDs des tweets puis collectera les tweets eux-même en utilisant le retriever, à configurer). Vous aurez besoin de l'outil `jq`

```
sudo apt-get install jq
./downloadmatchs.sh
```

Vous obtiendrez pour chaque groupe et match de l'entraînement (première journée de l'Euro)
- IDs des tweets
- fichiers JSON
- texte brut des tweets
