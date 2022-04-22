from bson import ObjectId
from typing import Optional, Any

from .staff import Staff


class Film:
    def __init__(self):
        self.id: Optional[ObjectId] = None
        self.title: Optional[str] = None
        self.year: Optional[int] = None
        self.country: Optional[str] = None
        self.genre: Optional[str] = None
        self.slogan: Optional[str] = None
        self.staff: Optional[Staff] = None
        self.budget: Optional[str] = None
        self.usa_fees: Optional[str] = None
        self.rus_fees: Optional[str] = None
        self.world_fees: Optional[str] = None
        self.premiere_in_russia: Optional[str] = None
        self.premiere_in_world: Optional[str] = None
        self.dvd_release: Optional[str] = None
        self.age_restrictions: Optional[str] = None
        self.rating_mpaa: Optional[str] = None
        self.duration: Optional[str] = None

    @staticmethod
    def from_attrs(attrs: dict[str, Any]) -> "Film":
        film = Film()
        film.title = attrs.get("title")
        film.year = attrs.get("year")
        film.country = attrs.get("country")
        film.genre = attrs.get("genre")
        film.slogan = attrs.get("slogan")
        film.staff = Staff.from_attrs(attrs.get("staff", {}))
        film.budget = attrs.get("budget")
        film.usa_fees = attrs.get("usa_fees")
        film.rus_fees = attrs.get("rus_fees")
        film.world_fees = attrs.get("world_fees")
        film.premiere_in_russia = attrs.get("premiere_in_russia")
        film.premiere_in_world = attrs.get("premiere_in_world")
        film.dvd_release = attrs.get("dvd_release")
        film.age_restrictions = attrs.get("age_restrictions")
        film.rating_mpaa = attrs.get("rating_mpaa")
        film.duration = attrs.get("duration")
        return film
