class Solution:
    def numDecodings(self, s: str) -> int:
        # ways(s[i:]) = ways(s[i+1:])    if the first digit is a valid letter
        #               + ways(s[i+2:])  if the first two digits are a valid letter
        # dp[i] = number of ways to decode the substring s[i:]
        # the answer we want is dp[0]
        # each position depends on the next one/two positions -> bottom up DP:

        # base case: dp[len(s)]=1 /dp1 = 1 , empty stirng has one valid decoding:
        # ecoding means turning digits into a message of letters. 
        # An empty string of digits turns into an empty message of no letters. 
        # There’s exactly one way to do that: write nothing. 

        # That one “do nothing” way counts as 1, not 0.
        # iterate i from right to left: if s[i] == '0' -> dp[i] = 0 (invalid)
        # else : take one digit / take two digit (if valid)
        n = len(s)
        dp1 = 1 # ways to decode s[i+1:] (one position ahead)
        dp = 0 # ways to decode s[i:] (the one you’re computing now)	
        dp2 = 0 # ways to decode s[i+2:] (two position ahead)

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                # take one digit choice, just shift, carry over the count
                dp = dp1
            if (i + 1 < n) and ((s[i] == "1") or (s[i] == "2" and s[i + 1] in "0123456")):
                # take two digit, if two v
                dp += dp2
            dp1, dp2 = dp, dp1

        # shift at the end of every iteration, 
        # dp1 now is where the final answer ends up.
        return dp1 



        