#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twython, time, sys, json

# Connect to Twitter
from config import *
twitter = twython.Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#twitter.verify_credentials()

# Create chunks of 100 tweets
nb = 0
tweetBulks = []
tweetIds = []
for tweetId in open(sys.argv[1]):
	tweetId = tweetId.strip()
	nb += 1
	tweetIds.append(tweetId)
	if not nb%100:
		tweetBulks.append(tweetIds)
		tweetIds = []
tweetBulks.append(tweetIds)
print '--- Ids in list:', nb

# Open output file
out = open(sys.argv[2], 'w')

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
				json.dump(tweet, out)
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
