#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, gensim, argparse, codecs, numpy, scipy.spatial.distance, itertools

aparser = argparse.ArgumentParser(description='Retrieve media tweets as list of IDs')
aparser.add_argument('-g', '--gensimfile', help='Gensim precomputed model', required=True)
aparser.add_argument('-m', '--mediasfile', help='Tweeter medias json file', required=True)
aparser.add_argument('-u', '--userfile', help='User txt file', required=True)
args = aparser.parse_args()

euromodel = gensim.models.Doc2Vec.load(args.gensimfile)

# Represent media sentences in the corresponding model
mediadocs = {}
jsontmp = ''
mediajsons = []
for line in open(args.mediasfile):
	jsontmp += line
	if line.startswith('}'):
		mediajsons.append(jsontmp)
		jsontmp = ''
mediajsons = '['+','.join(mediajsons)+']'
tweets = json.loads(mediajsons)
for tweet in tweets:
	#print tweet['user']
	screenname = tweet['user']['screen_name']
	if not screenname in mediadocs:
		mediadocs[screenname] = []
	gensimtext = gensim.models.doc2vec.LabeledSentence(words=tweet['text'].split(' '), tags=[u'SENT'])
	mediadocs[screenname].append(euromodel.infer_vector(gensimtext.words))

# Internal similarity
for media1 in mediadocs:
	for media2 in mediadocs:
		mediavecs = mediadocs[media1]
		sims = numpy.array([-1.0]*len(mediavecs))
		for i in range(len(mediavecs)):
			for uservec in mediadocs[media2]:
				sim = 1 - scipy.spatial.distance.cosine(mediavecs[i], uservec)
				if sim > sims[i]:
					sims[i] = sim
		print 'Comparing media', media1, 'with media', media2, ':', sims.mean()

# Compare user file with medias
uservecs = []
for line in codecs.open(args.userfile, encoding='utf8'):
	line = line.strip()
	if len(line):
		gensimtext = gensim.models.doc2vec.LabeledSentence(words=line, tags=[u'SENT'])
		uservecs.append(euromodel.infer_vector(gensimtext.words)) # Should be UTF8 size...
mediasims = []
for media in mediadocs:
	mediavecs = mediadocs[media]
	sims = numpy.array([-1.0]*len(mediavecs))
	for i in range(len(mediavecs)):
		for uservec in uservecs:
			sim = 1 - scipy.spatial.distance.cosine(mediavecs[i], uservec)
			if sim > sims[i]:
				sims[i] = sim
	mediasims.append(sims.mean())
	print 'Comparing with media', media, ':', mediasims[-1]

print 'Score final: ', ':', numpy.array(mediasims).mean()
