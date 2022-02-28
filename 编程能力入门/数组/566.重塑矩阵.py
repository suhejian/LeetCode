class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        nums = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[i]))]
        res = []
        for i in range(r):
            res.append(nums[i*c: (i+1)*c])
        return res