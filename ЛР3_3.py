class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author

    def _str_(self):
        return f"Книга {self.name}. Автор {self.author}"

    def _repr_(self):
        return f"{self._class_._name_}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def _init_(self, name: str, author: str, pages: int):
        super()._init_(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.pages = value

    def _repr_(self):
        return f"{self._class_._name_}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def _init_(self, name: str, author: str, duration: float):
        super()._init_(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.duration = float(value)

    def _repr_(self):
        return f"{self._class_._name_}(name={self.name!r}, author={self.author!r}, duration={self.duration})"