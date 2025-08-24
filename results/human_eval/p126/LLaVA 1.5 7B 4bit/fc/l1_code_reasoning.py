from typing import List

def evaluate_list_sort_duplication(nums: List[int]) -> str:
    """
    Implements the described algorithm:
    1) Check if the input list is sorted (non-decreasing).
    2) If not sorted, sort the list in ascending order.
    3) In the (sorted) list, check for any duplicate values.
    4) If there are no duplicates -> Yes message.
       If there is at least one duplicate -> No message.
    """

    def is_sorted(seq: List[int]) -> bool:
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                return False
        return True
    if is_sorted(nums):
        current = list(nums)
    else:
        current = sorted(nums)
    has_duplicates = any((current[i] == current[i + 1] for i in range(len(current) - 1)))
    if not has_duplicates:
        return 'Yes, the list is sorted and has no more than one duplication of the same number.'
    else:
        return 'No, the list is not sorted and has duplications.'