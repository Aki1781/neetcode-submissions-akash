class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = set()
        nums.sort()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    if (nums[i], nums[left], nums[right]) not in track:
                        track.add((nums[i], nums[left], nums[right]))
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
        
        return res

