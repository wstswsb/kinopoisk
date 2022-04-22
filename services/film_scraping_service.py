from time import sleep

from .staff_parsing_service import StaffParsingService
from .film_parsing_service import FilmParsingService
from .film_service import FilmService
from wrappers import ChromiumWrapper
from loggers import app_logger


class FilmScrapingService:
    def __init__(
            self,
            browser_wrapper: ChromiumWrapper,
            film_parsing_service: FilmParsingService,
            staff_parsing_service: StaffParsingService,
            film_service: FilmService):
        self.base_url = "https://kinopoisk.ru"
        self.browser_wrapper = browser_wrapper
        self.film_parsing_service = film_parsing_service
        self.staff_parsing_service = staff_parsing_service
        self.film_service = film_service

    def scrape_top_250(self) -> None:
        pages_count = 5
        links = []
        for page_number in range(1, pages_count + 1):
            app_logger.debug(f"Processing of {page_number} page")
            page_source = self.get_top_films_page_source(page_number)
            links += self.film_parsing_service.parse_film_links(page_source)
            self.delay(5)

        for relative_link in links:
            app_logger.debug(f"Processing {relative_link = }")
            self.scrape_one(relative_link)
            self.delay(5)

    def scrape_one(self, relative_link: str):
        app_logger.debug(f"Scrape film with {relative_link = }")
        self.delay(4)
        source = self.get_film_about_page_source(relative_link)
        staff_page_source = self.get_film_staff_page_source(relative_link)
        attrs = self.film_parsing_service.parse(source)

        attrs["staff"] = self.staff_parsing_service.parse(staff_page_source)
        self.film_service.create(attrs)

    def get_film_staff_page_source(self, relative_link: str):
        url = f"{self.base_url}{relative_link}cast"
        app_logger.debug(f"Open page with {url = }")

        self.browser_wrapper.get_in_new_tab(url)
        self.browser_wrapper.scroll_down()
        wait = self.browser_wrapper.get_wait(30)
        wait.until_presence_by_class("block_left")
        page_source = self.browser_wrapper.page_source
        self.browser_wrapper.close_tab()
        return page_source

    def get_film_about_page_source(self, relative_link: str):
        url = f"{self.base_url}{relative_link}"
        app_logger.debug(f"Open page with {url = }")

        self.browser_wrapper.get_in_new_tab(url)
        self.browser_wrapper.scroll_down()
        wait = self.browser_wrapper.get_wait(30)
        wait.until_presence_by_tag("h3")
        page_source = self.browser_wrapper.page_source
        self.browser_wrapper.close_tab()

        return page_source

    def get_top_films_page_source(self, page_number: int):
        url = f"{self.base_url}/lists/movies/top250/?page={page_number}"
        app_logger.debug(f"Open page with {url = }")
        self.browser_wrapper.get_in_new_tab(url)
        self.browser_wrapper.scroll_down()
        wait = self.browser_wrapper.get_wait(30)
        wait.until_presence_by_tag("main")

        page_source = self.browser_wrapper.page_source
        self.browser_wrapper.close_tab()

        return page_source

    def delay(self, seconds: int):
        app_logger.debug(f"Delay for {seconds} seconds")
        sleep(seconds)
