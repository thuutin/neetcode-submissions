class Node:
    def __init__(self):
        self.childen = {}
        self.end = False
class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for cc in word:
            if cc not in curr.childen:
                curr.childen[cc] = Node()
            curr = curr.childen[cc]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for cc in word:
            if cc not in curr.childen:
                return False
            curr = curr.childen[cc]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for cc in prefix:
            if cc not in curr.childen:
                return False
            curr = curr.childen[cc]
        return True
        