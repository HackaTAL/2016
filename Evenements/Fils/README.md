# Évaluation des fils de tweets
------------------------------------------

## Génération d'un fil

Il s'agit de générer un fil (texte ligne par ligne), qui corresponde le plus à un ensemble de fils récupérés sur des médias. L'évaluation se fait par similarité sur un modèle gensim calculé sur l'ensemble des tweets (train ou eval).


## Récupération du modèle

Sur http://helium.lab.parisdescartes.fr:2232/tweets/gensim-models/train_euro2016.gensim.tgz
Les extraires dans Evenements/Fils

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

Calculer une similarité entre deux tweets `text1` et `text2` :

```
gensimtext1 = gensim.models.doc2vec.LabeledSentence(text1.split(' '), tags=[u'SENT'])
vecs1 = euromodel.infer_vector(gensimtext.words)
gensimtext2 = gensim.models.doc2vec.LabeledSentence(text2.split(' '), tags=[u'SENT'])
vecs2 = euromodel.infer_vector(gensimtext.words)
sim = 1 - scipy.spatial.distance.cosine(mediavecs[i], uservec)
````