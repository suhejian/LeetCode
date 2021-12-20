class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * len(nums) # dp[i]表示以i结尾的最大连续子数组和
        res = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
        
        return res