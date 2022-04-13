from models import Film
from repositories import FilmRepository
from .validation_service import ValidationService


class FilmService:
    def __init__(
            self,
            repository: FilmRepository,
            create_validation_service: ValidationService):
        self.repository = repository
        self.create_validation_service = create_validation_service

    def create(self, attrs: dict) -> Film:
        self.create_validation_service.validate(attrs)
        film = Film.from_attrs(attrs)
        film.id = self.repository.create(film)
        return film
