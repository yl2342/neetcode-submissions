# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ###################
        # ## Recursive DFS ##
        # ###################
        # if not root:
        #     return 0
        
        # leftDepth = self.maxDepth(root.left)
        # rightDepth = self.maxDepth(root.right)

        # return 1 + max(leftDepth,rightDepth)


        ###################
        ## BFS ##
        ###################
        q = deque()
        if root:
            q.append(root)
        
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
        
        