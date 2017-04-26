import json
import inspect

class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj




class TwitterAPP(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

class FileStorageConfig(object):
    def __init__(self,outputfile_prefix,tweets_per_outputfile):
        self.outputfile_prefix = outputfile_prefix
        self.tweets_per_outputfile = tweets_per_outputfile
    

class configJsonSaver(object):
    def __init__(self,consumer_key, consumer_secret, access_token, access_secret,hashtags,outputfile_prefix,tweets_per_outputfile):
        #self.hashtags = hashtags
        self.TwitterAPP         = [TwitterAPP(consumer_key, consumer_secret, access_token, access_secret)]
        #self.FileStorageConfig = [FileStorageConfig(outputfile_prefix,tweets_per_outputfile)]
    
    #def save(self):
    #    print json.dumps(self, cls=ObjectEncoder, indent=2, sort_keys=True)
        #falta que guarde
