from pathlib import Path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
)
import selenium.webdriver
from random import choice
from loggers import app_logger


class ChromiumWrapper:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome(options=self.__get_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.origin_tab = self.driver.current_window_handle

    def __get_options(self) -> Options:
        options = Options()
        options.headless = True
        options.add_argument("--no-sandbox")
        options.add_argument(
            'User-Agent="Mozilla/5.0 (X11; Linux x86_64; rv:96.0) '
            'Gecko/2010    0101 Firefox/96.0 '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/72.0.3626.121 Safari/537.36"'
        )
        return options

    @property
    def page_source(self) -> str:
        return self.driver.page_source

    def get_in_new_tab(self, url: str) -> None:
        self.driver.switch_to.new_window("tab")
        self.set_random_user_agent()
        self.driver.get(url)

    def scroll_down(self):
        driver_script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(driver_script)

    def close_tab(self) -> None:
        self.driver.close()
        self.driver.switch_to.window(self.origin_tab)

    def get_wait(self, duration: int) -> "ExplicitWaitWrapper":
        return ExplicitWaitWrapper(self.driver, duration)

    def set_random_user_agent(self) -> None:
        self.driver.execute_cdp_cmd(
            'Network.setUserAgentOverride',
            {"userAgent": self.get_random_user_agent()},
        )

    def get_random_user_agent(self) -> str:
        user_agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/54.0.2840.99 Safari/537.36',

            'Mozilla/5.0 (Windows NT 10.0; WOW64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/54.0.2840.99 Safari/537.36',

            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/54.0.2840.99 Safari/537.36',

            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
            'AppleWebKit/602.2.14 (KHTML, '
            'like Gecko) Version/10.0.1 Safari/602.2.14',

            'Mozilla/5.0 (Windows NT 10.0; WOW64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/54.0.2840.71 Safari/537.36',

            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
            'AppleWebKit/537.36 (KHTML, '
            'like Gecko) Chrome/54.0.2840.98 Safari/537.36',

            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
            'AppleWebKit/537.36 (KHTML, '
            'like Gecko) Chrome/54.0.2840.98 Safari/537.36',

            'Mozilla/5.0 (Windows NT 6.1; WOW64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/54.0.2840.71 Safari/537.36',

            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/54.0.2840.99 Safari/537.36',

            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) '
            'Gecko/20100101 Firefox/50.0'
        ]
        return choice(user_agents)


class ExplicitWaitWrapper:
    def __init__(self, driver, duration: int):
        self.wait = WebDriverWait(driver, duration)

    def until_presence_by_tag(self, tag: str):
        app_logger.debug(f"Wait until presence element with {tag = }")
        self.wait.until(presence_of_element_located((By.TAG_NAME, tag)))
