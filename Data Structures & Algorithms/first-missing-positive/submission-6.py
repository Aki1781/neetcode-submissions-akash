class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        boolean_arr = [False] * (len(nums))

        for num in nums:
            if num > 0 and num <= len(nums):
                boolean_arr[num - 1] = True
        
        for j in range(1, len(nums) + 1):
            if not boolean_arr[j - 1]:
                return j
        
        return len(nums) + 1