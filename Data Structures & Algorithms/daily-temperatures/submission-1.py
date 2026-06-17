class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonious decreasing stack
        # set result to 0 for default
        res = [0] * len(temperatures)
        stack = [] # store a tuple for both index and temperature (index, temp)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1]< t:
                (index, temp) = stack.pop()
                res[index] = i - index # ! beauty of it
            stack.append((i,t))
        return res 
        
        