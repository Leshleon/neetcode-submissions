class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        brack_list = []
        latest_b = ""
        for c in s:
            if c in ["(", "{", "["]:
                brack_list.append(c)
            else:
                if not brack_list:
                    return False
                elif c != brackets[brack_list[-1]]:
                    return False
                else:
                    brack_list.pop(-1)

        return True if not brack_list else False


        