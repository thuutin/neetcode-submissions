class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for origin, destination in tickets :
            adj[origin].append((destination))

        for k in adj.keys():
            adj[k] = sorted(adj[k], reverse= True)
        
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
            while adj[node]:
                dst = adj[node].pop()
                dfs(dst)
            path.append(node)
        dfs('JFK')
        #print(path)
        return path[::-1]