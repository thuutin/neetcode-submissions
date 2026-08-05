class TimeMap:

    def __init__(self):
        self.H = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.H[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.H[key]
        if len(values) == 0 or values[0][0] > timestamp:
            return ""
        start, end = 0, len(values) - 1
        while start < end:
            mid = (start + end + 1) // 2
            t, v = values[mid]
            if t > timestamp:
                end = mid - 1
            else:
                start = mid
        return values[start][1]
