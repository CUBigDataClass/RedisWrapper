import redis
from WatchDogs_MongoWrapper import MongoWrapper

class RedisWrapper():
    def __init__(self):
        self.redicclient = redis.StrictRedis(host='35.236.16.13', port=6379, db=0, decode_responses=True)
        self.mng = MongoWrapper()

    def redis_update_json(self, api_string, key):
        if api_string == 'get_tweets_with_lat_long/':
            try:
                json_data = self.mng.get_tweets_with_lat_long(key)
                self.redicclient.execute_command('JSON.SET', api_string+key, '.', json_data)
            except:
                print('Something is terribly wrong')
                raise
        elif api_string == 'get_polarity_tweets_of_stock/':
            try:
                json_data = self.mng.get_polarity_tweets_of_stock(key)
                self.redicclient.execute_command('JSON.SET', api_string + key, '.', json_data)
            except:
                print('Something is terribly wrong')
                raise

    def redis_insert_tweet(self, api_string, key, tweet):
        try:
            lat_long_list = tweet['Geo']['coordinates']
        except:
            lat_long_list = ['None', 'None']
        sentiment_polarity = tweet["Sentiment_Polarity"]
        full_text = tweet["Text"]
        root_json_path = """{"Latitude": {lat}, "Longitude": {long},
             "Sentiment_Polarity": {sentiment_polarity}, "Tweet_Text": {full_text}
             }""".format(lat=lat_long_list[0], long=lat_long_list[1], sentiment_polarity=sentiment_polarity,
                         full_text = full_text)

        if api_string == 'get_tweets_with_lat_long/':
            try:
                self.redicclient.execute_command('JSON.ARRAPPEND', api_string+key, '.', root_json_path)
            except:
                print('Something is terribly wrong')
                raise
        elif api_string == 'get_polarity_tweets_of_stock/':
            try:
                if sentiment_polarity == -1:
                    root_path = '.Negative_Tweets'
                elif sentiment_polarity == 0:
                    root_path = '.Neutral_Tweets'
                elif sentiment_polarity == 1:
                    root_path = '.Positive_Tweets'
                self.redicclient.execute_command('JSON.ARRAPPEND', api_string + key, root_path, root_json_path)
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

