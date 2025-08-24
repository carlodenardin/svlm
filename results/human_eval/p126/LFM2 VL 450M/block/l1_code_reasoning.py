from typing import List

def verify_list_condition(nums: List[int], target: int) -> bool:
    sorted_ok = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            sorted_ok = False
            break
    duplicates = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            duplicates += 1
            if duplicates > 1:
                break
    duplicates_ok = duplicates <= 1
    contains_target = target in nums
    return sorted_ok and duplicates_ok and contains_target