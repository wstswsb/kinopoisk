from click import echo
from typing import Any, Generator
from bs4 import BeautifulSoup
from time import sleep

from wrappers import ChromiumWrapper
from extractors import FilmTitleExtractor, RelativeLinksExtractor


class FilmParsingService:
    def __init__(
            self,
            browser: ChromiumWrapper,
            relative_links_extractor: RelativeLinksExtractor,
            title_extractor: FilmTitleExtractor,
            attributes_extractors: list):

        self.base_url = "https://kinopoisk.ru"
        self.browser = browser
        self.relative_links_extractor = relative_links_extractor
        self.title_extractor = title_extractor
        self.attributes_extractors = attributes_extractors

    def parse_by_url(self, url: str) -> dict[str, Any]:
        try:
            self.browser.get_in_new_tab(url)
            self.browser.scroll_down()
            wait = self.browser.get_wait(30)
            wait.until_presence_by_tag("h3")
            page_source = self.browser.page_source
        finally:
            self.browser.close_tab()

        soup = BeautifulSoup(page_source)

        attributes = {"title": self.title_extractor.extract(soup)}

        for extractor in self.attributes_extractors:
            key = extractor.key_alias
            attributes[key] = extractor.extract(soup)

        return attributes

    def parse_top_250(self) -> Generator:
        echo("FilmParsingService.parse_top_250() was started")

        url = f"{self.base_url}/lists/movies/top250/"

        echo(f"{url = }")
        try:
            echo("open url ...")
            self.browser.get_in_new_tab(url)
            self.browser.scroll_down()
            wait = self.browser.get_wait(30)
            wait.until_presence_by_tag("main")
            page_source = self.browser.page_source
            echo("page_source loaded")
        finally:
            self.browser.close_tab()
            echo("tab was closed")

        soup = BeautifulSoup(page_source, "lxml")
        echo("start parsing relative links")
        relative_links = self.relative_links_extractor.extract(soup)
        echo(f"{relative_links = }")

        for link in relative_links:
            echo(f"parse {link = }")
            yield self.parse_by_url(f"{self.base_url}{link}")
            self.delay(5)

    def delay(self, seconds) -> None:
        echo(f"sleeping for {seconds}...")
        sleep(seconds)
