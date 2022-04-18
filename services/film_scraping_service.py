from .film_parsing_service import FilmParsingService
from .film_service import FilmService


class FilmScrapingService:
    def __init__(
            self,
            parsing_service: FilmParsingService,
            film_service: FilmService):
        self.parsing_service = parsing_service
        self.film_service = film_service

    def scrape_top_250(self) -> None:
        for film_attrs in self.parsing_service.parse_top_250():
            self.film_service.create(film_attrs)
