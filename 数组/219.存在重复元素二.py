class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                # 第一次出现, 记录该数值的索引
                hashmap[nums[i]] = i
            else:
                # 已经出现过一次, 检查索引是否符合要求
                pre = hashmap[nums[i]]
                now = i
                if now - pre <= k:
                    return True
                else:
                    # 更新
                    hashmap[nums[i]] = i
        return False