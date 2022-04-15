from structure import film_service, film_repository


class TestFilmService:
    def setup(self):
        self.service = film_service

    def test_create_by_url(self):
        url = "https://www.kinopoisk.ru/film/77443"
        model = self.service.create_by_url(url)
        db_document = film_repository.find_by_id(model.id)

        assert db_document["year"] == 2005
        assert db_document["country"] == "США"
        assert db_document["genre"] == [
            "боевик", "триллер",
            "криминал", "детектив",
        ]
        assert db_document["slogan"] == "«Deadly little Miho»"
        assert db_document["directors"] == [
            "Фрэнк Миллер",
            "Квентин Тарантино",
            "Роберт Родригес",
        ]
        assert db_document["screenwriters"] == [
            "Фрэнк Миллер",
            "Роберт Родригес",
        ]
        assert db_document["producers"] == [
            "Элизабет Авеллан",
            "Билл Скотт",
            "Боб Вайнштейн",
        ]
        assert db_document["operators"] == ["Роберт Родригес"]
        assert db_document["composers"] == [
            "Джон Дебни",
            "Грэм Ревелл",
            "Роберт Родригес",
        ]
        assert db_document["artists"] == [
            "Стив Джойнер",
            "Жанетт Скотт",
            "Дэвид Хэк",
        ]
        assert db_document["editors"] == ["Роберт Родригес"]
        assert db_document["budget"] == "$40000000"
        assert db_document["usa_fees"] == "$74103820"
        assert db_document["world_fees"] == "$158733820"
        assert db_document["rus_fees"] == "$2385000"
        assert db_document["premiere_in_russia"] == "26 мая 2005"
        assert db_document["premiere_in_world"] == "28 марта 2005"
        assert db_document["dvd_release"] == "4 августа 2005, «West Video»"
        assert db_document["age_restrictions"] == "16+"
        assert db_document["rating_mpaa"] == "R"
        assert db_document["duration"] == "124 мин. / 02:04"
