class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers
        START_IDX = 0
        MAX_LEN = 0

        def find_longest(s, l, r):
            nonlocal START_IDX, MAX_LEN
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > MAX_LEN:
                    START_IDX = l
                    MAX_LEN = r - l + 1
                l -= 1
                r += 1
        for i in range(len(s)):
            # odd number
            find_longest(s, i, i)
            # even number 
            find_longest(s, i, i+1)
        
        return s[START_IDX : START_IDX + MAX_LEN]

        
        
        