class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums2)):
            key = nums2[i]
            dic[key] = -1
            for j in range(i+1, len(nums2)):
                if nums2[j] > key:
                    dic[key] = nums2[j]
                    break
        return [dic[num] for num in nums1]