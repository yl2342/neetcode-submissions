class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open < n
        # only add close paranthesis if close < open
        # valid if openN == closeN == n
        stack = []
        res = []

        def backtrack(openN, closeN):
            # base case
            if openN == closeN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closeN)
                stack.pop() # clean and clear the path
            
            if closeN < openN :
                stack.append(')')
                backtrack(openN, closeN+1)
                stack.pop()
                
        backtrack(0, 0)
        return res

                


        