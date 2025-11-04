"""
Модуль: lambda_functions
------------------------

Демонстрирует использование лямбда-функций.
"""
from basics import functions


def demonstrate_lambda_functions() -> None:
    """
    Демонстрирует лямбда-функции.
    """
    print("=== Лямбда-функции ===")

    square = lambda x: x ** 2
    print(f"Квадрат числа 5: {square(5)}")

    numbers: list[int] = [3, 1, 4, 2]
    sorted_numbers = sorted(numbers, key=lambda x: -x)
    print(f"Отсортированные числа: {sorted_numbers}")


if __name__ == "__main__":
    demonstrate_lambda_functions()

