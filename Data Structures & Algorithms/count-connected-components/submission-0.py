class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { node : [] for node in range(n) }
        num_comps = 0
        visit = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(vertex):
            if vertex in visit:
                return
            
            visit.add(vertex)

            for neighbor in adj[vertex]:
                if neighbor not in visit:
                    dfs(neighbor)
            
            return
        

        for node in range(n):
            if node not in visit:
                num_comps += 1
                dfs(node)
        
        return num_comps
