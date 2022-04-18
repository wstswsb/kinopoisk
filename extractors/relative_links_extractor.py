from bs4 import BeautifulSoup


class RelativeLinksExtractor:
    def extract(self, soup: BeautifulSoup) -> list[str]:
        main_tag = soup.find("main")
        if not main_tag:
            return []
        film_containers = main_tag.find_all("div", class_=None)

        relative_links = []

        for container in film_containers:
            link_class = "base-movie-main-info_link__YwtP1"
            link = container.find("a", class_=link_class).get("href")

            if link:
                relative_links.append(link)

        return relative_links
