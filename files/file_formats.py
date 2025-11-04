"""
Модуль: file_operations
-----------------------

Демонстрирует основные операции с файлами: чтение и запись.
"""


def demonstrate_file_operations() -> None:
    """
    Демонстрирует чтение и запись файлов.
    """
    print("=== Операции с файлами ===")

    # Запись в файл
    with open("example.txt", "w", encoding="utf-8") as file:
        file.write("Привет, это тестовый файл!\n")
        file.write("Это вторая строка.\n")

    # Чтение из файла
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)


if __name__ == "__main__":
    demonstrate_file_operations()


