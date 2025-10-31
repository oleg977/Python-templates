"""
Модуль: working_with_paths
--------------------------

Демонстрирует работу с путями к файлам.
"""

import os
from pathlib import Path


def demonstrate_working_with_paths() -> None:
    """
    Демонстрирует работу с путями к файлам.
    """
    print("=== Работа с путями ===")

    # Использование os.path
    current_directory = os.getcwd()
    print(f"Текущая директория: {current_directory}")

    file_path = os.path.join(current_directory, "example.txt")
    print(f"Путь к файлу: {file_path}")

    if os.path.exists(file_path):
        print("Файл существует.")
    else:
        print("Файл не существует.")

    # Использование pathlib
    path = Path("example.txt")
    if path.exists():
        print("Pathlib: Файл существует.")
    else:
        print("Pathlib: Файл не существует.")


if __name__ == "__main__":
    demonstrate_working_with_paths()

