class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            if n == parent[n]:
                return n
            return (find(parent[n]))
        
        def union(n1, n2) -> bool:
            """Detect cycle: 1 means successfully union for tree 0 means cycle appear"""
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False # would cause cycle
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1, n2]
            

        