class NumArray:

    def __init__(self, nums: List[int]):
        # 前缀和
        self.pre_sums = [0]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.pre_sums.append(total)


    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sums[right+1] - self.pre_sums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)