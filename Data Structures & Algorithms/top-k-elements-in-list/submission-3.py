class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = Counter(nums)
        heap = []
        result = []

        for num, freq in nums_map.items():
            heap.append((freq, num))
        
        heapq.heapify_max(heap)

        while k != 0:
            freq, num = heapq.heappop_max(heap)
            result.append(num)
            k -= 1

        return result


