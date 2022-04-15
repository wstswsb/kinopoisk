from pathlib import Path
from bs4 import BeautifulSoup
from structure import resources_path
from extractors import FeesExtractor


class TestWorldFeesExtractor:
    def setup(self):
        self.page_source = self.__read_page_source()
        self.soup = BeautifulSoup(self.page_source, "lxml")

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_budget(self):
        extractor = FeesExtractor("Бюджет")
        expected = "$40000000"
        assert extractor.extract(self.soup) == expected

    def test_extract_usa_fees(self):
        extractor = FeesExtractor("Сборы в США")
        expected = "$74103820"
        assert extractor.extract(self.soup) == expected

    def test_extract_rus_fees(self):
        extractor = FeesExtractor("Сборы в России")
        expected = "$2385000"
        assert extractor.extract(self.soup) == expected
