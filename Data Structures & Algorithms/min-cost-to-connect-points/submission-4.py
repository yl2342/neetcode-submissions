
## (Optional) Kruskal's algorithm: Union-find
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node] # not node (different node remain unchanged in rach call stack)
    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.parent[p2] = self.parent[p1]
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p1] = self.parent[p2]
            self.rank[p1] += self.rank[p2]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # # MST problem: minimum spanning tree 
        # # prim's algorithm
        # n = len(points)
        # adj = {i:[] for i in range(n)}
        # # construct edges
        # for i in range(n):
        #     x1, y1 = points[i]
        #     for j in range(i+1, n, 1):
        #         x2, y2 = points[j]
        #         dist = abs(x2 - x1) + abs(y2 - y1)
        #         adj[i].append([dist, j])
        #         adj[j].append([dist, i])
        
        # res = 0
        # visit = set()
        # minheap = [[0, 0]]
        # while len(visit) < n:
        #     w_cur, i_cur = heapq.heappop(minheap)
        #     if i_cur in visit:
        #         continue
        #     visit.add(i_cur)
        #     res += w_cur
        #     for w_nei, i_nei in adj[i_cur]:
        #         # check i_nei not in visit is also important
        #         if i_nei not in visit:
        #             heapq.heappush(minheap, [w_nei, i_nei]) 
        # return res
        # this solution only returns the total cost (res). 
        # To get the actual edges, carry the parent in each heap entry and record the edge when a new point is accepted:
        # res = 0
        # visit = set()
        # mst_edges = []
        # minH = [[0, 0, -1]]               # [cost, node, parent]
        # while len(visit) < n:
        #     cost, i, parent = heapq.heappop(minH)
        #     if i in visit:
        #         continue
        #     res += cost
        #     visit.add(i)
        #     if parent != -1:
        #         mst_edges.append((parent, i, cost))
        #     for neiCost, nei in adj[i]:
        #         if nei not in visit:
        #             heapq.heappush(minH, [neiCost, nei, i])
        # return res, mst_edges


        # Union find solution:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                edges.append([dist, i, j])
        edges.sort() # important to sort first
        res = 0
        for dist, n1, n2 in edges:
            if dsu.union(n1, n2):
                res += dist
        return res


        

                



        