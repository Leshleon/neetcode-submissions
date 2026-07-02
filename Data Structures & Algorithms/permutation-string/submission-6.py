class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_list = list(s1)

        for r in range(len(s2)):
            if s2[r] not in s1_list:
                if s2[r] in s1:
                    while l < r:
                        if s2[r] == s2[l]:
                            l += 1
                            break
                        s1_list.append(s2[l])
                        l += 1
                else:
                    l += 1
                    s1_list = list(s1)

            else:
                s1_list.remove(s2[r])
            
            if not s1_list:
                return True
        
        return False
