"""
Модуль: basic_functions
-----------------------

Демонстрирует базовые принципы работы с функциями в Python.
"""


def demonstrate_basic_functions() -> None:
    """
    Демонстрирует создание и вызов простых функций.
    """
    print("=== Базовые функции ===")

    def greet() -> None:
        print("Привет, мир!")

    greet()


# Области видимости
def demonstrate_scopes() -> None:
    """
    Демонстрирует области видимости: локальные и глобальные переменные.
    """
    global_variable: int = 10

    def local_scope():
        local_variable: int = 5
        print(f"Локальная переменная: {local_variable}")
        print(f"Глобальная переменная внутри функции: {global_variable}")

    local_scope()
    print(f"Глобальная переменная вне функции: {global_variable}")


if __name__ == "__main__":
    demonstrate_basic_functions()
    demonstrate_scopes()

