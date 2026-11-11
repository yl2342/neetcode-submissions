class Solution:
    def rob(self, nums: List[int]) -> int:
        # skip means best_one_back, and rob means best_two_back + n.
        best_two_back, best_one_back = 0, 0 
        
        for num in nums:
            best_two_back, best_one_back = best_one_back, max(best_two_back + num, best_one_back)
        return best_one_back
        