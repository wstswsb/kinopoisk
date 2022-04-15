from typing import Any, Generator
from bs4 import BeautifulSoup

from wrappers import ChromiumWrapper
from extractors import FilmTitleExtractor


class FilmParsingService:
    def __init__(
            self,
            browser: ChromiumWrapper,
            title_extractor: FilmTitleExtractor,
            attributes_extractors: list):

        self.browser = browser
        self.title_extractor = title_extractor
        self.attributes_extractors = attributes_extractors

    def parse_by_url(self, url: str) -> dict[str, Any]:
        self.browser.get_in_new_tab(url)
        wait = self.browser.get_wait(30)
        wait.until_presence_by_tag("h3")
        page_source = self.browser.page_source
        self.browser.close_tab()

        soup = BeautifulSoup(page_source)

        attributes = {"title": self.title_extractor.extract(soup)}

        for extractor in self.attributes_extractors:
            key = extractor.key_alias
            attributes[key] = extractor.extract(soup)

        return attributes

    def parse_list_by_url(self, urls: list[str]) -> Generator:
        for url in urls:
            yield self.parse_by_url(url)
