"""
Модуль: custom_exceptions
-------------------------

Демонстрирует создание и использование собственных исключений.
"""


# Создание собственного исключения
class NegativeNumberError(Exception):
    """
    Исключение, возникающее при работе с отрицательными числами.
    """

    def __init__(self, message: str = "Число не может быть отрицательным"):
        self.message = message
        super().__init__(self.message)


def check_positive_number(value: int) -> None:
    """
    Проверяет, является ли число положительным.
    Если число отрицательное, вызывает собственное исключение.
    """
    if value < 0:
        raise NegativeNumberError()


def demonstrate_custom_exceptions() -> None:
    """
    Демонстрирует использование собственных исключений.
    """
    print("=== Собственные исключения ===")

    try:
        check_positive_number(-5)
    except NegativeNumberError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    demonstrate_custom_exceptions()