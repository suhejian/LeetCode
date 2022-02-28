class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                
            fast += 1
        # 0的个数：fast - slow + 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1