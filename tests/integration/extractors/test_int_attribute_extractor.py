from bs4 import BeautifulSoup
from pathlib import Path
from structure import resources_path, year_extractor


class TestIntAttributeExtractor:
    def setup(self):
        self.extractor = year_extractor
        self.page_source = self.__read_page_source()
        self.soup = BeautifulSoup(self.page_source, "lxml")

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_year(self):
        assert self.extractor.extract(self.soup) == 2005

    def test_extract_year_none(self):
        soup = BeautifulSoup("<html></html>", "lxml")
        assert self.extractor.extract(soup) is None
