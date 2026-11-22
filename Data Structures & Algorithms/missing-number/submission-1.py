class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n # only n missing from index of nums
        for i in range(n):
            xorr = xorr ^ i ^ nums[i]
        return xorr


        # res = n # missing n in the index
        # for i in range(n):
        #     res += (i-nums[i])
        # return res


        