from typing import Any
from bs4 import BeautifulSoup

from wrappers import ChromiumWrapper
from extractors import FilmTitleExtractor, RelativeLinksExtractor
from loggers import app_logger


class FilmParsingService:
    def __init__(
            self,
            browser: ChromiumWrapper,
            relative_links_extractor: RelativeLinksExtractor,
            title_extractor: FilmTitleExtractor,
            attributes_extractors: list):

        self.browser = browser
        self.relative_links_extractor = relative_links_extractor
        self.title_extractor = title_extractor
        self.attributes_extractors = attributes_extractors

    def parse(self, page_source: str) -> dict[str, Any]:
        soup = BeautifulSoup(page_source, "lxml")
        attributes = {"title": self.title_extractor.extract(soup)}
        for extractor in self.attributes_extractors:
            key = extractor.key_alias
            attributes[key] = extractor.extract(soup)
        return attributes

    def parse_film_links(self, page_source: str) -> list[str]:
        app_logger.debug("Parse film links")
        soup = BeautifulSoup(page_source, "lxml")
        return self.relative_links_extractor.extract(soup)
