#!/bin/bash

mkdir -p Matchs
wget -rnH --accept "*.json" http://helium.lab.parisdescartes.fr:2232/tweets/ -P Matchs
