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
logger = logging.getLogger(__name__)

import json
import os
import time
import datetime
import io
import math

class JsonFileStorage(object):
    def __init__(self, filePrefix, MaximaCantidadTweets):
        self.TweetsActuales = 0
        self.MaximaCantidadTweets = MaximaCantidadTweets
        self.filePrefix = filePrefix + str(datetime.datetime.now()).split(':')[0]
    
    def getfilename(self):
        FileNumber = int(math.floor(self.TweetsActuales / self.MaximaCantidadTweets))
        logger.debug('FileNumber: ' + str(FileNumber)) 
        filename = self.filePrefix + str(FileNumber) + '.json'
        logger.debug('FileName: ' + str(filename))
        return filename

    def saveTweet(self, tweetjson):
        logger.info("Saving tweet")
        logger.debug(tweetjson)

        try:
            filename = self.getfilename()
            with open(filename, 'a') as outfile:
                json.dump(tweetjson, outfile)
                self.TweetsActuales += 1
        except BaseException as e:
            logger.error(e)
            raise Exception('Error saving tweet',e)