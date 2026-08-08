class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        good = [False] * numCourses
        def dfs(which, path):
            if which in path:
                good[which] = False
                return False
            if good[which]:
                return True
            path.add(which)
            for d in adj[which]:
                if not dfs(d, path):
                    return False
            good[which] = True
            path.remove(which)
            return True

        for i in range(numCourses):

            if not dfs(i, set()):
                return False
        return True
        