"""
Bubble Sort
============

- Works by repeatedly comparing adjacent elements and swapping them if not in the correct order

This implementation has a time complexity of O(n^2) in the worst and average cases, but it can be optimized to O(n) in the best case (when the array is already sorted).

The space complexity of Bubble Sort is O(1), which means it uses constant extra space.

- Why is the space complexity O(1)?
Bubble Sort is an in-place sorting algorithm. This means it does not require additional memory proportional to the size of the input array. The only extra space used is for a few variables (like i, j, and swapped), which do not depend on the size of the input array. All the sorting is done by swapping elements within the original array itself.

Key Points:
No additional data structures are used (e.g., no extra arrays or lists).

The algorithm only uses a constant amount of extra space for loop counters and temporary variables during swaps.

Example:
If you have an array of size n, Bubble Sort will:

Use the same array to perform swaps.

Only require a few fixed-size variables (e.g., i, j, swapped), regardless of the value of n.

Thus, the space complexity is O(1).


Applications of Bubble Sort
---------------------------
When to use bubble sort?

Use bubble sort for

1. Small datasets.
2. When simplicity is more important than efficiency.
3. When the data is already partially sorted.

When not to use bubble sort?

Avoid bubble sort for large datasets and performance-critical applications.

In such cases, sorting algorithms like merge sort or quick sort are more suitable.
"""

def bubble_sort_descending(arr):
    """Sort the list in descending order"""
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort(arr: list[int]) -> None:
    """Sort the list in ascending order"""
    for i in range(len(arr)):
        # since we are comparing each element to its next element,
        # we only need to run the loop up to the second-last element
        # this is because the last element will not have a next element
        # for comparision
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort_optimized(arr: list[int]) -> None:
    """

    Outer Loop (for i in range(n)):
        This loop runs n times, where n is the length of the array. Each iteration of this loop places the next largest element in its correct position.

    Inner Loop (for j in range(0, n-i-1)):
        This loop compares adjacent elements and swaps them if they are in the wrong order. The range decreases with each iteration of the outer loop because the largest elements are already sorted and placed at the end.

    Swapped Flag:
        This flag is used to optimize the algorithm. If no elements are swapped during a full pass through the array, the array is already sorted, and the algorithm can terminate early.

    """
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # if swapped remains False after the inner loop
        # it means that none of the elements were swapped
        # therefore, the list is already sorted, and we can exit.
        if not swapped:
            break


if __name__ == '__main__':
    arr = [15, 16, 6, 8, 5]
    print(f'Before sorting: {arr}')
    bubble_sort_optimized(arr)
    print(f'After sorting: {arr}')
