"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BF --> create new node and new node for every neighbor
        # DFS
            # recursive chain to create node
            # map oldNode = newNode
        
        new_graph = {} # old : new

        def dfs(graph_node):
            if graph_node in new_graph:
                return new_graph[graph_node]
            if not graph_node:
                return
            
            new_node = Node(graph_node.val)
            new_graph[graph_node] = new_node

            for nei in graph_node.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return new_node
        
        return dfs(node)

# sol = Solution()
# adjList1 = [[2],[1,3],[2]]
# adjList2 = [[]]

# assert sol.cloneGraph(adjList1) ==  [[2],[1,3],[2]]
# assert sol.cloneGraph(adjList2) == [[]]

