class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() # (r, c) coordinate
        count = 0

        def dfs(r, c):
            # ending conditions
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == "0":
                return
            
            visit.add((r, c))

            # up, down, right, left
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return


        # loop thru the grid --> 1? --> recurse on the land
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    count += 1

        return count
