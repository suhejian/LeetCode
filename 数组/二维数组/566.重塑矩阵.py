class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        raw_r, raw_c = len(mat), len(mat[0])
        if raw_r * raw_c != r * c:
            return mat
 
        all_elements = []
        for i in range(raw_r):
            for j in range(raw_c):
                all_elements.append(mat[i][j])
        
        res = [all_elements[i: i+c] for i in range(0, len(all_elements), c)]

        return res