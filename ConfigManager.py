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
import json

logger = logging.getLogger(__name__)


class ConfigManager(object):
    def __init__(self):
        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_secret = None
        self.keyword_list = []
        self.tweets_per_output_file = 1
        self.loadConfigData()

    def loadConfigData(self):
        logger.info("Loading Config Options")
        with open('escucharTweets.json', 'r') as config_file:
            filecontents = json.load(config_file)
            self.consumer_key = filecontents['TwitterAPP'][0]['consumer_key']
            self.consumer_secret = filecontents['TwitterAPP'][0]['consumer_secret']
            self.access_token = filecontents['TwitterAPP'][0]['access_token']
            self.access_secret = filecontents['TwitterAPP'][0]['access_secret']
            self.outputfileprefix = filecontents['FileStorageConfig'][0]['outputfile_prefix']
            self.tweets_per_output_file = filecontents['FileStorageConfig'][0]['tweets_per_outputfile']
            self.keyword_list = filecontents['HashTags']
            logger.info("Searching for Hastags: %s", ' '.join(self.keyword_list))
