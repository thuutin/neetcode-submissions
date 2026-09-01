from sortedcontainers import SortedDict 
class LFUCache:

    def __init__(self, capacity: int):
        self.use_freq = defaultdict(lambda: (0, None))
        self.freq_heap = [] # (freq, key)
        self.capacity = capacity
        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.use_freq:
            return -1
        self.time += 1
        self.use_freq[key] = (self.use_freq[key][0] + 1), self.use_freq[key][1] 
        heapq.heappush(self.freq_heap, (self.use_freq[key], self.time, key))
        return self.use_freq[key][1]
        
    def ensureCapacity(self, incommingKey):
        if incommingKey in self.use_freq:
            return
        while len(self.use_freq) >= self.capacity:
            freq, timestamp, key = heapq.heappop(self.freq_heap)
            if freq == self.use_freq[key]:
                del self.use_freq[key]

    def put(self, key: int, value: int) -> None:
        self.time += 1
        self.ensureCapacity(key)
        # insert
        self.use_freq[key] = (self.use_freq[key][0] + 1), value
        heapq.heappush(self.freq_heap, (self.use_freq[key], self.time, key))


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)