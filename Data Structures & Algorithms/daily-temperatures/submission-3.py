class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stackInd, stackTemp = stack.pop()
                output[stackInd] = i - stackInd
            stack.append((i, t))
        
        return output
            
        