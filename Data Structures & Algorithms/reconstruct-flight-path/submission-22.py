class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for origin, destination in sorted(tickets, reverse = True):
            adj[origin].append((destination))

        stack = ['JFK']
        res = []
        while stack:
            node = stack[-1]
            if adj[node]:
                stack.append(adj[node].pop())
            else:
                res.append(stack.pop())
        return res[::-1]