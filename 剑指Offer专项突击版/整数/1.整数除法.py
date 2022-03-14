class Solution:
    def divide(self, a: int, b: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31-1
        if a == INT_MIN and b == -1:
            return INT_MAX
        # 符号
        abs_a, abs_b, res = abs(a), abs(b), 0
        for i in range(31, -1, -1):
            if (abs_b << i) <= abs_a:
                res += (1 << i)
                abs_a -= (abs_b << i)
        return res if (a > 0) == (b > 0) else -res