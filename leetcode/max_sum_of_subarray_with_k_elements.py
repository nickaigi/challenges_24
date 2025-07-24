from typing import List


def solution(arr: List[int], k: int) -> int:
    n = len(arr)

    if n <= k:
        print('Invalid')
        return -1
    window_sum = sum(arr[:k])

    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum


if __name__ == '__main__':
    arr = [100, 200, 300, 400]
    k = 2
    print(solution(arr=arr, k=k))
