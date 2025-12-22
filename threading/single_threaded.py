import time

COUNT = 50_000_000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    start = time.perf_counter()
    countdown(COUNT)
    elapsed = time.perf_counter() - start

    print(f"Time taken in seconds: {elapsed}")
