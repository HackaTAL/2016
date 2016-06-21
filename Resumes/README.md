# Résumé des matches de l'Euro
----------------------------------

On résume un match avec les champs suivants

- `URL` : si le résumé est manuel, source du résumé
- `LOC` : lieu de la rencontre
- `POSS NB NB` : proportion de possession de la balle (chiffres selon le nom du fichier)
- `GOALS (joueur,pays,min)*` : liste de buts avec les infos les concernant
- `EVTS` liste des évènements, un par ligne, avec leur minute, parmi
	- `min B joueur` : but d'un joueur
	- `min T joueur` : tir d'un joueur
	- `min CJ joueur` : carton jaune pour un joueur
	- `min CR joueur` : carton rouge pour un joueur
	- `min P pays` : penalty pour un pays (celui qui commet la faute)
- `SUMMARY` résumé textuel du match
