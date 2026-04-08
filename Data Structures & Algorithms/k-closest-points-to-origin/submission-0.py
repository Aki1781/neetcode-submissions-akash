import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # BF --> O(N^2)
        # Use heap to always get closest points
        # heap can store (distance, point)

        heap = []
        res = []

        for point in points:
            x, y = point
            dist = math.sqrt(((0 - x)**2) + ((0 - y)**2))

            heap.append((dist, point))
        
        heapq.heapify(heap)

        while len(res) < k:
            distance, cord = heapq.heappop(heap)
            x, y = cord
            res.append([x, y])
        
        return res
