class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        output = []

        for anchor in range(len(new_nums) - 2):
            target = -new_nums[anchor]
            left = anchor + 1
            right = len(new_nums) - 1

            if new_nums[anchor] > 0:
                break
            
            if anchor > 0 and new_nums[anchor] == new_nums[anchor - 1]:
                continue
            
            while left < right:
                if left > anchor + 1 and new_nums[left] == new_nums[left - 1]:
                    left += 1
                    continue 

                if new_nums[left] + new_nums[right] < target:
                    left += 1
                elif new_nums[left] + new_nums[right] > target:
                    right -= 1
                else:
                    output.append([new_nums[anchor], new_nums[left], new_nums[right]])
                    left += 1

        return output