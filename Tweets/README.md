# Données (tweets) sur l'Euro 2016
----------------------------------

Les tweets ont été sélectionnés par Systran en utilisant de l'API (streaming). Nous en diffusons ici la liste des identifiants afin que vous puissiez les récupérer pour chaque match.

## Préalable

Il vous faut des clés pour utiliser l'API de Twitter
- loguez-vous sur https://apps.twitter.com/
- sélectionnez *Create New App*
- les clés à utiliser sont dans *Keys and Access Tokens*

## Récupération de tweets

En Python
- aller dans `Retriever/Python`
- configurer le `config.py` (les clés)
- `python retrieveids.py ../../IDs/maliste.ids ../../JSON/mestweets.json`

En Java (à tester,  merci à Amel / Cyril / Patrick / DEFT)
- aller dans le `Retriever/Java`
- configurer le `App.properties` (les clés, éventuellement le fichiers d'IDs et le répertoire de sortie)
- `java -jar  tweet_basic-retriever.jar`
