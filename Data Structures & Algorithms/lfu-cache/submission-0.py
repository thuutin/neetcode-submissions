from sortedcontainers import SortedDict 
class LFUCache:

    def __init__(self, capacity: int):
        self.values = {}
        self.use_freq = defaultdict(int)
        self.freq_heap = [] # (freq, key)
        self.capacity = capacity
        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self.time += 1
        self.use_freq[key] += 1
        heapq.heappush(self.freq_heap, (self.use_freq[key], self.time, key))
        return self.values[key]
                  
    def ensureCapacity(self, incommingKey):
        if incommingKey in self.values:
            return
        while len(self.values) == self.capacity:
            freq, timestamp, key = heapq.heappop(self.freq_heap)
            if freq == self.use_freq[key]:
                del self.values[key]
                del self.use_freq[key]

    def put(self, key: int, value: int) -> None:
        self.time += 1
        self.ensureCapacity(key)
        # insert
        self.values[key] = value
        self.use_freq[key] += 1
        heapq.heappush(self.freq_heap, (self.use_freq[key], self.time, key))
        # handle eviction
     

        # get smallest freq elements
        # get the one with smallest timestamps


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)