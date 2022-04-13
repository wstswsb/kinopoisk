import os
from exceptions import VariableNotFoundException


class EnvWrapper:
    def get_var(self, key: str) -> str:
        try:
            return os.environ[key]
        except KeyError:
            raise VariableNotFoundException(f'{key} variable not found')

    def read_file(self, file_path: str) -> str:
        with open(file_path) as file:
            content = file.read()
        return content
