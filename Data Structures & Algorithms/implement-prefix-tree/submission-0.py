
class PrefixTree:

    def __init__(self, char = "$", ternimal = False):
        self.nodes = {}
        self.char = char
        self.ternimal = ternimal

    def insert(self, word: str) -> None:
        c = word[0]
        if c not in self.nodes:
            self.nodes[c] = PrefixTree(c)
        if len(word) > 1:
            self.nodes[c].insert(word[1:])
        else:
            self.nodes[c].ternimal = True

    def search(self, word: str) -> bool:
        c = word[0]
        if c not in self.nodes:
            return False
        if len(word) > 1:
            return self.nodes[c].search(word[1:])
        else:
            return self.nodes[c].ternimal
        

    def startsWith(self, prefix: str) -> bool:
        c = prefix[0]
        if c not in self.nodes:
            return False
        if len(prefix) > 1:
            return self.nodes[c].startsWith(prefix[1:])
        return True
        