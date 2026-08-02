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
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                    continue
                if a + b > target:
                    j -= 1
                else:
                    i += 1
            return k
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            pairs = two(i + 1, -a)
            for b, c in pairs:
                res.append((a, b, c))
        return list(res)