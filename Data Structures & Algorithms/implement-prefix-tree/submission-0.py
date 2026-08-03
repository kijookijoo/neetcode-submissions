class TrieNode:
    def __init__(self, end=False):
        self.children = {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True 

    def search(self, word: str) -> bool:
        curr = self.node
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        