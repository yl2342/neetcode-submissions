class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height)-1
        lm, rm = height[l], height[r]
        res = 0

        while l < r:
            if lm < rm:
                l += 1
                lm = max(height[l], lm)
                res += lm - height[l]
                
            else:
                r -= 1
                rm = max(height[r], rm)
                res += rm - height[r]
        return res




        