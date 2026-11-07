class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_to_count = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for n, count in num_to_count.items():
            bucket[count].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) >= k:
                    return res