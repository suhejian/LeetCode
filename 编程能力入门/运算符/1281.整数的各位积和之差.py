class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = []
        while n:
            nums.append(n % 10)
            n = n // 10
        mul = 1
        for i in range(len(nums)):
            mul *= nums[i]
        
        return mul - sum(nums)