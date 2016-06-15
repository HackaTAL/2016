#!/bin/bash

echo "Using soccer-cli https://github.com/architv/soccer-cli"
export SOCCER_CLI_API_TOKEN=$(cat apikey.txt)
echo "Token key: $SOCCER_CLI_API_TOKEN"
out=""

echo "Matches prévus aujourd'hui et demain"
soccer $out --league EURO --upcoming --time=2

echo "Prochains matches de l'équipe de France"
soccer $out --league EURO --team FRA --upcoming --time=10

echo "Matches prévus demain"
soccer $out --league EURO --upcoming --time=2

echo "Résultats des 3 derniers jours"
soccer $out --league EURO --time=3
