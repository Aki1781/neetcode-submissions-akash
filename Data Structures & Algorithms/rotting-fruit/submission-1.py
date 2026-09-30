class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh_count = 0
        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_count += 1
        

        while queue:
            r, c, time = queue.popleft()
            res = time

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if (nr >= 0 and nr < len(grid)) and (nc >= 0 and nc < len(grid[0])) and grid[nr][nc] == 1:
                    queue.append((nr, nc, time + 1))
                    grid[nr][nc] = 2
                    fresh_count -= 1
        
        if fresh_count == 0:
            return res
        else:
            return -1

            

