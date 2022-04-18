from pathlib import Path

from dependencies import Dependencies
from repositories import FilmRepository
from translators import FilmTranslator
from services import (
    FilmService,
    FilmParsingService,
    FilmScrapingService,
)
from services.tools import TypesConvertingService
from wrappers import ChromiumWrapper
from extractors import (
    FilmTitleExtractor,
    RelativeLinksExtractor,
    AttributeExtractor,
    IntAttributeExtractor,
    ListAttributeExtractor,
    FeesExtractor,
    WorldFeesExtractor,
    PremiereExtractor,
    RatingExtractor,
)

root_dir_path = Path(__file__).parent
resources_path = root_dir_path / "resources"

deps = Dependencies()

# Translators
film_translator = FilmTranslator()

# Repositories
film_repository = FilmRepository(
    collection=deps.pymongo_wrapper().get_collection(
        client=deps.mongo(),
        collection_name="films",
    ),
    film_translator=film_translator,
    indexes=[],
)
# Services Without Entities
types_converting_service = TypesConvertingService()

# Extractors
title_extractor = FilmTitleExtractor()
relative_links_extractor = RelativeLinksExtractor()
year_extractor = IntAttributeExtractor(
    "Год производства",
    types_converting_service,
    key_alias="year",
)
country_extractor = AttributeExtractor("Страна", "country")
genre_extractor = ListAttributeExtractor("Жанр", "genre")
slogan_extractor = AttributeExtractor("Слоган", "slogan")
directors_extractor = ListAttributeExtractor("Режиссер", "directors")
screenwriters_extractor = ListAttributeExtractor("Сценарий", "screenwriters")
producers_extractor = ListAttributeExtractor("Продюсер", "producers")
operators_extractor = ListAttributeExtractor("Оператор", "operators")
composers_extractor = ListAttributeExtractor("Композитор", "composers")
artists_extractor = ListAttributeExtractor("Художник", "artists")
editors_extractor = ListAttributeExtractor("Монтаж", "editors")
budget_extractor = FeesExtractor("Бюджет", "budget")
usa_fees_extractor = FeesExtractor("Сборы в США", "usa_fees")
rus_fees_extractor = FeesExtractor("Сборы в России", "rus_fees")
world_fees_extractor = WorldFeesExtractor("Сборы в мире", "world_fees")
premiere_in_russia_extractor = PremiereExtractor(
    "Премьера в Росcии",
    "premiere_in_russia",
)
premiere_in_world_extractor = PremiereExtractor(
    "Премьера в мире",
    "premiere_in_world",
)
dvd_release_extractor = AttributeExtractor("Релиз на DVD", "dvd_release")
age_restrictions_extractor = AttributeExtractor("Возраст", "age_restrictions")
rating_mpaa_extractor = RatingExtractor("Рейтинг MPAA", "rating_mpaa")
duration_extractor = AttributeExtractor("Время", "duration")


# Wrappers
chromium_wrapper = ChromiumWrapper()

# Services
film_parsing_service = FilmParsingService(
    chromium_wrapper,
    relative_links_extractor,
    title_extractor,
    attributes_extractors=[
        year_extractor,
        country_extractor,
        genre_extractor,
        slogan_extractor,
        directors_extractor,
        screenwriters_extractor,
        producers_extractor,
        operators_extractor,
        composers_extractor,
        artists_extractor,
        editors_extractor,
        budget_extractor,
        usa_fees_extractor,
        rus_fees_extractor,
        world_fees_extractor,
        premiere_in_russia_extractor,
        premiere_in_world_extractor,
        dvd_release_extractor,
        age_restrictions_extractor,
        rating_mpaa_extractor,
        duration_extractor,
    ]
)

film_service = FilmService(film_repository)

film_scraping_service = FilmScrapingService(
    film_parsing_service,
    film_service,
)
