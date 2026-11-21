# XOR (short for Exclusive OR) is a logical and bitwise operation that outputs True (1) only when its two inputs are different, and False (0) when they are the same.
# In Python (and most programming languages), the bitwise XOR operator is the caret symbol: ^.



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ a = 0 a number XORed with itself cancels out
        # a ^ 0 = a (XOR with 0 keeps the number unchanged)
        # XOR is commutative and associative, so order does not matter
        # Because of these properties:
        # all numbers that appear twice will cancel each other out
        # the number that appears once will remain
        res = 0
        for num in nums:
            res = res ^ num
        return res

