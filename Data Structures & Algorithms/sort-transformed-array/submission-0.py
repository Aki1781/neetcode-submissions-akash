class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        for index, num in enumerate(nums):
            new_a = a * (num ** 2)
            new_b = b * num
            new_num = new_a + new_b + c

            nums[index] = new_num
        
        return sorted(nums)