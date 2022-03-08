class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # 直接暴力会超时
            # for j in range(i+1, len(nums)):
            #     for k in range(j+1, len(nums)):
            #         if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0 and [sorted_nums[i], sorted_nums[j], sorted_nums[k]] not in res:
            #             res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
            target = -nums[i]
            start, end = i+1, len(nums)-1
            while start < end:
                if nums[start] + nums[end] == target:
                    if [nums[i], nums[start], nums[end]] not in res:
                        res.append([nums[i], nums[start], nums[end]])
                    # 去重
                    while start < end:
                        start = start + 1
                        if nums[start-1] != nums[start]: break
                    while start < end:
                        end = end - 1
                        if nums[end+1] != nums[end]: break
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    start += 1
        return res