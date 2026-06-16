class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        stack = [] # first in last out

        for i in range(len(s)):
            # close , check last 
            if s[i] in close2open:
                if stack and stack.pop() == close2open[s[i]]:
                    continue
                # if stack and stack[-1] == close2open[s[i]]:
                #     stack.pop()
                else:
                    return False
            else:
                # open, append to top of stack
                stack.append(s[i])
        
        # Finally
        # if not stack      → True for [], None, 0, "", False (any falsy value)
        # if stack == None  → True only for None (but use 'is' instead of '==')
        # if stack is None  → True only for None (recommended way to check None)

        return True if not stack else False

                




        