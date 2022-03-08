class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归会超时
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        if n <= 2:
            return n
        a, b = 1, 2
        res = 0
        for i in range(n-2):
            res = a + b
            a, b = b, res
        return res