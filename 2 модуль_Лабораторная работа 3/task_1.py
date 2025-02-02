class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self)-> str:
        return self._name
    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть целым числом')
        if not pages > 0:
            raise ValueError ('Количество страниц должно быть положительным числом')
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}, Количество страниц - {self.pages}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError('Продолжительность книги должна быть выражена числом с плавающей запятой')
        if not duration > 0:
            raise ValueError ('Продолжительность книги должна быть положительным числом')
        self._duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}, Продолжительность аудиокниги - {self.duration}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    paper_book = PaperBook("1984", "George Orwell", 328)
    audio_book = AudioBook("1984", "George Orwell", 11.5)

    print(paper_book)
    print(audio_book)

    print(repr(paper_book))
    print(repr(audio_book))