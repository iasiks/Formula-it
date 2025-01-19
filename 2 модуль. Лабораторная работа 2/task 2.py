from pydantic import BaseModel, Field
from typing import List, Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book(BaseModel):
    id_: int = Field(...)
    name: str = Field(...)
    pages: int = Field(..., gt=0)


# TODO написать класс Library
class Library(BaseModel):
    books: Optional[List[Book]] = []


    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        else:
            return max(book.id_ for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError ("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
