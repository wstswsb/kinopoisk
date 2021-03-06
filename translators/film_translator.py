from models import Film


class FilmTranslator:
    def __init__(self, staff_translator):
        self.staff_translator = staff_translator

    def to_document(self, model: Film) -> dict:
        return {
            "_id": model.id,
            "title": model.title,
            "year": model.year,
            "country": model.country,
            "genre": model.genre,
            "slogan": model.slogan,
            "staff": self.staff_translator.to_document(model.staff),
            "budget": model.budget,
            "usa_fees": model.usa_fees,
            "rus_fees": model.rus_fees,
            "world_fees": model.world_fees,
            "premiere_in_russia": model.premiere_in_russia,
            "premiere_in_world": model.premiere_in_world,
            "dvd_release": model.dvd_release,
            "age_restrictions": model.age_restrictions,
            "rating_mpaa": model.rating_mpaa,
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

        film.staff = self.staff_translator.from_document(
            document.get("staff", {})
        )

        film.budget = document.get("budget")
        film.usa_fees = document.get("usa_fees")
        film.rus_fees = document.get("rus_fees")
        film.world_fees = document.get("world_fees")
        film.premiere_in_russia = document.get("premiere_in_russia")
        film.premiere_in_world = document.get("premiere_in_world")
        film.dvd_release = document.get("dvd_release")
        film.age_restrictions = document.get("age_restrictions")
        film.rating_mpaa = document.get("rating_mpaa")
        film.duration = document.get("duration")
        return film
