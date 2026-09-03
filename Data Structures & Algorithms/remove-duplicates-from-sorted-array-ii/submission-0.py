class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # map of int : count
        # 1 : 2, 2 : 0, 3 : 0
        run_count = {}
        pointer = 0

        for num in nums:
            if num not in run_count:
                run_count[num] = 0
        
        for i in range(len(nums)):
            if run_count[nums[i]] >= 2:
                continue
            else:
                nums[pointer] = nums[i]
                run_count[nums[i]] += 1
                pointer += 1
        
        return pointer
        

