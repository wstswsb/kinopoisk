from wrappers import (
    EnvWrapper,
    PymongoWrapper,
)


class Dependencies:
    def environment_wrapper(self):
        return EnvWrapper()

    def pymongo_wrapper(self):
        return PymongoWrapper(self.environment_wrapper())

    def mongo(self):
        return self.pymongo_wrapper().get_client()
