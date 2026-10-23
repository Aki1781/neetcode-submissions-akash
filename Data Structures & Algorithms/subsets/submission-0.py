class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []


        def dfs(s, start):
            subsets.append(s.copy())

            for i in range(start, len(nums)):
                s.append(nums[i])
                dfs(s, i + 1)
                s.pop()


        dfs([], 0)
        return subsets