class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k, path):
            c = word[k]
            if board[i][j] != c:
                return False
            if k == len(word) - 1:
                return True
            path.add((i, j))
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= len(board):
                    continue
                if nj < 0 or nj >= len(board[i]):
                    continue
                if (ni, nj) in path:
                    continue

                if backtrack(ni, nj, k + 1, path):
                    return True
            path.remove((i, j))
            return False
            

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j, 0, set()):
                    return True
        return False
            