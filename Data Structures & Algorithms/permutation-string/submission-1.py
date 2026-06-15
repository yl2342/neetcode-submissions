class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        count1, count2= [0] * 26,  [0] * 26
        
        # for starter: len(s1) substring
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1
        
        # then check match count:
        m= 0
        for j in range(26):
            m += (1 if count1[j]==count2[j] else 0)
        
        # then slide window
        l = 0
        for r in range(len(s1), len(s2), 1):
            if m == 26:
                return True
            # right pointer
            idx_r = ord(s2[r])-ord('a')
            count2[idx_r] += 1
            if count1[idx_r] == count2[idx_r]:
                m += 1
            elif (count1[idx_r]+1) == count2[idx_r]:
                m -= 1

            # left pointer
            idx_l = ord(s2[l])-ord('a')
            count2[idx_l] -= 1
            if count1[idx_l] == count2[idx_l]:
                m += 1
            elif (count1[idx_l]-1) == count2[idx_l]:
                m -= 1
            l += 1
            
        return m == 26
                
            


        