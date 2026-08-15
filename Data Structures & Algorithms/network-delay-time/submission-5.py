class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = [(0, k)]
        D = {k: 0}
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while pq:
            time, node = heapq.heappop(pq)
            if time > D[node]:
                continue
            for nei, weight in adj[node]:
                if nei in D and D[nei] <= time + weight:
                    continue
                D[nei] = time + weight
                heapq.heappush(pq, (time + weight, nei))
        if len(D) == n:
            return max(D.values())
        return -1