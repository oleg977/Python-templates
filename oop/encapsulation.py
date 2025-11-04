"""
Модуль: encapsulation
---------------------

Демонстрирует инкапсуляцию.
"""


class BankAccount:
    """
    Класс, представляющий банковский счет.
    """

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance  # Приватный атрибут

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение: {amount}. Новый баланс: {self.__balance}")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снятие: {amount}. Новый баланс: {self.__balance}")
        else:
            print("Недостаточно средств или некорректная сумма.")


def demonstrate_encapsulation() -> None:
    """
    Демонстрирует инкапсуляцию.
    """
    print("=== Инкапсуляция ===")

    account = BankAccount("Alice", 1000)
    account.deposit(500)
    account.withdraw(200)


if __name__ == "__main__":
    demonstrate_encapsulation()

