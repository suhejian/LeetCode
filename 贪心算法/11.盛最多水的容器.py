class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i, j = 0, len(height) - 1
        while i < j:
            # 总是移动短板
            if height[i] < height[j]:
                ans = max(ans, (j-i) * height[i])
                i += 1
            else:
                ans = max(ans, (j-i) * height[j])
                j -= 1
        return ans
