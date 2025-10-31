"""
Модуль: module_basics
---------------------

Демонстрирует базовые принципы работы с модулями.
"""

# Пример простого модуля
def greet(name: str) -> None:
    """
    Выводит приветствие.
    """
    print(f"Привет, {name}!")

def calculate_square(x: int) -> int:
    """
    Вычисляет квадрат числа.
    """
    return x ** 2

if __name__ == "__main__":
    print("=== Базовые принципы модулей ===")
    greet("Алиса")
    print(f"Квадрат числа 5: {calculate_square(5)}")

    