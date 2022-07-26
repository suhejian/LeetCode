class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def isBoundary(grid, r, c):
            return 0 == r or 0 == c or r == len(grid)- 1 or c == len(grid[0]) - 1
        
        def dfs(grid, r, c):
            # 用来判断从grid[r][c]出发能不能找到封闭岛屿
            if isBoundary(grid, r, c) and grid[r][c] == 0:
                # 在边界位置肯定不是封闭岛屿
                return False
            
            flag = True
            grid[r][c] = 1
            for (x, y) in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 1:
                    continue
                flag = flag & dfs(grid, x, y)
            return flag
        
        count = 0
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == 0:
                    if dfs(grid, i, j):
                        count += 1
        
        return count
            