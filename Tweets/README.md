# Données (tweets) sur l'Euro 2016
----------------------------------

## Tweets de train et de dev

### Téléchargement des matchs

Les tweets ont été sélectionnés par Systran en utilisant de l'API (streaming). Nous les avons stockés sur un [serveur accessible avec un navigateur](http://helium.lab.parisdescartes.fr:2232/tweets/train_euro2016/), ils peuvent être téléchargés automatiquement grâce au script `downloadmatchs.sh` (qui vous créera l'arborescence dans votre git).

### Extraction des textes




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
