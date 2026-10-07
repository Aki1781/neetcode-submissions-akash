class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s) : True}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = False

            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        res = True
            dp[i] = res
            return res

        return dfs(0)