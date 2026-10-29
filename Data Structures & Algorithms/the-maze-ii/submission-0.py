class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        if maze[destination[0]][destination[1]] == 1:
            return -1

        heap = []
        x, y = start
        heap.append((0, x, y))
        heapq.heapify(heap)

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        ROWS, COLS = len(maze), len(maze[0])

        dist = [[float('inf')] * COLS for _ in range(ROWS)]
        dist[x][y] = 0

        while heap:
            distance, r, c = heapq.heappop(heap)

            if distance > dist[r][c]:
                continue

            if r == destination[0] and c == destination[1]:
                return distance
            
            for dr, dc in directions:
                nr, nc = r, c
                steps = 0

                while 0 <= nr + dr < ROWS and 0 <= nc + dc < COLS and maze[nr + dr][nc + dc] != 1:
                    nr += dr
                    nc += dc
                    steps += 1
                
                if (distance + steps) < dist[nr][nc]:
                    heapq.heappush(heap, (distance + steps, nr, nc))
                    dist[nr][nc] = distance + steps
        
        return -1
