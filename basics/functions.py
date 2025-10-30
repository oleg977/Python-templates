"""
Модуль: functions
-----------------

Данный модуль демонстрирует работу с функциями в Python:
определение функций, параметры, возвращаемые значения и лямбда-функции.
Также включает примеры распространенных ошибок при работе с функциями.
"""


# === Раздел 1: Определение и вызов функций ===

def demonstrate_function_basics() -> None:
    """
    Демонстрирует базовые принципы работы с функциями.

    Функции позволяют организовать код в повторно используемые блоки.
    """
    print("=== Определение и вызов функций ===")

    # Простая функция без параметров
    def greet() -> None:
        print("Привет, мир!")

    # Вызов функции
    greet()


# === Раздел 2: Параметры и возвращаемые значения ===

def demonstrate_parameters_and_returns() -> None:
    """
    Демонстрирует использование параметров и возвращаемых значений.

    Функции могут принимать параметры и возвращать значения.
    """
    print("\n=== Параметры и возвращаемые значения ===")

    # Функция с параметрами
    def add_numbers(a: int, b: int) -> int:
        return a + b

    # Вызов функции с аргументами
    result: int = add_numbers(5, 7)
    print(f"Результат сложения: {result}")

    # Функция с параметром по умолчанию
    def greet_user(name: str = "Гость") -> str:
        return f"Привет, {name}!"

    # Вызов функции с параметром и без
    print(greet_user("Алиса"))
    print(greet_user())


# === Раздел 3: Лямбда-функции ===

def demonstrate_lambda_functions() -> None:
    """
    Демонстрирует использование лямбда-функций.

    Лямбда-функции - это анонимные функции для коротких операций.
    """
    print("\n=== Лямбда-функции ===")

    # Пример лямбда-функции
    square = lambda x: x ** 2
    print(f"Квадрат числа 5: {square(5)}")

    # Использование лямбда-функции с sorted
    numbers: list[int] = [3, 1, 4, 2]
    sorted_numbers = sorted(numbers, key=lambda x: -x)  # Сортировка по убыванию
    print(f"Отсортированные числа: {sorted_numbers}")


# === Раздел 4: Лучшие практики ===

def demonstrate_best_practices() -> None:
    """
    Демонстрирует лучшие практики работы с функциями.

    Включает использование осмысленных имен функций, аннотации типов и т.д.
    """
    print("\n=== Лучшие практики ===")

    # Осмысленные имена функций
    def calculate_average(scores: list[float]) -> float:
        return sum(scores) / len(scores)

    scores: list[float] = [85.0, 90.0, 78.0]
    average: float = calculate_average(scores)
    print(f"Средний балл: {average:.2f}")

    # Аннотации типов
    def multiply(a: float, b: float) -> float:
        return a * b

    print(f"Произведение 3.5 и 2: {multiply(3.5, 2)}")


# === Раздел 5: Распространенные ошибки ===

def demonstrate_common_errors() -> None:
    """
    Демонстрирует распространенные ошибки при работе с функциями.

    Включает ошибки: пропущенный return, некорректное использование параметров,
    работа с изменяемыми объектами по умолчанию и т.д.
    """
    print("\n=== Распространенные ошибки ===")

    # 1. Пропущенный return
    print("\nПример: пропущенный return может привести к возврату None.")

    def forgot_return(x: int) -> int:
        x += 1  # Забыли вернуть значение

    print(f"Результат: {forgot_return(5)} (Ожидается None)")

    # 2. Некорректное использование параметров
    try:
        print("\nПример: передача неправильного количества аргументов.")

        def subtract(a: int, b: int) -> int:
            return a - b

        print(subtract(10))  # Недостаточно аргументов
    except TypeError as e:
        print(f"Ошибка: {e} - Передано недостаточно аргументов.")

    # 3. Работа с изменяемыми объектами по умолчанию
    print("\nПример: изменяемый объект по умолчанию может привести к неожиданному поведению.")

    def append_to_list(value: int, lst: list[int] = []) -> list[int]:
        lst.append(value)
        return lst

    print(append_to_list(1))  # [1]
    print(append_to_list(2))  # [1, 2] - Ошибка: список сохраняет состояние между вызовами


if __name__ == "__main__":
    """
    Точка входа в модуль.

    Выполняет все демонстрационные функции при запуске скрипта напрямую.
    """
    demonstrate_function_basics()
    demonstrate_parameters_and_returns()
    demonstrate_lambda_functions()
    demonstrate_best_practices()
    demonstrate_common_errors()

    запускаем файл
    python basics/functions.py