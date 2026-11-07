class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs version
        adj = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        visit = set()
        def dfs(node):
            # base case : explicit (optional), if already been to this node
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
        # iterate throuh all node
        res = 0
        for node in range(n):
            # each time check if node in visit
            if not node in visit:
                dfs(node)
                res += 1
        return res

            

         