"""
Модуль: creating_packages
-------------------------

Демонстрирует создание и использование пакетов.
"""

# Для демонстрации создадим структуру:
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# Предположим, что у нас есть пакет my_package с двумя модулями:
from my_package.module1 import greet
from my_package.module2 import calculate_square


def demonstrate_packages() -> None:
    """
    Демонстрирует использование пакетов.
    """
    print("=== Создание и использование пакетов ===")

    greet("Боб")
    print(f"Квадрат числа 7: {calculate_square(7)}")


if __name__ == "__main__":
    demonstrate_packages()

