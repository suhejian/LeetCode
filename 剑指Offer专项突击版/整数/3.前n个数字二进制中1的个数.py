class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(num):
            return sum(1 for i in range(32) if num & (1 << i))
        return [countBit(num) for num in range(n + 1)]