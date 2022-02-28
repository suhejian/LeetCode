class Solution:
    def arraySign(self, nums: List[int]) -> int:
        from collections import Counter
        sig_nums = []
        for num in nums:
            if num == 0:
                sig_nums.append(0)
            if num < 0:
                sig_nums.append(-1)
            if num > 0:
                sig_nums.append(1)
        counter = Counter(sig_nums)
        if counter.get(0):
            return 0
        if counter.get(-1) and counter.get(-1) % 2 == 1:
            return -1
        else:
            return 1