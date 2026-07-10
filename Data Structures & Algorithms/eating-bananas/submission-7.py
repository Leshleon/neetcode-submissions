class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k_opt = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            k = (r - l) // 2 + l
            
            h_test = 0
            for n in piles:
                h_test += ((n + k - 1) // k)
            
            if h_test > h:
                l = k + 1
            elif k <= k_opt:
                k_opt = k
                r = k - 1
        
        return k_opt




            



        