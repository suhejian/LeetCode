class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        res = set(list(range(n))) - set(nums)
        return list(res)[0]