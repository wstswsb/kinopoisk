from typing import Sized

from .base_validator import BaseKeyValidator


class PresenceValidator(BaseKeyValidator):
    def is_valid(self, args: dict) -> bool:
        value = args.get(self.key, '')
        if isinstance(value, Sized):  # Tested with tuple, list, dict, str
            return len(value) > 0
        return value is not None

    def error(self) -> dict:
        return {
            'message': 'Has to be present',
            'key': 'error_presence'
        }
