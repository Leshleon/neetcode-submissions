class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_f = 0
        max_len = 0
        s_dict = {}

        for r in range(len(s)):
            s_dict[s[r]] = s_dict.get(s[r], 0) + 1
            max_f = max(max_f, s_dict[s[r]])

            while k < r - l + 1 - max_f:
                s_dict[s[l]] -= 1
                if max_f not in s_dict.values():
                    max_f -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
            
        return max_len








        