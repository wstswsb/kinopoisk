from pathlib import Path
from bs4 import BeautifulSoup
from structure import resources_path, world_fees_extractor


class TestWorldFeesExtractor:
    page_source = Path(
        resources_path,
        "page_sources",
        "sin_city.html",
    ).read_text()
    soup = BeautifulSoup(page_source, "lxml")

    def setup(self):
        self.extractor = world_fees_extractor

    def __read_page_source(self):
        path = Path(resources_path, "page_sources", "sin_city.html")
        return path.read_text()

    def test_extract_world_fees(self):
        assert self.extractor.extract(self.soup) == "$158733820"
