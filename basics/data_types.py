"""
Модуль: data_types
-----------------------

Данный модуль демонстрирует работу с основными структурами данных в Python:
списки (lists), кортежи (tuples), множества (sets) и словари (dictionaries).
Также включает примеры распространенных ошибок при работе с этими структурами.
"""


# === Раздел 1: Списки (Lists) ===

def demonstrate_lists() -> None:
    """
    Демонстрирует работу со списками.

    Списки - это упорядоченные, изменяемые коллекции элементов.
    """
    print("=== Списки (Lists) ===")

    # Создание списка
    fruits: list[str] = ["apple", "banana", "cherry"]
    print(f"Исходный список: {fruits}")

    # Добавление элемента
    fruits.append("orange")
    print(f"После добавления элемента: {fruits}")

    # Удаление элемента
    fruits.remove("banana")
    print(f"После удаления элемента: {fruits}")

    # Доступ по индексу
    print(f"Первый элемент: {fruits[0]}")
    print(f"Последний элемент: {fruits[-1]}")


# === Раздел 2: Кортежи (Tuples) ===

def demonstrate_tuples() -> None:
    """
    Демонстрирует работу с кортежами.

    Кортежи - это упорядоченные, неизменяемые коллекции элементов.
    """
    print("\n=== Кортежи (Tuples) ===")

    # Создание кортежа
    coordinates: tuple[float, float] = (10.0, 20.0)
    print(f"Кортеж координат: {coordinates}")

    # Доступ по индексу
    print(f"X-координата: {coordinates[0]}")
    print(f"Y-координата: {coordinates[1]}")

    # Попытка изменения кортежа (вызовет ошибку)
    print("Кортежи неизменяемы, их нельзя изменять после создания.")


# === Раздел 3: Множества (Sets) ===

def demonstrate_sets() -> None:
    """
    Демонстрирует работу с множествами.

    Множества - это неупорядоченные коллекции уникальных элементов.
    """
    print("\n=== Множества (Sets) ===")

    # Создание множества
    unique_numbers: set[int] = {1, 2, 3, 3}
    print(f"Множество: {unique_numbers} (дубликаты автоматически удаляются)")

    # Добавление элемента
    unique_numbers.add(4)
    print(f"После добавления элемента: {unique_numbers}")

    # Удаление элемента
    unique_numbers.remove(2)
    print(f"После удаления элемента: {unique_numbers}")


# === Раздел 4: Словари (Dictionaries) ===

def demonstrate_dictionaries() -> None:
    """
    Демонстрирует работу со словарями.

    Словари - это коллекции пар ключ-значение.
    """
    print("\n=== Словари (Dictionaries) ===")

    # Создание словаря
    student_info: dict[str, str] = {
        "name": "Alice",
        "major": "Computer Science"
    }
    print(f"Исходный словарь: {student_info}")

    # Добавление новой пары ключ-значение
    student_info["age"] = 21
    print(f"После добавления нового ключа: {student_info}")

    # Обновление значения
    student_info["major"] = "Data Science"
    print(f"После обновления значения: {student_info}")

    # Доступ по ключу
    print(f"Имя студента: {student_info['name']}")


# === Раздел 5: Распространенные ошибки ===

def demonstrate_common_errors() -> None:
    """
    Демонстрирует распространенные ошибки при работе со структурами данных.

    Включает ошибки: выход за границы списка, изменение неизменяемых объектов,
    работа с несуществующими ключами словаря и т.д.
    """
    print("\n=== Распространенные ошибки ===")

    # 1. Выход за границы списка
    try:
        fruits: list[str] = ["apple", "banana", "cherry"]
        print(fruits[3])  # Индекс 3 выходит за границы списка
    except IndexError as e:
        print(f"Ошибка: {e} - Индекс выходит за границы списка.")

    # 2. Попытка изменить кортеж
    try:
        coordinates: tuple[float, float] = (10.0, 20.0)
        coordinates[0] = 15.0  # Кортежи неизменяемы
    except TypeError as e:
        print(f"Ошибка: {e} - Кортежи нельзя изменять.")

    # 3. Работа с несуществующими ключами словаря
    try:
        student_info: dict[str, str] = {"name": "Alice"}
        print(student_info["age"])  # Ключ 'age' не существует
    except KeyError as e:
        print(f"Ошибка: {e} - Ключ отсутствует в словаре.")

    # 4. Добавление некорректного типа данных в множество
    try:
        unique_numbers: set[int] = {1, 2, 3}
        unique_numbers.add([4, 5])  # Нельзя добавлять изменяемые типы в множество
    except TypeError as e:
        print(f"Ошибка: {e} - В множество можно добавлять только неизменяемые типы данных.")


if __name__ == "__main__":
    """
    Точка входа в модуль.

    Выполняет все демонстрационные функции при запуске скрипта напрямую.
    """
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_sets()
    demonstrate_dictionaries()
    demonstrate_common_errors()

    запускаем файл
    python basics / data_types.py