# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(root):
            """
            return the heigt/depth rather than diameter/result
            but update the result meanwhile
            """
            if not root:
                return 0
            
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)

            self.diameter = max(self.diameter, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        
        dfs(root)

        return self.diameter
        


        