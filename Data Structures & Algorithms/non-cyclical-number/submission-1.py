class Solution:
    def isHappy(self, n: int) -> bool:
        # like a link list problem
        # fast & slow pointer : Floyd's cycle detection
        def sumOfSqure(n):
            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            return output
        
        fast = slow = n
        while True:
            slow = sumOfSqure(slow)
            fast = sumOfSqure(fast)
            fast = sumOfSqure(fast)
            if fast == 1:
                return True
            if fast == slow:
                return False
        
        