"""
Модуль: magic_methods
---------------------

Демонстрирует использование магических методов в Python.
"""


class Book:
    """
    Класс, представляющий книгу.
    """

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователей.
        """
        return f"'{self.title}' by {self.author}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчиков.
        """
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __len__(self) -> int:
        """
        Возвращает количество страниц в книге.
        """
        return self.pages

    def __add__(self, other: 'Book') -> int:
        """
        Позволяет складывать книги (по количеству страниц).
        """
        if isinstance(other, Book):
            return self.pages + other.pages
        raise TypeError("Unsupported operand type for +")


def demonstrate_magic_methods() -> None:
    """
    Демонстрирует использование магических методов.
    """
    print("=== Магические методы ===")

    book1 = Book("Python Crash Course", "Eric Matthes", 560)
    book2 = Book("Automate the Boring Stuff with Python", "Al Sweigart", 592)

    # __str__ и __repr__
    print(f"Строковое представление (str): {book1}")
    print(f"Представление для разработчиков (repr): {repr(book1)}")

    # __len__
    print(f"Количество страниц в книге '{book1.title}': {len(book1)}")

    # __add__
    total_pages = book1 + book2
    print(f"Общее количество страниц в двух книгах: {total_pages}")


if __name__ == "__main__":
    demonstrate_magic_methods()
