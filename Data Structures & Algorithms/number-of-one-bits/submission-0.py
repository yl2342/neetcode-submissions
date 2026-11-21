class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # check if current least significant digit is 1
            # if n % 2:
            #     res += 1
            res += n % 2
            n = n >> 1 # Shift n one bit to the right
        return res
        