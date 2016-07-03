# Évaluation des fils de tweets
------------------------------------------

## Génération d'un fil

Il s'agit de générer un fil (texte ligne par ligne), qui corresponde le plus à un ensemble de fils récupérés sur des médias. L'évaluation se fait par similarité sur un modèle gensim calculé sur l'ensemble des tweets (train ou eval).

## Évaluation du fil par rapport aux médias

La métrique est une combinaison de

- meilleur appariement pour le test vis à vis du média, puis moyenne
- moyenne sur les médias (lequipe beinsports_FR Le_Figaro lemondefr le_Parisien 20minutesSport)

```
python evalfil.py -g train_euro2016.gensim -m ../../Tweets/Medias/all.json -u testfil.txt
```

Quelques exemples de scores obtenus :

- baseline mot football : 0.0525807619907
- baseline mot #Euro2016 : 0.0525807619907
- baseline quarante mots les plus fréquents : 0.228415901191


