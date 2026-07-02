class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        max_len = 0
        set_s = set()

        for r in range(len(s)):
            while s[r] in set_s:
                set_s.remove(s[l])
                l+=1

            set_s.add(s[r])
            max_len = max(max_len, len(set_s))
            

        return max_len


        