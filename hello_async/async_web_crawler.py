"""
ASYNC == wait on many things at the same time

methods defined with async are called coroutines.
a traditional function call e.g do_work() -> does not actually run the function... it just creates the coroutine

await --> wait here until this thing is done, pausing the current task if necessary

time.sleep(1) is not a asynchronous function, replace with asyncio.sleep(1)

asyncio.create_task(task()) --> allows us to create a schedule multiple tasks before waiting on any of them

done, pending = asyncio.wait(tasks_list, timeout=2.0) --> wait on all the tasks
    if you don't specify a timeout, pending will be empty
"""
import time
import asyncio


async def do_work(s: str, delay_s: float = 1.0) -> None:
    print(f'{s} started')
    await asyncio.sleep(delay_s)  # simulate a long running task
    print(f'{s} done')


async def main():
    start = time.perf_counter()
    todo: list[str] = [
        'get package',
        'laundry',
        'bake cake',
    ]

    tasks = [asyncio.create_task(do_work(task)) for task in todo]
    done, pending = await asyncio.wait(tasks)
    for task in done:
        result = task.result()

    # using asyncio.gather
    coros = [do_work(item) for item in todo]
    results = await asyncio.gather(*coros)

    # in Python 3.11+ you can do the following
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(do_work(item)) for item in todo]


    end = time.perf_counter()
    print(f'It took: {end - start:.2f}s')


if __name__ == '__main__':
    asyncio.run(main())  # starts the event loop
