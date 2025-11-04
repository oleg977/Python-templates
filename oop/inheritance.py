"""
Модуль: inheritance
-------------------

Демонстрирует принцип наследования.
"""


class Vehicle:
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def display_info(self) -> None:
        """
        Выводит базовую информацию о транспортном средстве.
        """
        print(f"{self.brand} {self.model}")


class Car(Vehicle):
    """
    Производный класс, представляющий автомобиль.
    """

    def __init__(self, brand: str, model: str, doors: int):
        super().__init__(brand, model)
        self.doors = doors

    def display_info(self) -> None:
        """
        Переопределяет метод для вывода дополнительной информации.
        """
        super().display_info()
        print(f"Количество дверей: {self.doors}")


def demonstrate_inheritance() -> None:
    """
    Демонстрирует наследование.
    """
    print("=== Наследование ===")

    vehicle = Vehicle("Generic", "Vehicle")
    vehicle.display_info()

    car = Car("Toyota", "Corolla", 4)
    car.display_info()


if __name__ == "__main__":
    demonstrate_inheritance()

