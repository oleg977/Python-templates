"""
Модуль: stacks_and_queues
-------------------------

Демонстрирует реализацию стеков и очередей.
"""

from collections import deque


def demonstrate_stacks() -> None:
    """
    Демонстрирует работу со стеками.
    """
    print("=== Стеки ===")

    stack = []
    stack.append("first")
    stack.append("second")
    stack.append("third")
    print(f"Стек: {stack}")

    # Удаление элемента (LIFO)
    print(f"Удален: {stack.pop()}")
    print(f"Оставшийся стек: {stack}")


def demonstrate_queues() -> None:
    """
    Демонстрирует работу с очередями.
    """
    print("\n=== Очереди ===")

    queue = deque()
    queue.append("first")
    queue.append("second")
    queue.append("third")
    print(f"Очередь: {queue}")

    # Удаление элемента (FIFO)
    print(f"Удален: {queue.popleft()}")
    print(f"Оставшаяся очередь: {queue}")


if __name__ == "__main__":
    demonstrate_stacks()
    demonstrate_queues()