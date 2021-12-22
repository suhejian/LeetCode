class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        init_res = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            init_res.append(temp)
        # return init_res

        for i in range(2, numRows):
            for j in range(1, i):
                init_res[i][j] = init_res[i-1][j] + init_res[i-1][j - 1]
        return init_res