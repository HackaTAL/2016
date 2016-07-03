# Évaluation des résumés de matches
-----------------------------------

## Métriques et calculs

Les slides présentant la métrique sans dans le dossier [Présentations](../../Presentations/).

## Fonctionnement du script d'évaluation

Il faut lui fournir les fichiers de référence et la sortie du système.

```
python combine_event_files.py ../Resumes/Albanie_Suisse_2016-06-11_15h_fr.tsv > ref.tsv
python combine_event_files.py Exemple_Tests/Albanie_Suisse_2016-06-11_15h_fr.tsv > test.tsv
python eval_events_euro2016.py ref.tsv test.tsv
```
