class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #for r in matrix:
            #print(r)
        n = len(matrix)
        for size in range(len(matrix) // 2):
            for j in range(size, n - 1 - size):
                top = matrix[size][j]
                right = matrix[j][n - 1 - size]
                bottom = matrix[n-1-size][n - 1 - j]
                left = matrix[n - j - 1][size]
                #print(top, right, bottom, left)
                top, right, bottom, left = left, top, right, bottom
                matrix[size][j] = top
                matrix[j][n - 1 - size] = right
                matrix[n-1-size][n - 1 - j] = bottom
                matrix[n - j - 1][size] = left
                #print("")
                #for r in matrix:
                #    print(r)
        #print("")
        #for r in matrix:
        #    print(r)

        return None