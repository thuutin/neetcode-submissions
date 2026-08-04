class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, x in enumerate(nums[:k - 1]):
            heap.append((-x, i))
        heapq.heapify(heap)
        res = []
        for i in range( k-1, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            left = i - k + 1
            while heap[0][1] < left:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res
