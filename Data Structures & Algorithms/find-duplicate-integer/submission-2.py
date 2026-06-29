class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # consider as pointer questions for finding cycles
        # floyd's alorithms: fast/slow pointers
        s, f = 0, 0 # start from 0 and o will not consititude the cycle
        
        # first loop to find first intersection
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        # second loop, initate slow pointer 2
        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s

            

        
        