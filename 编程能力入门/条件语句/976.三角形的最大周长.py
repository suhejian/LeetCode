class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)[::-1]
        def isTri(a, b, c):
            # 判断能否构成三角形
            if a + b > c and a + c > b and b + c > a:
                return True
            else:
                return False
        
        res = 0
        for i in range(len(nums)-2):
            if isTri(sorted_nums[i], sorted_nums[i+1], sorted_nums[i+2]):
                res = sorted_nums[i] + sorted_nums[i+1] + sorted_nums[i+2]
                break
        return res