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
    def __init__(self, consumerKey, consumerSecret, accessToken, accessSecret):
        self.consumer_key = consumerKey
        self.consumer_secret = consumerSecret
        self.access_token = accessToken
        self.access_secret = accessSecret

class FileStorageConfig(object):
    def __init__(self,outputfile_prefix,tweets_per_outputfile):
        self.outputfile_prefix = outputfile_prefix
        self.tweets_per_outputfile = tweets_per_outputfile
    

class configJsonSaver(object):
    def __init__(self,consumer_key, consumer_secret, access_token, access_secret,listaHashtags,outputfile_prefix,tweets_per_outputfile):
        self.HashTags = listaHashtags
        self.TwitterAPP = [TwitterAPP(consumer_key, consumer_secret, access_token, access_secret)]
        self.FileStorageConfig = [FileStorageConfig(outputfile_prefix,tweets_per_outputfile)]
    
    def save(self):

        try:
            filename = "escucharTweets.json"
            with open(filename, 'w') as outfile:
                json.dump(self, outfile, cls=ObjectEncoder, indent=2, sort_keys=True)
        except BaseException as e:
            logger.error(e)
            raise Exception('Error saving configuration file',e)
