class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [0 for i in range(n+1)]
        # # dp[i]表示到达第i个台阶的最小花费, 所要求的就是dp[n]
        # dp[0] = 0
        # dp[1] = 0
        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # return dp[n]

        # 滚动数组
        # len(cost) >= 2
        pre, cur = 0, 0
        for i in range(2, len(cost) + 1):
            nex = min(pre + cost[i-2], cur + cost[i-1])
            pre, cur = cur, nex
        return cur