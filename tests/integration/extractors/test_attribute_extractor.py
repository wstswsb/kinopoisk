from bs4 import BeautifulSoup
from pathlib import Path
from structure import resources_path
from extractors import AttributeExtractor


def read_page_source():
    path = Path(resources_path, "page_sources", "sin_city.html")
    return path.read_text()


page_source = read_page_source()
soup = BeautifulSoup(page_source, "lxml")


class TestAttributeExtractor:
    def setup(self):
        self.page_source = page_source
        self.soup = soup

    def test_extract_year(self):
        extractor = AttributeExtractor("Год производства")
        assert extractor.extract(self.soup) == "2005"

    def test_extract_country(self):
        extractor = AttributeExtractor("Страна")
        assert extractor.extract(self.soup) == "США"

    def test_extract_genre(self):
        extractor = AttributeExtractor("Жанр")
        expected = "боевик,триллер,криминал,детектив"
        assert extractor.extract(self.soup) == expected

    def test_extract_slogan(self):
        extractor = AttributeExtractor("Слоган")
        expected = "«Deadly little Miho»"
        assert extractor.extract(self.soup) == expected

    def test_extract_directors(self):
        extractor = AttributeExtractor("Режиссер")
        expected = "Фрэнк Миллер,Квентин Тарантино,Роберт Родригес"
        assert extractor.extract(self.soup) == expected

    def test_extract_screenwriters(self):
        extractor = AttributeExtractor("Сценарий")
        expected = "Фрэнк Миллер,Роберт Родригес"
        assert extractor.extract(self.soup) == expected

    def test_extract_composers(self):
        extractor = AttributeExtractor("Композитор")
        expected = "Джон Дебни,Грэм Ревелл,Роберт Родригес"
        assert extractor.extract(self.soup) == expected

    def test_extract_artists(self):
        extractor = AttributeExtractor("Художник")
        expected = "Стив Джойнер,Жанетт Скотт,Дэвид Хэк"
        assert extractor.extract(self.soup) == expected

    def test_extract_editors(self):
        extractor = AttributeExtractor("Монтаж")
        expected = "Роберт Родригес"
        assert extractor.extract(self.soup) == expected

    def test_extract_producers(self):
        extractor = AttributeExtractor("Продюсер")
        expected = "Элизабет Авеллан,Билл Скотт,Боб Вайнштейн,..."
        assert extractor.extract(self.soup) == expected

    def test_extract_budget(self):
        extractor = AttributeExtractor("Бюджет")
        expected = "$40 000 000"
        assert extractor.extract(self.soup) == expected

    def test_extract_usa_fees(self):
        extractor = AttributeExtractor("Сборы в США")
        expected = "$74 103 820"
        assert extractor.extract(self.soup) == expected

    def test_extract_world_fees(self):
        extractor = AttributeExtractor("Сборы в мире")
        expected = "+ $84 630 000 = $158 733 820сборы"
        assert extractor.extract(self.soup) == expected

    def test_extract_russia_fees(self):
        extractor = AttributeExtractor("Сборы в России")
        expected = "$2 385 000"
        assert extractor.extract(self.soup) == expected

    def test_extract_premiere_in_russia(self):
        extractor = AttributeExtractor("Премьера в Росcии")
        expected = "26 мая 2005,«West»"
        assert extractor.extract(self.soup) == expected

    def test_extract_premiere_in_world(self):
        extractor = AttributeExtractor("Премьера в мире")
        expected = "28 марта 2005,..."
        assert extractor.extract(self.soup) == expected

    def test_extract_dvd_release(self):
        extractor = AttributeExtractor("Релиз на DVD")
        expected = "4 августа 2005, «West Video»"
        assert extractor.extract(self.soup) == expected

    def test_extract_age_restrictions(self):
        extractor = AttributeExtractor("Возраст")
        expected = "16+"
        assert extractor.extract(self.soup) == expected

    def test_extract_mpaa_restrictions(self):
        extractor = AttributeExtractor("Рейтинг MPAA")
        expected = "Rлицам до 17 лет обязательно присутствие взрослого"
        assert extractor.extract(self.soup) == expected

    def test_extract_duration(self):
        extractor = AttributeExtractor("Время")
        expected = "124 мин. / 02:04"
        assert extractor.extract(self.soup) == expected
