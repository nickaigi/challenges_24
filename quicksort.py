"""
Divide and Conquer
1. Pick a pivot
2. Partition the array into two sub-arrays:
    - elements <= pivot
    - elements > pivot
3. Call quicksort recursively on the two sub-arrays
"""


def quicksort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    arr = [10, 5, 2, 3]
    print(f"arr={arr} and quicksort returns {quicksort([10, 5, 2, 3])}")
