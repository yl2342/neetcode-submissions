"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # use to break the cycle
        def dfs(node):
            # base case
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors:
                oldToNew[node].neighbors.append(dfs(n))
            return oldToNew[node]
        return dfs(node) if node else None


        