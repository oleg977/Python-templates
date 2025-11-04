"""
Модуль: lists_and_tuples
------------------------

Демонстрирует работу со списками и кортежами.
"""


def demonstrate_lists() -> None:
    """
    Демонстрирует основные операции со списками.
    """
    print("=== Списки ===")

    fruits = ["apple", "banana", "cherry"]
    print(f"Исходный список: {fruits}")

    # Добавление элемента
    fruits.append("orange")
    print(f"После добавления: {fruits}")

    # Удаление элемента
    fruits.remove("banana")
    print(f"После удаления: {fruits}")

    # Сортировка
    fruits.sort()
    print(f"После сортировки: {fruits}")


def demonstrate_tuples() -> None:
    """
    Демонстрирует основные операции с кортежами.
    """
    print("\n=== Кортежи ===")

    coordinates = (10, 20)
    print(f"Кортеж координат: {coordinates}")

    # Доступ к элементам
    print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

    # Попытка изменения (вызовет ошибку)
    try:
        coordinates[0] = 15
    except TypeError as e:
        print(f"Ошибка: {e} - Кортежи неизменяемы.")


if __name__ == "__main__":
    demonstrate_lists()
    demonstrate_tuples()