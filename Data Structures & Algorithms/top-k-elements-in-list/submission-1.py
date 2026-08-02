class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        freq = [None] * (len(nums) + 1)
        for kk, f in counts.items():
            if freq[f] == None:
                freq[f] = []
            freq[f].append(kk)
        res = []
        #print(freq)
        for f in freq[::-1]:
            if f is not None and len(f) > 0 and k > 0:
                k -= len(f)
                res.extend(f)
            #print(res, k)
        return res
        #return list(map(lambda x: x[0], freq[-k:]))