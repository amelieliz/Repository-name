import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.title
        'Война и мир'
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not author.strip():
            raise ValueError("Автор книги не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
        self.current_page = 1

    def is_finished(self) -> bool:
        """
        Проверяет, прочитана ли книга полностью

        :return: True если книга прочитана, False если нет

        Примеры:
        >>> book = Book("Маленький принц", "Антуан де Сент-Экзюпери", 96)
        >>> book.current_page = 96
        >>> book.is_finished()
        True
        """
        ...

    def read_pages(self, pages_to_read: int) -> int:
        """
        Чтение указанного количества страниц

        :param pages_to_read: Количество страниц для чтения
        :return: Номер текущей страницы после чтения

        :raise ValueError: Если количество страниц для чтения отрицательное
                         или превышает оставшееся количество страниц

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.read_pages(50)
        51
        """
        if not isinstance(pages_to_read, int):
            raise TypeError("Количество страниц для чтения должно быть типа int")
        if pages_to_read < 0:
            raise ValueError("Количество страниц для чтения не может быть отрицательным")
        if self.current_page + pages_to_read > self.pages + 1:
            raise ValueError(f"Нельзя прочитать больше {self.pages - self.current_page + 1} страниц")
        ...

    def get_bookmark(self) -> dict:
        """
        Получение информации о текущем месте в книге

        :return: Словарь с информацией о текущей позиции

        Примеры:
        >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 672)
        >>> book.current_page = 150
        >>> book.get_bookmark()
        {'title': 'Преступление и наказание', 'current_page': 150, 'progress': 22.32}
        """
        ...






    def charge_battery(self, minutes: int) -> float:
        """
        Зарядка аккумулятора

        :param minutes: Время зарядки в минутах
        :return: Уровень заряда после зарядки в процентах

        :raise ValueError: Если время зарядки отрицательное

        Примеры:
        >>> phone = SmartPhone("Xiaomi", "Redmi Note 12", 5000)
        >>> phone.battery_level = 20
        >>> phone.charge_battery(30)
        65.0
        """
        if not isinstance(minutes, int):
            raise TypeError("Время зарядки должно быть типа int")
        if minutes < 0:
            raise ValueError("Время зарядки не может быть отрицательным")
        ...

    def install_app(self, app_name: str, app_size: int) -> str:
        """
        Установка приложения на смартфон

        :param app_name: Название приложения
        :param app_size: Размер приложения в МБ
        :return: Сообщение об успешной установке

        Примеры:
        >>> phone = SmartPhone("Google", "Pixel 7", 4355)
        >>> phone.install_app("Telegram", 85)
        'Приложение Telegram успешно установлено'
        """
        if not isinstance(app_name, str):
            raise TypeError("Название приложения должно быть типа str")
        if not app_name.strip():
            raise ValueError("Название приложения не может быть пустым")

        if not isinstance(app_size, int):
            raise TypeError("Размер приложения должен быть типа int")
        if app_size <= 0:
            raise ValueError("Размер приложения должен быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()