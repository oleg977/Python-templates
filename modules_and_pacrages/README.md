# Modules

This directory contains examples and explanations of working with modules in Python:

## Files

- **module_basics.py**: Introduction to modules and their usage.
- **importing_modules.py**: Different ways to import modules and libraries.
- **creating_packages.py**: Creating and using packages.
- **common_errors.py**: Common mistakes when working with modules and how to avoid them.

## Usage

Run individual files using:
```bash
python modules/module_basics.py

---

### Как добавить пакет для примера?

Чтобы продемонстрировать работу с пакетами, создайте следующую структуру:

#### `my_package/module1.py`:
```python
def greet(name: str) -> None:
    print(f"Привет, {name}!")
def calculate_square(x: int) -> int:
    return x ** 2