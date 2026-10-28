class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # initial thoughts:
            # the brute force would be doing some tpye of dfs traversal where we search the 8 possible moves
            # we may be able to add memoization to make sure the saem squares are not searched
        directions = [
            [2, 1],
            [2, -1],
            [-2, -1],
            [-2, 1],
            [1, 2],
            [1, -2],
            [-1, 2],
            [-1, -2]
        ]

        x, y = abs(x), abs(y)
        q = deque()
        q.append((0, 0, 0))
        visit = set()
        visit.add((0, 0))

        while q:
            a, b, steps = q.popleft()

            if a == x and b == y:
                return steps
            
            for dr, dc in directions:
                nr, nc = a + dr, b + dc

                if (nr, nc) not in visit and -2 <= nr <= x + 2 and -2 <= nc <= y + 2:
                    q.append((nr, nc, steps + 1))
                    visit.add((nr, nc))
        
        