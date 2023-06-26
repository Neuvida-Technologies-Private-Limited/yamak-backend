from abc import ABC
from abc import abstractmethod


class KeyValueCacheStorage(ABC):

    @abstractmethod
    def contains(self, key):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def add(self, key, value, time_to_live):
        pass

    @abstractmethod
    def remove(self, key):
        pass