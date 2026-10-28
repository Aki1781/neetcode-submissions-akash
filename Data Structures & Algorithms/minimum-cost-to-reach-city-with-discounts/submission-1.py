class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        # cities from 0 to n-1
        # given one way highways from a to b with cost toll
        # we have a certain number of discount coupons (toll // 2)
        # we want the least cost path to reach n-1 city

        # we want to do a modified dikjstras algorithm

        dist = [[float('inf')] * (discounts + 1) for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)] # cost, city, discounts used
        heapq.heapify(heap)

        graph = defaultdict(list)

        for a, b, toll in highways:
            graph[a].append((b, toll))
            graph[b].append((a, toll))
        
        while heap:
            # don't use discount
            cost, city, used = heapq.heappop(heap)

            if cost > dist[city][used]:
                continue

            if city == n - 1:
                return cost
            
            for nei, toll in graph[city]:
                new_cost = cost + toll

                if new_cost < dist[nei][used]:
                    dist[nei][used] = new_cost
                    heapq.heappush(heap, (new_cost, nei, used))

                # use discount
                if used < discounts:
                    new_discount_cost = cost + (toll // 2)

                    if new_discount_cost < dist[nei][used + 1]:
                        dist[nei][used + 1] = new_discount_cost
                        heapq.heappush(heap, (new_discount_cost, nei, used + 1))
        

        return -1
        

        
