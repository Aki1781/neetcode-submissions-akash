"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph_copy = {} # node --> neighbors

        def dfs(graph_node):
            if graph_node in graph_copy:
                return graph_copy[graph_node]
            if not graph_node:
                return
            
            new_node = Node(graph_node.val)
            graph_copy[graph_node] = new_node

            for neighbor in graph_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            
            return new_node
        
        return dfs(node)
        

            