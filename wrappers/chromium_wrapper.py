from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
)
import selenium.webdriver


class ChromiumWrapper:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome(options=self.__get_options())
        self.driver.maximize_window()
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
    def page_source(self):
        return self.driver.page_source

    def get_in_new_tab(self, url: str):
        self.driver.switch_to.new_window("tab")
        self.driver.get(url)

    def close_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.origin_tab)

    def get_wait(self, duration: int):
        return ExplicitWaitWrapper(self.driver, duration)


class ExplicitWaitWrapper:
    def __init__(self, driver, duration: int):
        self.wait = WebDriverWait(driver, duration)

    def until_presence_by_tag(self, tag: str):
        self.wait.until(presence_of_element_located((By.TAG_NAME, tag)))
