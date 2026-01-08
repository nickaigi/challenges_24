# Given an array of positive integers arr[], return the second largest element from the array.
# If the second largest element doesn't exist then return -1.
# Note: The second largest element should not be equal to the largest element.


def getSecondLargest(arr: list[int]) -> int:
    largest, second_largest = -1, -1
    n = len(arr)
    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
    return second_largest


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
