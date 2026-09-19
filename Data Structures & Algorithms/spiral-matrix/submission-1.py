class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        layer = 0
        m = len(matrix)
        res = []
        n = len(matrix[0])
        def go(topleft, bottomright):
            top, left = topleft
            bottom, right = bottomright
            added = set()
            R = []
            for j in range(left, right + 1):
                R.append((top, j))
            for i in range(top, bottom + 1):
                R.append( (i, right) )
            for j in range(right, left - 1, -1):
                R.append((bottom, j))
            for i in range(bottom, top - 1, -1):
                R.append((i, left))
            
            for i, j in R:
                if (i, j) not in added:
                    added.add((i, j))
                    res.append(matrix[i][j])
            


        while True:
            topleft = layer, layer
            bottomright = m - 1 - layer, n - 1 - layer
            if topleft[0] <= bottomright[0] and topleft[1] <= bottomright[1]:
                go(topleft, bottomright)
            else:
                break
            
            layer += 1
        return res