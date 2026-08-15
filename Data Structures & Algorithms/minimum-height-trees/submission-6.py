class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        subtree_heights = [0] * n
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parents = {}
        import random
        node = 0
        q = deque([node])
        parents[node] = -1

        while q:
            node = q.popleft()
            children = []
            for child in adj[node]:
                if child == parents[node]:
                    continue
                children.append(child)
            if all(map(lambda x: subtree_heights[x] > 0, children)):
                if len(children) == 0:
                    subtree_heights[node] = 1
                else:
                    subtree_heights[node] = 1 + max([subtree_heights[x] for x in children])
            else:
                q.appendleft(node)
                for child in children:
                    parents[child] = node
                    q.appendleft(child)

        minHeight = float("inf")
        cache = {}
        res = []
        for node in range(n):
            height = subtree_heights[node]
            parent = parents[node]
            length = 1
            prev = node
            while parent != -1:
                height = max(height, length + 1)
                for sibling in adj[parent]:
                    if sibling == prev or parents[sibling] != parent:
                        continue
                    height = max(height, subtree_heights[sibling] + length + 1)
                    #print(node, height, sibling, parent)
                cache[(prev, parent)] = subtree_heights[sibling] + 2
                prev, parent = parent, parents[parent]
                length += 1
            if minHeight == height:
                res.append(node)
            elif minHeight > height:
                res = [node]
                minHeight = height
            else:
                pass
        return res