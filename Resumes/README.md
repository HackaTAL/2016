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
	- `min C joueur1 joueur2` : changement de joueurs (joueur sortant et joueur entrant)
	- `min DP1 pays1 pays2` : début de la première période du match entre les deux pays indiqués
	- `min FP1 score` : fin de la première période et score
	- `min DP2` : début de la deuxième période
	- `min FP2 score` : fin de la deuxième période et score
	- `min DPR` : début de prolongation
	- `min FPR` : fin de prolongation
- `SUMMARY` résumé textuel du match
