class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqaure_nums = [num ** 2 for num in nums]
        return sorted(sqaure_nums)