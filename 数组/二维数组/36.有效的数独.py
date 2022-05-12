class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 用于记录每行, 每列, 每个box中的元素是否出现过
        # 本质是HashMap
        record_r, record_c = defaultdict(set), defaultdict(set)
        record_mid = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                val = board[i][j]
                box_num = i // 3 * 3 + j // 3
                if val in record_r[i] or val in record_c[j] or val in record_mid[box_num]:
                    return False
                
                # val在第i行已经出现
                record_r[i].add(val)
                # val在第j列已经出现
                record_c[j].add(val)
                # val在第box_num个方块中已经出现
                record_mid[box_num].add(val)
        
        return True