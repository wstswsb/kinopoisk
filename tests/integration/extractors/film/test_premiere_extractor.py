from pathlib import Path
from bs4 import BeautifulSoup
from structure import resources_path
from extractors.film import PremiereExtractor


class TestWorldFeesExtractor:
    page_source = Path(
        resources_path,
        "page_sources",
        "sin_city.html",
    ).read_text()
    soup = BeautifulSoup(page_source, "lxml")

    def test_extract_rus_premiere(self):
        extractor = PremiereExtractor("Премьера в Росcии")
        expected = "26 мая 2005"
        assert extractor.extract(self.soup) == expected

    def test_extract_world_premiere(self):
        extractor = PremiereExtractor("Премьера в мире")
        expected = "28 марта 2005"
        assert extractor.extract(self.soup) == expected
