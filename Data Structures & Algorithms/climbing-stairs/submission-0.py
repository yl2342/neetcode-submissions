class Solution:
    def climbStairs(self, n: int) -> int:
        # dynamic programming: bottom up 
        # At any step, the number of ways depends only on the previous two steps. So instead of storing all values in a DP array, we can just keep two variables that represent:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(n-2):
            a, b = b, a+b
        return b


        