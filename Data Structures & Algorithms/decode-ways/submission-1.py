class Solution:
    def numDecodings(self, s: str) -> int:
        # ways(s[i:]) = ways(s[i+1:])    if the first digit is a valid letter
        #               + ways(s[i+2:])  if the first two digits are a valid letter
        # dp[i] = number of ways to decode the substring s[i:]
        # the answer we want is dp[0]
        # each position depends on the next one/two positions -> bottom up DP:
        # base case: dp[len(s)]=1 , empty stirng has one valid decoding
        # iterate i from right to left: if s[i] == '0' -> dp[i] = 0 (invalid)
        # else : take one digit / take two digit (if valid)
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # take one digit choice, just shift, carry over the count
                dp[i] = dp[i+1] 
            if (i + 1 < n) and ((s[i] == "1") or (s[i] == "2" and s[i + 1] in "0123456")):
                # take two digit, if two v
                dp[i] += dp[i+2] 

        return dp[0]



        