class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口, 先移动右端点至符合条件，然后再移动左端点
        # 如此反复
        start, end = 0, 0
        min_length = len(nums) + 1
        total = 0
        while end < len(nums):
            total += nums[end]
            ####################################
            # 中间这段代码用来移动左端点
            while total >= target:
                min_length = min(min_length, end - start + 1)
                total -= nums[start]
                start += 1
            ####################################
            end += 1
        return 0 if min_length == len(nums) + 1 else min_length