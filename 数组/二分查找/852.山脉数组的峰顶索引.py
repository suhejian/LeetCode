class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # for i in range(1, len(arr)):
        #     if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        #         return i

        left, right = 1, len(arr) - 2
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid + 1]:
                # mid + 1及以后的排除
                right = mid
            else:
                # mid及之前的排除
                left = mid + 1
        return right
