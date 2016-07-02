#!/bin/bash

echo "Téléchargement des matchs"
mkdir -p Matchs
wget -c -N -P Matchs http://helium.lab.parisdescartes.fr:2232/tweets/train_euro2016.tgz
tar -xvzf Matchs/train_euro2016.tgz -C Matchs

echo "Récupération des résumés"
cp $(find Matchs -name *.tsv) ../Evenements/Resumes/

echo "Extract tweets IDs and text"
for json in $(find Matchs -name *.json); do
	jsonbn=$(basename $json .json)
	jsondn=$(dirname $json)
	echo "Extract ids and text from $jsonbn"
	jq -r '.id_str' $json > $jsondn/$jsonbn.ids
	jq -r '.text' $json > $jsondn/$jsonbn.txt
done

echo "Fichier contenant tous les textes des tweets"
cat $(find Matchs -name *.txt) > Matchs/all.txt

echo "Récupération des textes bruts"
wget -c -N -P Matchs http://helium.lab.parisdescartes.fr:2232/tweets/train_euro2016.txt.tgz
tar -xvzf Matchs/train_euro2016.txt.tgz -C Matchs

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
