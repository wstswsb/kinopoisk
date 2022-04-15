from bs4 import BeautifulSoup
from pathlib import Path
from structure import resources_path
from extractors import RatingExtractor


class TestRatingExtractor:
    def setup(self):
        self.page_source = self.__read_page_source()
        self.soup = BeautifulSoup(self.page_source, "lxml")

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_mpaa(self):
        extractor = RatingExtractor("Рейтинг MPAA")
        expected = "R"
        assert extractor.extract(self.soup) == expected
