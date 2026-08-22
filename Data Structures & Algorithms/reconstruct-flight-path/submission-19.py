class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for origin, destination in sorted(tickets, reverse = True):
            adj[origin].append((destination))

        path = []
        def dfs(node):
            while adj[node]:
                dst = adj[node].pop()
                dfs(dst)
            path.append(node)
        dfs('JFK')
        #print(path)
        return path[::-1]