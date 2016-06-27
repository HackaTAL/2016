#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, gensim, argparse, codecs, numpy, scipy.spatial.distance, itertools

aparser = argparse.ArgumentParser(description='Retrieve media tweets as list of IDs')
aparser.add_argument('-d', '--docfile', help='Tweeter documents json file', required=True)
aparser.add_argument('-m', '--mediasfile', help='Tweeter medias json file', required=True)
aparser.add_argument('-u', '--userfile', help='User txt file', required=True)
args = aparser.parse_args()

# Retrieve tweeets as documents
documents  = []
for line in open(args.docfile):
	tweet = json.loads(line)
	#print tweet['text']
	documents.append(gensim.models.doc2vec.LabeledSentence(words=tweet['text'].split(' '), tags=[u'SENT']))

euromodel = gensim.models.Doc2Vec(documents, size=100, window=8, min_count=5, workers=4)

#model.save(fname)

# Represent media sentences in the corresponding model
mediadocs = {}
for line in open(args.mediasfile):
	tweet = json.loads(line)
	#print tweet['user']
	screenname = tweet['user']['screen_name']
	if not screenname in mediadocs:
		mediadocs[screenname] = []
	mediadocs[screenname].append(euromodel.infer_vector(tweet['text']))

# Internal similarity
for media1, media2 in itertools.combinations(mediadocs.keys(), 2):
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
	uservecs.append(euromodel.infer_vector(line[:140])) # Should be UTF8 size...
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
