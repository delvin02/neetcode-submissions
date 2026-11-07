import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # todo, uise quick select method

        count = Counter(nums)
        unique_nums = list(count.keys())
        n = len(unique_nums)

        def partition(left, right, pivot_index):
            pivot_freq = count[unique_nums[pivot_index]]
            # unique_nums[pivot_index], unique_nums[right] = unique_nums[right], unique_nums[pivot_index]

            store = left
            for i in range(left, right):
                if count[unique_nums[i]] < pivot_freq:
                    unique_nums[store], unique_nums[i] = unique_nums[i], unique_nums[store]
                    store += 1
            unique_nums[right], unique_nums[store] = unique_nums[store], unique_nums[right]
            return store

        def quickselect(left, right, target):
            if left >= right:
                return

            # pivot_index = random.randint(left, right)
            p = partition(left,right, right)
            if p == target:
                return
            elif p > target:
                quickselect(left, p - 1, target)
            else:
                quickselect(p + 1, right, target)
            
        quickselect(0, n - 1, n - k)
        return unique_nums[n-k:]
