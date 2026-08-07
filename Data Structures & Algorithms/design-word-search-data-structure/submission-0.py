class Node:
    def __init__(self):
        self.nodes = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = Node()
            curr = curr.nodes[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        q = deque([(self.root, 0)])
        while q:
            node, i = q.popleft()
            if i >= len(word):
                if node.endOfWord:
                    return True
                continue
            c = word[i]
            if c == ".":
                for next in node.nodes.values():
                    q.append((next, i + 1))
            if c in node.nodes:
                q.append((node.nodes[c], i + 1))
            
        return False
                


