class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            nums[i] *= -1

        heapq.heapify(nums)

        while count < k - 1:
            heapq.heappop(nums)
            count += 1
        
        return heapq.heappop(nums) * -1