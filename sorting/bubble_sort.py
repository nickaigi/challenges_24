"""
Bubble Sort
- Works by repeatedly comparing adjacent elements and swapping them if not in the correct order
"""

def bubble_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        # since we are comparing each element to its next element,
        # we only need to run the loop up to the second-last element
        # this is because the last element will not have a next element
        # for comparision
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    arr = [15, 16, 6, 8, 5]
    print(f'Before sorting: {arr}')
    bubble_sort(arr)
    print(f'After sorting: {arr}')
