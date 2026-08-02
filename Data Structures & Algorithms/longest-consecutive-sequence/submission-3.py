class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mm = 0
        for x in s:
            if x - 1 in s:
                continue
            y = x
            while y in s:
                y += 1
            mm = max(mm, y - x)
        return mm