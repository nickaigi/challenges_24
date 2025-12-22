import time
from threading import Thread


COUNT = 50_000_000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    t1 = Thread(target=countdown, args=(COUNT // 2,))
    t2 = Thread(target=countdown, args=(COUNT // 2,))

    start = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    elapsed = time.perf_counter() - start
    print(f"Time taken: {elapsed}")
