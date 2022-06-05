class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        # 找到第一个>=target的数的索引
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        
        if nums[end] != target:
            return [-1, -1]
        # 找到最后一个<=target的数的索引
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        return [start, left]