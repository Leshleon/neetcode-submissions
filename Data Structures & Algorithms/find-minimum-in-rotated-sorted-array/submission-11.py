class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        max_flag, min_flag = nums[l], nums[r]

        if max_flag < min_flag:
            return max_flag

        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] >= max_flag:
                l = mid + 1
            else:
                min_flag = nums[mid]
                r = mid - 1
                
    
        return min_flag