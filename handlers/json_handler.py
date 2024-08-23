from abc import ABC, abstractmethod
from typing import Any


class JSONHandler(ABC):

    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def _load_data(self) -> Any:
        pass

    @abstractmethod
    def _save_data(self, data: Any):
        pass

    @abstractmethod
    def _delete_data_by_id(self, id: Any):
        pass
