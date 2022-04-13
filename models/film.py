from bson import ObjectId
from typing import Optional, Any


class Film:
    def __init__(self):
        self.id: Optional[ObjectId] = None
        self.title: Optional[str] = None
        self.year: Optional[int] = None
        self.country: Optional[str] = None
        self.genre: Optional[str] = None
        self.slogan: Optional[str] = None
        self.directors: Optional[list[str]] = None
        self.screenwriters: Optional[list[str]] = None
        self.producers: Optional[list[str]] = None
        self.operators: Optional[list[str]] = None
        self.composers: Optional[list[str]] = None
        self.artists: Optional[list[str]] = None
        self.editors: Optional[list[str]] = None
        self.budget: Optional[str] = None
        self.usa_fees: Optional[str] = None
        self.world_fees: Optional[str] = None
        self.premiere_in_russia: Optional[str] = None
        self.premiere_in_world: Optional[str] = None
        self.dvd_release: Optional[str] = None
        self.age_restrictions: Optional[str] = None
        self.MPAA_rating: Optional[str] = None
        self.duration: Optional[str] = None

    @staticmethod
    def from_attrs(attrs: dict[str, Any]) -> "Film":
        film = Film()
        film.title = attrs.get("title")
        film.year = attrs.get("year")
        film.country = attrs.get("country")
        film.genre = attrs.get("genre")
        film.slogan = attrs.get("slogan")
        film.directors = attrs.get("directors")
        film.screenwriters = attrs.get("screenwriters")
        film.producers = attrs.get("producers")
        film.operators = attrs.get("operators")
        film.composers = attrs.get("composers")
        film.artists = attrs.get("artists")
        film.editors = attrs.get("editors")
        film.budget = attrs.get("budget")
        film.usa_fees = attrs.get("usa_fees")
        film.world_fees = attrs.get("world_fees")
        film.premiere_in_russia = attrs.get("premiere_in_russia")
        film.premiere_in_world = attrs.get("premiere_in_world")
        film.dvd_release = attrs.get("dvd_release")
        film.age_restrictions = attrs.get("age_restrictions")
        film.MPAA_rating = attrs.get("MPAA_rating")
        film.duration = attrs.get("duration")
        return film
