class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeats = set()

        for num in nums:
            if num in repeats:
                return True
            repeats.add(num)
        
        return False