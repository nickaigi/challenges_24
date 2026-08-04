import asyncio
from typing import Awaitable


async def demo1() -> None:
    fut = asyncio.Future()
    assert not fut.done()
    assert not fut.cancelled()
    fut.set_result("result is set!")
    assert fut.done()
    assert fut.result() == "result is set!"


async def get_result(awaitable: Awaitable) -> str:
    try:
        result = await awaitable
    except Exception as e:
        print("Oops", e)
        return "no result :("
    else:
        return result


async def demo2() -> None:
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    loop.call_later(10, fut.set_result, "this is my result")
    res = await get_result(fut)
    print(res)


def gen():
    counter = 0
    while counter < 10:
        yield counter
        counter += 1


def demo3():
    g = gen()
    # print("g.gi_running: ", g.gi_running)  # False
    # print("g.gi_frame.f_locals", g.gi_frame.f_locals)  # {}
    print("next(g): ", next(g))  # 0
    # print("g.gi_running: ", g.gi_running)  # True
    print("next(g): ", next(g))  # 1
    print("next(g): ", next(g))  # 2
    print("next(g): ", next(g))  # 3
    print("next(g): ", next(g))  # 4
    print("next(g): ", next(g))  # 5
    print("next(g): ", next(g))  # 6
    print("next(g): ", next(g))  # 7
    print("next(g): ", next(g))  # 8
    print("next(g): ", next(g))  # 9
    # print("g.gi_running: ", g.gi_running)  # True


async def example(count: int) -> str:
    await asyncio.sleep(0)
    if count == 0:
        return "result"
    for i in range(count):
        await asyncio.sleep(i)
    return await example(count - 1)


if __name__ == "__main__":
    pass
