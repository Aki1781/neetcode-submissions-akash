class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_seen = 0

        # left > right --> right
        # right > left --> left
        # == then move left

        while left <= right:
            max_seen = max(max_seen, (right - left) * min(heights[left], heights[right]))

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] <= heights[right]:
                left += 1
        
        return max_seen