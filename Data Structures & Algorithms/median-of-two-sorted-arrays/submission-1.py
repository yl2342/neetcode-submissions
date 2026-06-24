class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # assign short/long array
        if len(nums1) <= len(nums2):
            S, L = nums1, nums2 # short, long
        else:
            S, L = nums2, nums1
        
        total = len(nums1) + len(nums2) # total number
        half = total // 2
        
        # do binary search  on S and auto update on L
        # start l from -1, as sm can reach -1 to make left partition total empty
        l, r = -1, len(S)-1 
        while l <= r:
            sm = (l + r) // 2 # middle idx in S, use as the upperbound in S 
            lm = half - sm - 2 # # middle idx in L, use as the upperbound in L 

            # S = [  |  3, 5, 7 ]
            #        ↑ nothing on the left of S
            # If the left partition of S is empty, we need Sleft to be "infinitely small" 
            # so that the condition Sleft <= Lright is always satisfied — meaning S contributes nothing to the left side, and that's perfectly fine.
            # S = [ 2, 4, 6  |  ]
            #                ↑ nothing on the right of S
            # If the right partition of S is empty, Sright should be "infinitely large" 
            # so that Lleft <= Sright is always satisfied — meaning S contributes nothing to the right side, also fine.
            # Without these sentinels, you'd get an IndexError and couldn't handle arrays where the partition sits at either extreme end.


            Sleft =  S[sm] if sm >=0 else float("-infinity") # if sm <0 then left partition of S is empty
            Sright= S[sm+1] if (sm+1) < len(S) else float("infinity") # if sm >=len(S) then right partition of S is empty, Sright should be "infinitely large", so that Lleft <= Sright is always satisfied — meaning S contributes nothing to the right side
            Lleft =  L[lm] if lm >=0 else float("-infinity") # if lm <0 then left partition of L is empty
            Lright= L[lm+1] if (lm+1) < len(L) else float("infinity") #  right partition of L is empty, Lright should be "infinitely large", so that Sleft <= Lright is always satisfied — meaning S contributes nothing to the right side

            if Sleft <= Lright and Lleft <= Sright:
                # if odd
                if total % 2:
                    return min(Sright, Lright)
                # if even
                else:
                    return (max(Sleft, Lleft) + min(Sright, Lright)) / 2
            elif Sleft > Lright:
                # too many S, shrink S towards left
                r = sm - 1
            else:
                l = sm + 1

 

    