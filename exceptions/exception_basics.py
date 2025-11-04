"""
Модуль: exception_basics
------------------------

Демонстрирует основы работы с исключениями.
"""


def demonstrate_exception_basics() -> None:
    """
    Демонстрирует использование try-except для обработки исключений.
    """
    print("=== Основы работы с исключениями ===")

    try:
        result = 10 / 0  # Попытка деления на ноль
    except ZeroDivisionError as e:
        print(f"Ошибка: {e} - Нельзя делить на ноль.")

    try:
        value = int("not_a_number")  # Попытка преобразования строки в число
    except ValueError as e:
        print(f"Ошибка: {e} - Строка не является числом.")


if __name__ == "__main__":
    demonstrate_exception_basics()