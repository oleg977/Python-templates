"""
Модуль: linked_lists
--------------------

Демонстрирует реализацию и работу со связанными списками.
"""


# Узел связанного списка
class Node:
    """
    Класс, представляющий узел связанного списка.
    """

    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Ссылка на следующий узел


class LinkedList:
    """
    Класс, представляющий связанный список.
    """

    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data) -> None:
        """
        Добавляет новый узел в конец связанного списка.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data) -> None:
        """
        Добавляет новый узел в начало связанного списка.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data) -> None:
        """
        Удаляет первый узел с указанным значением.
        """
        if not self.head:
            print("Список пуст.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f"Узел с данными {data} не найден.")

    def find(self, data) -> bool:
        """
        Ищет узел с указанным значением.
        Возвращает True, если узел найден, иначе False.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self) -> None:
        """
        Выводит все элементы связанного списка.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


def demonstrate_linked_lists() -> None:
    """
    Демонстрирует работу со связанными списками.
    """
    print("=== Связанные списки ===")

    # Создание связанного списка
    linked_list = LinkedList()

    # Добавление элементов
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(5)
    print("Список после добавления элементов:")
    linked_list.display()

    # Поиск элемента
    print("\nПоиск элемента:")
    print(f"Найден ли элемент 20? {linked_list.find(20)}")
    print(f"Найден ли элемент 40? {linked_list.find(40)}")

    # Удаление элемента
    print("\nУдаление элемента:")
    linked_list.delete_with_value(20)
    print("Список после удаления элемента 20:")
    linked_list.display()


if __name__ == "__main__":
    demonstrate_linked_lists()