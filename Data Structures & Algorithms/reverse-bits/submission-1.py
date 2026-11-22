# bit manipulation
# shifts the number right so the bit you want lands at position 0.
# Shifting right slides every bit to the right.
# Bits that slide off the right edge disappear, 
# and zeros fill in on the left.
# & 1 masks off everything except that last bit.
# &  compares two numbers bit by bit. 
# The result bit is 1 only if both bits are 1
# The number 1 in binary is ...00000001: all zeros except position 0. 
# ANDing with it keeps position 0 and forces every other position to 0:


class Solution:
    def reverseBits(self, n: int) -> int:
        
        # Extract each bit from the original number starting from the least significant bit
        # Place that bit into the correct reversed position in the result
        # Repeat this for all 32 bits
        res = 0
        # walks from right: (LSB) least significant bit
        for i in range(32):
            # extracts the bit at position i
            # bit is a whole number after shift, not a single loose bit. 
            # Written out as 32 bits, 000...001 / 000...000
            bit = (n >> i) & 1
            # bit << (31 - i) moves the bit (0 or 1) to its mirrored position.
            # Shift this bit to position (31 - i)
            res += (bit << (31 -i))
        return res

        