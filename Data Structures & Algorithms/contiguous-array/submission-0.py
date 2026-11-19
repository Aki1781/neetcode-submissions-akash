class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pass

        # brute force
            # O(n^2) --> We go through every single possible subarray
        
        # [0, 1, 1, 0, 1, 0]
        # [0] --> [0, 1] --> [0, 1, 1] --> [0, 1, 1, 0]

        # dict --> running sum : index seen
        # anytime we see a dup running sum, we take current index - index seen + 1 as our window

        sum_to_index = {0 : -1}
        prefix = [0] * len(nums)
        curr_sum = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr_sum += -1
            else:
                curr_sum += 1

            prefix[i] = curr_sum
        
        for j in range(len(prefix)):
            if prefix[j] in sum_to_index:
                res = max(res, j - sum_to_index[prefix[j]])
            else:
                sum_to_index[prefix[j]] = j
        
        return res
