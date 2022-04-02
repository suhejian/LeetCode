class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        size = len(nums)
        res = []
        
        def dfs(nums, begin, k, path, res):
            if len(path) == k:
                res.append(path[:])
            
            for i in range(begin, len(nums)):
                path.append(nums[i])
                dfs(nums, i + 1, k, path, res)
                path.pop()
        
        dfs(nums, 0, k, [], res)
        return res