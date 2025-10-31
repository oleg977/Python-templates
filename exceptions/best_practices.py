"""
Модуль: handling_errors
-----------------------

Демонстрирует различные способы обработки ошибок.
"""


def demonstrate_handling_errors() -> None:
    """
    Демонстрирует обработку нескольких типов исключений.
    """
    print("=== Обработка ошибок ===")

    try:
        # Попытка выполнить несколько операций
        print(10 / 0)  # Деление на ноль
        print(int("abc"))  # Преобразование строки в число
    except ZeroDivisionError as e:
        print(f"Ошибка деления: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        print("Блок finally выполняется всегда.")


if __name__ == "__main__":
    demonstrate_handling_errors()