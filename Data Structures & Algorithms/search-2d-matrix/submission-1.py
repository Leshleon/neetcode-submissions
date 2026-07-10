class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        l, r = 0, rows*columns - 1

        while l <= r:
            mid = (r - l) // 2 + l
            mid_val = matrix[mid // columns][mid % columns]

            if mid_val == target:
                return True
            elif mid_val > target:
                r = mid - 1
            elif mid_val < target:
                l = mid + 1

        return False
        
        