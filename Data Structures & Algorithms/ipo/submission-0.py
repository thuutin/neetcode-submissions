class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = [(c, p) for (c, p) in zip(capital, profits)]
        projects.sort(key = lambda x: -x[0])
        while k > 0:
            # add eligible projects
            while projects and projects[-1][0] <= w:
                pCapital, pProfit = projects.pop()
                heapq.heappush(heap, -pProfit)
            # pick a project
            if not heap:
                break
            p = -heapq.heappop(heap) # empty?
            w += p
            k -= 1
        return w