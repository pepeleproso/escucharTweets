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
# import EscucharTweetsMainWindow
import ErrorCredencialesException
import tweepy
import time
import ConfigManager
from FileStorageListener import FileStorageListener

logger = logging.getLogger(__name__)


class TweepyBot(object):
    def __init__(self, escucharTweetsMainWindow):
        self.escucharTweetsWindow = escucharTweetsMainWindow
        self.config = ConfigManager.ConfigManager()
        self.twitterStream = None

    def InitListening(self):
        logger.info("init tweet listening")
        logger.info("Listening Hastags: %s", ' '.join(self.config.keyword_list))
        auth = tweepy.OAuthHandler(self.config.consumer_key, self.config.consumer_secret)
        auth.set_access_token(self.config.access_token, self.config.access_secret)

        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        tw = api.statuses_lookup(760139029291630592,True,False,False)
        print(tw)



        #try:
         #   start_time = time.time()
          #  file_storage = FileStorageListener(self,start_time, filePrefix=self.config.outputfileprefix, tweetsPerOutputFile=self.config.tweetsPerOutputFile)
           # self.twitterStream = tweepy.Stream(auth, file_storage)
           # self.twitterStream.filter(track=self.keyword_list, stall_warnings=True, async=True, encoding='utf8')
        #except ErrorCredencialesException.ErrorCredencialesException as ex:
         #   logger.error(ex)
          #  if self.twitterStream is not None:
           #     self.StopListening()
            #    raise
       # except Exception as ex:
        #    logger.error(ex)
         #   if self.twitterStream is not None:
          #      self.StopListening()

    #def StopListening(self):
     #   logging.info("stop tweet listening")
      #  self.twitterStream.disconnect()

#    def errorAutentificacion(self):
 #       self.escucharTweetsWindow.autenticarCredencial()
