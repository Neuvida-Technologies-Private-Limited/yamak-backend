from redis.client import StrictRedis

from .entities import KeyValueCacheStorage


class RedisKeyValueCacheStorage(KeyValueCacheStorage):
    """Redis cache implementation"""

    def __init__(self, host, port):

        self.__client = StrictRedis(
            host=host,
            port=port,
            charset='utf-8',
            decode_responses=True,
        )

    def contains(self, key):
        return self.__client.exists(key)

    def get(self, key):

        if not self.contains(key=key):
            return None

        return self.__client.get(key)

    def add(self, key, value, time_to_live):
        """
        time_to_live is in seconds
        Cache key gets expired after time_to_live
        """

        self.__client.set(
            name=key,
            value=value,
            ex=time_to_live,
        )

    def remove(self, key):
        self.__client.delete(key)
