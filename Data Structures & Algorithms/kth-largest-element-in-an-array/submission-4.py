class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = k-1 # for index
        def quickselect(l,r):
            # in reverse order, biggest comes first
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] > pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quickselect(l, p-1)
            elif p < k:
                return quickselect(p+1, r)
            else:
                return nums[p]
        return quickselect(0, len(nums)-1)
        