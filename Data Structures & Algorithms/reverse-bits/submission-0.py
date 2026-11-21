class Solution:
    def reverseBits(self, n: int) -> int:
        # bit manipulation
        # Extract each bit from the original number starting from the least significant bit
        # Place that bit into the correct reversed position in the result
        # Repeat this for all 32 bits
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res