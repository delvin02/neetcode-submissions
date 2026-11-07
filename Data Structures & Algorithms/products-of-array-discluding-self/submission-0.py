class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1] * len(nums)
        left = 1
        
        for i in range(len(nums)):
            pre[i] = left
            left *= nums[i]

        post = [1] * len(nums)
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = right
            right *= nums[i]

        return [pre[i] * post[i] for i in range(len(nums))]

