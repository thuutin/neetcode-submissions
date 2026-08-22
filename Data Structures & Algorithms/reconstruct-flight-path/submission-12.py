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
        
        def dfs(node, path):
            path.append(node)
            if all(map(lambda x: x[1] in visited, adj[node])):
                return True
            paths = []
            for  nei, index  in adj[node]:
                if index in visited:
                    continue
                path1 = []
                visited.add(index)
                paths.append(path1)
                dfs(nei, path1)
            for p in paths[::-1]:
                path.extend(p)
            
        a = []
        dfs('JFK', a)
        print(a)
        return a
