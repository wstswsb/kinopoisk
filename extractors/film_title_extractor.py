from typing import Optional

from bs4 import BeautifulSoup


class FilmTitleExtractor:
    def extract(self, soup: BeautifulSoup) -> Optional[str]:
        title_tag = soup.find("h1")
        if title_tag is None:
            return None

        return title_tag.get_text()
