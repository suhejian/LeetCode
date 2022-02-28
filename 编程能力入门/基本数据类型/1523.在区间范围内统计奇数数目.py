class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 前缀和
        # 计算[0-x]之前的奇数个数: (x+1) // 2
        prex = lambda x: (x + 1) // 2
        return prex(high) - prex(low-1)
        