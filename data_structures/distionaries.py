"""
Модуль: dictionaries
--------------------

Демонстрирует работу со словарями.
"""


def demonstrate_dictionaries() -> None:
    """
    Демонстрирует основные операции со словарями.
    """
    print("=== Словари ===")

    student = {
        "name": "Alice",
        "age": 25,
        "courses": ["Math", "Physics"]
    }
    print(f"Исходный словарь: {student}")

    # Добавление нового ключа
    student["major"] = "Computer Science"
    print(f"После добавления ключа: {student}")

    # Итерация по ключам и значениям
    print("\nИтерация по ключам и значениям:")
    for key, value in student.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    demonstrate_dictionaries()