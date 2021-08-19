#!/usr/bin/env python

import twitter
import requests as re
import os
import pprint as pp
import IPython
import json

consumer_key = os.environ["TWITTER_CONSUMER_ID"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS"]
access_token_secret = os.environ["TWITTER_ACCESS_SECRET"]

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

## FOLLOWING FUNCTION WILL COLLECT REAL-TIME TWEETS IN OUR COMPUTER

# data returned will be for any tweet mentioning strings in the list FILTER
FILTER = ['#datascience']

# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
LANGUAGES = ['en']

# path, location, FILTER, LANGUAGES
def main(path='output.txt', LOCATIONS=[''], FILTER=['#datascience'], LANGUAGES=['en']):
    with open(path, 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES, locations=LOCATIONS):
            f.write(json.dumps(line))
            #pp.pprint(json.dumps(line))
            f.write('\n')

# Execute function
main()