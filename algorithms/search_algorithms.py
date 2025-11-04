"""
Модуль: search_algorithms
-------------------------

Демонстрирует алгоритмы поиска.
"""


def linear_search(arr, target):
    """
    Линейный поиск.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Бинарный поиск (работает только на отсортированном массиве).
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def demonstrate_search_algorithms() -> None:
    """
    Демонстрирует работу алгоритмов поиска.
    """
    print("=== Алгоритмы поиска ===")

    array = [11, 12, 22, 25, 34, 64, 90]
    target = 25

    # Линейный поиск
    index = linear_search(array, target)
    print(f"Линейный поиск: элемент {target} найден на позиции {index}.")

    # Бинарный поиск
    index = binary_search(array, target)
    print(f"Бинарный поиск: элемент {target} найден на позиции {index}.")


if __name__ == "__main__":
    demonstrate_search_algorithms()