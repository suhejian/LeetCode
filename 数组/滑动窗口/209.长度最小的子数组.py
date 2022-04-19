class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        slow, fast, total = 0, 0, 0
        min_length = len(nums) + 1
        for fast in range(len(nums)):
            total += nums[fast]
            while total >= target:
                min_length = min(min_length, fast - slow + 1)
                total -= nums[slow]
                slow += 1
        return 0 if min_length == len(nums) + 1 else min_length