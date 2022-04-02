class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        candidates.sort()
        if size == 0:
            return []
        begin = 0
        res = []
        def dfs(candidates, begin, target, path, res):
            # if target < 0:
            #     return
            if target == 0:
                res.append(path[:])
                return

            for i in range(begin, len(candidates)):
                # 剪枝
                if target - candidates[i] < 0:
                    break
                path.append(candidates[i])
                dfs(candidates, i, target-candidates[i], path, res)
                path.pop()
        dfs(candidates, begin, target, [], res)
        return res