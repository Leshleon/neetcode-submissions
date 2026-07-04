class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count_t = {}
        for r in t:
            count_t[r] = count_t.get(r , 0) + 1
        
        c = ""
        count_s = {}
        having, needed = 0, len(set(t))
        res, res_len = "", len(s) + 1
        r, l = len(s) - 1, 0

        for r in range(len(s)):
            c = s[r]
            count_s[c] = count_s.get(c, 0) + 1

            if c in count_t and count_t[c] == count_s[c]:
                having += 1
            
            while having == needed:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = s[l: r + 1]
                
                if s[l] in count_t and count_t[s[l]] == count_s[s[l]]:
                    having -= 1

                count_s[s[l]] -= 1
                l+=1
            
        return res








            
        