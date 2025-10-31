"""
Модуль: polymorphism
--------------------

Демонстрирует полиморфизм.
"""


class Animal:
    """
    Базовый класс для всех животных.
    """

    def speak(self) -> str:
        """
        Возвращает звук, издаваемый животным.
        """
        return "Some generic sound"


class Dog(Animal):
    """
    Производный класс, представляющий собаку.
    """

    def speak(self) -> str:
        """
        Переопределяет метод для собаки.
        """
        return "Woof!"


class Cat(Animal):
    """
    Производный класс, представляющий кошку.
    """

    def speak(self) -> str:
        """
        Переопределяет метод для кошки.
        """
        return "Meow!"


def demonstrate_polymorphism() -> None:
    """
    Демонстрирует полиморфизм.
    """
    print("=== Полиморфизм ===")

    animals: list[Animal] = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())


if __name__ == "__main__":
    demonstrate_polymorphism()

    запускаем файл
    python oop/polimorphism.py