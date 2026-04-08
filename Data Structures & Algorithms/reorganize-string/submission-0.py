class Solution:
    def reorganizeString(self, s: str) -> str:
        # BF --> O(n^2)
        # Heap --> O(n)
        # heap will store (count, letter)
        # ties broken based on previous letter

        count = Counter(s)
        res = ""
        heap = []

        for key, value in count.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)

        prev = None
        while heap or prev:
            if prev and not heap:
                return ""

            count_of_char, char_to_add = heapq.heappop(heap)
            res += char_to_add
            
            current_count = count_of_char + 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if current_count < 0:
                prev = (current_count, char_to_add)
        
        return res