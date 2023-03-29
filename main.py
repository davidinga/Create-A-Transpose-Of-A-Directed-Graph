"""
Given a strongly connected directed graph, return its transpose. The graph will be given as a reference to one of its nodes; the rest of the graph can be discovered by walking its edges.

Constraints:

1 <= number of nodes <= 315
Node values are unique integers, and 1 <= node value <= number of nodes
No multiple edges (connecting any pair of nodes in one direction) or self loops (edges connecting a node with itself) in the input graph
"""

class GraphNode:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    
def create_transpose(node) -> int:
    adjList = {}
    
    def dfs(node) -> GraphNode:
        if not node: 
            return None
            
        if node.value in adjList:
            return adjList[node.value]
        
        copy = GraphNode(node.value)
        
        adjList[copy.value] = copy
        
        for neighbor in node.neighbors:
            neighborCopy = dfs(neighbor)
            neighborCopy.neighbors.append(copy)
        
        return copy
        
    return dfs(node)