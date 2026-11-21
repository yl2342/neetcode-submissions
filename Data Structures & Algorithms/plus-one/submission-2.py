class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # backward
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                # first loop is add one 
                # if loop continue then must be carry
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        # loop end without return -> [0, 0 ..]
        digits.append(0)
        digits[0] = 1
        return digits

        # python basics:
        # List concatenation (+) does not modify digits in place. Instead, Python allocates a brand-new list of length $n + 1$ in memory and copies [1] followed by all $n$ elements of digits into it ([1, 0, 0, 0]).Because that newly allocated list grows proportionally to the input size $n$, it takes $O(n)$ memory.
        # [1] + digits  -> O(n)



        