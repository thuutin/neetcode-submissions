class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q = deque([(0, None)])
        visit = set([0])
        while q:
            node, parent = q.popleft()
            for neibour in adj[node]:
                if neibour == parent:
                    continue
                if neibour in visit:
                    return False
                visit.add(neibour)
                q.append((neibour, node))
        return len(visit) == n
