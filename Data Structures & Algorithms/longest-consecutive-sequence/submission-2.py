class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mm = 0
        for x in s:
            if x - 1 in s:
                continue
            c = 0
            while x in s:
                c += 1
                x += 1
            mm = max(mm, c)
        return mm