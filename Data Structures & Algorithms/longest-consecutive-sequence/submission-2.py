class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #############
        # Hash set ##
        #############
        numSet = set(nums)
        res = 0
        for n in nums:
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length +=1 # notice we need increments
                res = max(res, length)
        return res


        # ##############
        # ## Hash map ##
        # ##############
        # d = defaultdict(int) # default to 0
        # res = 0
        # for n in nums:
        #     if not d[n]:
        #         d[n] = 1+ d[n-1] + d[n+1]
        #         d[n - d[n-1]] = d[n]
        #         d[n + d[n+1]] = d[n]
        #         res = max(res, d[n])
        # return res



                

        

        