class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) == len(t):
            for i, (s_val, t_val) in enumerate(zip(s, t)):
                if s_val in s_dict:
                    s_dict[s_val] += 1
                else:
                    s_dict[s_val] = 1
                
                if t_val in t_dict:
                    t_dict[t_val] += 1
                else:
                    t_dict[t_val] = 1
            
            return s_dict == t_dict
        return False

