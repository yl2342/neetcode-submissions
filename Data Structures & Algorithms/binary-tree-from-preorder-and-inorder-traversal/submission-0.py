# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        # root (of a subtree) will always be the first in the preorder
        # do it in order and recursively 
        root = TreeNode(preorder[0])
        p = inorder.index(preorder[0]) # partition
        root.left = self.buildTree(preorder[1:p+1], inorder[:p])
        root.right = self.buildTree(preorder[p+1:], inorder[p+1:])
        return root



        