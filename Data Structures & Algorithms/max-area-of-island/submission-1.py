class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0


        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r, c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r, c))
            
            return (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1)



        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res