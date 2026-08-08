class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for u, v in prerequisites:
            indegree[v] += 1
            adj[u].append(v)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for dependent in adj[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        if len(res) < numCourses:
            return []
        return res[::-1]