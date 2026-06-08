class Solution:
    # two pointers-like
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        # prefix loop
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        # postfix loop
        post = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= post
            post *= nums[i]
        
        return res

        # O(n), O(1)



        
        
