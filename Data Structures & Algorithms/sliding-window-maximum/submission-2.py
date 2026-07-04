import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = []
        heapq.heapify(window)
        output =  []

        for r in range(len(nums)):
            heapq.heappush(window, (-nums[r], r))
            if r >= k-1:
                while window[0][1] <= r - k:
                    heapq.heappop(window)
                output.append(window[0][0] * -1)            
        
        return output



            



        