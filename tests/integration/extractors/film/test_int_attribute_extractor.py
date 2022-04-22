from bs4 import BeautifulSoup
from pathlib import Path
from structure import resources_path, year_extractor


class TestIntAttributeExtractor:
    page_source = Path(
        resources_path,
        "page_sources",
        "sin_city.html",
    ).read_text()
    soup = BeautifulSoup(page_source, "lxml")

    def setup(self):
        self.extractor = year_extractor

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_year(self):
        assert self.extractor.extract(self.soup) == 2005

    def test_extract_year_none(self):
        soup = BeautifulSoup("<html></html>", "lxml")
        assert self.extractor.extract(soup) is None
