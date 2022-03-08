class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        pre = 0 # 计算前缀和
        hashmap = {}    # 记录该前缀和第一次出现的位置
        hashmap[0] = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                pre += 1
            if nums[i] == 0:
                pre -= 1
            if pre in hashmap:
                # 如果该前缀和已经出现过一次, 当前和-之前的前缀和 = 0
                max_length = max(max_length, i - hashmap[pre])
            else:
                hashmap[pre] = i
        return max_length