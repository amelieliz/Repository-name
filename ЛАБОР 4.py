class MusicalInstrument:
    """Класс музыкального инструмента."""

    def _init_(self, name: str, price: float):
        self.name = name
        self._price = price
        self._is_tuned = False

    def play(self) -> str:
        """Играть на инструменте."""
        if not self._is_tuned:
            return f"{self.name} не настроен, нужно настроить"
        return f"{self.name} издает какой-либо звук"

    def tune(self) -> None:
        """Настроить инструмент."""
        self._is_tuned = True
        print(f"{self.name} настроен")

    def _str_(self) -> str:
        return f"Инструмент: {self.name}, цена: {self._price} руб."

    def _repr_(self) -> str:
        return f"MusicalInstrument('{self.name}', {self._price})"


class Guitar(MusicalInstrument):
    """Класс гитары."""

    def _init_(self, name: str, price: float, strings: int):
        super()._init_(name, price)
        self.strings = strings  # количество струн

    def play(self) -> str:
        """
        Переопределяем метод play.

        Причина: гитара играет перебором струн.
        """
        if not self._is_tuned:
            return f"{self.name} не настроена"
        return f"{self.name} играет перебором {self.strings} струн"

    def change_string(self) -> None:
        """Поменять струны"""
        print(f"Струны на {self.name} заменены")
        self._is_tuned = False  # после замены струн нужно настроить

    def _str_(self) -> str:
        return f"Гитара: {self.name}, струн: {self.strings}, цена: {self._price} руб."

    def _repr_(self) -> str:
        return f"Guitar('{self.name}', {self._price}, {self.strings})"


class Piano(MusicalInstrument):
    """Класс пианино."""

    def _init_(self, name: str, price: float, keys: int):
        super()._init_(name, price)
        self.keys = keys  # количество клавиш

    def play(self) -> str:
        """
        Переопределяем метод play.

        Причина: пианино играет нажатием клавиш.
        """
        if not self._is_tuned:
            return f"{self.name} не настроено"
        return f"{self.name} играет нажатием {self.keys} клавиш"

    def press_key(self, note: str) -> None:
        """Нажать конкретную клавишу"""
        print(f"Нажата клавиша {note} на {self.name}")

    def _str_(self) -> str:
        return f"Пианино: {self.name}, клавиш: {self.keys}, цена: {self._price} руб."

    def _repr_(self) -> str:
        return f"Piano('{self.name}', {self._price}, {self.keys})"


# Пример использования
guitar = Guitar("Fender Stratocaster", 50000, 6)
piano = Piano("Yamaha", 150000, 88)

print(guitar.play())  # Fender Stratocaster не настроен, нужно настроить
guitar.tune()  # Fender Stratocaster настроен
print(guitar.play())  # Fender Stratocaster играет перебором 6 струн

print(piano.play())  # Yamaha не настроено, нужно настроить
piano.press_key("C4")  # Нажата клавиша C4 на Yamaha