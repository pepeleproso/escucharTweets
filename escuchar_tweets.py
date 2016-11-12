from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import os
import time
import datetime
import io

class JsonFileStorage(object):
    def __init__(self, prefijoNombre):
        self.filename = prefijoNombre + str(datetime.datetime.now()).split(':')[0] + '.json'
    
    def guardarTweet(self, tweetjson):
        try:
            with open(self.filename, 'a') as outfile:
                json.dump(tweetjson, outfile)
        except BaseException, e:
            raise Exception('Error guardando tweet',e)

class listener(StreamListener):
    def __init__(self, start_time, time_limit=2):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []
        self.TweetStorage = JsonFileStorage('tweetsMarcha')


    def on_data(self, data):
        print(data)

        try:
            self.TweetStorage.guardarTweet(data)
            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(5)
            pass

    def on_error(self, status):
        with open('logError.json', 'a') as errfile:
            errfile.write(status)
            errfile.write('\n')

class EscucharTweets(object):
    def __init__(self):
        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_secret = None
        self.keyword_list = []

        #iniciar el cliente
        escucharTweets.CargarDatosTwitterApp()

    def CargarDatosTwitterApp(self):
        with open('twitterApp.json', 'r') as twitterAppfile:
                filecontents = json.load(twitterAppfile)
                self.consumer_key = filecontents['TwitterAPP'][0]['consumer_key']
                self.consumer_secret = filecontents['TwitterAPP'][0]['consumer_secret']
                self.access_token = filecontents['TwitterAPP'][0]['access_token']
                self.access_secret = filecontents['TwitterAPP'][0]['access_secret']
                self.keyword_list = filecontents['HasTags']
    
    def IniciarEscucha(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        start_time = time.time()
        twitterStream = Stream(auth, listener(start_time))
        twitterStream.filter(track=self.keyword_list, stall_warnings=True, async=False, encoding='utf8')

escucharTweets = EscucharTweets()
escucharTweets.IniciarEscucha()