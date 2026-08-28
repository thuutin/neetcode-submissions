class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # do 2 topological sortings of k vertexes with rol/col conditions as edges
        # 
        def toposort(edges):
            indegree = defaultdict(int)
            a = set(range(1, k + 1))
            adj = defaultdict(list)
            for u, v in edges:
                indegree[v] += 1
                a.discard(v)
                adj[u].append(v)
            res = []
            queue = deque(a)
            if not queue:
                return None
            #print(queue)
            while queue:
                x = queue.popleft()
                res.append(x)
                for v in adj[x]:
                    indegree[v] -= 1
                    if indegree[v] <= 0:
                        queue.append(v)
            return res

            # return a valid order or None if cycle exists
        
        # build the matrix
        vertical_order = toposort(rowConditions)
        horizontal_order = toposort(colConditions)

        if not vertical_order or not horizontal_order:
            return []

        cols = {}
        rows = {}
        for i, x in enumerate(vertical_order):
            rows[x] = i
        for i, x in enumerate(horizontal_order):
            cols[x] = i
        
        res = [[0] * k for _ in range(k)]
        for x in range(1, k + 1):
            r = rows[x]
            c = cols[x]
            res[r][c] = x
        return res