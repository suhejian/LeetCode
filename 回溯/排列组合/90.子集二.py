class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        res = []
        begin = 0
        used = [False for _ in range(size)]

        def dfs(nums, path, res, begin, used):
            if len(path) <= len(nums):
                res.append(path[:])
            
            for i in range(begin, len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, path, res, i + 1, used)
                    path.pop()
                    used[i] = False
        
        dfs(nums, [], res, begin, used)
        return res