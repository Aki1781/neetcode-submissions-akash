class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for p in points:
            x, y = p
            distance = math.sqrt(((x - 0)**2) + ((y - 0)**2))

            heap.append((distance, x, y))
        
        heapq.heapify(heap)

        while k > 0:
            distance, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        
        return res