class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        if num == 1:
            return False
        nums = [1]
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                nums.append(i)
                nums.append(int(num / i))
        nums = list(set(nums))
        return sum(nums) == num