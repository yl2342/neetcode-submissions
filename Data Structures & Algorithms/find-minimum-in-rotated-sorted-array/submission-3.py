class Solution:
    def findMin(self, nums: List[int]) -> int:
        # hint: sorted + logn -> binary search
        # two flavors of binary search:
        # Flavor 1: l <= r — find an exact target, return inside the loop
        # Flavor 2: l < r — converge to a single answer, return after the loop, to Find a boundary / minimum / peak
        # For flavor 2: There's no exact target to find and return early on. You're narrowing toward a position,
        # and the answer only becomes unambiguous when the window collapses to one element.
        # The asymmetry in updates (r = m vs l = m + 1) is what makes Flavor 2 safe — 
        # it guarantees the l < r will always eventually become l == r and exit cleanly.
        # l <= r works when you always shrink by at least 1 on every branch (r = m-1 / l = m+1). 
        # l < r is required when one branch only does r = m, which would stall if l == r.
        # Flavor 2 (l < r): no early return, so you must stop at 2 elements, So you must stop before l == r, meaning stop when l < r is no longer true — i.e., exit at l == r.


        
        l, r = 0, len(nums)-1
        # nums[r] is always a safe anchor — the minimum is always ≤ nums[r], so you never accidentally discard it.
        # When nums[m] < nums[r], m itself could be the minimum. So keep m in the search window with r = m. (Setting r = m - 1 would skip it.) - This also explains the loop condition l < r (not l <= r) — once they meet, you've found it.
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m  # m still could be the min
            else:
                l = m + 1
        return nums[l] # lower bound





        # res = nums[0]
        # while l <= r:
        #     # finally be in a left-side sorted subsection
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break
        #     m = (l + r) // 2
        #     res = min(res, nums[m])
        #     # if in left sorted order, go to right part
        #     # basically try to find the pivot point
        #     if nums[l] <= nums[m]:
        #         l = m + 1
        #     else:
        #         r = m -1
        # return res

                

        
        