class Solution:
    def hammingWeight(self, n: int) -> int:
        # 得到二进制字符串，然后统计'1'的个数
        # str_n = bin(n)
        # total = 0
        # for i in range(len(str_n)):
        #     if str_n[i] == '1':
        #         total += 1
        # return total

        # 循环求每一位是否为1
        return sum(1 for i in range(32) if n & (1 << i))