"""
Модуль: sorting_algorithms
--------------------------

Демонстрирует различные алгоритмы сортировки.
"""


def bubble_sort(arr):
    """
    Сортировка пузырьком.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def quick_sort(arr):
    """
    Быстрая сортировка.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def demonstrate_sorting_algorithms() -> None:
    """
    Демонстрирует работу алгоритмов сортировки.
    """
    print("=== Алгоритмы сортировки ===")

    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Исходный массив: {array}")

    # Пузырьковая сортировка
    bubble_sort(array)
    print(f"После пузырьковой сортировки: {array}")

    # Быстрая сортировка
    array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = quick_sort(array)
    print(f"После быстрой сортировки: {sorted_array}")


if __name__ == "__main__":
    demonstrate_sorting_algorithms()