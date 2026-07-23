import datetime
import asyncio


def print_now():
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        try:
            await asyncio.sleep(0.50)
        except asyncio.CancelledError:
            print(name, "was cancelled")
            break


async def print3times():
    for _ in range(3):
        print_now()
        await asyncio.sleep(0.1)


async def async_main_error_handling() -> None:
    try:
        await asyncio.wait_for(keep_printing("Hey"), 10)
    except asyncio.TimeoutError:
        print("Oops, time's up")


async def async_main() -> None:
    try:
        await asyncio.wait_for(
            asyncio.gather(
                keep_printing("First"),
                keep_printing("Second"),
                keep_printing("Third"),
            ),
            5,
        )
    except asyncio.TimeoutError:
        print("Oops, time's up")


if __name__ == "__main__":
    asyncio.run(async_main())
    # print("Ready!")
