"""
Модуль: parameters_and_returns
------------------------------

Демонстрирует работу с параметрами и возвращаемыми значениями.
"""
from basics import functions


def demonstrate_parameters_and_returns() -> None:
    """
    Демонстрирует использование параметров и возвращаемых значений.
    """
    print("=== Параметры и возвращаемые значения ===")

    def add(a: int, b: int) -> int:
        return a + b

    result: int = add(5, 7)
    print(f"Результат сложения: {result}")


def demonstrate_default_parameters() -> None:
    """
    Демонстрирует параметры по умолчанию.
    """
    print("\n=== Параметры по умолчанию ===")

    def greet(name: str = "Гость") -> str:
        return f"Привет, {name}!"

    print(greet("Алиса"))
    print(greet())


if __name__ == "__main__":
    demonstrate_parameters_and_returns()
    demonstrate_default_parameters()

