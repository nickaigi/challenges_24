"""
Move all zeros to the end of an array while maintaining the order of the other elements. Given an array of integers, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Constraints
- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.

For example, given the input array [0, 1, 0, 3, 12], after calling your function, the array should be [1, 3, 12, 0, 0].


Soln: Modify BubbleSort
"""

from typing import List


def moveZerosToEnd(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] == 0 and arr[j + 1] != 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr

if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    print(f'Before: {arr}')
    print(f'After: {moveZerosToEnd([0, 1, 0, 3, 12])}')
