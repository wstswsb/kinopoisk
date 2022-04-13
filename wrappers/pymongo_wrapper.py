import pymongo


class PymongoWrapper:
    def __init__(self, env_wrapper) -> None:
        self.scheme = env_wrapper.get_var('MONGO_SCHEME')
        self.username = env_wrapper.get_var('MONGO_USERNAME')
        self.password = env_wrapper.get_var('MONGO_PASSWORD')
        self.host = env_wrapper.get_var('MONGO_HOST')
        self.port = env_wrapper.get_var('MONGO_PORT')
        self.name = env_wrapper.get_var('MONGO_NAME')

    def get_client(self):
        credentials = ''
        if self.username:
            credentials = f'{self.username}:{self.password}@'
        url = f'{self.scheme}://{credentials}{self.host}:{self.port}'
        return pymongo.MongoClient(url)

    def get_collection(self, client, collection_name: str):
        return client[self.name][collection_name]
