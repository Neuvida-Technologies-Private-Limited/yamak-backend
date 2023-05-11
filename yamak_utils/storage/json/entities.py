from abc import ABC
from abc import abstractmethod


class JSONStorage(ABC):

    @abstractmethod
    def save(self, file_key: str, json_data) -> str:
        pass

    @abstractmethod
    def delete(self, file_key: str) -> str:
        pass

    @abstractmethod
    def get_short_time_url(
        self,
        file_key: str,
        expires_in: int,
        inline=False,
        content_type=None,
    ) -> str:
        pass