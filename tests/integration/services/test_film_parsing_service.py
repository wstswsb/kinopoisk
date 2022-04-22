from pathlib import Path
from structure import film_parsing_service, resources_path


class TestFilmParsingService:
    page_source = Path(
        resources_path,
        "page_sources",
        "sin_city.html",
    ).read_text()

    def setup(self):
        self.service = film_parsing_service

    def test_parse(self):
        result = self.service.parse(self.page_source)

        assert result["year"] == 2005
        assert result["country"] == "США"
        assert result["genre"] == [
            "боевик", "триллер",
            "криминал", "детектив",
        ]
        assert result["slogan"] == "«Deadly little Miho»"
        assert result["directors"] == [
            "Фрэнк Миллер",
            "Квентин Тарантино",
            "Роберт Родригес",
        ]
        assert result["screenwriters"] == ["Фрэнк Миллер", "Роберт Родригес"]
        assert result["producers"] == [
            "Элизабет Авеллан",
            "Билл Скотт",
            "Боб Вайнштейн",
        ]
        assert result["operators"] == ["Роберт Родригес"]
        assert result["composers"] == [
            "Джон Дебни",
            "Грэм Ревелл",
            "Роберт Родригес",
        ]
        assert result["artists"] == [
            "Стив Джойнер",
            "Жанетт Скотт",
            "Дэвид Хэк",
        ]
        assert result["editors"] == ["Роберт Родригес"]
        assert result["budget"] == "$40000000"
        assert result["usa_fees"] == "$74103820"
        assert result["world_fees"] == "$158733820"
        assert result["rus_fees"] == "$2385000"
        assert result["premiere_in_russia"] == "26 мая 2005"
        assert result["premiere_in_world"] == "28 марта 2005"
        assert result["dvd_release"] == "4 августа 2005, «West Video»"
        assert result["age_restrictions"] == "16+"
        assert result["rating_mpaa"] == "R"
        assert result["duration"] == "124 мин. / 02:04"
