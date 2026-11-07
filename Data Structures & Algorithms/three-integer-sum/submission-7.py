class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        print(nums)
        for i, n in enumerate(nums):
            # skip duplicates
            if i > 0 and n == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = nums[l] + nums[r] + n
                if threeSum == 0:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1 
        return res