class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # do 2 topological sortings of k vertexes with rol/col conditions as edges
        # 
        def toposort(edges, out):
            indegree = defaultdict(int)
            a = set(range(1, k + 1))
            adj = defaultdict(list)
            for u, v in edges:
                indegree[v] += 1
                if v in a:
                    a.remove(v)
                adj[u].append(v)
            if not a:
                return None
            queue = deque(a)
            i = 0
            #print(queue)
            while queue:
                x = queue.popleft()
                out[x] = i
                i += 1
                while adj[x]:
                    v = adj[x].pop()
                    if indegree[v] == 1:
                        queue.append(v)
                    else:
                        indegree[v] -= 1
            return out

            # return a valid order or None if cycle exists
        
        # build the matrix
        horizontal_order = {}
        if not toposort(colConditions, horizontal_order):
            return []
        vertical_order = {}
        if not toposort(rowConditions, vertical_order):
            return []
        
        cols = horizontal_order
        rows = vertical_order
        res = [[0] * k for _ in range(k)]
        for x in range(1, k + 1):
            r = rows[x]
            c = cols[x]
            res[r][c] = x
        return res