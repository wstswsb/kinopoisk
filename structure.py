from pathlib import Path

from dependencies import Dependencies
from repositories import FilmRepository
from translators import FilmTranslator
from services import (
    ValidationService,
    FilmService,
    FilmParsingService,
)
from services.tools import TypesConvertingService
from wrappers import ChromiumWrapper
from validators import TypeValidator
from extractors import (
    FilmTitleExtractor,
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

# Validation Services
create_film_validation_service = ValidationService(
    [
        TypeValidator("title", str),
        TypeValidator("year", int),
        TypeValidator("country", str),
        TypeValidator("genre", list),
        TypeValidator("slogan", str),
        TypeValidator("directors", list),
        TypeValidator("screenwriters", list),
        TypeValidator("producers", list),
        TypeValidator("operators", list),
        TypeValidator("composers", list),
        TypeValidator("artists", list),
        TypeValidator("editors", list),
        TypeValidator("budget", str),
        TypeValidator("usa_fees", str),
        TypeValidator("rus_fees", str),
        TypeValidator("world_fees", str),
        TypeValidator("premiere_in_russia", str),
        TypeValidator("premiere_in_world", str),
        TypeValidator("dvd_release", str),
        TypeValidator("age_restrictions", str),
        TypeValidator("rating_mpaa", str),
        TypeValidator("duration", str),
    ]
)

# Wrappers
chromium_wrapper = ChromiumWrapper()

# Services
film_parsing_service = FilmParsingService(
    chromium_wrapper,
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

film_service = FilmService(
    film_repository,
    film_parsing_service,
    create_film_validation_service,
)
