"""
Модуль: handling_exceptions
---------------------------

Демонстрирует обработку исключений при работе с файлами.
"""


def demonstrate_exception_handling() -> None:
    """
    Демонстрирует обработку исключений.
    """
    print("=== Обработка исключений ===")

    # Попытка открыть несуществующий файл
    try:
        with open("non_existent_file.txt", "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Ошибка: {e} - Файл не найден.")

    # Попытка записи в файл без прав доступа
    try:
        with open("/root/restricted.txt", "w", encoding="utf-8") as file:
            file.write("Тестовая запись.")
    except PermissionError as e:
        print(f"Ошибка: {e} - Нет прав доступа.")

    # Общая обработка ошибок
    try:
        file = open("example.txt", "r", encoding="utf-8")
        print(file.read())
        file.close()
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    demonstrate_exception_handling()

