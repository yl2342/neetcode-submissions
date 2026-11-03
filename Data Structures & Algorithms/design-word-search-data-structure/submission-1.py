class TrieNode():
    def __init__(self):
        self.children = {}
        self.eow = False # end of word


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True
        

    def search(self, word: str) -> bool:
        # backtracking/recursion: dfs
        def dfs(i, root) -> bool:
            curr = root
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.eow

        return dfs(0, self.root)








        
