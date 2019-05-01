from redis_wrapper import RedisWrapper
import unittest
class RedisWrapperTests(unittest.TestCase):
    def test_push(self):
        redis_connection = RedisWrapper()
        api_string = 'get_tweets_with_lat_long/'
        key = 'Facebook'
        redis_connection.redis_update_json(api_string, key)

    def test_push2(self):
        redis_connection = RedisWrapper()
        api_string = 'get_polarity_tweets_of_stock/'
        key = 'Facebook'
        redis_connection.redis_update_json(api_string, key)

    def test_pull(self):
        redis_connection = RedisWrapper()
        api_string = 'get_tweets_with_lat_long/'
        key = 'Facebook'
        json_string = redis_connection.redis_get_json(api_string, key)
        decoded_string = json_string.decode("utf-8")
        print(decoded_string)

    def test_pull2(self):
        redis_connection = RedisWrapper()
        api_string = 'get_polarity_tweets_of_stock/'
        key = 'Facebook'
        json_string = redis_connection.redis_get_json(api_string, key)
        decoded_string = json_string.decode("utf-8")
        print(decoded_string)


if __name__ == '__main__':
    unittest.main()