#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twython, time, sys, json, argparse

aparser = argparse.ArgumentParser(description='Retrieve media tweets as list of IDs')
aparser.add_argument('-i', '--ids', help='File containing IDs (one per line)', required=True)
aparser.add_argument('-o', '--outfile', help='Output file', required=True)
args = aparser.parse_args()

# Connect to Twitter
from config import *
twitter = twython.Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#twitter.verify_credentials()

# Create chunks of 100 tweets
nb = 0
tweetBulks = []
tweetIds = []
for tweetId in open(args.ids):
	tweetId = tweetId.strip()
	nb += 1
	tweetIds.append(tweetId)
	if not nb%100:
		tweetBulks.append(tweetIds)
		tweetIds = []
tweetBulks.append(tweetIds)
print '--- Ids in list:', nb

# Open output file
outfile = open(args.outfile, 'w')

# Loop to retrieve tweets via API
nb = 0
excludeRetweets = False
for tweetBulk in tweetBulks:
	try:
		tweets = []
		print '--- Searching'
		print ','.join(tweetBulk)
		tweets = twitter.lookup_status(id=','.join(tweetBulk))
		nbRetrieved = 0
		for tweet in tweets:
			if excludeRetweets and 'retweeted_status' in tweet:
				print '--- Excluding retweet', tweet['id_str']
			else:
				print '--- Output', tweet['id_str']
				json.dump(tweet, outfile)
				outfile.write('\n')
				nb += 1
		print '--- Retrieved:', nb
	except twython.TwythonRateLimitError as error:
		remainder = float(twitter.get_lastfunction_header(header='x-rate-limit-reset')) - time.time()
		print '--- Sleeping:', remainder
		if remainder > 0:
			time.sleep(remainder)
		continue
	except Exception, e:
		print e
		print '--- Unkown exception.... sleeping 15 min anyway before retry'
		time.sleep(60*15)

print '--- Finished with:', nb
