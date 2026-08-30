class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = [(0, room) for room in range(n)]
        asignment_count = defaultdict(int)
        
        for (start, end) in sorted(meetings):
            while available and available[0][0] < start:
                time, room = heapq.heappop(available)
                heapq.heappush(available, (start, room))
            time, room = heapq.heappop(available)
            asignment_count[room] += 1
            actual_start = max(time, start)
            delay = actual_start - start
            next_available = end + delay
            heapq.heappush(available, (next_available, room))
        room = max(asignment_count.items(), key = lambda x: x[1])[0]
        return room