class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for t in tasks:
            counts[t] += 1
        h = []
        for k, v in counts.items():
            h.append((1, -v, k))
        heapq.heapify(h)
        cycle = 0
        while h:
            time, remaining, task = heapq.heappop(h)
            remaining *= -1
            cycle = max(time, cycle + 1)
            if remaining > 1:
                heapq.heappush(h, (time + n + 1, -(remaining - 1), task))
        return cycle