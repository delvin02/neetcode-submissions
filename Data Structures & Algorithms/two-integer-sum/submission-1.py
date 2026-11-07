class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_index = {}

        for index, num in enumerate(nums):
            if num in diff_to_index:
                return [diff_to_index[num], index]
            else:
                diff = target - num
                diff_to_index[diff] = index