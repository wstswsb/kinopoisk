from pathlib import Path
from structure import staff_parsing_service, resources_path


def read_page_source():
    path = Path(resources_path, "page_sources", "sin_city_staff.html")
    return path.read_text()


page_source = read_page_source()


class TestStaffParsingService:
    def setup(self):
        self.service = staff_parsing_service
        self.page_source = page_source

    def test_parse_directors(self):
        expected = [
            "Фрэнк Миллер",
            "Квентин Тарантино",
            "Роберт Родригес",
        ]
        staff = self.service.parse(self.page_source)
        assert staff["directors"] == expected

    def test_parse_actors(self):
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
        staff = self.service.parse(self.page_source)
        assert staff["actors"] == expected

    def test_parse_producers(self):
        expected = [
            "Элизабет Авеллан",
            "Билл Скотт",
            "Боб Вайнштейн",
            "Харви Вайнштейн"
        ]
        staff = self.service.parse(self.page_source)
        assert staff["producers"] == expected

    def test_parse_dubbing_directors(self):
        expected = ["Юлия Бирюкова"]
        staff = self.service.parse(self.page_source)
        assert staff["dubbing_directors"] == expected

    def test_parse_dubbing_actors(self):
        expected = [
            'Алексей Колган', 'Владимир Антоник',
            'Валерий Сторожик', 'Ольга Кузнецова',
            'Анастасия Волкова', 'Александр Груздев',
            'Людмила Шувалова', 'Андрей Бархударов',
            'Жанна Никонова', 'Елена Соловьева',
            'Олег Куценко', 'Рогволд Суховерко',
            'Александр Клюквин', 'Андрей Гриневич',
            'Всеволод Кузнецов', 'Илья Бледный',
            'Никита Прозоровский', 'Олег Форостенко',
            'Сергей Бурунов', 'Александр Комлев',
            'Александр Котов', 'Юрий Меншагин',
            'Леонид Белозорович', 'Андрей Казанцев',
            'Дарья Юрченко', 'Дмитрий Полонский',
            'Мария Овчинникова',
        ]
        staff = self.service.parse(self.page_source)
        assert staff["dubbing_actors"] == expected

    def test_parse_screenwriters(self):
        expected = [
            "Фрэнк Миллер",
            "Роберт Родригес",
        ]
        staff = self.service.parse(self.page_source)
        assert staff["screenwriters"] == expected

    def test_parse_operators(self):
        expected = ["Роберт Родригес"]
        staff = self.service.parse(self.page_source)
        assert staff["operators"] == expected

    def test_parse_composers(self):
        expected = [
            "Джон Дебни",
            "Грэм Ревелл",
            "Роберт Родригес",
        ]
        staff = self.service.parse(self.page_source)
        assert staff["composers"] == expected

    def test_parse_artists(self):
        expected = [
            "Стив Джойнер",
            "Жанетт Скотт",
            "Дэвид Хэк",
        ]
        staff = self.service.parse(self.page_source)
        assert staff["artists"] == expected

    def test_parse_editors(self):
        expected = ["Роберт Родригес"]
        staff = self.service.parse(self.page_source)
        assert staff["editors"] == expected
