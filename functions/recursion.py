"""
Модуль: recursion
-----------------

Демонстрирует рекурсивные функции.
"""

def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def demonstrate_recursion() -> None:
    """
    Демонстрирует рекурсию.
    """
    print("=== Рекурсия ===")
    number: int = 5
    print(f"Факториал числа {number}: {factorial(number)}")

if __name__ == "__main__":
    demonstrate_recursion()

    запускаем файл
    python functions/recursion.py