class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #traverse the board
        # pointers:
            # 1) word-point --> letter we are looking for
            # 2) cord --> (r, c) of last matching letter
        # algo:
        # We look for word[word-point]
            # once we find, we set cord to that entry and check the 4 directions.
                # 2 cases
                # 1) we find next letter --> update word-point, save prev cord, and update curr-cord
                # 2) we don't find --> add 1 to base cord

        visit = set()
        ROWS, COLS = len(board), len(board[0])


        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or board[r][c] != word[index]:
                return False
            
            visit.add((r, c))

            res = dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c - 1, index + 1) or dfs(r, c + 1, index + 1)

            visit.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
