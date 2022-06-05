class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x == 2:
            return 1
        start, end = 1, x - 1
        while start < end:
            mid = start + (end - start) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid
            elif mid * mid < x:
                start = mid + 1
        return start - 1