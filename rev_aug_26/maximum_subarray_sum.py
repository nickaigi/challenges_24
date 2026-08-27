def maximum_subarray_sum(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


if __name__ == "__main__":
    assert maximum_subarray_sum([2, 3, -8, 7, -1, 2, 3]) == 11
    assert maximum_subarray_sum([5, 4, 1, 7, 8]) == 25
    assert maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("All Tests Passed")
