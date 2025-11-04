"""
Модуль: abstraction
-------------------

Демонстрирует абстракцию.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Абстрактный класс для геометрических фигур.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры.
        """
        pass


class Circle(Shape):
    """
    Производный класс, представляющий круг.
    """

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь круга.
        """
        return 3.14159 * self.radius ** 2


def demonstrate_abstraction() -> None:
    """
    Демонстрирует абстракцию.
    """
    print("=== Абстракция ===")

    circle = Circle(5)
    print(f"Площадь круга: {circle.area():.2f}")


if __name__ == "__main__":
    demonstrate_abstraction()

