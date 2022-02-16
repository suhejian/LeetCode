class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # from collections import Counter

        # # 统计每个数出现的次数
        # counter = Counter(nums)
        # for num in counter:
        #     if counter[num] == 1:
        #         return num

        # 方法二, 得到结果的第i位的二进制数
        ans = 0
        for i in range(32):
            # (x >> i) & 1 得到x的第i位二进制数
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
