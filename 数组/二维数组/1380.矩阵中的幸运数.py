class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        """判断某一个元素是不是该行的最小元素，该列的最大元素"""
        r, c = len(matrix), len(matrix[0])
        res = []
        min_row = [min(row) for row in matrix]  # 每一行的最小值
        max_col = [max(col) for col in zip(*matrix)]    # 每一列的最大值
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == min_row[i] == max_col[j]:
                    res.append(x)
        return res