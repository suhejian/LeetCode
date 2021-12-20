class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res =[]
        for num in set(nums1):
            if num in set(nums2):
                n = min(nums1.count(num), nums2.count(num))
                res += n * [num]
        return res