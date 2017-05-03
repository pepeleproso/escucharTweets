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
import TweepyBot
import time
logger = logging.getLogger(__name__)

try:
    import NetworkManager.NetworkManagerDbus as NetworkChecker
except Exception as e:
    logger.error(e)

try:
    import NetworkManager.NetworkManagerHelperWin32 as NetworkChecker
except Exception as e:
    logger.error(e)


class Bot(object):
    def __init__(self, escucharTweetsMainWindow):
        self.tweetBot = TweepyBot.TweepyBot(escucharTweetsMainWindow)
        self.networkChecker = NetworkChecker.NetworkChecker()

    def StopListening(self, available):
        print ('stop')
        self.tweetBot.StopListening()

    def InitListening(self, avariable):
        if self.tweetBot is not None:
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
            if self.tweetBot is not None:
                self.tweetBot.StopListening()
