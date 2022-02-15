class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        res = {nums[0], }
        for i in range(1, len(nums)):
            if not nums[i] in res:
                res.add(nums[i])
            else:
                return nums[i]