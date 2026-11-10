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
            """
            dfs(c) answers one question: “starting from c, did I run into a cycle?” 
            True means yes, False (or None) means no. The return value is purely an alarm signal."""
            if c in visiting:
                return visiting[c] # True: cycle
            # Why return true for a cycle: 
            # 1. Local: When a call returns True, each caller returns True right away, skip the remaining work, since once a cycle exists nothing else matters.
            # 2. Global: deliver the “invalid input” signal to the very top, which turns it into return "".
            
            
            # so the rest of its neighbor loop is skipped, and visited[char] = False and res.append(char) never run for those nodes.
            visiting[c] = True
            for c_after in adj[c]:
                if dfs(c_after):
                    return True # True gets passed upward
            visiting[c] = False # backtrack, one all dfs[c_after] ran and 
            res.append(c)
            # What happens when there’s no cycle: The function falls off the end and returns None, 
            # which is falsy. So if dfs(neighChar): is false and the loop carries on. 
            # That’s why there’s no explicit return False at the bottom.
        
        for c in adj:
            if dfs(c):
                return "" # detect cycle
        
        res.reverse()
        return "".join(res)
            

        
        