class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        c = Counter()
        for index, (origin, destination) in enumerate(tickets):
            adj[origin].append((destination,  index))
            c[(origin, destination)] += 1

        for k in adj.keys():
            adj[k] = sorted(adj[k])
        
        visited = set() # 1, 3, 4, 5, 6, 2
        #1, 4, 5, 6, 2, 3
        # 1, 4, 5, 6, 2, 3
 
        #      c
        #      |3 up  
        #a 1-> b 2<- d 
        #     4|    |6up
        #     e 5-> f   
        path = []
        def dfs(node):
            for  nei, index  in adj[node]:
                if index in visited:
                    continue
                visited.add(index)
                dfs(nei)
            path.append(node)
        dfs('JFK')
        return path[::-1]
