"""
Модуль: classes_and_objects
----------------------------

Демонстрирует основы работы с классами и объектами.
"""


class Car:
    """
    Простой класс, представляющий автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self) -> None:
        """
        Выводит информацию об автомобиле.
        """
        print(f"{self.year} {self.brand} {self.model}")


def demonstrate_classes_and_objects() -> None:
    """
    Демонстрирует создание и использование классов и объектов.
    """
    print("=== Классы и объекты ===")

    # Создание объекта
    car = Car("Toyota", "Corolla", 2020)
    car.display_info()


if __name__ == "__main__":
    demonstrate_classes_and_objects()

     запускаем файл
    python oop/classes_and_objects.py