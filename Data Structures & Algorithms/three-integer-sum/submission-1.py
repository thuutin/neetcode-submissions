class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        def two(i, target):
            k = []
            j = len(nums) - 1
            while i < j:
                a = nums[i]
                b = nums[j]
                if a + b == target:
                    k.append((a,b))
                if a + b >= target:
                    j -= 1
                else:
                    i += 1
            return k
        res = set()
        for i in range(len(nums)):
            a = nums[i]
            pairs = two(i + 1, -a)
            for b, c in pairs:
                res.add(tuple(sorted([a, b, c])))
        return list(res)