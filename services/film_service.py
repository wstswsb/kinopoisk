from models import Film
from repositories import FilmRepository
from .validation_service import ValidationService
from .film_parsing_service import FilmParsingService


class FilmService:
    def __init__(
            self,
            repository: FilmRepository,
            film_parsing_service: FilmParsingService,
            create_validation_service: ValidationService):
        self.repository = repository
        self.parsing_service = film_parsing_service
        self.create_validation_service = create_validation_service

    def create(self, attrs: dict) -> Film:
        self.create_validation_service.validate(attrs)
        film = Film.from_attrs(attrs)
        film.id = self.repository.create(film)
        return film

    def create_by_url(self, url: str):
        attrs = self.parsing_service.parse_by_url(url)
        model = self.create(attrs)
        return model
