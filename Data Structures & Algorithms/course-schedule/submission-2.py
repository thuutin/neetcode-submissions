class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for u, v in prerequisites:
            indegree[u] += 1
            adj[v].append(u)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        C = 0
        while q:
            course = q.popleft()
            C += 1
            for dependent in adj[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        return C == numCourses       