class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        begin = 0

        def dfs(nums, res, path, begin):
            if len(path) <= len(nums):
                res.append(path[:])
            
            for i in range(begin, len(nums)):
                # if i > 0 and nums[i] == nums[i-1]:
                #     continue
                path.append(nums[i])
                dfs(nums, res, path, i + 1)
                path.pop()
        dfs(nums, res, [], begin)
        return res