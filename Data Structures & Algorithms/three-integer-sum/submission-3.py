class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums) - 1
        nums.sort()
        target = 0
        res = []
        for index, num in enumerate(nums):
            if index > 0 and nums[index-1] == num:
                continue

            left, right = index + 1, n
            while left < right:
                cur_sum = nums[left] + nums[right] + num
                if cur_sum == target:
                    res.append([nums[left], nums[right], num])
                    
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif cur_sum > target:
                    right -= 1
                else:
                    left += 1
        return res