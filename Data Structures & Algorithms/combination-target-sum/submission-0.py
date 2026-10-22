class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []


        def dfs(curr, curr_sum, start):
            if curr_sum > target:
                return
            if curr_sum == target:
                combos.append(curr.copy())
                return

            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(curr, curr_sum + nums[i], i)
                curr.pop()
            
        
        dfs([], 0, 0)
        return combos
    