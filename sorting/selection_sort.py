"""
Selection sort.
This algorithm sorts the list in ascending order by repeatedly finding the minimum element from the unsorted part and putting it at the beginning.
Its time complexity is O(n^2).


Selection Sort-Specific Tips
1. Inefficient for Large Data Sets:

-Selection Sort has a time complexity of O(n^2), making it unsuitable for large datasets.
-Consider more efficient algorithms like Merge Sort O(nlogn)) or Quick Sort O(nlogn) on average) for larger data.

2. In-Place Sorting:

- Selection Sort doesn’t require extra memory since it sorts the array in place. Use it if memory is a constraint, but performance isn’t critical.

3. Stable vs Unstable Sorting:

- The standard implementation of Selection Sort is unstable.
For example, if the list contains duplicate elements, their order may change.
If stability is required, consider alternative algorithms or modify the swap logic.

4. Adaptive Use Cases:

Selection Sort is good when memory writes are expensive since it performs fewer swaps (n−1 swaps in total).
This can be useful in embedded systems or when sorting hardware constraints exist.
"""

def selection_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # swap in place

if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(f'Before Sorting: {arr}')
    selection_sort(arr)
    print(f'After Sorting: {arr}')
