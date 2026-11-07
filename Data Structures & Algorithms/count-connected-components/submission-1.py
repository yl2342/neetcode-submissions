# Union-find (also called disjoint-set union, or DSU) is a data structure that tracks a collection of elements split into non-overlapping groups
# Each group is stored as a tree. Every element points to a parent, and the root points to itself. find follows parent pointers up to the root. union links one root under the other.
# A naive version can degrade into long chains, so two optimizations are standard:
# Path compression: during find, point every node you visit directly at the root, flattening the tree for future queries.
# Union by rank (or size): when merging, attach the shorter (or smaller) tree under the taller (or larger) one so trees stay shallow.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DSU/Union-find version
        parent = [i for i in range(n)] # initialize as itself
        rank = [1] * n
        # define find first
        def find(node) -> int:
            """return the parent node"""
            res = node
            while res != parent[res]:
                # path compression: skips over its parent by pointing at its grandparent, then moves up to continue from there, resulting halving: each step moves up two levels but only rewires every other node on the path, so the path length is roughly cut in half per find
                parent[res] = parent[parent[res]] # path compression, halving
                # find(parent[res]) # standard, recursively
                res = parent[res]
            return res
        def union(n1, n2) -> int:
            """union return if executed 0/1"""
            p1 = find(n1) 
            p2 = find(n2)
            # if parent the same, already connected, no union needed/executed this time: 0
            if p1 == p2:
                return 0
            # move smaller size/rank node under the higher one
            if rank[p1] < rank[p2]:
                parent[p1] = parent[p2]
                rank[p2] += rank[p1]
            else:
                parent[p2] = parent[p1]
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1 , n2 in edges:
            res -= union(n1, n2)
        return res
        


















        # # dfs version
        # adj = {i:[] for i in range(n)}
        # for node1, node2 in edges:
        #     adj[node1].append(node2)
        #     adj[node2].append(node1)
        # visit = set()
        # def dfs(node):
        #     # base case : explicit (optional), if already been to this node
        #     if node in visit:
        #         return
        #     visit.add(node)
        #     for nei in adj[node]:
        #         dfs(nei)
        # # iterate throuh all node
        # res = 0
        # for node in range(n):
        #     # each time check if node in visit
        #     if not node in visit:
        #         dfs(node)
        #         res += 1
        # return res

            

         