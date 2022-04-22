from pathlib import Path
from bs4 import BeautifulSoup
from structure import resources_path, relative_links_extractor


class TestRelativeLinksExtractor:
    page_source = Path(
        resources_path,
        "page_sources",
        "top_250.html",
    ).read_text()
    soup = BeautifulSoup(page_source, "lxml")

    def setup(self):
        self.extractor = relative_links_extractor

    def test_extract_relative_links(self):
        expected = [
            '/film/435/', '/film/326/', '/film/329/', '/film/3498/',
            '/film/448/', '/film/312/', '/film/328/', '/film/535341/',
            '/film/342/', '/film/42664/', '/film/2360/', '/film/258687/',
            '/film/679486/', '/film/476/', '/film/279102/', '/film/447301/',
            '/film/111543/', '/film/361/', '/film/522/', '/film/370/',
            '/film/46708/', '/film/474/', '/film/44386/', '/film/32898/',
            '/film/301/', '/film/77263/', '/film/430/', '/film/957887/',
            '/film/41519/', '/film/43395/', '/film/4374/', '/film/397667/',
            '/film/526/', '/film/1143242/', '/film/324/', '/film/25108/',
            '/film/42782/', '/film/322/', '/film/325/', '/film/573759/',
            '/film/689/', '/film/41520/', '/film/649917/', '/film/2213/',
            '/film/42770/', '/film/470553/', '/film/586397/', '/film/381/',
            '/film/389/', '/film/49684/',
        ]
        assert self.extractor.extract(self.soup) == expected
