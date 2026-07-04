class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        window_max = nums[0]
        output = []
        for r in range(k - 1, len(nums)):
            window_max = nums[l]
            for num in nums[l:r+1]:
                window_max = max(window_max, num)
            output.append(window_max)
            l+=1
        
        return output


        