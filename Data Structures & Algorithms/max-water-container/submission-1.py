class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            h = min(heights[l], heights[r]) # 1
            w = r - l  # 8
            a = h * w # 8
            res = max(res, a) # 8 

            if heights[l] > heights[r]: # false
                r -= 1
            else:
                l += 1

        return res