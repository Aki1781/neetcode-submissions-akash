class Solution:
    def check(self, nums: List[int]) -> bool:
        flags = 0

        for i in range(len(nums)):
            if nums[(i + 1) % len(nums)] < nums[i]:
                flags += 1
            if flags > 1:
                return False
        
        return True
