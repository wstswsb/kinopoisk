from click import echo

from models import Film
from repositories import FilmRepository


class FilmService:
    def __init__(
            self,
            repository: FilmRepository):
        self.repository = repository

    def create(self, attrs: dict) -> Film:
        echo(f"film {attrs = }")
        film = Film.from_attrs(attrs)
        film.id = self.repository.create(film)
        return film
