import time
from multiprocessing import Pool


COUNT = 50_000_000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    pool = Pool(processes=2)

    start = time.perf_counter()
    r1 = pool.apply_async(countdown, [COUNT // 2])
    r2 = pool.apply_async(countdown, [COUNT // 2])

    pool.close()
    pool.join()
    elapsed = time.perf_counter() - start
    print(f"Time taken: {elapsed}")
