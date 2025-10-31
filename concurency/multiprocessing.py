from multiprocessing import Process
import os

def task(name):
    print(f"Процесс {name} (PID: {os.getpid()}) начался.")
    time.sleep(2)
    print(f"Процесс {name} завершился.")

def demonstrate_multiprocessing():
    processes = []
    for i in range(3):
        process = Process(target=task, args=(f"#{i+1}",))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    demonstrate_multiprocessing()