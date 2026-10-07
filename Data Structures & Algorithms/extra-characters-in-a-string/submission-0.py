class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:   
        # Brute Force
            # determine every substring and compare to dict
            # any chars with zero hits --> increment our count
        
        memo = {len(s) : 0}
        words = set(dictionary)
        count = 0

        def dfs(i):
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]
            
            # skip curr char
            res = 1 + dfs(i + 1)

            for j in range(i, len(s)):
                if s[i : j + 1] in words:
                    res = min(res, dfs(j + 1))
            
            memo[i] = res
            return res
            
        
        return dfs(0)
            
            

