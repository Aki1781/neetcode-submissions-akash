class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
            # three loops to find a certain triplet --> if sum if zero, we add to our result
            # O(n^3)
        
        # solution
            # target = -1 --> we look for pair that sums to +1
            # loop through the nums array with each element being our target
            # determine the pairs for said target and add triplets to our result
        
        result = [] # hold our triplets
        nums.sort()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                threeSum = nums[left] + nums[i] + nums[right]
                # threeSum > 0
                if threeSum > 0:
                    right -= 1
                # threeSum < 0
                elif threeSum < 0:
                    left += 1
                # threeSum == 0
                else:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        

        return result


