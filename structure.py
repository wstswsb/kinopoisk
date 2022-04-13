from pathlib import Path

from dependencies import Dependencies
from repositories import FilmRepository
from translators import FilmTranslator
from services import (
    ValidationService,
    FilmService,
    TypesConvertingService,
)
from validators import PresenceValidator, TypeValidator
from extractors import (
    FilmAttributeExtractor,
    FilmTitleExtractor,
    IntAttributeExtractor,
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
year_extractor = IntAttributeExtractor(
    "Год производства",
    types_converting_service,
)

# Validators
create_film_presence_validators = [
    PresenceValidator("title"),
    PresenceValidator("year"),
    PresenceValidator("country"),
    PresenceValidator("genre"),
    PresenceValidator("slogan"),
    PresenceValidator("directors"),
    PresenceValidator("screenwriters"),
    PresenceValidator("producers"),
    PresenceValidator("operators"),
    PresenceValidator("composers"),
    PresenceValidator("artists"),
    PresenceValidator("editors"),
    PresenceValidator("budget"),
    PresenceValidator("usa_fees"),
    PresenceValidator("world_fees"),
    PresenceValidator("premiere_in_russia"),
    PresenceValidator("premiere_in_world"),
    PresenceValidator("dvd_release"),
    PresenceValidator("age_restrictions"),
    PresenceValidator("MPAA_rating"),
    PresenceValidator("duration"),
]
create_film_type_validators = [
    TypeValidator("title", str),
    TypeValidator("year", int),
    TypeValidator("country", str),
    TypeValidator("genre", str),
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
    TypeValidator("world_fees", str),
    TypeValidator("premiere_in_russia", str),
    TypeValidator("premiere_in_world", str),
    TypeValidator("dvd_release", str),
    TypeValidator("age_restrictions", str),
    TypeValidator("MPAA_rating", str),
    TypeValidator("duration", str),

]
# Validation Services
create_film_validation_service = ValidationService(
    [
        *create_film_presence_validators,
        *create_film_type_validators,
    ]
)

# Services
film_service = FilmService(
    film_repository,
    create_film_validation_service,
)
