from abc import ABC, abstractmethod


class BaseValidator(ABC):
    @abstractmethod
    def is_valid(self, args) -> bool:
        pass

    @abstractmethod
    def error(self) -> dict:
        pass


class BaseKeyValidator(BaseValidator):
    def __init__(self, key: str) -> None:
        self.key = key
