#!/bin/bash

echo "Téléchargement des ids de tweets pour les matchs"
mkdir -p Matchs
wget -c -N -P Matchs http://helium.lab.parisdescartes.fr:2232/tweets/train_euro2016.ids.tgz
tar -xvzf Matchs/train_euro2016.ids.tgz -C Matchs
wget -c -N -P Matchs http://helium.lab.parisdescartes.fr:2232/tweets/eval_euro2016.ids.tgz
tar -xvzf Matchs/eval_euro2016.ids.tgz -C Matchs

echo "Récupération des résumés"
cp $(find Matchs -name *.tsv) ../Evenements/Resumes/

echo "Récupération des tweets à partir des IDs (ceci peut-être très long)"
for f in $(find Matchs/*/* -name *.ids); do
	fn=$(echo $f | sed 's/.ids$/.json/')
	echo "- $fn"
	python Retriever/retrieveids.py -i $f -o $fn
done

echo "Extraction des textes depuis le json"
for json in $(find Matchs -name *.json); do
	jsonbn=$(basename $json .json)
	jsondn=$(dirname $json)
	echo "- $jsonbn"
	jq -r '.text' $json > $jsondn/$jsonbn.txt
done

echo "Création d'un fichier contenant tous les textes"
cat $(find Matchs -name *.txt) > Matchs/all.txt

echo "Téléchargement des fichiers gensim"
wget -c -N -P ../Evenements/Fils http://helium.lab.parisdescartes.fr:2232/tweets/gensim-models/train_euro2016.gensim.tgz
tar -xvzf ../Evenements/Fils/train_euro2016.gensim.tgz -C ../Evenements/Fils

echo "Extraction des médias"
mkdir -p Medias
rm -rf Medias/all.json
for media in lequipe beinsports_FR Le_Figaro lemondefr le_Parisien 20minutesSport; do
	echo "- $media"
	rm -rf Medias/$media.json
	for json in $(find Matchs/ -name *fr.json); do
		jq -r ". | select(.user.screen_name==\"$media\")" $json >> Medias/$media.json
	done
	cat Medias/$media.json >> Medias/all.json
done
