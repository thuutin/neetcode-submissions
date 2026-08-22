class FreqStack:

    def __init__(self):
        self.t = 0
        self.freq = defaultdict(int)
        self.heap = []
        

    def push(self, val: int) -> None:
        self.t += 1
        self.freq[val] += 1   
        heapq.heappush(self.heap, (-self.freq[val], -self.t, val))   

    def pop(self) -> int:
        f, t, val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()