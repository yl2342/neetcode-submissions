class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        # memoization
        dp = {} 
        def dfs(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return True
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            
            if i1 < len(s1) and s1[i1] == s3[i1 + i2] and dfs(i1 + 1, i2):
                return True # go along s1
            if i2 < len(s2) and s2[i2] == s3[i1 + i2] and dfs(i1, i2 + 1):
                return True # go along s2
            dp[(i1, i2)] = False
            return False
        return dfs(0,0)

        
        