import redis
from WatchDogs_MongoWrapper import MongoWrapper

class RedisWrapper():
    def __init__(self):
        self.redicclient = redis.Redis(host='35.236.16.13', port=6379, db=0)

    def redis_update_json(self, key, json_string):
        pass

    def redis_get_json(self, key):
        pass

    def redis_flush_all(self):
        """
        Danger. This flushes the whole DB. Careful
        :return:
        """
        self.redicclient.flushdb()

