class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isArea(grid, r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        def dfs(grid, r, c):
            if not isArea(grid, r, c):
                return 
            
            if grid[r][c] != '1':
                return
            
            grid[r][c] = '2'  # 访问过的陆地置为2
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        
        return count