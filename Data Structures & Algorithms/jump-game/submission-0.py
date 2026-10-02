class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums --> nums[i] = how far we can jump
        # False --> can't reach end, True --> can reach end

        # intuition --> can we reach index i for i in n?

        # think goal post

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False