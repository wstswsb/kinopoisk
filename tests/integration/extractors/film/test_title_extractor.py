from pathlib import Path
from structure import resources_path, title_extractor
from bs4 import BeautifulSoup


class TestFilmTitleExtractor:
    page_source = Path(
        resources_path,
        "page_sources",
        "sin_city.html",
    ).read_text()

    def setup(self):
        self.extractor = title_extractor

    def test_extract_title(self):
        title = "Город грехов (2005)"
        soup = BeautifulSoup(self.page_source, "lxml")
        assert self.extractor.extract(soup) == title

    def test_extract_title_not_found(self):
        self.page_source = "<html> ... </html>"
        soup = BeautifulSoup(self.page_source, "lxml")
        assert self.extractor.extract(soup) is None
