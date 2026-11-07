class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        longest_streak = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                current_num = num
                streak = 1
                while current_num + 1 in set_nums:
                    current_num += 1
                    streak += 1

                longest_streak = max(streak, longest_streak)


        return longest_streak