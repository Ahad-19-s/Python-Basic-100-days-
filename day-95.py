import asyncio

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay} seconds")
    return name

async def main():
    t1 = asyncio.create_task(task("A", 2))
    t2 = asyncio.create_task(task("B", 1))
    
    print("Waiting for tasks to complete...")
    
    result = await asyncio.gather(t1, t2)
    print("Results:", result)

asyncio.run(main())
