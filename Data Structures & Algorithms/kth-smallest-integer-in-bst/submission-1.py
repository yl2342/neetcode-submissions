# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # # dfs + inorder traversal
        # array = []
        # def dfs(root):
        #     if not root:
        #         return # A bare return with no value means the function immediately exits and gives back None to whoever called it.
        #     dfs(root.left)
        #     array.append(root.val)
        #     dfs(root.right)

        # dfs(root)
        # return array[k-1]

        # iterative version
        stack = []
        curr = root

        while curr or stack:
            # traverse to (subtree's)left: in order traverse
            while curr:
                stack.append(curr)
                curr = curr.left
            # done with the left, pop back
            curr = stack.pop()
            k -= 1 # k should >0
            if k == 0:
                return curr.val
            curr = curr.right

        
        
        