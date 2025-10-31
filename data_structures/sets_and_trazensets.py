"""
Модуль: sets_and_frozensets
--------------------------

Демонстрирует работу с множествами и неизменяемыми множествами.
"""


def demonstrate_sets() -> None:
    """
    Демонстрирует основные операции с множествами.
    """
    print("=== Множества ===")

    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    print(f"Множество 1: {set1}")
    print(f"Множество 2: {set2}")

    # Объединение
    union = set1.union(set2)
    print(f"Объединение: {union}")

    # Пересечение
    intersection = set1.intersection(set2)
    print(f"Пересечение: {intersection}")

    # Разность
    difference = set1.difference(set2)
    print(f"Разность: {difference}")


def demonstrate_frozensets() -> None:
    """
    Демонстрирует работу с неизменяемыми множествами.
    """
    print("\n=== Неизменяемые множества ===")

    frozenset1 = frozenset([1, 2, 3])
    frozenset2 = frozenset([3, 4, 5])

    print(f"Неизменяемое множество 1: {frozenset1}")
    print(f"Неизменяемое множество 2: {frozenset2}")

    # Объединение
    union = frozenset1.union(frozenset2)
    print(f"Объединение: {union}")


if __name__ == "__main__":
    demonstrate_sets()
    demonstrate_frozensets()