class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return [max(nums)]

        output = []
        # better to store the index of the number
        # queue needs to be in decreasing order, max is always at the left most
        dq = collections.deque()
        l, r = 0, 0

        while r < len(nums):

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop() # keep pop the right value if it is smaller than the num[r] to be added, if nothing in sq, just add one, keep at least one element in dq at all time
            dq.append(r) # becomes the leftmost and only value in dq, dp[0], if all orgianl values is sammler than num[r]

            # update deque, remove outated elements (no longer captured in the window)
            if l > dq[0]:
                dq.popleft()
            
            # start incrementingh l to keep the window and update the result
            if (r+1) >= k:
                output.append(nums[dq[0]])
                l += 1 

            r +=1

        return output


