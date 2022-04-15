from pathlib import Path
from structure import resources_path
from extractors import FilmTitleExtractor
from bs4 import BeautifulSoup


class TestFilmTitleExtractor:
    def setup(self):
        self.page_source = self.__read_page_source()
        self.extractor = FilmTitleExtractor()

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_title(self):
        title = "Город грехов (2005)"
        soup = BeautifulSoup(self.page_source, "lxml")
        assert self.extractor.extract(soup) == title

    def test_extract_title_not_found(self):
        self.page_source = "<html> ... </html>"
        soup = BeautifulSoup(self.page_source, "lxml")
        assert self.extractor.extract(soup) is None
