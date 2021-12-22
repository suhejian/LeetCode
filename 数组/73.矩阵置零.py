class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        record_r = [False for i in range(r)]
        record_c = [False for i in range(c)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    record_r[i] = True
                    record_c[j] = True
        
        for i in range(r):
            for j in range(c):
                if record_r[i] or record_c[j]:
                    matrix[i][j] = 0