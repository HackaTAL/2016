#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, gensim, argparse, codecs, numpy, scipy.spatial.distance, itertools

aparser = argparse.ArgumentParser(description='Retrieve media tweets as list of IDs')
aparser.add_argument('-t', '--txtfile', help='Documents txt file', required=True)
aparser.add_argument('-g', '--gensimfile', help='Gensim precomputed model', required=True)
args = aparser.parse_args()

# Retrieve tweeets as documents
documents  = []
for line in open(args.txtfile):
	line = line.strip()
	documents.append(gensim.models.doc2vec.LabeledSentence(words=line.split(' '), tags=[u'SENT']))

euromodel = gensim.models.Doc2Vec(documents, size=300, window=10, min_count=3, workers=4)
euromodel.save(args.gensimfile)
