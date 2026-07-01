class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums_len = len(nums)
        heapq.heapify(nums)

        previous = None
        max_seq = 0
        for i in range(0, nums_len):
            current = heapq.heappop(nums)
            if previous == None:
                previous = current
                running = max_seq = 1
                continue
            if previous == current - 1:
                running += 1
                previous = current
            else:
                previous = current
                running = 1
            if running > max_seq:
                    max_seq = running
        
        return max_seq
            


        