class Solution:
    def isHappy(self, n: int) -> bool:
        cur = []   # 记录已经出现过的数
        def get_num(n):
            nums = []
            while n > 0:
                nums.append(n % 10)
                n = n // 10
            return nums[::-1]
        while n != 1:
            if n in cur:
                # 这个数已经出现过，会导致死循环
                return False
            cur.append(n)
            nums = get_num(n)
            n = sum(num * num for num in nums)
        return True