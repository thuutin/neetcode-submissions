class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h1, -num)
        if len(self.h1) > len(self.h2):
            x = -heapq.heappop(self.h1)
            heapq.heappush(self.h2, x)
        if self.h2 and self.h1 and self.h2[0] < -self.h1[0]:
            x = -heapq.heappop(self.h1)
            y = heapq.heappop(self.h2)
            heapq.heappush(self.h1, -y)
            heapq.heappush(self.h2, x)

    def findMedian(self) -> float:
        if (len(self.h1) + len(self.h2)) % 2== 0 :
            return (-self.h1[0] + self.h2[0]) / 2
        return self.h2[0]
        
        