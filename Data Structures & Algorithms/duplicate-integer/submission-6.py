class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = defaultdict(int)
        for n in nums:
            nums_dict[n] += 1
        return any(x > 1 for x in nums_dict.values())
        