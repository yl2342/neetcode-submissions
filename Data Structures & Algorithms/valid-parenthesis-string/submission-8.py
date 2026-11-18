class Solution:
    def checkValidString(self, s: str) -> bool:
        # # greedy
        # leftMin, leftMax = 0, 0
        # for c in s:
        #     if c == "(":
        #         leftMin, leftMax = leftMin + 1, leftMax + 1
        #     elif c == ")":
        #         leftMin, leftMax = leftMin - 1, leftMax - 1
        #     else:
        #         leftMin, leftMax = leftMin - 1, leftMax + 1
        #     if leftMax < 0:
        #         return False
        #     if leftMin < 0:
        #         leftMin = 0
        # return leftMin == 0


        # stack 
        left = []
        star = []
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else:
                if not left and not star:
                    # no openining left p
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            # star has to combe after to ensure close the left (if any)
            if left.pop() > star.pop():
                return False
        return not left # should guarantee empty left  

                





        