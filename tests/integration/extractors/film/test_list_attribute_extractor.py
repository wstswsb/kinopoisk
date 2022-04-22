from bs4 import BeautifulSoup
from pathlib import Path
from structure import resources_path
from extractors.film import ListAttributeExtractor


class TestListAttributeExtractor:
    def setup(self):
        self.page_source = self.__read_page_source()
        self.soup = BeautifulSoup(self.page_source, "lxml")

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_genre(self):
        extractor = ListAttributeExtractor("Жанр")
        expected = ["боевик", "триллер", "криминал", "детектив"]
        assert extractor.extract(self.soup) == expected

    def test_extract_directors(self):
        extractor = ListAttributeExtractor("Режиссер")
        expected = ["Фрэнк Миллер", "Квентин Тарантино", "Роберт Родригес"]
        assert extractor.extract(self.soup) == expected

    def test_extract_producers(self):
        extractor = ListAttributeExtractor("Продюсер")
        expected = ["Элизабет Авеллан", "Билл Скотт", "Боб Вайнштейн"]
        assert extractor.extract(self.soup) == expected

    def test_extract_composers(self):
        extractor = ListAttributeExtractor("Композитор")
        expected = ["Джон Дебни", "Грэм Ревелл", "Роберт Родригес"]
        assert extractor.extract(self.soup) == expected

    def test_extract_artists(self):
        extractor = ListAttributeExtractor("Художник")
        expected = ["Стив Джойнер", "Жанетт Скотт", "Дэвид Хэк"]
        assert extractor.extract(self.soup) == expected
