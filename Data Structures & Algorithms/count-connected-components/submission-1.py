class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            
            parents[root_x] = root_y

        for u, v in edges:
            union(u, v)
        
        components = set()
        for i in range(n):
            components.add(find(i))
        return len(components)