from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import os
import time
import datetime
import io

class listener(StreamListener):
    def __init__(self, start_time, time_limit=2):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []

    def on_data(self, data):
        print(data)
        filename = 'tweetsMarcha' + str(datetime.datetime.now()).split(':')[0] + '.json'
 
        try:
            with open(filename, 'a') as outfile:
                json.dump(data, outfile)
                return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(5)
            pass

	def on_error(self, status):
		print statuses

consumer_key = "wPvbnar6XewHPJBfreavg5urr"
consumer_secret ="w6Ufk0mRRoCDpMssOrQEgTqVo9AmAKbd9sXByVHGYHMIcrYVnU"

access_token = "747416373228376064-KqDPF1xJSmnaHUJ4gKSLqqy8l2qMgVP"
access_secret = "wyqdEYIQmavVfAmH0xXb1qUwW8842ajbnaZ84U08ziLxI"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

keyword_list = ["#Femicidio", "#BuenDomingo"]

start_time = time.time()
twitterStream = Stream(auth, listener(start_time))
twitterStream.filter(track=keyword_list, stall_warnings=True, async=False, encoding='utf8')