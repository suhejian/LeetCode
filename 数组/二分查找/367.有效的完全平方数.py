class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid < num:
                # mid及之前的需要排除
                left = mid + 1
            else:
                right = mid
        
        return left * left == num