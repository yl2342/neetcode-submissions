class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        # initiate adjacency list
        adj = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visit = set()

        # pass prev to differentiate neigbour or cycle
        def dfs(node, prev) -> bool:
            # basecase
            if node in visit:
                return False
            visit.add(node)
            for neighbour in adj[node]:
                # pass the previous neibouring node
                if neighbour == prev:
                    continue
                if not dfs(neighbour, node):
                    return False # return false imediately
            return True
        # condition 1: no cycle , use -1 as default value for first's prev
        cond1 = dfs(0,-1)

        # condition 2: every node visited through one point
        cond2 = len(visit) == n

        return cond1 and cond2


        