class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        l = 0
        res_len = len(s) + 1
        result = ""

        for r in range(len(s)):

            if s[r] in countT.keys():
                countT[s[r]] -= 1
            if max(countT.values()) <= 0:
                while countT.get(s[l], -1) < 0:
                    if s[l] in countT.keys():
                        countT[s[l]] += 1
                    l += 1
                if r - l + 1 < res_len:
                    result = s[l:r+1]
                    res_len = len(result)                
            
        return result








            


        