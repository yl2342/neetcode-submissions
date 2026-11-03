class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False # end of word
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eow = True

        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res = set() # 
        visited = set() # (r,c)

        def dfs(r, c, node, word_so_far):
            # base case
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r,c) in visited or board[r][c] not in node.children):
                return 
            
            visited.add((r,c))
            word_so_far += board[r][c]
            node = node.children[board[r][c]]
            if node.eow:
                res.add(word_so_far)

            dfs(r+1, c , node, word_so_far) # move right
            dfs(r-1, c , node, word_so_far) # move left 
            dfs(r, c+1 , node, word_so_far) # move down
            dfs(r, c-1 , node, word_so_far) # move up
            # backtrack
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)







        