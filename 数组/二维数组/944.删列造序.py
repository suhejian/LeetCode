class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        chars = "abcdefghijklmnopqrstuvwxyz"
        num_col = len(strs[0])
        num_row = len(strs)
        cnt = 0
        for i in range(num_col):
            # 列遍历
            for j in range(1, num_row):
                # 行遍历
                if chars.index(strs[j][i]) < chars.index(strs[j - 1][i]):
                    cnt += 1
                    break

        return cnt