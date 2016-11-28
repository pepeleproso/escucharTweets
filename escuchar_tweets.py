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


class listener(StreamListener):
    def __init__(self, start_time, time_limit=2, prefijoArchivo='tweets'):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []
        self.TweetStorage = JsonFileStorage(prefijoArchivo)

    def on_data(self, data):
        #print(data)
        print 'aca'
        try:
            self.TweetStorage.guardarTweet(data)
            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(5)
            pass

    def on_error(self, status):
        with open('logError.json', 'a') as errfile:
            errfile.write(str(status))
            errfile.write('\n')

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 

class EscucharTweets(object):
    def __init__(self):
        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_secret = None
        self.keyword_list = []
        self.twitterStream = None
        #iniciar el cliente
        self.CargarDatosTwitterApp()

    def CargarDatosTwitterApp(self):
        with open('escucharTweets.json', 'r') as twitterAppfile:
                filecontents = json.load(twitterAppfile)
                self.consumer_key = filecontents['TwitterAPP'][0]['consumer_key']
                self.consumer_secret = filecontents['TwitterAPP'][0]['consumer_secret']
                self.access_token = filecontents['TwitterAPP'][0]['access_token']
                self.access_secret = filecontents['TwitterAPP'][0]['access_secret']
                self.prefijoArchivoSalida = filecontents['ConfiguracionLogger'][0]['prefijo_archivo_salida']
                self.keyword_list = filecontents['HasTags']
    
    def IniciarEscucha(self):
        print 'iniciar escucha'
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        start_time = time.time()
        self.twitterStream = Stream(auth, listener(start_time, self.prefijoArchivoSalida))
        self.twitterStream.filter(track=self.keyword_list, stall_warnings=True, async=True, encoding='utf8')
    
    def DetenerEscucha(self):
        print 'detener escucha'
        self.twitterStream.disconnect()

class Bot(object):
    def __init__(self):
        self.escucharTweets = EscucharTweets()
        self.network = NetworkChecker()

    def Disconnect(self, avariable):
#        print 'desconectado'
        self.escucharTweets.DetenerEscucha()

    def Connect(self, avariable):
#        print 'conectado'
        if self.escucharTweets != None:
            self.escucharTweets.DetenerEscucha()
        time.sleep(15)
        self.escucharTweets.IniciarEscucha()

    def iniciar(self):
        self.escucharTweets.IniciarEscucha()
        self.network.subscribe('NetworkConnect', self.Connect)
        self.network.subscribe('NetworkDisconnect', self.Disconnect)
        self.network.iniciar()

bot = Bot()
bot.iniciar()