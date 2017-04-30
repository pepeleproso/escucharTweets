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
import EscucharTweetsMainWindow
logger = logging.getLogger(__name__)
import argparse
import json
import os
import io
import time

from NetworkManager import NetworkChecker
from TweepyBot import TweepyBot

class Bot(object):
    def __init__(self,escucharTweetsMainWindow):
        
        #self.escucharTweetsWindows = escucharTweetsMainWindow
        self.tweetBot = TweepyBot(escucharTweetsMainWindow)
        self.networkChecker = NetworkChecker()

    def StopListening(self, available):
        print 'stop'
        self.tweetBot.StopListening()

    def InitListening(self, avariable):
        if self.tweetBot != None:
            self.tweetBot.StopListening()
        time.sleep(15)
        self.tweetBot.InitListening()

    def init(self):
        try:
            self.tweetBot.InitListening()
            self.networkChecker.subscribe('NetworkConnect', self.InitListening)
            self.networkChecker.subscribe('NetworkDisconnect', self.StopListening)
            self.networkChecker.init()
        except KeyboardInterrupt as ex:
            if (self.tweetBot is not None):
                self.tweetBot.StopListening()