class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d = []
        for y in arr:
            diff = abs(y - x)
            heapq.heappush(d, (diff, y))
        d.sort()
        d = d[:k]
        d = list(map( lambda x: x[1], d))
        return sorted(d)