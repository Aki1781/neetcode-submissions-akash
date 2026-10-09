class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # we use some graph traversal/recursion to figure out the neighbors. The question is how can we traverse in legographical order?
        graph = defaultdict(list)
        res = []
        visit = set()

        for edge in tickets:
            from_i, to_i = edge

            if from_i not in graph:
                graph[from_i] = []
            
            graph[from_i].append(to_i)
        
        for node, neighbors in graph.items():
            graph[node].sort(reverse=True)

        def dfs(t):
            if not t:
                return
            
            while graph[t]:
                neighbor = graph[t].pop()    
                dfs(neighbor)

            res.append(t)

            return t
        
        dfs("JFK")
        return res[::-1]
            

            

            


