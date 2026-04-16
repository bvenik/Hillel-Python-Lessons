import asyncio
import random


async def cook(name, queue):
    while True:
        order = await queue.get()
        print(f"Кухар {name} розпочав готувати {order}...")
        cook_time = random.uniform(2, 5)
        await asyncio.sleep(cook_time)
        f" Кухар {name} видав {order} за {cook_time:.2f}с."
        queue.task_done()


async def cashier(name, queue, orders_count):
    for i in range(1, orders_count + 1):
        order_name = f"Замовлення #{i} від Касира {name}"
        await queue.put(order_name)
        print(f"Замовлення #{i} від Касира {name}")
        await asyncio.sleep(random.uniform(0.5, 1.5))


async def main():
    kitchen_queue = asyncio.Queue()
    cooks = [
        asyncio.create_task(cook('Michael', kitchen_queue)),
        asyncio.create_task(cook('Max', kitchen_queue)),
        asyncio.create_task(cook('Mark', kitchen_queue))
    ]
    cashiers = [
        asyncio.create_task(cashier('Marina', kitchen_queue, 5)),
        asyncio.create_task(cashier('Milana', kitchen_queue, 5)),
    ]
    await asyncio.gather(*cashiers)
    await kitchen_queue.join()
    for c in cooks:
        c.cancel()
    print("\n Всі замовлення видані! Ресторан зачиняється.")

if __name__ == '__main__':
    asyncio.run(main())
