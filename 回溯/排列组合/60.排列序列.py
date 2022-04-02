class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 会超时的
        # if k == 1:
        #     return "".join(str(x) for x in range(1, n + 1))
        
        # used = [False for _ in range(n)]
        # res = []
        # nums = [i for i in range(1, n + 1)]

        # def dfs(nums, used, path, res):
        #     if len(path) == len(nums):
        #         res.append(path[:])
        #         if len(res) == k:
        #             return "".join(str(x) for x in res[-1])
            
        #     for i in range(len(nums)):
        #         if not used[i]:
        #             used[i] = True
        #             path.append(nums[i])
        #             dfs(nums, used, path, res)
        #             used[i] = False
        #             path.pop()
        
        # dfs(nums, used, [], res)
        # ans = res[k - 1]
        # return "".join(str(x) for x in ans)

        if n == 0:
            return ""
        
        used = [False for _ in range(n + 1)]
        path = []
        # 计算阶乘, factorial[i]表示i的阶乘
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i-1] * i
        
        def dfs(n, k, depth, path):
            if depth == n:
                return
            # 该分支下一共有多少种可能
            cnt = factorial[n - 1 - depth]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(n, k, depth + 1, path)
                # 后面的数没有必要遍历去尝试了
                return
        
        dfs(n, k, 0, path)
        return "".join([str(x) for x in path])