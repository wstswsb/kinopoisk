from pathlib import Path
from bs4 import BeautifulSoup
from structure import resources_path
from extractors.staff import NamesExtractor


def read_page_source():
    path = Path(
        resources_path,
        "page_sources",
        "sin_city_only_actors_staff.html",
    )
    return path.read_text()


page_source = read_page_source()
soup = BeautifulSoup(page_source, "lxml")


class TestActorsExtractor:
    def setup(self):
        self.extractor = NamesExtractor()
        self.page_source = page_source
        self.soup = soup

    def test_extract(self):
        expected = [
            'Брюс Уиллис', 'Микки Рурк', 'Клайв Оуэн',
            'Розарио Доусон', 'Джессика Альба', 'Бенисио Дель Торо',
            'Джейми Кинг', 'Ник Стал', 'Девон Аоки',
            'Алексис Бледел', 'Бриттани Мерфи', 'Карла Гуджино',
            'Пауэрс Бут', 'Майкл Кларк Дункан', 'Элайджа Вуд',
            'Рутгер Хауэр', 'Майкл Мэдсен', 'Томми Флэнаган',
            'Джош Хартнетт', 'Марли Шелтон', 'Джуд Чикколелла',
            'Кара Д. Бриггс', 'Джесси Де Луна', 'Jj Dashnaw',
            'Джейсон Дуглас', 'Кристина Франкенфилд', 'Рик Гомес',
            'Дэвид Хикки', 'Эвелин Хёрли', 'Грег Ингрэм',
            'Никки Кэтт', 'Хелен Кирк', 'Этан Маникис',
            'Джейсон МакДональд', 'Джон МакЛеод', 'Кларк Миддлтон',
            'Фрэнк Миллер', 'Этан Рэйнс', 'Лиза Мари Ньюмайер',
            'Томми Никс', 'Ник Офферман', 'Марко Перелья',
            'Сэм Рэй', 'Рендал Ридер', 'Дэвид Алекс Руис',
            'Райан Рутледж', 'Джефф Шван', 'Кори Симеоне',
            'Пол Т. Тейлор', 'Скотт Титерс', 'Кен Томас',
            'Рикардо Торрес', 'Макензи Вега', 'Эри Вервин',
            'Патрисия Вонне', 'Шон Уэйнрайт-Брэниган', 'Крис Уорнер',
            'Дэнни Вайнандс', 'Дж.Д. Янг', 'Чарисса Аллен',
            'Джо Баскез', 'Джессика Хейл', 'Сэмми Харт',
            'Майкл Ламберт', 'Ashley Moore', 'Аманда Филлипс',
            'Лорен-Элейн Пауэлл', 'Тексас', 'Эмми Роббин',
            'Келли Робинс', 'Роберт Родригес', 'Моника Спрёч',
            'Пенни Витал', 'Кэтерин Уиллис',
        ]
        assert self.extractor.extract(self.soup) == expected