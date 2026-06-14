class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        cSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l = l+1
            cSet.add(s[r])
            res = max(res, r-l+1)
        return res


        

        