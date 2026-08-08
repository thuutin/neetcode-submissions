"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = set()
        originalNode = node
        edges = defaultdict(list)
        q = deque([node])
        while q:
            node = q.popleft()
            if node in nodes:
                continue
            nodes.add(node)
            for neibour in node.neighbors:
                edges[node].append(neibour)
                q.append(neibour)
        newNodes = {}
        for node in nodes:
            newNodes[node] = Node(node.val)
        for node, neibours in edges.items():
            for nei in neibours:
                newNodes[node].neighbors.append(newNodes[nei])
        return newNodes[originalNode]
