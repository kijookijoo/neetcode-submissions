class TrieNode:
    def __init__(self,end=False):
        self.children = {}
        self.end = end

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
        
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end

            c = word[i]
            if c == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True
            else:
                if c not in node.children:
                    return False
                else:
                    return dfs(node.children[c], i + 1)
            return False

        return dfs(self.node, 0)
            
        
