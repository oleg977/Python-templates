import asyncio

async def task(name):
    print(f"Асинхронная задача {name} началась.")
    await asyncio.sleep(2)
    print(f"Асинхронная задача {name} завершилась.")

async def main():
    tasks = [task(f"#{i+1}") for i in range(3)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())