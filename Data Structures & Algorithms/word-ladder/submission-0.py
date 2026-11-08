class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # python basic prerequisite: string[a:b] returns the characters from index a up to, but not including, index b
        if endWord not in wordList:
            return 0
        # initialize adjacency list
        neighbours = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbours[pattern].append(word)
        # BFS
        visit = set([beginWord]) # add iterable
        q = deque([beginWord])
        res = 1

        while q:
            # one level at a time
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for k in range(len(word)):
                    pattern = word[:k] + "*" + word[k+1:]
                    for nei in neighbours[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1
        
        return 0
                    








        