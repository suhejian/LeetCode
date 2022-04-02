class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        size = len(nums)
        used = [False for _ in range(size)]
        # 保存结果
        res = []
        def dfs(nums, size, depth, path, used, res):
            # depth用来标记遍历到哪一步
            # path是符合要求的结果, 全局只有这一个变量
            # used标记哪些元素已经用过
            if depth == size:
                res.append(path[:])
                return 
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth+1, path, used, res)

                    # 还原到之前的状态
                    used[i] = False
                    path.pop()

        
        dfs(nums, size, 0, [], used, res)
        return res