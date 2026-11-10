class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # post order DFS
        adj = {c:set() for word in words for c in word}
        # compare in pairs iteriatively 
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1] # already in order: w1 , w2
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                # one of the two ways the input can be invalid
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        # three state for visit 
        # 1. not in visit: never seen 
        # 2. True: currently on the  DFS path (in progress)
        # 3. False: visited & finised, already added to res
        visiting = {}
        res = []

        def dfs(c):
            """A dfs return True/False/None, and if dfs(c) treats False and None the same way"""
            if c in visiting:
                return visiting[c] # True: cycle
            visiting[c] = True
            for c_after in adj[c]:
                if dfs(c_after):
                    return True
            visiting[c] = False # backtrack, one all dfs[c_after] ran and 
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return "" # detect cycle
        
        res.reverse()
        return "".join(res)
            

        
        