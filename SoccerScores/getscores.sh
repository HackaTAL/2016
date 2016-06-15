#!/bin/bash

echo "Using soccer-cli https://github.com/architv/soccer-cli"
export SOCCER_CLI_API_TOKEN=$(cat apikey.txt)
echo "Token key: $SOCCER_CLI_API_TOKEN"

echo "Matches prévus aujourd'hui et demain"
soccer --league EURO --upcoming --time=2

echo "Prochains matches de l'équipe de France"
soccer --league EURO --team FRA --upcoming --time=10

echo "Matches prévus demain"
soccer --league EURO --upcoming --time=2

echo "Résultats des 3 derniers jours"
soccer --league EURO --time=3
