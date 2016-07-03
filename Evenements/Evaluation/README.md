# Évaluation des résumés de matches
-----------------------------------

## Métriques et calculs

Les slides présentant la métrique sans dans le dossier [Présentations](../../Presentations/).

## Fonctionnement du script d'évaluation

Il faut lui fournir les fichiers de référence et la sortie du système.

```
python combine_event_files.py ../Resumes/Albanie_Suisse_2016-06-11_15h_fr.tsv > ref.tsv
python combine_event_files.py Exemple_Tests/Albanie_Suisse_2016-06-11_15h_fr.tsv > test.tsv
python eval_events_euro2016.py -t team_name -s system_name ref.tsv test.tsv
```

Pour évaluer une archive de soumission :

```
python combine_event_files.py ../Resumes/Albanie_Suisse_2016-06-11_15h_fr.tsv > ref.tsv
bash evaluate_submission.sh ./tmp ./ref.tsv ./Exemple_Tests/team1_sys1.tgz
``` 