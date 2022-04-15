from typing import Optional
from bs4 import BeautifulSoup
import unicodedata
import re

from services.tools import TypesConvertingService


class AttributeExtractor:
    def __init__(self, key: str, key_alias: str = None):
        self.key = key
        self.key_alias = key_alias or key

    def extract(self, soup: BeautifulSoup) -> Optional[str]:
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


class IntAttributeExtractor(AttributeExtractor):
    def __init__(
            self,
            key: str,
            types_converting_service: TypesConvertingService,
            key_alias: str = None):
        super().__init__(key, key_alias)
        self.types_converting_service = types_converting_service

    def extract(self, soup: BeautifulSoup) -> Optional[int]:
        return self.types_converting_service.to_int(super().extract(soup))


class ListAttributeExtractor(AttributeExtractor):
    def extract(self, soup: BeautifulSoup) -> list[str]:
        raw_attribute = super().extract(soup)
        if not raw_attribute:
            return []
        attrs = [item for item in raw_attribute.split(",")]
        if attrs[-1] == "...":
            attrs.pop(-1)
        return attrs


class FeesExtractor(AttributeExtractor):
    def extract(self, soup: BeautifulSoup) -> Optional[str]:
        raw_attribute = super().extract(soup)
        if not raw_attribute:
            return None
        return raw_attribute.replace(" ", "")


class WorldFeesExtractor(AttributeExtractor):
    def extract(self, soup: BeautifulSoup) -> Optional[str]:
        raw_attribute = super().extract(soup)
        if not raw_attribute:
            return None
        fees = re.findall(r"[$][0-9 ]+", raw_attribute)
        if not fees:
            return None
        if len(fees) != 2:
            return None

        world_fees = fees[1]
        return world_fees.replace(" ", "")


class PremiereExtractor(AttributeExtractor):
    def extract(self, soup: BeautifulSoup) -> Optional[str]:
        raw_attribute = super().extract(soup)
        if not raw_attribute:
            return None
        premiere = re.findall(r"[0-9]{1,2} \w+ [0-9]{1,4}", raw_attribute)
        if not premiere:
            return None
        if len(premiere) != 1:
            return None
        return premiere[0]


class RatingExtractor(AttributeExtractor):
    def extract(self, soup: BeautifulSoup) -> Optional[str]:
        ratings = ("NC-17", "PG-13", "PG", "G", "R")
        raw_attribute = super().extract(soup)
        if not raw_attribute:
            return None

        upper_attribute = raw_attribute.upper()
        max_rating_length = len(max(ratings, key=lambda x: len(x)))
        matching_attribute_part = upper_attribute[:max_rating_length]

        for rating in ratings:
            if rating not in matching_attribute_part:
                continue
            return rating
        return None
