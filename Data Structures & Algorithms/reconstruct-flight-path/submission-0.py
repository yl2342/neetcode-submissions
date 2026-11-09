class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # "assuming each ticket was used exactly once." -> Eulerian path or circuit problem
        # use Hierholzer’s algorithm: It’s an O(E) algorithm for finding an Eulerian path or circuit in a graph: a walk that uses every edge exactly once.
        # The core idea: Walk along unused edges until you get stuck. In a graph where an Eulerian path exists, you can only get stuck at the path’s end vertex, because every other vertex has a spare outgoing edge whenever you enter it. But getting stuck doesn’t mean you’ve used all the edges. Some may be left on loops you skipped. Hierholzer’s handles that by recording a vertex only when it has no unused edges left (post-order), and by splicing in the leftover loops as you backtrac
        adj = collections.defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        res = []
        def dfs(src):
            # base case: till get stuck/end
            if not adj[src]:
                res.append(src)
                return 
            dst = adj[src].pop()
            dfs(dst) # follow the ticket and exhaust everything beyond dst
            dfs(src) # come back and handle any tickets still left at src
        dfs("JFK")
        return res[::-1]


            


