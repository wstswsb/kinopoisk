import re

from bs4 import BeautifulSoup

from extractors.staff import NamesExtractor
from loggers import app_logger


class StaffParsingService:
    def __init__(self, names_extractor: NamesExtractor):
        self.names_extractor = names_extractor

    def parse(self, page_source: str) -> dict[str, list[str]]:
        app_logger.debug("Parse staff")

        pattern = r'<a\s?name="{}"></a>(.*)<a\s?name="{}"></a>'
        boundary_case_pattern = r'<a\s?name="{}"></a>(.*)<table'
        post_pattern_mapping = {
            "directors": pattern.format("director", "actor"),
            "actors": pattern.format("actor", "producer"),
            "producers": pattern.format("producer", "voice_director"),
            "dubbing_directors": pattern.format("voice_director", "voice"),
            "dubbing_actors": pattern.format("voice", "writer"),
            "screenwriters": pattern.format("writer", "operator"),
            "operators": pattern.format("operator", "composer"),
            "composers": pattern.format("composer", "design"),
            "artists": pattern.format("design", "editor"),
            "editors": boundary_case_pattern.format("editor"),
        }

        return {
            post: self.parse_names(page_source, pattern)
            for post, pattern
            in post_pattern_mapping.items()
        }

    def parse_names(self, page_source: str, re_pattern: str):
        found_sources = re.findall(re_pattern, page_source, re.DOTALL)
        if not found_sources:
            return []
        source = found_sources[0]
        soup = BeautifulSoup(source, "lxml")
        names = self.names_extractor.extract(soup)
        return names
