class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BF --> mark adj rotten fruits and loop repeatedly
        # BFS
            # preprocessing --> counting fresh fruits and keep track of rotten
            # multi-source bfs solution
        
        fresh = 0 # number of fresh fruit
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        total_time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0)) # tuple (r, c, time)
        

        while queue:
            row, col, time = queue.popleft()
            total_time = time

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                new_time = time + 1

                if new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < COLS and grid[new_row][new_col] == 1:
                    queue.append((new_row, new_col, new_time))
                    grid[new_row][new_col] = 2
                    fresh -= 1
        
        return total_time if fresh == 0 else -1
