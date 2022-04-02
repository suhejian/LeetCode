class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        size = len(nums)
        res = []
        used = [False for _ in range(size)]
        nums.sort()
        def dfs(nums, size, depth, used, path ,res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:

                    # 剪枝
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth+1, used, path, res)

                    used[i] = False
                    path.pop()
        dfs(nums, size, 0, used, [], res)
        return res