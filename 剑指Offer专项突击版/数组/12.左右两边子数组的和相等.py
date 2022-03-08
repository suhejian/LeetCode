class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, res = sum(nums), -1
        pre = 0
        for i in range(len(nums)):
            if pre == total - pre - nums[i]:
                return i 
            pre += nums[i]
        return res