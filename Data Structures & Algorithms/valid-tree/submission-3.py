class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cnt = set()
        def dfs(node, parent, path):
            nonlocal cnt
            if node in path:
                return False
            cnt.add(node)
            path.add(node)
            for v in adj[node]:
                if v == parent:
                    continue
                if not dfs(v, node, path):
                    return False
            path.remove(node)
            return True

        if not dfs(0, None, set()):
            return False
        return len(cnt) == n