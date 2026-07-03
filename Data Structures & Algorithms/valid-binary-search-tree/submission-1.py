# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs
        def in_range(node, lower, upper):
            if not node:
                return True
            if (lower < node.val < upper):
                return (
                    in_range(node.left, lower, node.val) and 
                    in_range(node.right, node.val, upper)
                )
            else:
                return False

        return in_range(root, float("-inf"), float("inf"))

        
        