class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # key insights from the question:
        # no matter how fast/ how large k can be, take at least 1 hour to finish 1 pile
        # so k shoud >=0 and <= max(P), we have a finite k to loop through [1, max(piles)]
        l, r = 1, max(piles)
        res = r
        # loop through k 
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                # can try eat slower 
                res = min(res, k)
                r = k - 1
            if hours > h:
                # should eat faster
                l = k + 1
        return res

                
        
            
    


        