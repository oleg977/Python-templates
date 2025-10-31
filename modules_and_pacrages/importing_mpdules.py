"""
Модуль: importing_modules
-------------------------

Демонстрирует различные способы импорта модулей.
"""

# Импорт модуля целиком
import math

# Импорт конкретных функций
from random import randint

# Импорт с псевдонимом
import datetime as dt


def demonstrate_imports() -> None:
    """
    Демонстрирует использование импортированных модулей.
    """
    print("=== Импорт модулей ===")

    # Использование модуля math
    print(f"Квадратный корень из 16: {math.sqrt(16)}")

    # Использование функции randint из модуля random
    print(f"Случайное число от 1 до 10: {randint(1, 10)}")

    # Использование модуля datetime с псевдонимом
    now = dt.datetime.now()
    print(f"Текущая дата и время: {now}")


if __name__ == "__main__":
    demonstrate_imports()

    запускаем файл
    python modules_and_pacrages/importing_modules.py