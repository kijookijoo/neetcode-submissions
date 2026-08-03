class TrieNode:
        def __init__(self, end=False):
            self.children = {}
            self.end = end

class Trie:
    def __init__(self):
        self.node = TrieNode()
    
    def insert(self, word):
        curr = self.node
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        ROWS, COLS = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # return a list of words that can be formed using the given point as the starting point
        def dfs(i, j, node, path, idx, visited):
            nonlocal res
            if i < 0 or j < 0 or i == ROWS or j == COLS or (i,j) in visited:
                return 
            if board[i][j] not in node.children:
                return 

            visited.add((i,j))
            path.append(board[i][j])

            curr = node.children[board[i][j]]
            if curr.end:
                currWord = "".join(path)
                if currWord not in res:
                    res.add(currWord)
            
            dfs(i + 1, j, curr, path, idx + 1, visited) 
            dfs(i - 1, j, curr, path, idx + 1, visited) 
            dfs(i, j + 1, curr, path, idx + 1, visited) 
            dfs(i, j - 1, curr, path, idx + 1, visited) 
            visited.remove((i,j))
            path.pop()
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.node, [], 0, set())
        
        return list(res)
        
