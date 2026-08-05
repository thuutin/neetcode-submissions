class LRUCache:

    def __init__(self, capacity: int):
        self.H = {}
        self.t = 0
        self.q = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.H:
            return -1
        self.t += 1
        val, _ = self.H[key]
        self.H[key] = (val, self.t)
        self.q.append((key, self.t))
        return val

        

    def put(self, key: int, value: int) -> None:
        self.t += 1
        self.H[key] = (value, self.t)
        self.q.append((key, self.t))
        while len(self.H) > self.capacity:
            k, t = self.q.popleft()
            if self.H[k][1] == t:
                del self.H[k]
