class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class PrefixTree:
    def __init__(self, ternimal = False):
        self.nodes = {}
        self.ternimal = ternimal

    def insert(self, word: str, i = 0) -> None:
        c = word[i]
        if c not in self.nodes:
            self.nodes[c] = PrefixTree()
        if i < len(word) - 1:
            self.nodes[c].insert(word, i + 1)
        else:
            self.nodes[c].ternimal = True

    def search(self, word: str, i = 0) -> bool:
        c = word[i]
        if c not in self.nodes:
            return False
        if i < len(word) - 1:
            return self.nodes[c].search(word, i + 1)
        else:
            return self.nodes[c].ternimal
        
    def startsWith(self, prefix: str, i = 0) -> bool:
        c = prefix[i]
        if c not in self.nodes:
            return False
        if i < len(prefix) - 1:
            return self.nodes[c].startsWith(prefix, i + 1)
        return True
        