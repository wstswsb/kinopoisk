from bs4 import BeautifulSoup


class NamesExtractor:

    def extract(self, soup: BeautifulSoup) -> list[str]:
        info_divs = soup.find_all("div", {"class": "info"})
        if not info_divs:
            return []

        name_links = []
        for div in info_divs:
            name_link = div.find("a")
            if name_link:
                name_links.append(name_link)

        names = [name_link.get_text() for name_link in name_links]
        return names
