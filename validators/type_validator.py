from .base_validator import BaseKeyValidator


class TypeValidator(BaseKeyValidator):
    def __init__(self, key: str, arg_type: type) -> None:
        super().__init__(key)
        self.type = arg_type

    def is_valid(self, args: dict) -> bool:
        value = args.get(self.key)
        return isinstance(value, self.type)

    def error(self) -> dict:
        return {
            'message': f'{self.key} must be {self.type.__name__}',
            'key': 'error_invalid_type_of_argument'
        }
