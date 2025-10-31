"""
Модуль: common_errors
---------------------

Демонстрирует распространенные ошибки при работе с модулями.
"""


def demonstrate_common_errors() -> None:
    """
    Демонстрирует распространенные ошибки.
    """
    print("=== Распространенные ошибки ===")

    # 1. Циклический импорт
    try:
        from circular_dependency_a import func_a
        func_a()
    except ImportError as e:
        print(f"Ошибка: {e} - Циклический импорт может вызвать проблемы.")

    # 2. Неправильное имя модуля
    try:
        import non_existent_module
    except ModuleNotFoundError as e:
        print(f"Ошибка: {e} - Проверьте правильность имени модуля.")

    # 3. Импорт внутри блока if
    print("\nПример: импорт внутри блока if может привести к проблемам.")
    condition = True
    if condition:
        import math
        print(f"Квадратный корень из 25: {math.sqrt(25)}")


if __name__ == "__main__":
    demonstrate_common_errors()

