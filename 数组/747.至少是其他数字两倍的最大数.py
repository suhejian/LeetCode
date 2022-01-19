class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sorted_nums = sorted(nums)
        max_num = sorted_nums[-1]
        if max_num >= 2 * sorted_nums[-2]:
            return nums.index(max_num)
        return -1