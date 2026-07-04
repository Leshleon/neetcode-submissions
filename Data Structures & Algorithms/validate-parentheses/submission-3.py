class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        brack_list = []
        for c in s:
            if c in brackets:
                brack_list.append(c)
            else:
                if brack_list and c == brackets[brack_list[-1]]:
                    brack_list.pop(-1)
                else:
                    return False
                    
        return True if not brack_list else False


        