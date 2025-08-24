def is_sorted_and_no_more_than_twice(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    for count in freq.values():
        if count > 2:
            return False
    return True