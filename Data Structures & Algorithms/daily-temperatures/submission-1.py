class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        stack = []
        heapq.heapify(stack)

        for i in range(len(temperatures) - 1, -1, -1):

            while stack and stack[0][0] <= temperatures[i]:
                print(stack)
                heapq.heappop(stack)
                
            
            if stack:
                output[i] = stack[0][1] - i

            heapq.heappush(stack, (temperatures[i], i))
        
        return output
            
            

        