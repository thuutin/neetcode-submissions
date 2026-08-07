class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #(4 ^ k) * m * n * len(words) 
        #4^10 * 30k * 12 * 12
        m = len(board)
        n = len(board[0])
        class Node:
            def __init__(self):
                self.children = {}
        
        root = Node()

        def search(word):
            curr = root
            for c in word:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return True

        ## build trie
        def backtrack(i, j, path, trie):
   
            path.add((i, j))
            c = board[i][j]
            if c not in trie.children:
                trie.children[c] = Node()
            node = trie.children[c]

            for di, dj in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m:
                    continue
                if nj < 0 or nj >= n:
                    continue
                if (ni, nj) in path:
                    continue
                if len(path) >= 10:
                    break
                c = board[ni][nj]
                backtrack(ni, nj, path, node)
            path.remove((i, j))
            

        for i in range(len(board)):
            for j in range(len(board[i])):
                path = set()
                backtrack(i, j, path, root)
        
        res = []
        for word in words:
            if search(word):
                res.append(word)
        return res
