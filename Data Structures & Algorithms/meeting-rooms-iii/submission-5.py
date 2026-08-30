class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = [(room, 0) for room in range(n)]
        asignment_count = defaultdict(int)
        used = []        
            
        for (start, end) in sorted(meetings, key = lambda x: x[0]):
            while used and (used[0][0] <= start or not available):
                time, room = heapq.heappop(used)
                heapq.heappush(available, (room, time))
            room, time = heapq.heappop(available)
            asignment_count[room] += 1
            actual_start = max(time, start)
            next_available_start = actual_start + (end - start)
            heapq.heappush(used, (next_available_start, room))
        room = max(asignment_count.items(), key = lambda x: x[1])[0]
        return room
        



