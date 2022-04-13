from models import Film


class FilmTranslator:
    def to_document(self, model: Film) -> dict:
        return {
            "_id": model.id,
            "title": model.title,
            "year": model.year,
            "country": model.country,
            "genre": model.genre,
            "slogan": model.slogan,
            "directors": model.directors,
            "screenwriters": model.screenwriters,
            "producers": model.producers,
            "operators": model.operators,
            "composers": model.composers,
            "artists": model.artists,
            "editors": model.editors,
            "budget": model.budget,
            "usa_fees": model.usa_fees,
            "world_fees": model.world_fees,
            "premiere_in_russia": model.premiere_in_russia,
            "premiere_in_world": model.premiere_in_world,
            "dvd_release": model.dvd_release,
            "age_restrictions": model.age_restrictions,
            "MPAA_rating": model.MPAA_rating,
            "duration": model.duration,
        }

    def from_document(self, document: dict) -> Film:
        film = Film()
        film.id = document.get("_id")
        film.title = document.get("title")
        film.year = document.get("year")
        film.country = document.get("country")
        film.genre = document.get("genre")
        film.slogan = document.get("slogan")
        film.directors = document.get("directors")
        film.screenwriters = document.get("screenwriters")
        film.producers = document.get("producers")
        film.operators = document.get("operators")
        film.composers = document.get("composers")
        film.artists = document.get("artists")
        film.editors = document.get("editors")
        film.budget = document.get("budget")
        film.usa_fees = document.get("usa_fees")
        film.world_fees = document.get("world_fees")
        film.premiere_in_russia = document.get("premiere_in_russia")
        film.premiere_in_world = document.get("premiere_in_world")
        film.dvd_release = document.get("dvd_release")
        film.age_restrictions = document.get("age_restrictions")
        film.MPAA_rating = document.get("MPAA_rating")
        film.duration = document.get("duration")
        return film
