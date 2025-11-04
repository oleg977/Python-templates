"""
Модуль: file_formats
--------------------

Демонстрирует работу с различными форматами файлов: JSON, CSV.
"""

import json
import csv


def demonstrate_json_operations() -> None:
    """
    Демонстрирует работу с JSON-файлами.
    """
    print("=== Работа с JSON ===")

    # Запись данных в JSON
    data = {"name": "Alice", "age": 25, "city": "New York"}
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("Данные записаны в JSON.")

    # Чтение данных из JSON
    with open("data.json", "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        print("Данные из JSON:")
        print(loaded_data)


def demonstrate_csv_operations() -> None:
    """
    Демонстрирует работу с CSV-файлами.
    """
    print("\n=== Работа с CSV ===")

    # Запись данных в CSV
    rows = [["Name", "Age", "City"], ["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"]]
    with open("data.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Данные записаны в CSV.")

    # Чтение данных из CSV
    with open("data.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        print("Данные из CSV:")
        for row in reader:
            print(row)


if __name__ == "__main__":
    demonstrate_json_operations()
    demonstrate_csv_operations()