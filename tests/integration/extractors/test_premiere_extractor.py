from pathlib import Path
from bs4 import BeautifulSoup
from structure import resources_path
from extractors import PremiereExtractor


class TestWorldFeesExtractor:
    def setup(self):
        self.page_source = self.__read_page_source()
        self.soup = BeautifulSoup(self.page_source, "lxml")

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_rus_premiere(self):
        # second "c" in "Росcии" from English ABC
        extractor = PremiereExtractor("Премьера в Росcии")
        expected = "26 мая 2005"
        assert extractor.extract(self.soup) == expected

    def test_extract_world_premiere(self):
        extractor = PremiereExtractor("Премьера в мире")
        expected = "28 марта 2005"
        assert extractor.extract(self.soup) == expected
