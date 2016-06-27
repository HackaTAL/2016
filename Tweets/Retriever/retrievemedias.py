#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twython, time, sys, json, datetime, argparse

aparser = argparse.ArgumentParser(description='Retrieve media tweets for a given date')
aparser.add_argument('-d', '--date', help='Date in format YYYYMMDD', required=True)
aparser.add_argument('-l', '--lang', help='Lang of tweet', required=True)
aparser.add_argument('-o', '--outfile', help='Output file', required=True)
args = aparser.parse_args()

# Connect to Twitter
from config import *
twitter = twython.Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#twitter.verify_credentials()

# Query
datestart = datetime.datetime.strptime(args.date, '%Y%m%d') # UTC is convenient as it is Paris 2am to 2am
dateend = datestart + datetime.timedelta(days=1)
query = '(#Euro2016 AND since:'+datestart.strftime('%Y-%m-%d')+' AND until:'+dateend.strftime('%Y-%m-%d')+' AND lang:'+args.lang+' AND (from:lequipe OR from:beinsports_FR OR from:Le_Figaro OR from:lemondefr OR from:le_Parisien OR from:20minutesSport))'

# Open output file
outfile = open(args.outfile, 'w')

# Loop to retrieve tweets
nb = 0
nbMax = 50000
maxid = None
excludeRetweets = False
while nb < nbMax:
	print '--- Retrieved:', nb, '(max: ', str(maxid), ')'
	try:
		tweets = []
		print '--- Searching'
		tweets = twitter.search(q=query, max_id = maxid, count=100)['statuses']
		nbRetrieved = 0
		for tweet in tweets:
			if excludeRetweets and 'retweeted_status' in tweet:
				print '--- Excluding retweet', tweet['id_str']
			else:
				print '--- Output', tweet['id_str']
				json.dump(tweet, outfile)
				outfile.write('\n')
				maxid = tweet['id_str']
				nbRetrieved += 1
		if nbRetrieved and nb < nbMax:
			nb += nbRetrieved
			maxid = int(maxid) - 1
		else:
			print '--- No more tweets, exiting'
			break
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
