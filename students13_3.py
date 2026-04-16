import asyncio


def microtask_callback(task_id):
    print(f"[Мікрозадача] Стікер: Видати чек для {task_id}")


async def macrotask_callback(task_id):
    print(f"[Макрозадача] Початок обробки: {task_id}")
    loop = asyncio.get_event_loop()
    loop.call_soon(microtask_callback, task_id)
    print(f"[Макрозадача] Завершено: {task_id}")


async def main():
    print("Ресторан відчиняється!\n")
    task1 = asyncio.create_task(macrotask_callback("Замовлення №1"))
    task2 = asyncio.create_task(macrotask_callback("Замовлення №2"))
    task3 = asyncio.create_task(macrotask_callback("Замовлення №3"))
    await asyncio.gather(task1, task2, task3)
    print("\nВсі справи зроблено.")


if __name__ == '__main__':
    asyncio.run(main())
