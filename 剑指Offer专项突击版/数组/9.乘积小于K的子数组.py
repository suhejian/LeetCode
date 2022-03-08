class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 滑动窗口, 防止重复计算需要以右边界为准计算
        # ABCX -> X, CX, BCX, ABCX
        start = 0   # 滑动窗口左侧
        res = 0 # 最终结果
        total = 1 # 计算当前积
        for end in range(len(nums)):
            total *= nums[end]
            while start <= end and total >= k:
               total = total // nums[start]
               start += 1
            res += (end - start + 1)
        return res 