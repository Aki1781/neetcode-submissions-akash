class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in num_set:
                curr = 1 
                while num + 1 in num_set:
                    num = num + 1
                    curr += 1
                max_length = max(max_length, curr)
        
        return max_length