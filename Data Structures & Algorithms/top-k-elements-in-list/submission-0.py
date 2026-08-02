class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        freq = sorted(counts.items(), key = lambda x: x[1])
        return list(map(lambda x: x[0], freq[-k:]))