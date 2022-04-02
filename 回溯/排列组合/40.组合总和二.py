class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        candidates.sort()
        if size == 0:
            return []
        res = []

        def dfs(candidates, begin, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
            for i in range(begin, len(candidates)):
                if candidates[i] > target:
                    break
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(candidates, i + 1, path, res, target - candidates[i])
                path.pop()
        dfs(candidates, 0, [], res, target)
        return res