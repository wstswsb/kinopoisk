from models import Film
from repositories import FilmRepository
from loggers import app_logger


class FilmService:
    def __init__(
            self,
            repository: FilmRepository):
        self.repository = repository

    def create(self, attrs: dict) -> Film:
        app_logger.debug(f"Creating film with title: {attrs.get('title')}")
        film = Film.from_attrs(attrs)
        film.id = self.repository.create(film)
        return film
