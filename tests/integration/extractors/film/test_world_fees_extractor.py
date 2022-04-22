from pathlib import Path
from bs4 import BeautifulSoup
from structure import resources_path
from extractors.film import WorldFeesExtractor


class TestWorldFeesExtractor:
    def setup(self):
        self.page_source = self.__read_page_source()
        self.soup = BeautifulSoup(self.page_source, "lxml")
        self.extractor = WorldFeesExtractor("Сборы в мире")

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_world_fees(self):
        assert self.extractor.extract(self.soup) == "$158733820"
