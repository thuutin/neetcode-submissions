class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        h = []
        for i, x in enumerate(nums):
            heapq.heappush(h, (-x, i))
            
            if i >= k - 1:
                while h and h[0][1] <= i - k:
                    heapq.heappop(h)
                res.append(-h[0][0])
        return res