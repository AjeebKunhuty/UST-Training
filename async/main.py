import asyncio
import time

async def async_sleep(i):
    print("Before sleep", i)
    for n in range(i):
        yield n
        await asyncio.sleep(n)
    print("After sleep", i)

async def print_hello():
    print("Hello")

async def main():
    start = time.time()
    # task = asyncio.create_task(async_sleep(1))
    # task2 = asyncio.create_task(print_hello())
    # await async_sleep(2) 
    # await print_hello() # Control given to next if current statement is a task
    # await task
    # try:
    #     await asyncio.gather(asyncio.wait_for(async_sleep(30), 5), async_sleep(6), print_hello()) # Run concurrently
    # except asyncio.TimeoutError:
    #     print("Timeout")
    # await task2
    async for k in async_sleep(5):
        print(k)
    
    print("Total time: ", time.time() - start)

if __name__ == '__main__':
    asyncio.run(main())