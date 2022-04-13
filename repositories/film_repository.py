from pymongo.collection import Collection

from .base_repository import BaseRepository


class FilmRepository(BaseRepository):
    def __init__(
            self,
            collection: Collection,
            film_translator,
            indexes):
        super().__init__(collection, film_translator, [], indexes)
