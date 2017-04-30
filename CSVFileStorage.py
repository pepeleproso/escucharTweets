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
import csv
import os
import time
import datetime
import io
import math

class CSVFileStorage(object):
    def __init__(self, filePrefix):
        self.TweetsActuales = 1
        #recuperar ultimo id de archivo
        self.filePrefix = filePrefix 
        self.separator = ';'
        #if not(os.path.isfile(self.getfilename)):
        self.writeColumnsNames()
    
    def getfilename(self):
        filename = self.filePrefix + '.csv'
        logger.debug('FileName: ' + str(filename))
        return filename

    def saveTweet(self, tweetjsonstr):
        logger.info("Saving tweet")
        logger.debug(tweetjsonstr)

        try:
            filename = self.getfilename()
            with open(filename,'a') as csvfile:
                csvWriter = csv.writer(csvfile,quoting=csv.QUOTE_MINIMAL)
                #json.dump(tweetjsonstr,    csvWriter)
                tweetjson = json.loads(tweetjsonstr)
                line = []
                line.append(self.TweetsActuales)
                line.append(str(tweetjson['text']).encode('utf8'))
                line.append(str(tweetjson['retweet_count']).encode('utf8'))
                line.append(str(tweetjson['favorited']).encode('utf8'))
                line.append(str(tweetjson['truncated']).encode('utf8'))
                line.append(str(tweetjson['id_str']).encode('utf8'))
                line.append(str(tweetjson['in_reply_to_screen_name']).encode('utf8'))
                line.append(str(tweetjson['retweeted']).encode('utf8'))
                line.append(str(tweetjson['created_at']).encode('utf8'))
                line.append(str(tweetjson['in_reply_to_status_id_str']).encode('utf8'))
                line.append(str(tweetjson['in_reply_to_user_id_str']).encode('utf8'))
                line.append(str(tweetjson['lang']).encode('utf8'))
                line.append(str(tweetjson['user']['listed_count']).encode('utf8'))
                line.append(str(tweetjson['user']['verified']).encode('utf8'))
                line.append(str(tweetjson['user']['location']).encode('utf8'))
                line.append(str(tweetjson['user']['id_str']).encode('utf8'))
                line.append(str(tweetjson['user']['description']).encode('utf8'))
                line.append(str(tweetjson['user']['geo_enabled']).encode('utf8'))
                line.append(str(tweetjson['user']['created_at']).encode('utf8'))
                line.append(str(tweetjson['user']['statuses_count']).encode('utf8'))
                line.append(str(tweetjson['user']['followers_count']).encode('utf8'))
                line.append(str(tweetjson['user']['favourites_count']).encode('utf8'))
                line.append(str(tweetjson['user']['protected']).encode('utf8'))
                line.append(str(tweetjson['user']['url']).encode('utf8'))
                line.append(str(tweetjson['user']['name']).encode('utf8'))
                line.append(str(tweetjson['user']['time_zone']).encode('utf8'))
                line.append(str(tweetjson['user']['lang']).encode('utf8'))
                line.append(str(tweetjson['user']['utc_offset']).encode('utf8'))
                line.append(str(tweetjson['user']['friends_count']).encode('utf8'))
                line.append(str(tweetjson['user']['screen_name']).encode('utf8'))
                #line.append(str(tweetjson['user']['country_code']).encode('utf8'))
                line.append('')
                #line.append(str(tweetjson['user']['country']).encode('utf8'))
                line.append('')
                #line.append(str(tweetjson['place_type']).encode('utf8'))
                line.append('')
                #line.append(str(tweetjson['full_name']).encode('utf8'))
                line.append('')
                #line.append(str(tweetjson['place_name']).encode('utf8'))
                line.append(str(tweetjson['place']).encode('utf8'))
                #line.append(str(tweetjson['place_lat']).encode('utf8'))
                #line.append(str(tweetjson['place_lon']).encode('utf8'))
                line.append(str(tweetjson['coordinates']).encode('utf8'))
                
                try:
                    line.append(str(tweetjson['retweeted_status']['entities']['media'][0]['expanded_url']).encode('utf8'))
                except Exception as ex:
                    line.append('')

                try:
                    line.append(str(tweetjson['retweeted_status']['user']['url']).encode('utf8'))
                except Exception as ex:
                    line.append('')
                
                try:
                    line.append(str(tweetjson['retweeted_status']['created_at']).encode('utf8'))
                except Exception as ex:
                     line.append('')

                csvWriter.writerow(line)
                self.TweetsActuales += 1
                #el archivo csv se cierra solo
        except BaseException as e:
            logger.error(e)
            raise Exception('Error saving tweet',e)

    def writeColumnsNames(self):
        try:
            filename = self.getfilename()
            with open(filename,'a') as csvfile:
                csvWriter = csv.writer(csvfile,quoting=csv.QUOTE_MINIMAL)
                #json.dump(tweetjsonstr,    csvWriter)
                line = []
                line.append('id')
                line.append('text') 
                line.append('retweet_count') 
                line.append('favorited') 
                line.append('truncated') 
                line.append('id_str') 
                line.append('in_reply_to_screen_name') 
                line.append('retweeted') 
                line.append('created_at') 
                line.append('in_reply_to_status_id_str') 
                line.append('in_reply_to_user_id_str') 
                line.append('lang') 
                line.append('user_listed_count') 
                line.append('user_verified') 
                line.append('user_location') 
                line.append('user_id_str') 
                line.append('user_description') 
                line.append('user_geo_enabled') 
                line.append('user_created_at') 
                line.append('user_statuses_count') 
                line.append('user_followers_count') 
                line.append('user_favourites_count') 
                line.append('user_protected') 
                line.append('user_url') 
                line.append('user_name') 
                line.append('user_time_zone') 
                line.append('user_lang') 
                line.append('user_utc_offset') 
                line.append('user_friends_count') 
                line.append('user_screen_name') 
                #line. append('user']['country_code') 
                line.append('user_country_code')
                #line.append(unicode(tweetjson['user']['country']).encode('utf8'))
                line.append('user_country')
                #line.append(unicode(tweetjson['place_type']).encode('utf8'))
                line.append('place_type')
                #line.append(unicode(tweetjson['full_name']).encode('utf8'))
                line.append('full_name')
                #line.append(unicode(tweetjson['place_name']).encode('utf8'))
                line.append('place')
                #line.append(unicode(tweetjson['place_lat']).encode('utf8'))
                #line.append(unicode(tweetjson['place_lon']).encode('utf8'))
                line.append('coordinates') 
                line.append('retweeted_status_expanded_url')
                line.append('retweeted_status_user_url')
                line.append('retweeted_status_created_at')
                csvWriter.writerow(line)
               
                #el archivo csv se cierra solo
        except BaseException as e:
            logger.error(e)
            raise Exception('Error saving tweet',e)