def build_prefix_sum(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [0] * n

    prefix[0] = nums[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]

    return prefix


if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    prefix_sums = build_prefix_sum(arr)

    for i in prefix_sums:
        print(i, end=" ")
