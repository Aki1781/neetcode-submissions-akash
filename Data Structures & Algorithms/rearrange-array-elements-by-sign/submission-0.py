class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pointer = 0

        for num in nums:
            if num > 0 and pointer < len(nums):
               res[pointer] = num
               pointer += 2

        pointer = 1

        for num in nums:
            if num < 0 and pointer < len(nums):
                res[pointer] = num
                pointer += 2
        
        return res
         