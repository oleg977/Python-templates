
#### Пример содержимого файлов:

##### `threading_example.py`
```python
import threading
import time

def task(name):
    print(f"Задача {name} началась.")
    time.sleep(2)
    print(f"Задача {name} завершилась.")

def demonstrate_threading():
    threads = []
    for i in range(3):
        thread = threading.Thread(target=task, args=(f"#{i+1}",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    demonstrate_threading()