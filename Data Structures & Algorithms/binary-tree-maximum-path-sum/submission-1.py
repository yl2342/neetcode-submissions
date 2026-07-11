# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Assigning to res inside dfs makes Python treat res 
        # as a local variable of dfs (that's how Python's scoping rules work 
        # any variable assigned anywhere in a function is local to that function
        # unless declared otherwise). Since res is read before being assigned in that same statement, 
        # you'd get an UnboundLocalError.
        
        # Use a mutable object (like a one-element list res = [root.val]) 
        # and do res[0] = .... This works because you're not reassigning res itself 
        # (which would make it local) — you're mutating the object res points to, 
        # which is allowed without any special declaration.
        res = [root.val]

        # return max path sum without spliting
        def dfs(root):
            if not root:
                return 0
            # return 
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            
            # check maximum
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        
        path_from_root = dfs(root)

        return res[0]

















