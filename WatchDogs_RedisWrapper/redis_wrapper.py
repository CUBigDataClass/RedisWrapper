import redis
from WatchDogs_MongoWrapper import MongoWrapper
from bson.json_util import dumps
import json

class RedisWrapper():
    def __init__(self):
        self.redicclient = redis.StrictRedis(host='35.236.16.13', port=6379, db=0)
        self.mng = MongoWrapper()

    def redis_update_json(self, api_string, key):
        if api_string == 'get_tweets_with_lat_long/':
            data_frame = self.mng.get_tweets_with_lat_long(key)
            json_data = data_frame.to_json()
            self.redicclient.execute_command('JSON.SET', api_string+key, '.', json_data)
        elif api_string == 'get_polarity_tweets_of_stock/':
            try:
                neg, neu, pos = self.mng.get_polarity_tweets_of_stock(key)
                neg_tweets = dumps(neg)
                neu_tweets = dumps(neu)
                pos_tweets = dumps(pos)
                data = {"neg_tweets": neg_tweets, "neu_tweets": neu_tweets, "pos_tweets": pos_tweets}
                json_data = json.dumps(data)
                self.redicclient.execute_command('JSON.SET', api_string + key, '.', json_data)
            except:
                print('Something is terribly wrong')
                raise



    def redis_get_json(self, api_string, key):
        return self.redicclient.execute_command('JSON.GET', api_string+key)

    def redis_flush_all(self):
        """
        Danger. This flushes the whole DB. Careful
        :return:
        """
        self.redicclient.flushdb()

