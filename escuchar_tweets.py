# -*- coding: utf-8 -*-

#    This file is part of escucharTweets.
#
#    escucharTweets is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    emesene is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with escucharTweets; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import os
import time
import datetime
import io
from NetworkManager import NetworkChecker
from JsonFileStorage import JsonFileStorage


class FileStorageListener(StreamListener):
    def __init__(self, start_time, time_limit=2, filePrefix='tweets'):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []
        self.TweetStorage = JsonFileStorage(filePrefix)

    def on_data(self, data):
        logger.info("Tweet received")
        logger.info(data)

        try:
            self.TweetStorage.saveTweet(data)
            return True
        except BaseException as e:
            logger.error('failed ondata: %s', str(e))
            time.sleep(5)

    def on_error(self, status):
        logger.error('Error Status: %s', status)

        with open('logError.json', 'a') as errfile:
            errfile.write(str(status))
            errfile.write('\n')

    def on_timeout(self):
        logger.error("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 

class TweetBot(object):
    def __init__(self):
        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_secret = None
        self.keyword_list = []
        self.twitterStream = None
        self.loadConfigData()

    def loadConfigData(self):
        logger.info("Loading Config Options")
        with open('escucharTweets.json', 'r') as twitterAppfile:
                filecontents = json.load(twitterAppfile)
                self.consumer_key = filecontents['TwitterAPP'][0]['consumer_key']
                self.consumer_secret = filecontents['TwitterAPP'][0]['consumer_secret']
                self.access_token = filecontents['TwitterAPP'][0]['access_token']
                self.access_secret = filecontents['TwitterAPP'][0]['access_secret']
                self.outputfileprefix = filecontents['ConfiguracionLogger'][0]['prefijo_archivo_salida']
                self.keyword_list = filecontents['HasTags']
                logger.info("Searching for Hastags: %s", ' '.join(self.keyword_list))
    
    def InitListening(self):
        logging.info("init tweet listening")
        print ("init tweet listening")
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        start_time = time.time()
        self.twitterStream = Stream(auth, FileStorageListener(start_time, self.outputfileprefix))
        self.twitterStream.filter(track=self.keyword_list, stall_warnings=True, async=True, encoding='utf8')
    
    def StopListening(self):
        logging.info("stop tweet listening")
        print ("stop tweet listening")
        self.twitterStream.disconnect()

class Bot(object):
    def __init__(self):
        self.tweetBot = TweetBot()
        self.networkChecker = NetworkChecker()

    def Disconnect(self, avariable):
        self.tweetBot.StopListening()

    def Connect(self, avariable):
        if self.tweetBot != None:
            self.tweetBot.StopListening()
        time.sleep(15)
        self.tweetBot.InitListening()

    def init(self):
        try:
            self.tweetBot.InitListening()
            self.networkChecker.subscribe('NetworkConnect', self.Connect)
            self.networkChecker.subscribe('NetworkDisconnect', self.Disconnect)
            self.networkChecker.iniciar()
        except KeyboardInterrupt as ex:
            if (self.tweetBot is not None):
                self.tweetBot.StopListening()
        
bot = Bot()
bot.init()