class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {(len(s1), len(s2)) : True}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = False
            if i < len(s1) and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    res = True
            if j < len(s2) and s2[j] == s3[i + j]:
                if dfs(i, j + 1):
                    res = True
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0)
            

