"""
Модуль: recursion_examples
--------------------------

Демонстрирует примеры рекурсии.
"""


def factorial(n):
    """
    Вычисляет факториал числа.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Вычисляет n-е число Фибоначчи.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def demonstrate_recursion() -> None:
    """
    Демонстрирует работу рекурсивных функций.
    """
    print("=== Рекурсия ===")

    print(f"Факториал числа 5: {factorial(5)}")
    print(f"Число Фибоначчи под номером 7: {fibonacci(7)}")


if __name__ == "__main__":
    demonstrate_recursion()