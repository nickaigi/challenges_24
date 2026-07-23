import time
import asyncio
from typing import Callable, Coroutine
import httpx


addr = "https://langa.pl/crawl/"
todo = set()


async def crawl0(prefix: str, url: str = "") -> None:
    url = url or prefix
    print(f"Crawling {url}")
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
    for line in res.text.splitlines():
        if line.startswith(prefix):
            await crawl0(prefix, line)


async def progress_old(url: str, algo: Callable[..., Coroutine]) -> None:
    asyncio.create_task(algo(url), name=url)
    todo.add(url)
    start = time.perf_counter()
    while len(todo):
        print(f"{len(todo)}: " + ", ".join(sorted(todo))[-38:])
        await asyncio.sleep(0.5)
    end = time.perf_counter()
    print(f"Took {int(end - start)} seconds")


async def progress(url: str, algo: Callable[..., Coroutine]) -> None:
    task = asyncio.create_task(algo(url), name=url)
    todo.add(task)
    start = time.perf_counter()
    while len(todo):
        done, _pending = await asyncio.wait(todo, timeout=0.5)
        todo.difference_update(done)
        urls = (t.get_name() for t in todo)
        print(f"{len(todo)}: " + ", ".join(sorted(urls))[-75:])
    end = time.perf_counter()
    print(f"Took {int(end - start)} seconds")


async def crawl1(prefix: str, url: str = "") -> None:
    url = url or prefix
    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    for line in res.text.splitlines():
        if line.startswith(prefix):
            todo.add(line)
            await crawl1(prefix, line)
    todo.discard(url)


async def crawl2(prefix: str, url: str = "") -> None:
    url = url or prefix
    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    for line in res.text.splitlines():
        if line.startswith(prefix):
            task = asyncio.create_task(
                crawl2(prefix, line),
                name=line,
            )
            todo.add(task)


async def async_main() -> None:
    try:
        await progress(addr, crawl2)
    except asyncio.CancelledError:
        for task in todo:
            task.cancel()
        done, pending = await asyncio.wait(todo, timeout=1.0)
        todo.difference_update(done)
        todo.difference_update(pending)
        if todo:
            print("Warning: more tasks added while we were cancelling")


if __name__ == "__main__":
    # asyncio.run(progress(addr, crawl2))
    print("Ready!")
