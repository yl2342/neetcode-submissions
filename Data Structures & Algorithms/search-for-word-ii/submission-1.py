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
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = set() # 
        visited = set() # (r,c)

        def dfs(r, c, node, path):
            # r, c are the cordinates on the board
            # node is trie node that represent the prefix we 've built so far: 
            # i've spelled path so where am i in the trie? 
            # node.children is the next position

            # 1. base case
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return
            if (r,c) in visited:
                return 
            if board[r][c] not in node.children:
                return 
            
            # 2. choose
            visited.add((r,c))
            node = node.children[board[r][c]] # move to the neighbour position
            path += board[r][c] # concatenate the character 
            
            # 3. record
            if node.eow:
                res.add(path)

            # 4. explore
            for dr, dc in DIRS:
                dfs(r + dr, c + dc, node, path)
            
            # 5. unchoose
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)







        