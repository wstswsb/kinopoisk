from bs4 import BeautifulSoup
from pathlib import Path
from structure import resources_path
from extractors.film import RatingExtractor


class TestRatingExtractor:
    page_source = Path(
        resources_path,
        "page_sources",
        "sin_city.html",
    ).read_text()
    soup = BeautifulSoup(page_source, "lxml")

    def test_extract_mpaa(self):
        extractor = RatingExtractor("Рейтинг MPAA")
        expected = "R"
        assert extractor.extract(self.soup) == expected
