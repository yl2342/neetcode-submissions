class Solution:
    def myPow(self, x: float, n: int) -> float:
        # divide & conquer O(logn)
        def pow_dc(x, n):
            # basecase:
            if x == 0:
                return 0
            if x == 1 or n == 0:
                return 1
            res = pow_dc(x, n//2)
            res = res * res
            return x * res if n % 2 else res
        res = pow_dc(x, abs(n))
        return res if n >= 0 else 1 / res


        