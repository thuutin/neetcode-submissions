class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n // 3
        t = defaultdict(int)
        r = set()
        for x in nums:
            t[x] += 1
            if t[x] > threshold:
                r.add(x)
        return list(r)