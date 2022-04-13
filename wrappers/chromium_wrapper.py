from selenium.webdriver.chromium.options import ChromiumOptions


class ChromiumWrapper:
    def __init__(self):
        self.options = self.__get_options()

    def __get_options(self) -> ChromiumOptions:
        options = ChromiumOptions()
        options.headless = True
        options.add_argument("--no-sandbox")
        options.add_argument(
            'User-Agent="Mozilla/5.0 (X11; Linux x86_64; rv:96.0) '
            'Gecko/2010    0101 Firefox/96.0 '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/72.0.3626.121 Safari/537.36"'
        )
        return options
