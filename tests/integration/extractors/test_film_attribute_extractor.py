from bs4 import BeautifulSoup
from pathlib import Path
from structure import resources_path
from extractors import FilmAttributeExtractor


class TestFilmAttributeExtractor:
    def setup(self):
        self.page_source = self.__read_page_source()
        self.soup = BeautifulSoup(self.page_source, "lxml")

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_year(self):
        extractor = FilmAttributeExtractor("Год производства")
        assert extractor.extract(self.soup) == "2005"

    def test_extract_country(self):
        extractor = FilmAttributeExtractor("Страна")
        assert extractor.extract(self.soup) == "США"

    def test_extract_genre(self):
        extractor = FilmAttributeExtractor("Жанр")
        expected = "боевик,триллер,криминал,детектив"
        assert extractor.extract(self.soup) == expected

    def test_extract_slogan(self):
        extractor = FilmAttributeExtractor("Слоган")
        expected = "«Deadly little Miho»"
        assert extractor.extract(self.soup) == expected

    def test_extract_directors(self):
        extractor = FilmAttributeExtractor("Режиссер")
        expected = "Фрэнк Миллер,Квентин Тарантино,Роберт Родригес"
        assert extractor.extract(self.soup) == expected

    def test_extract_screenwriters(self):
        extractor = FilmAttributeExtractor("Сценарий")
        expected = "Фрэнк Миллер,Роберт Родригес"
        assert extractor.extract(self.soup) == expected

    def test_extract_composers(self):
        extractor = FilmAttributeExtractor("Композитор")
        expected = "Джон Дебни,Грэм Ревелл,Роберт Родригес"
        assert extractor.extract(self.soup) == expected

    def test_extract_artists(self):
        extractor = FilmAttributeExtractor("Художник")
        expected = "Стив Джойнер,Жанетт Скотт,Дэвид Хэк"
        assert extractor.extract(self.soup) == expected

    def test_extract_editors(self):
        extractor = FilmAttributeExtractor("Монтаж")
        expected = "Роберт Родригес"
        assert extractor.extract(self.soup) == expected

    def test_extract_budget(self):
        extractor = FilmAttributeExtractor("Бюджет")
        expected = "$40 000 000"
        assert extractor.extract(self.soup) == expected

    def test_extract_usa_fees(self):
        extractor = FilmAttributeExtractor("Сборы в США")
        expected = "$74 103 820"
        assert extractor.extract(self.soup) == expected

    def test_extract_world_fees(self):
        extractor = FilmAttributeExtractor("Сборы в мире")
        expected = "+ $84 630 000 = $158 733 820"
        assert extractor.extract(self.soup) == expected

    def test_extract_russia_fees(self):
        extractor = FilmAttributeExtractor("Сборы в России")
        expected = "$2 385 000"
        assert extractor.extract(self.soup) == expected

    def test_extract_premiere_in_russia(self):
        extractor = FilmAttributeExtractor("Премьера в Росcии")
        expected = "26 мая 2005,«West»"
        assert extractor.extract(self.soup) == expected

    def test_extract_premiere_in_world(self):
        extractor = FilmAttributeExtractor("Премьера в мире")
        expected = "28 марта 2005"
        assert extractor.extract(self.soup) == expected

    def test_extract_dvd_release(self):
        extractor = FilmAttributeExtractor("Релиз на DVD")
        expected = "4 августа 2005, «West Video»"
        assert extractor.extract(self.soup) == expected

    def test_extract_age_restrictions(self):
        extractor = FilmAttributeExtractor("Возраст")
        expected = "16+"
        assert extractor.extract(self.soup) == expected

    def test_extract_mpaa_restrictions(self):
        extractor = FilmAttributeExtractor("Рейтинг MPAA")
        expected = "R"
        assert extractor.extract(self.soup) == expected

    def test_extract_duration(self):
        extractor = FilmAttributeExtractor("Время")
        expected = "124 мин. / 02:04"
        assert extractor.extract(self.soup) == expected
