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