class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # return -1

        n = len(nums)
        start, end = 0, n-1
        if target < nums[start] or target > nums[end]:
            return -1
        while start <= end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1