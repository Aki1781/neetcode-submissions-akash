class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        heap = []

        for key, value in count.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)

        while len(res) < k:
            freq, val = heapq.heappop(heap)
            res.append(val)
        
        return res


