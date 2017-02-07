# -*- coding: utf-8 -*-

#    This file is part of escucharTweets.
#
#    escucharTweets is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    escucharTweets is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with escucharTweets; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging
logger = logging.getLogger(__name__)

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
import json
#import os
import time
import io
import ssl
import socket
import datetime

from FileStorageListener import FileStorageListener

class TweepyBot(object):
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
                self.outputfileprefix = filecontents['FileStorageConfig'][0]['outputfile_prefix']
                self.tweetsPerOutputFile = filecontents['FileStorageConfig'][0]['tweets_per_outputfile']
                self.keyword_list = filecontents['HashTags']
                logger.info("Searching for Hastags: %s", ' '.join(self.keyword_list))
    
    def InitListening(self):
        logging.info("init tweet listening")
        logger.info ("Listening Hastags: %s", ' '.join(self.keyword_list))
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        try:
            start_time = time.time()
            self.twitterStream = Stream(auth, FileStorageListener(start_time, filePrefix=self.outputfileprefix, tweetsPerOutputFile=self.tweetsPerOutputFile))
            self.twitterStream.filter(track=self.keyword_list, stall_warnings=True, async=True, encoding='utf8')
        except Exception as ex:
            logger.error(ex)
            if (self.twitterStream is not None):
                self.StopListening()

    def StopListening(self):
        logging.info("stop tweet listening")
        self.twitterStream.disconnect()
