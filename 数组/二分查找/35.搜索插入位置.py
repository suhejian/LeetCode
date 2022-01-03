class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        if target < nums[start]:
            return 0
        elif target > nums[end - 1]:
            return end
        else:
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid
                elif nums[mid] < target:
                    start = mid + 1
            return start
