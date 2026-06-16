class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(t) > len(s):
            return ""
        
        countT, window = {}, {}
        # for c in t:
        #     countT[c] = countT.get(c,0) + 1
        countT = collections.Counter(t)

        have, need = 0, len(countT)
        res_l, res_r = -1, -1 # result lef right index
        res_len = float("inf")

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                # update result only once meet the criteria
                if (r - l + 1) < res_len:
                    res_l, res_r = l, r 
                    res_len = r - l + 1

                # pop from left then update the have
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        return s[res_l : res_r+1] if res_len != float("inf") else ""

            

        