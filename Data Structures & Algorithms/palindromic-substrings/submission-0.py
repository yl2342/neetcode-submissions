class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(l,r) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        RES = 0
        for i in range(len(s)):
            RES += count(i, i) + count(i, i+1)
        return RES



        