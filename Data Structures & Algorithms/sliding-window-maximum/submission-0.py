class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i + 1 < k:
                continue
            left = i - k + 1
            while heap[0][1] < left:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res
