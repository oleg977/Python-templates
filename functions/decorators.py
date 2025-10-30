"""
Модуль: decorators
------------------

Демонстрирует использование декораторов.
"""
from basics import functions


def my_decorator(func):
    """
    Простой декоратор.
    """
    def wrapper():
        print("До выполнения функции.")
        func()
        print("После выполнения функции.")
    return wrapper

@my_decorator
def say_hello():
    """
    Функция, которая выводит "Привет!".
    """
    print("Привет!")

if __name__ == "__main__":
    say_hello()

    запускаем файл
    python functions/decorators.py