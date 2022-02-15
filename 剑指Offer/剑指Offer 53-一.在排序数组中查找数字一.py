class Solution:
    def search(self, nums: List[int], target: int) -> int:
        from collections import Counter

        counter = Counter(nums)
        return counter[target]