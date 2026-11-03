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
        def dfs(node, i) -> bool:
            # base case: consumed the whole word
            if i == len(word):
                return node.eow
            c = word[i]
            # case 1: wildcard, try every child
            if c == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            # case 2: normal letter, follow it if it exist
            if c not in node.children:
                return False
            return dfs(node.children[c], i+1)    
        return dfs(self.root, 0)








        
