class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # pre存前缀和, hashmap统计各前缀和出现的次数
        hashmap = {}
        hashmap[0] = 1
        pre = 0
        total = 0   # 计数
        for i in range(len(nums)):
            pre += nums[i]
            total += hashmap.get(pre-k, 0)
            hashmap[pre] = hashmap.get(pre, 0) + 1
        return total