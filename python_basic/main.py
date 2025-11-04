# Базовый шаблон Python-программы

import logging

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("Программа запущена")
    print("Hello, Python!")


if __name__ == "__main__":
    main()
