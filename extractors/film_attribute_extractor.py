from bs4 import BeautifulSoup
import unicodedata


class FilmAttributeExtractor:
    def __init__(self, key: str):
        self.key = key

    def extract(self, soup: BeautifulSoup):
        key_div = soup.find("div", string=self.key)
        if key_div is None:
            return None

        key_value_container = key_div.parent
        if key_value_container is None:
            return None

        linked_value = key_value_container.find("a")
        if linked_value is None:
            return self.process_not_linked_case(key_value_container)

        value_container = linked_value.parent
        if not value_container:
            return None

        value = value_container.get_text(strip=True)
        return self.__normalize_string(value)

    def process_not_linked_case(self, key_value_container: BeautifulSoup):
        key_value_list = key_value_container.find_all("div")
        if key_value_list is None:
            return None

        value = key_value_list[-1].get_text()
        return self.__normalize_string(value)

    def __normalize_string(self, value: str) -> str:
        return unicodedata.normalize("NFKC", value)
