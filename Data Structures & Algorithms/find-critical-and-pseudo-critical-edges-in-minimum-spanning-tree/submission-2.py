class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [ (u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key = lambda x: x[2])
        def min_spanning_tree_skip_edge(skip_index, force):
            root = [i for i in range(n)]
            size = [1] * n
            def find(x):
                if root[x] != x:
                    root[x] = find(root[x])
                return root[x]

            def union(x, y):
                rootx = find(x)
                rooty = find(y)
                if rootx == rooty:
                    return False
                if size[rooty] > size[rootx]:
                    rootx, rooty = rooty, rootx
                root[rooty] = root[rootx]
                size[rootx] += size[rooty]
                return True
            total = 0
            if force != -1:
                for (u, v, w, i) in edges:
                    if i == force and union(u, v):
                        total += w                

            for (u, v, w, i) in edges:
                if i == skip_index or i == force:
                    continue
                if union(u, v):
                    total += w                

            return total

        whole_tree_weight = min_spanning_tree_skip_edge(-1, -1)

        critical = set()
        pseudo = set()
        for i in range(len(edges)):
            weight = min_spanning_tree_skip_edge(edges[i][3], -1)
            if weight != whole_tree_weight:
                critical.add(edges[i][3])
        for i in range(len(edges)):
            if edges[i][3] not in critical:
                weight = min_spanning_tree_skip_edge(-1, edges[i][3])
                if weight == whole_tree_weight:
                    pseudo.add(edges[i][3])
            
        return [list(critical), list(pseudo)]