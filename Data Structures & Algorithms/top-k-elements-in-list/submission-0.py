class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        mapped = {}
        
        for num in nums:
            mapped[num] = mapped.get(num, 0) + 1
        
        for num, freq in mapped.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res



        