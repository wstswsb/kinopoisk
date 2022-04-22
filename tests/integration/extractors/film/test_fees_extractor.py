from pathlib import Path
from bs4 import BeautifulSoup
from structure import resources_path
from extractors.film import FeesExtractor


class TestWorldFeesExtractor:
    page_source = Path(
        resources_path,
        "page_sources",
        "sin_city.html",
    ).read_text()
    soup = BeautifulSoup(page_source, "lxml")

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
