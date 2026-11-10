class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # The Bellman-Ford algorithm finds the shortest paths from a single source vertex to all other vertices in a weighted graph.
        # Its main advantage over Dijkstra’s algorithm is that it handles negative edge weights and can detect negative cycles. 
        # How it normally works: 
        # 1. Set the distance to the source as 0 and every other vertex as infinity.
        # 2. Repeat V − 1 times (V = number of vertices): for every edge (u, v) with weight w, check whether going through u gives a shorter route to v. 
        # 3. If dist[u] + w < dist[v], update dist[v]. This is called “relaxing” the edge.
        # 4. Do one more pass over all edges. If any edge can still be relaxed, the graph contains a negative cycle reachable from the source, so shortest paths aren’t well defined. 

        # Difference with Dijkstra’s
        # Dijkstra’s algorithm finds shortest paths from a single source by always expanding the closest unvisited vertex next, using a priority queue. 
        # Once a vertex is finalized, its distance never changes. That “greedy” assumption is exactly what breaks when edges can be negative.
        # Dijkstra’s Much faster: O((V + E) log V) with a binary heap, versus O(V · E) for Bellman-Ford. Bellman-Ford is exhaustive: it relaxes every edge repeatedly, 
        # so distances keep getting corrected until they settle.

        prices = [float("inf")] * n
        prices[src] = 0
        # iterate through stops
        for i in range(k + 1):
            temp = prices.copy()
            # iterate through edges: k+1 stops
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    # not yet connected from the source
                    continue
                if prices[s] + p < temp[d]:
                    # compare with the original/price from last level-iteration 
                    # update the temp inplace instead
                    temp[d] = prices[s] + p
            prices = temp
        return -1 if prices[dst] == float("inf") else prices[dst]
            




        
        

        

        

        

        