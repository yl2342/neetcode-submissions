# python basics
# math.fmod(x, 10) keeps the sign of x (the dividend)
# x % 10 keeps the sign of 10 (the divisor)
# Floor Division (//) — Rounds Toward - inifinity: -7 // 2 = -4
# int(-7 /2 ) = -3

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31
        MAX = 2 ** 31 -1
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10) # round towards
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MAX % 10):
                return 0
            res = (res * 10) + digit # add backward
        return res