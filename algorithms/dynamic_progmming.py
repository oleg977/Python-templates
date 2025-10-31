"""
Модуль: dynamic_programming
---------------------------

Демонстрирует задачи динамического программирования.
"""


def fibonacci_dp(n):
    """
    Вычисляет n-е число Фибоначчи с использованием динамического программирования.
    """
    fib_table = [0, 1]
    for i in range(2, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])
    return fib_table[n]


def knapsack(weights, values, capacity):
    """
    Задача о рюкзаке (Knapsack Problem) с использованием динамического программирования.
    """
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def demonstrate_dynamic_programming() -> None:
    """
    Демонстрирует задачи динамического программирования.
    """
    print("=== Динамическое программирование ===")

    print(f"Число Фибоначчи под номером 7: {fibonacci_dp(7)}")

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print(f"Максимальная стоимость рюкзака: {knapsack(weights, values, capacity)}")


if __name__ == "__main__":
    demonstrate_dynamic_programming()