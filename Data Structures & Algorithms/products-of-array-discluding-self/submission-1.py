class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # n
        computed = [1] * len(nums)
        left = 1
        
        for i in range(len(nums)):
            computed[i] = left
            left *= nums[i]

        # n
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            computed[i] *= right
            right *= nums[i]

        return computed

