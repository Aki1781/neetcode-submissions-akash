class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # [2, 4, 5, 8] x = 6
        #     l  r

        left, right = 0, len(arr) - 1

        while right - left >= k:
            # left is > dist
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            # right is > dist
            else:
                right -= 1
        
        return arr[left:right + 1]

