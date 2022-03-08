class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        p, q, r, v = 0, 1, 1, 2
        for i in range(n-3):
            p, q, r = q, r, v
            v = p + q + r 
        return v