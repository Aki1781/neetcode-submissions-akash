class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}


        def dfs(arr_index, index):
            if arr_index == len(triangle):
                return 0
            if (arr_index, index) in dp:
                return dp[(arr_index, index)]
            
            # 2 choices:
                # explore i from current spot
                # explore i + 1 form current spot
            
            res = min(dfs(arr_index + 1, index), dfs(arr_index + 1, index + 1)) + triangle[arr_index][index]
            dp[(arr_index, index)] = res
            return res
        
        return dfs(0, 0)